import sympy as sp
from itertools import product

alpha=sp.diag(1,-1,-1)
basis=[sp.eye(3)[:,i] for i in range(3)]

def br(x,y,z):
    return sp.Matrix([0,0,sp.expand((x[0]*y[1]-x[1]*y[0])*z[0])])

def prod_def(E,x,y,z):
    F=E*alpha
    Fx,Fy,Fz=F*x,F*y,F*z
    lhs=br(Fx,Fy,Fz)
    rhs=(F*br(Fx,Fy,z)+F*br(x,Fy,Fz)+F*br(Fx,y,Fz)+F*br(x,y,z)
         -br(Fx,y,z)-br(x,Fy,z)-br(x,y,Fz))
    return sp.simplify(lhs-rhs)

rr=sp.symbols("rr")
Ep=sp.Matrix([[1,0,0],[0,1,0],[0,rr,-1]])
Em=sp.Matrix([[-1,0,0],[0,-1,0],[0,rr,1]])
for M in (alpha,-alpha,Ep,Em):
    assert sp.simplify(M*M-sp.eye(3))==sp.zeros(3)
    assert sp.simplify(M*alpha-alpha*M)==sp.zeros(3)
    for x,y,z in product(basis,repeat=3):
        assert sp.simplify(prod_def(M,x,y,z))==sp.zeros(3,1)

def perfect_def(E,x,y,z):
    F=E*alpha
    return sp.simplify(F*br(x,y,z)-br(F*x,F*y,F*z))

for M in (alpha,-alpha):
    for x,y,z in product(basis,repeat=3):
        assert sp.simplify(perfect_def(M,x,y,z))==sp.zeros(3,1)
assert any(sp.simplify(perfect_def(Ep,x,y,z))!=sp.zeros(3,1) for x,y,z in product(basis,repeat=3))
assert any(sp.simplify(perfect_def(Em,x,y,z))!=sp.zeros(3,1) for x,y,z in product(basis,repeat=3))

x,y,w=sp.symbols("x y w", nonzero=True)
g=sp.Matrix([[x,0,0],[0,y,0],[0,w,x**2*y]])
assert sp.simplify(g*Ep*g.inv())==sp.Matrix([[1,0,0],[0,1,0],[0,rr*x**2+2*w/y,-1]])
assert sp.simplify(g*Em*g.inv())==sp.Matrix([[-1,0,0],[0,-1,0],[0,rr*x**2-2*w/y,1]])

def mm(A,B,Q):
    return tuple(sum(A[3*i+k]*B[3*k+j] for k in range(3))%Q for i in range(3) for j in range(3))

def mv(A,v,Q):
    return tuple(sum(A[3*i+j]*v[j] for j in range(3))%Q for i in range(3))

def inv3(M,Q):
    A=[[M[3*i+j]%Q for j in range(3)]+[1 if i==j else 0 for j in range(3)] for i in range(3)]
    for col in range(3):
        piv=next((i for i in range(col,3) if A[i][col]%Q),None)
        if piv is None: return None
        A[col],A[piv]=A[piv],A[col]
        z=pow(A[col][col],-1,Q)
        A[col]=[(z*t)%Q for t in A[col]]
        for i in range(3):
            if i!=col and A[i][col]%Q:
                z=A[i][col]%Q
                A[i]=[(A[i][j]-z*A[col][j])%Q for j in range(6)]
    return tuple(A[i][j+3]%Q for i in range(3) for j in range(3))

def bq(x,y,z,Q):
    return (0,0,((x[0]*y[1]-x[1]*y[0])*z[0])%Q)

def alpha_v(v,Q):
    return (v[0]%Q,(-v[1])%Q,(-v[2])%Q)

def product_ok(M,Q):
    bas=((1,0,0),(0,1,0),(0,0,1))
    def Fv(v): return mv(M,alpha_v(v,Q),Q)
    for x,y,z in product(bas,repeat=3):
        Fx,Fy,Fz=Fv(x),Fv(y),Fv(z)
        lhs=bq(Fx,Fy,Fz,Q)
        pos=[Fv(bq(Fx,Fy,z,Q)),Fv(bq(x,Fy,Fz,Q)),Fv(bq(Fx,y,Fz,Q)),Fv(bq(x,y,z,Q))]
        neg=[bq(Fx,y,z,Q),bq(x,Fy,z,Q),bq(x,y,Fz,Q)]
        rhs=tuple((sum(t[i] for t in pos)-sum(t[i] for t in neg))%Q for i in range(3))
        if lhs!=rhs: return False
    return True

def perfect_ok(M,Q):
    bas=((1,0,0),(0,1,0),(0,0,1))
    def Fv(v): return mv(M,alpha_v(v,Q),Q)
    return all(Fv(bq(x,y,z,Q))==bq(Fv(x),Fv(y),Fv(z),Q) for x,y,z in product(bas,repeat=3))

def sq_identity(M,Q):
    return mm(M,M,Q)==(1,0,0,0,1,0,0,0,1)

def is_pmI(M,Q):
    I=(1,0,0,0,1,0,0,0,1)
    return M==I or M==tuple((-t)%Q for t in I)

def predicted(Q):
    S={
        (1,0,0,0,Q-1,0,0,0,Q-1),
        (Q-1,0,0,0,1,0,0,0,1),
    }
    for rr in range(Q):
        S.add((1,0,0,0,1,0,0,rr,Q-1))
        S.add((Q-1,0,0,0,Q-1,0,0,rr,1))
    return S

def auts(Q):
    return {
        (xx,0,0,0,yy,0,0,ww,(xx*xx*yy)%Q)
        for xx in range(1,Q) for yy in range(1,Q) for ww in range(Q)
    }

def is_aut(M,Q):
    if inv3(M,Q) is None: return False
    bas=((1,0,0),(0,1,0),(0,0,1))
    return all(mv(M,bq(X,Y,Z,Q),Q)==bq(mv(M,X,Q),mv(M,Y,Q),mv(M,Z,Q),Q)
               for X,Y,Z in product(bas,repeat=3))

def conj(M,g,Q):
    return mm(mm(g,M,Q),inv3(g,Q),Q)

for Q in (3,5,7):
    S=set()
    for aa,pp,qq,rr,ss in product(range(Q),repeat=5):
        M=(aa,0,0,0,pp,qq,0,rr,ss)
        if sq_identity(M,Q) and not is_pmI(M,Q) and product_ok(M,Q):
            S.add(M)
    assert S==predicted(Q)
    assert len(S)==2*Q+2
    perf={M for M in S if perfect_ok(M,Q)}
    assert len(perf)==2
    G=auts(Q)
    assert len(G)==Q*(Q-1)**2
    assert all(is_aut(g,Q) for g in G)
    seen=set(); orbits=[]
    for M in S:
        if M in seen: continue
        O={conj(M,g,Q) for g in G}
        assert O<=S
        seen |= O
        orbits.append(O)
    assert len(orbits)==4
    print({"q":Q,"product_structures":len(S),"perfect":len(perf),
           "automorphisms":len(G),"orbits":len(orbits),
           "orbit_sizes":sorted(len(O) for O in orbits)})
print("VERIFY_OK")
