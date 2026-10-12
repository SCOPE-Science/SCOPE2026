import sympy as sp
from itertools import product
from collections import Counter

a,b,c,d=sp.symbols("a b c d")
R=sp.Matrix([[a,b],[c,d]])
e1=sp.Matrix([1,0]); e2=sp.Matrix([0,1])
basis=(e1,e2)

def lie(x,y):
    return sp.Matrix([0,sp.expand(x[0]*y[1]-x[1]*y[0])])

def tri(x,y,z):
    return sp.simplify(lie(lie(x,y),z))

def defect(x,y,z):
    Rx,Ry,Rz=R*x,R*y,R*z
    lhs=tri(Rx,Ry,Rz)
    inside=tri(Rx,Ry,z)+tri(Rx,y,Rz)+tri(x,Ry,Rz)
    return sp.simplify(lhs-R*inside)

actual=[]
for x0 in basis:
    for y0 in basis:
        for z0 in basis:
            actual.extend(sp.factor(v) for v in defect(x0,y0,z0) if v!=0)

target=[
    b*(a*a+2*a*d-b*c),
    b*(b*c+d*d),
    b*b*(a+d),
    a*b*c+2*a*d*d-b*c*d,
]
G=sp.groebner(target,a,b,c,d,order="grevlex")
for v in actual:
    assert G.reduce(v)[1]==0
G2=sp.groebner(actual,a,b,c,d,order="grevlex")
for v in target:
    assert G2.reduce(v)[1]==0

# Binary affine-Lie Rota-Baxter equations.
def lie_defect(x,y):
    Rx,Ry=R*x,R*y
    return sp.simplify(lie(Rx,Ry)-R*(lie(Rx,y)+lie(x,Ry)))

lie_actual=[]
for x0 in basis:
    for y0 in basis:
        lie_actual.extend(sp.factor(v) for v in lie_defect(x0,y0) if v!=0)
lie_target=[b*(a+d),b*c+d*d]
LG=sp.groebner(lie_target,a,b,c,d,order="grevlex")
for v in lie_actual:
    assert LG.reduce(v)[1]==0
LG2=sp.groebner(lie_actual,a,b,c,d,order="grevlex")
for v in lie_target:
    assert LG2.reduce(v)[1]==0

# Symbolic automorphisms.
p,u,r,s=sp.symbols("p u r s")
P=sp.Matrix([[p,u],[r,s]])
aut_eq=[]
for x0 in basis:
    for y0 in basis:
        for z0 in basis:
            D=sp.simplify(P*tri(x0,y0,z0)-tri(P*x0,P*y0,P*z0))
            aut_eq.extend(sp.factor(v) for v in D if v!=0)
AG=sp.groebner([u,s*(p*p-1)],p,u,r,s,order="grevlex")
for v in aut_eq:
    assert AG.reduce(v)[1]==0

def lmod(x,y,Q):
    return (0,(x[0]*y[1]-x[1]*y[0])%Q)

def tmod(x,y,z,Q):
    return lmod(lmod(x,y,Q),z,Q)

def mv(M,x,Q):
    return ((M[0]*x[0]+M[1]*x[1])%Q,
            (M[2]*x[0]+M[3]*x[1])%Q)

def is_rb(M,Q):
    bas=((1,0),(0,1))
    for x in bas:
        for y in bas:
            for z in bas:
                Rx,Ry,Rz=mv(M,x,Q),mv(M,y,Q),mv(M,z,Q)
                lhs=tmod(Rx,Ry,Rz,Q)
                q1=tmod(Rx,Ry,z,Q)
                q2=tmod(Rx,y,Rz,Q)
                q3=tmod(x,Ry,Rz,Q)
                inside=((q1[0]+q2[0]+q3[0])%Q,(q1[1]+q2[1]+q3[1])%Q)
                if lhs!=mv(M,inside,Q):
                    return False
    return True

def is_lie_rb(M,Q):
    bas=((1,0),(0,1))
    for x in bas:
        for y in bas:
            Rx,Ry=mv(M,x,Q),mv(M,y,Q)
            lhs=lmod(Rx,Ry,Q)
            q1=lmod(Rx,y,Q); q2=lmod(x,Ry,Q)
            inside=((q1[0]+q2[0])%Q,(q1[1]+q2[1])%Q)
            if lhs!=mv(M,inside,Q):
                return False
    return True

def rank2(M,Q):
    aa,bb,cc,dd=M
    if all(v%Q==0 for v in M):
        return 0
    return 2 if (aa*dd-bb*cc)%Q else 1

def inv2(P,Q):
    aa,bb,cc,dd=P
    det=(aa*dd-bb*cc)%Q
    if det==0:
        return None
    di=pow(det,-1,Q)
    return (dd*di%Q,-bb*di%Q,-cc*di%Q,aa*di%Q)

def mm(A,B,Q):
    return tuple(sum(A[2*i+k]*B[2*k+j] for k in range(2))%Q
                 for i in range(2) for j in range(2))

def conj(M,P,Q):
    return mm(mm(P,M,Q),inv2(P,Q),Q)

for Q in (3,5,7):
    sols=[M for M in product(range(Q),repeat=4) if is_rb(M,Q)]
    expected_A={(0,0,cc,dd) for cc in range(Q) for dd in range(Q)}
    expected_B={(aa,0,cc,0) for aa in range(Q) for cc in range(Q)}
    expected_C={(aa,bb,(-aa*aa*pow(bb,-1,Q))%Q,(-aa)%Q)
                for aa in range(Q) for bb in range(1,Q)}
    expected=expected_A|expected_B|expected_C
    assert set(sols)==expected
    assert len(sols)==3*Q*Q-2*Q

    ranks=Counter(rank2(M,Q) for M in sols)
    assert tuple(ranks[i] for i in range(3))==(1,3*Q*Q-2*Q-1,0)

    lie_sols={M for M in product(range(Q),repeat=4) if is_lie_rb(M,Q)}
    assert lie_sols==(expected_B|expected_C)

    auts=[(eps%Q,0,rr,ss)
          for eps in (1,-1)
          for rr in range(Q)
          for ss in range(1,Q)]

    pool=set(sols); orbits=[]
    while pool:
        M=next(iter(pool))
        O={conj(M,P,Q) for P in auts}
        assert O<=set(sols)
        orbits.append(O)
        pool-=O

    sizes=Counter(len(O) for O in orbits)
    expected_sizes=Counter({1:1,Q-1:1,Q:2*(Q-1),Q*(Q-1):1})
    assert sizes==expected_sizes,(Q,sizes,expected_sizes)
    assert len(orbits)==2*Q+1

    print({
        "q":Q,
        "operators":len(sols),
        "ranks":tuple(ranks[i] for i in range(3)),
        "binary_lie_rb":len(lie_sols),
        "orbits":len(orbits),
        "orbit_sizes":dict(sorted(sizes.items())),
    })

print("VERIFY_OK")
