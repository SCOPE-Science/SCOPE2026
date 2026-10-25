"""Symbolic and numerical checks for a two-step symmetric sketched Ritz bound."""
import math
import numpy as np
import sympy as sp

a,b,e,d=sp.symbols('a b e d', positive=True, real=True)
z=sp.Symbol('z')
c=sp.sqrt(1-e**2)
G=sp.Matrix([[1-e**2,0,-e*c],[0,1,0],[-e*c,0,1+e**2]])
A=sp.Matrix([[d,a,0],[a,d,b],[0,b,d]])
E=G[:2,:2]
H=E.inv()*(G[:2,:]*A[:,:2])
T=sp.Matrix([[d,a-b*e/c],[a,d]])
assert all(sp.simplify(z0)==0 for z0 in H-T)
assert sp.factor(G.charpoly(z).as_expr()-(z-1)*((z-1)**2-e**2))==0
assert sp.simplify(T.charpoly(z).as_expr()-((z-d)**2+a*(b*e/c-a)))==0
# Exact critical certificate for arbitrary positive a,b.
ecrit=a/sp.sqrt(a*a+b*b)
assert sp.simplify((b*e/c-a).subs(e,ecrit))==0
# Reduce all possible metric cross-blocks to bounded t vectors.
# Sample independent symmetric matrices, random starting vectors and embeddings.
rng=np.random.default_rng(20261023)
count=0
for k in range(1000):
    n=int(rng.integers(3,8))
    M=rng.standard_normal((n,n))
    A=M.T@M+np.eye(n)
    v=rng.standard_normal(n);v/=np.linalg.norm(v)
    av=float(v@A@v)
    r=A@v-av*v
    aa=np.linalg.norm(r)
    if aa<1e-12: continue
    v2=r/aa
    diag=float(v2@A@v2)
    r2=A@v2-aa*v-diag*v2
    bb=np.linalg.norm(r2)
    if bb<1e-12: continue
    v3=r2/bb
    W=np.column_stack((v,v2,v3))
    eps=float(rng.uniform(.002,.95))
    X=rng.standard_normal((3,3))
    O,_=np.linalg.qr(X)
    Gnum=O@np.diag(1+eps*rng.uniform(-1,1,3))@O.T
    K=Gnum[:2,:2]
    t=np.linalg.solve(K,Gnum[:2,2])
    R=eps/math.sqrt(1-eps*eps)
    assert np.linalg.norm(t)<=R+1e-10,(t,R)
    Hnum=np.linalg.solve(K, Gnum[:2,:]@(W.T@A@W)[:,:2])
    Hform=np.array([[av,aa+bb*t[0]],[aa,diag+bb*t[1]]])
    assert np.allclose(Hnum,Hform,atol=1e-9)
    im=max(abs(vv.imag) for vv in np.linalg.eigvals(Hnum))
    bound=math.sqrt(max(0,aa*(bb*R-aa)))
    assert im<=bound+2e-7,(im,bound,eps,aa,bb)
    count+=1
assert count>=900
for aa,bb,eps in [(0.3,1.2,0.40),(1.,1.,0.80),(0.1,8.,0.6)]:
    cc=math.sqrt(1-eps**2)
    gn=np.array([[1-eps**2,0,-eps*cc],[0,1,0],[-eps*cc,0,1+eps**2]])
    d0=2+math.hypot(aa,bb)
    hn=np.linalg.solve(gn[:2,:2],gn[:2,:]@np.array([[d0,aa,0],[aa,d0,bb],[0,bb,d0]])[:,:2])
    expected=math.sqrt(max(0,aa*(bb*eps/cc-aa)))
    im=max(abs(vv.imag) for vv in np.linalg.eigvals(hn))
    assert abs(im-expected)<1e-8,(im,expected)
print(f'VERIFY_OK symbolic Gram/eigenvalue identities; {count} randomized Krylov-embedding checks; 3 sharp witnesses')
