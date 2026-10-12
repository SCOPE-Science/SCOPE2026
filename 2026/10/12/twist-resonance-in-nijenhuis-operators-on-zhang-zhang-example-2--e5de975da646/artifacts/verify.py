import sympy as sp
from itertools import product
from collections import Counter

lam,p,r,q,s,mu=sp.symbols("lam p r q s mu")
P=sp.Matrix([[p,r],[q,s]])
Beta=sp.diag(mu,1/mu)
comm=sp.simplify(P*Beta-Beta*P)
assert sp.simplify(comm[0,1]-r*(1/mu-mu))==0
assert sp.simplify(comm[1,0]-q*(mu-1/mu))==0

J=sp.Matrix([[0,1],[-1,0]])
assert sp.simplify(P.T*J+J*P-sp.trace(P)*J)==sp.zeros(2)
assert sp.simplify(P.T*J*P-sp.det(P)*J)==sp.zeros(2)
assert sp.simplify(lam*sp.trace(P)-lam**2-sp.det(P)+sp.det(P-lam*sp.eye(2)))==0

def mm(A,B,Q):
    return (
        (A[0]*B[0]+A[1]*B[2])%Q,
        (A[0]*B[1]+A[1]*B[3])%Q,
        (A[2]*B[0]+A[3]*B[2])%Q,
        (A[2]*B[1]+A[3]*B[3])%Q,
    )

def invm(A,Q):
    det=(A[0]*A[3]-A[1]*A[2])%Q
    if det==0: return None
    z=pow(det,-1,Q)
    return (A[3]*z%Q,-A[1]*z%Q,-A[2]*z%Q,A[0]*z%Q)

def conj(G,A,Q):
    return mm(mm(G,A,Q),invm(G,Q),Q)

def rank2(A,Q):
    if all(x%Q==0 for x in A): return 0
    return 2 if (A[0]*A[3]-A[1]*A[2])%Q else 1

def structural(lam,A,muv,Q):
    p,r,q,s=A
    mui=pow(muv,-1,Q)
    return ((r*(mui-muv))%Q==0 and (q*(muv-mui))%Q==0
            and ((p-lam)*(s-lam)-r*q)%Q==0)

def direct(lam,A,muv,Q):
    p,r,q,s=A
    mui=pow(muv,-1,Q)
    beta=(muv,0,0,mui)
    if mm(A,beta,Q)!=mm(beta,A,Q): return False
    h=pow(2,-1,Q)
    D=(muv*h%Q,0,0,mui*h%Q)
    def mv(M,v):
        return ((M[0]*v[0]+M[1]*v[1])%Q,(M[2]*v[0]+M[3]*v[1])%Q)
    bas=((1,0),(0,1))
    P2=mm(A,A,Q)
    for y in bas:
        Py=mv(A,y); Dy=mv(D,y)
        lhs1=mv(A,mv(D,Py))
        lhs2=tuple(lam*z%Q for z in mv(A,Dy))
        lhs3=mv(P2,Dy)
        rhs=tuple(lam*z%Q for z in mv(D,Py))
        if tuple((lhs1[i]+lhs2[i]-lhs3[i])%Q for i in range(2))!=rhs: return False
    def om(u,v): return (u[0]*v[1]-u[1]*v[0])%Q
    for y,z in product(bas,repeat=2):
        Py,Pz=mv(A,y),mv(A,z)
        lhs=(lam*om(y,Pz)+lam*om(Py,z)-lam*lam*om(y,z))%Q
        if lhs!=om(Py,Pz): return False
    return True

def aut_group(muv,Q):
    mui=pow(muv,-1,Q); beta=(muv,0,0,mui)
    return [A for A in product(range(Q),repeat=4)
            if (A[0]*A[3]-A[1]*A[2])%Q==1 and mm(A,beta,Q)==mm(beta,A,Q)]

def nij_set(muv,Q):
    return {(l,A) for l in range(Q) for A in product(range(Q),repeat=4) if structural(l,A,muv,Q)}

def nonsquare(Q):
    sq={x*x%Q for x in range(1,Q)}
    return next(x for x in range(1,Q) if x not in sq)

for Q in (3,5,7):
    for muv in range(1,Q):
        S=nij_set(muv,Q)
        D={(l,A) for l in range(Q) for A in product(range(Q),repeat=4) if direct(l,A,muv,Q)}
        assert S==D
        rc=Counter((1 if l else 0)+rank2(A,Q) for l,A in S)
        if (muv*muv)%Q==1:
            assert len(S)==Q**4+Q**3-Q**2
            assert tuple(rc[i] for i in range(4))==(1,(Q-1)*(Q+1)**2,Q*(Q**2-1),Q*(Q-1)*(Q**2-2))
        else:
            assert len(S)==2*Q**2-Q
            assert tuple(rc[i] for i in range(4))==(1,2*(Q-1),2*(Q-1),(Q-1)*(2*Q-3))
    print({"q":Q,"twists_checked":Q-1})

for Q in (3,5):
    S=nij_set(1,Q); G=aut_group(1,Q)
    assert len(G)==Q*(Q**2-1)
    seen=set(); orbits=[]
    for x in S:
        if x in seen: continue
        l,A=x
        O={(l,conj(g,A,Q)) for g in G}
        seen|=O; orbits.append(O)
    assert len(orbits)==Q*(Q+2)
    nu=nonsquare(Q)
    reps=set()
    for l in range(Q):
        reps.add((l,(l,0,0,l)))
        reps.add((l,(l,1,0,l)))
        reps.add((l,(l,nu,0,l)))
        for tau in range(1,Q):
            reps.add((l,((l+tau)%Q,0,0,l)))
    assert len(reps)==Q*(Q+2)
    assert all(len(O&reps)==1 for O in orbits)
    if Q>3:
        muv=2
        Sg=nij_set(muv,Q); Gg=aut_group(muv,Q)
        assert len(Gg)==Q-1 and len(Sg)==2*Q**2-Q
        assert all(all(conj(g,A,Q)==A for g in Gg) for l,A in Sg)
    print({"q":Q,"resonant_orbits":len(orbits)})

print("VERIFY_OK")
