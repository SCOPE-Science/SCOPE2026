import sympy as sp
from itertools import product
from collections import Counter

a,b,c,d=sp.symbols("a b c d")
R=sp.Matrix([[a,b],[c,d]])
e1=sp.Matrix([1,0]); e2=sp.Matrix([0,1])
basis=(e1,e2)

def br(x,y):
    return sp.Matrix([x[0]*y[1]-x[1]*y[0],0])

def tri(x,y,z):
    return sp.Matrix([(x[0]*y[1]-x[1]*y[0])*z[1],0])

def d2(x,y):
    Rx,Ry=R*x,R*y
    return sp.simplify(br(Rx,Ry)-R*(br(Rx,y)-br(Ry,x)))

def d3(x,y,z):
    Rx,Ry,Rz=R*x,R*y,R*z
    inside=tri(Rx,Ry,z)+tri(x,Ry,Rz)+tri(Rx,y,Rz)
    return sp.simplify(tri(Rx,Ry,Rz)-R*inside)

eq2=[]
eq3=[]
for x in basis:
    for y in basis:
        for v in d2(x,y):
            v=sp.factor(v)
            if v!=0:
                eq2.append(v)
for x in basis:
    for y in basis:
        for z in basis:
            for v in d3(x,y,z):
                v=sp.factor(v)
                if v!=0:
                    eq3.append(v)

G2=sp.groebner([a*a+b*c,c*(a+d)],a,b,c,d,order="grevlex")
for v in eq2:
    assert G2.reduce(sp.expand(v))[1]==0
for v in (a*a+b*c,c*(a+d)):
    assert sp.groebner(eq2,a,b,c,d,order="grevlex").reduce(v)[1]==0

full_targets=[a*a+b*c,c*(a+d),a*a*(a+d)]
GF=sp.groebner(full_targets,a,b,c,d,order="grevlex")
for v in eq2+eq3:
    assert GF.reduce(sp.expand(v))[1]==0

def brm(x,y,q):
    return ((x[0]*y[1]-x[1]*y[0])%q,0)

def trim(x,y,z,q):
    return (((x[0]*y[1]-x[1]*y[0])*z[1])%q,0)

def mv(M,x,q):
    return ((M[0]*x[0]+M[1]*x[1])%q,
            (M[2]*x[0]+M[3]*x[1])%q)

def is_rb(M,q):
    bas=((1,0),(0,1))
    for x in bas:
        for y in bas:
            Rx,Ry=mv(M,x,q),mv(M,y,q)
            lhs=brm(Rx,Ry,q)
            u=brm(Rx,y,q); v=brm(Ry,x,q)
            inside=((u[0]-v[0])%q,(u[1]-v[1])%q)
            if lhs!=mv(M,inside,q):
                return False
    for x in bas:
        for y in bas:
            for z in bas:
                Rx,Ry,Rz=mv(M,x,q),mv(M,y,q),mv(M,z,q)
                lhs=trim(Rx,Ry,Rz,q)
                u=trim(Rx,Ry,z,q)
                v=trim(x,Ry,Rz,q)
                w=trim(Rx,y,Rz,q)
                inside=((u[0]+v[0]+w[0])%q,(u[1]+v[1]+w[1])%q)
                if lhs!=mv(M,inside,q):
                    return False
    return True

def criterion(M,q):
    aa,bb,cc,dd=M
    A=(aa%q==0 and cc%q==0)
    N=((aa+dd)%q==0 and (aa*aa+bb*cc)%q==0)
    return A or N

def rank2(M,q):
    if all(v%q==0 for v in M):
        return 0
    aa,bb,cc,dd=M
    return 2 if (aa*dd-bb*cc)%q else 1

def inv2(P,q):
    aa,bb,cc,dd=P
    det=(aa*dd-bb*cc)%q
    if det==0:
        return None
    u=pow(det,-1,q)
    return (dd*u%q,-bb*u%q,-cc*u%q,aa*u%q)

def mm(A,B,q):
    return tuple(sum(A[2*i+k]*B[2*k+j] for k in range(2))%q
                 for i in range(2) for j in range(2))

def conj(M,P,q):
    return mm(mm(P,M,q),inv2(P,q),q)

for q in (2,3,5,7):
    sols=[]
    for M in product(range(q),repeat=4):
        direct=is_rb(M,q)
        expected=criterion(M,q)
        assert direct==expected,(q,M,direct,expected)
        if direct:
            sols.append(M)
    assert len(sols)==2*q*q-q
    ranks=Counter(rank2(M,q) for M in sols)
    assert tuple(ranks[i] for i in range(3))==(1,2*q*q-q-1,0)

    auts=[(s,t,0,1) for s in range(1,q) for t in range(q)]
    pool=set(sols); orbits=[]
    while pool:
        M=next(iter(pool))
        O={conj(M,P,q) for P in auts}
        assert O<=set(sols)
        orbits.append(O)
        pool-=O
    assert len(orbits)==q+2
    sizes=Counter(len(O) for O in orbits)
    expected_sizes=Counter()
    expected_sizes[1]+=1
    expected_sizes[q-1]+=1
    expected_sizes[q]+=q-1
    expected_sizes[q*(q-1)]+=1
    assert sizes==expected_sizes,(q,sizes,expected_sizes)
    print({"q":q,"operators":len(sols),
           "ranks":tuple(ranks[i] for i in range(3)),
           "orbits":len(orbits),
           "orbit_sizes":dict(sorted(sizes.items()))})

print("VERIFY_OK")
