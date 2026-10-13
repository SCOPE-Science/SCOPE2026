import sympy as sp
from itertools import product
from collections import Counter

# Symbolic Nijenhuis torsion.
a,b,c,d,u,v,f,p,qv=sp.symbols("a b c d u v f p qv")
N=sp.Matrix([[a,c,p],[b,d,qv],[u,v,f]])
basis=[sp.eye(3)[:,i] for i in range(3)]

def mul(x,y):
    return sp.Matrix([0,0,sp.expand(x[0]*y[1]+x[1]*y[0])])

def torsion(x,y):
    Nx,Ny=N*x,N*y
    return sp.simplify(mul(Nx,Ny)-N*(mul(Nx,y)+mul(x,Ny)-N*mul(x,y)))

def flat(M):
    return tuple(int(M[i,j]) for i in range(3) for j in range(3))

# The basis torsions force p=qv=0 over every field, and for char != 2:
# b(a-f)=0, c(d-f)=0, bc+(a-f)(d-f)=0.
eqs=[]
for x,y in product(basis,repeat=2):
    for z in torsion(x,y):
        z=sp.factor(z)
        if z!=0:
            eqs.append(z)
assert any(sp.factor(z-p*p)==0 or sp.factor(z+p*p)==0 for z in eqs)
assert any(sp.factor(z-qv*qv)==0 or sp.factor(z+qv*qv)==0 for z in eqs)
red=[sp.factor(z.subs({p:0,qv:0})) for z in eqs]
assert any(sp.factor(z-2*b*(a-f))==0 or sp.factor(z+2*b*(a-f))==0 for z in red)
assert any(sp.factor(z-2*c*(d-f))==0 or sp.factor(z+2*c*(d-f))==0 for z in red)
F=sp.expand(b*c+(a-f)*(d-f))
G=sp.groebner([b*(a-f),c*(d-f),F],a,b,c,d,f)
for z in red:
    assert G.reduce(sp.expand(z))[1]==0

def mm(A,B,Q):
    return tuple(sum(A[3*i+k]*B[3*k+j] for k in range(3))%Q
                 for i in range(3) for j in range(3))

def inv3(M,Q):
    A=[[M[3*i+j]%Q for j in range(3)]+[1 if i==j else 0 for j in range(3)]
       for i in range(3)]
    for col in range(3):
        piv=next((r for r in range(col,3) if A[r][col]%Q),None)
        if piv is None:
            return None
        A[col],A[piv]=A[piv],A[col]
        z=pow(A[col][col],-1,Q)
        A[col]=[(z*x)%Q for x in A[col]]
        for r in range(3):
            if r!=col and A[r][col]%Q:
                z=A[r][col]%Q
                A[r]=[(A[r][j]-z*A[col][j])%Q for j in range(6)]
    return tuple(A[i][j+3]%Q for i in range(3) for j in range(3))

def conj(M,g,Q):
    gi=inv3(g,Q)
    assert gi is not None
    return mm(mm(g,M,Q),gi,Q)

def rank3(M,Q):
    A=[list(M[3*i:3*i+3]) for i in range(3)]
    r=0
    for col in range(3):
        piv=next((i for i in range(r,3) if A[i][col]%Q),None)
        if piv is None:
            continue
        A[r],A[piv]=A[piv],A[r]
        z=pow(A[r][col],-1,Q)
        A[r]=[(z*x)%Q for x in A[r]]
        for i in range(3):
            if i!=r and A[i][col]%Q:
                z=A[i][col]%Q
                A[i]=[(A[i][j]-z*A[r][j])%Q for j in range(3)]
        r+=1
    return r

def nij_set(Q):
    S=set()
    for aa,dd,bb,uu,vv in product(range(Q),repeat=5):
        S.add((aa,0,0,bb,dd,0,uu,vv,aa))
    for aa,dd,cc,uu,vv in product(range(Q),repeat=5):
        S.add((aa,cc,0,0,dd,0,uu,vv,dd))
    return S

def aut_set(Q):
    G=set()
    for ss in range(1,Q):
        for tt in range(1,Q):
            for rr,ww in product(range(Q),repeat=2):
                G.add((ss,0,0,0,tt,0,rr,ww,ss*tt%Q))
                G.add((0,ss,0,tt,0,0,rr,ww,ss*tt%Q))
    return G

def algebra_mul(x,y,Q):
    return (0,0,(x[0]*y[1]+x[1]*y[0])%Q)

def mv(M,x,Q):
    return tuple(sum(M[3*i+j]*x[j] for j in range(3))%Q for i in range(3))

def is_aut(g,Q):
    if inv3(g,Q) is None:
        return False
    E=[(1,0,0),(0,1,0),(0,0,1)]
    return all(mv(g,algebra_mul(x,y,Q),Q)==algebra_mul(mv(g,x,Q),mv(g,y,Q),Q)
               for x,y in product(E,repeat=2))

def canonical_reps(Q):
    reps=set()
    I=(1,0,0,0,1,0,0,0,1)
    for aa in range(Q):
        # repeated-eigenvalue fiber
        base=(aa,0,0,0,aa,0,0,0,aa)
        def add_entries(M,inds):
            L=list(M)
            for i in inds:
                L[i]=(L[i]+1)%Q
            return tuple(L)
        reps.add(base)
        reps.add(add_entries(base,[6]))       # E31
        reps.add(add_entries(base,[6,7]))     # E31+E32
        reps.add(add_entries(base,[3]))       # E21
        reps.add(add_entries(base,[3,7]))     # E21+E32
        for dd in range(Q):
            if dd==aa:
                continue
            base=(aa,0,0,0,dd,0,0,0,aa)
            reps.add(base)
            reps.add(add_entries(base,[6]))
            reps.add(add_entries(base,[3]))
            reps.add(add_entries(base,[3,7]))
    assert len(reps)==Q*(4*Q+1)
    return reps

for Q in (3,5,7):
    S=nij_set(Q)
    assert len(S)==2*Q**5-Q**3
    ranks=Counter(rank3(M,Q) for M in S)
    expected=(
        1,
        (Q-1)*(Q+1)*(2*Q+1),
        2*Q*(Q-1)*(2*Q**2-1),
        Q**2*(Q-1)*(2*Q**2-2*Q-1),
    )
    assert tuple(ranks[i] for i in range(4))==expected
    print({"q":Q,"raw":len(S),"rank_profile":expected})

for Q in (3,5):
    S=nij_set(Q)
    G=aut_set(Q)
    assert len(G)==2*Q**2*(Q-1)**2
    assert all(is_aut(g,Q) for g in G)
    reps=canonical_reps(Q)
    seen=set()
    orbits=[]
    for M in S:
        if M in seen:
            continue
        O={conj(M,g,Q) for g in G}
        assert O<=S
        seen.update(O)
        orbits.append(O)
    assert len(orbits)==Q*(4*Q+1)
    assert all(len(O & reps)==1 for O in orbits)
    print({"q":Q,"automorphisms":len(G),"orbits":len(orbits),
           "orbit_sizes":dict(sorted(Counter(map(len,orbits)).items()))})

print("VERIFY_OK")
