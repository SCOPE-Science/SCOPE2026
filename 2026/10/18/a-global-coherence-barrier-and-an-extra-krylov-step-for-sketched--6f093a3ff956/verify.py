"""Reproduce the spectral formulas for sketched block KRR preconditioning.
Dependencies: Python 3, NumPy, SymPy. No data files or network access are needed.
"""
import numpy as np
import sympy as sp

def formulas(n,m,s,rho,lam):
    q=m//s;d=1-rho
    factor=sp.Rational(n*q,s) if isinstance(rho,sp.Basic) else n*q/s
    a=d*(d+lam*n)
    c=rho*(2*d+n*(rho+lam))
    tp=factor*d*(d+lam*s)
    tm=factor*(d+s*rho)*(d+s*rho+lam*s)
    return a,a+m*c,a/tp,a/tm,(a+m*c)/tm

def check(n,m,s,rho,lam):
    q=m//s
    Kn=(1-rho)*np.eye(n)+rho*np.ones((n,n))
    C=Kn[:,:m]
    Km=Kn[:m,:m]
    H=C.T@C+lam*n*Km
    Pb=np.zeros((m,m))
    for j in range(q):
        B=Km[j*s:(j+1)*s,j*s:(j+1)*s]
        Pb[j*s:(j+1)*s,j*s:(j+1)*s]=(n*q/s)*(B@B)+lam*n*q*B
    eig=np.linalg.eigvalsh(np.linalg.solve(np.linalg.cholesky(Pb),H) @ np.linalg.inv(np.linalg.cholesky(Pb).T))
    h0,hp,mu_inner,mu_contrast,mu_top=formulas(n,m,s,rho,lam)
    expected=sorted(([mu_inner]*(m-q) if s>1 else [])+[mu_contrast]*(q-1)+[mu_top])
    assert np.allclose(eig,expected,rtol=4e-9,atol=4e-10),(n,m,s,rho,lam,eig,expected)
    assert np.isclose(eig[-1]/eig[0],hp/h0,rtol=4e-9)
    if s>1:
        assert mu_contrast < mu_inner < mu_top
    return 1

checks=0
for n in [4,6,8,12,18]:
 for m in range(2,n+1):
  for s in range(1,m):
   if m%s: continue
   for rho in [0.01,0.15,0.6,0.91]:
    for lam in [0.02,0.3,2.,10.]:
     checks+=check(n,m,s,rho,lam)
# Symbolic exact equality of the Gram and block spectra for a rational example
n,m,s=8,4,2;rho=sp.Rational(3,5);lam=sp.Rational(1,10);q=m//s
d=1-rho
Kn=d*sp.eye(n)+rho*sp.ones(n,n)
C=Kn[:,:m]
Km=Kn[:m,:m]
H=C.T*C+lam*n*Km
P=sp.zeros(m,m)
for j in range(q):
 B=Km[j*s:(j+1)*s,j*s:(j+1)*s]
 T=sp.Rational(n*q,s)*B*B+lam*n*q*B
 P[j*s:(j+1)*s,j*s:(j+1)*s]=T
h0,hp,mi,mb,mg=formulas(n,m,s,rho,lam)
assert (P.inv()*H).eigenvals()=={mi:m-q,mb:q-1,mg:1}
checks+=1
print('PASS',checks,'matrix cases and exact spectral certificate')

def cg_exact(A,B,b,limit=6):
    """Exact preconditioned CG (B is the SPD inverse preconditioner)."""
    r=b.copy()
    p=B*r
    x=sp.zeros(b.rows,1)
    residuals=[r]
    z0=(r.T*B*r)[0]
    for i in range(limit):
        step=sp.cancel(z0/(p.T*A*p)[0])
        x+=step*p
        r=r-step*A*p
        residuals.append(sp.simplify(r))
        if r==sp.zeros(b.rows,1):return residuals
        z1=(r.T*B*r)[0]
        p=B*r+sp.cancel(z1/z0)*p
        z0=z1
    return residuals

bvec=sp.Matrix([1,2,3,4])
plain=cg_exact(H,sp.eye(m),bvec)
pre=cg_exact(H,P.inv(),bvec)
assert len(plain)-1==2 and len(pre)-1==3
assert all(v!=sp.zeros(m,1) for v in plain[:-1]+pre[:-1])
print('PASS exact CG termination: ordinary 2, preconditioned 3')
