import sympy as sp
from itertools import product
from collections import Counter

# Symbolic structure
a,b,c,d,e=sp.symbols("a b c d e")
A=sp.diag(1,-1,-1)
e1=sp.Matrix([1,0,0]); e2=sp.Matrix([0,1,0]); e3=sp.Matrix([0,0,1])
basis=(e1,e2,e3)

def br(x,y):
    return sp.Matrix([0,0,sp.expand(x[0]*y[1]-x[1]*y[0])])

# Multiplicativity and Hom-Jacobi.
for x,y in product(basis,repeat=2):
    assert sp.simplify(A*br(x,y)-br(A*x,A*y))==sp.zeros(3,1)
for x,y,z in product(basis,repeat=3):
    J=br(A*x,br(y,z))+br(A*y,br(z,x))+br(A*z,br(x,y))
    assert sp.simplify(J)==sp.zeros(3,1)

# General twist-compatible matrix.  The alpha-centralizer has 1+2 block form.
N=sp.Matrix([[a,0,0],[0,b,d],[0,c,e]])
assert sp.simplify(A*N-N*A)==sp.zeros(3,3)

def defect(x,y):
    Nx,Ny=N*x,N*y
    inside=br(Nx,y)+br(x,Ny)-N*br(x,y)
    return sp.simplify(br(Nx,Ny)-N*inside)

D12=tuple(sp.factor(v) for v in defect(e1,e2))
D13=tuple(sp.factor(v) for v in defect(e1,e3))
assert D12==(0,-d*(a-e),a*b-a*e-b*e+c*d+e**2)
assert D13==(0,-d**2,d*(a-e))

# Over a field, d^2=0 forces d=0.  The remaining equation factors.
assert sp.factor(D12[2].subs(d,0))==(a-e)*(b-e)

def bq(x,y,q):
    return (0,0,(x[0]*y[1]-x[1]*y[0])%q)

def mv(M,x,q):
    return tuple(sum(M[3*i+j]*x[j] for j in range(3))%q for i in range(3))

def add(*vs,q):
    return tuple(sum(v[i] for v in vs)%q for i in range(3))

def is_nij(M,q):
    bas=((1,0,0),(0,1,0),(0,0,1))
    # alpha = diag(1,-1,-1)
    for x in bas:
        ax=(x[0]%q,(-x[1])%q,(-x[2])%q)
        lhs=mv(M,ax,q)
        mx=mv(M,x,q)
        rhs=(mx[0]%q,(-mx[1])%q,(-mx[2])%q)
        if lhs!=rhs:
            return False
    for x,y in product(bas,repeat=2):
        Nx,Ny=mv(M,x,q),mv(M,y,q)
        lhs=bq(Nx,Ny,q)
        p1=bq(Nx,y,q); p2=bq(x,Ny,q); p3=mv(M,bq(x,y,q),q)
        inside=tuple((p1[i]+p2[i]-p3[i])%q for i in range(3))
        if lhs!=mv(M,inside,q):
            return False
    return True

def predicted(M,q):
    aa,_,_,_,bb,dd,_,cc,ee=M
    return dd%q==0 and ((aa-ee)*(bb-ee))%q==0

def rank3(M,q):
    A0=[list(M[3*i:3*i+3]) for i in range(3)]
    rr=0
    for col in range(3):
        piv=next((i for i in range(rr,3) if A0[i][col]%q),None)
        if piv is None:
            continue
        A0[rr],A0[piv]=A0[piv],A0[rr]
        u=pow(A0[rr][col],-1,q)
        A0[rr]=[(u*z)%q for z in A0[rr]]
        for i in range(3):
            if i!=rr and A0[i][col]%q:
                f=A0[i][col]%q
                A0[i]=[(A0[i][j]-f*A0[rr][j])%q for j in range(3)]
        rr+=1
    return rr

def matrix_from_params(aa,bb,cc,ee,q):
    return (aa%q,0,0, 0,bb%q,0, 0,cc%q,ee%q)

def zero_deformation(M,q):
    aa=M[0]; bb=M[4]; ee=M[8]
    return (aa+bb-ee)%q==0

# Hom-Lie automorphisms P(s,p,r).
def auts(q):
    return [(s,0,0, 0,p,0, 0,r,(s*p)%q)
            for s in range(1,q) for p in range(1,q) for r in range(q)]

def mm(X,Y,q):
    return tuple(sum(X[3*i+k]*Y[3*k+j] for k in range(3))%q
                 for i in range(3) for j in range(3))

def inv3(P,q):
    # P = [[s,0,0],[0,p,0],[0,r,sp]]
    s=P[0]; p=P[4]; r=P[7]
    si=pow(s,-1,q); pi=pow(p,-1,q)
    # inverse lower 2x2 block [[p,0],[r,sp]]
    return (si,0,0,
            0,pi,0,
            0,(-r*si*pi*pi)%q,(si*pi)%q)

def conj(P,M,q):
    return mm(mm(P,M,q),inv3(P,q),q)

for q in (3,5,7,11):
    sols=[]
    # enumerate the 5-parameter alpha-centralizer directly
    for aa,bb,cc,dd,ee in product(range(q),repeat=5):
        M=(aa,0,0, 0,bb,dd, 0,cc,ee)
        direct=is_nij(M,q)
        structural=predicted(M,q)
        assert direct==structural,(q,M,direct,structural)
        if direct:
            sols.append(M)

    assert len(sols)==2*q**3-q**2
    ranks=Counter(rank3(M,q) for M in sols)
    expected=(1,(q-1)*(q+2),(q-1)*(3*q-1),q*(q-1)*(2*q-3))
    assert tuple(ranks[i] for i in range(4))==expected

    zero=sum(zero_deformation(M,q) for M in sols)
    assert zero==2*q*q-q
    assert len(sols)-zero==q*(q-1)*(2*q-1)

    # Canonical orbit key from the exact conjugation formula.
    keys=set()
    for M in sols:
        aa,bb,cc,ee=M[0],M[4],M[7],M[8]
        if bb!=ee:
            # Nijenhuis condition forces aa=ee and translation kills cc.
            assert aa==ee
            keys.add(("I",aa,bb,ee))
        elif cc==0:
            keys.add(("II",aa,bb))
        else:
            keys.add(("III",aa,bb))
    assert len(keys)==3*q*q-q

    # For small fields, exhaustively reconstruct every conjugacy orbit.
    if q in (3,5):
        G=auts(q)
        unseen=set(sols)
        orbit_count=0
        while unseen:
            M=next(iter(unseen))
            orb={conj(P,M,q) for P in G}
            assert orb <= set(sols)
            unseen-=orb
            orbit_count+=1
        assert orbit_count==3*q*q-q

    print({
        "q":q,
        "nijenhuis":len(sols),
        "rank_profile":tuple(ranks[i] for i in range(4)),
        "zero_deformation":zero,
        "nonzero_deformation":len(sols)-zero,
        "conjugacy_classes":3*q*q-q,
    })

print("VERIFY_OK")
