import sympy as sp
from itertools import product
from collections import Counter

a,b,c,d=sp.symbols("a b c d")
R=sp.Matrix([[a,b],[c,d]])
e1=sp.Matrix([1,0]); e2=sp.Matrix([0,1])
basis=(e1,e2)

def br(x,y,z):
    return sp.Matrix([sp.expand((x[0]*y[1]-x[1]*y[0])*z[1]),0])

def defect(x,y,z):
    Rx,Ry,Rz=R*x,R*y,R*z
    inside=br(Rx,Ry,z)+br(x,Ry,Rz)+br(Rx,y,Rz)-br(Rx,Ry,Rz)
    return sp.simplify(br(Rx,Ry,Rz)-R*inside)

eqs=[]
for x,y,z in product(basis,repeat=3):
    for v in defect(x,y,z):
        v=sp.factor(v)
        if v!=0 and v not in eqs and -v not in eqs:
            eqs.append(v)

expected=[
    c*(a*a*d-a*a-a*b*c-b*c),
    c*c*(a*d-a-b*c-d),
    a*a*d*d-2*a*a*d-a*b*c*d+a*b*c-b*c*d,
    c*(a*d*d-2*a*d-b*c*d+b*c-d*d),
]
G=sp.groebner(eqs,a,b,c,d)
H=sp.groebner(expected,a,b,c,d)
for e in expected:
    assert G.reduce(sp.expand(e))[1]==0
for e in eqs:
    assert H.reduce(sp.expand(e))[1]==0

def bq(x,y,z,q):
    return (((x[0]*y[1]-x[1]*y[0])*z[1])%q,0)

def mv(M,x,q):
    return ((M[0]*x[0]+M[1]*x[1])%q,
            (M[2]*x[0]+M[3]*x[1])%q)

def add4(p1,p2,p3,p4,q):
    return tuple((p1[i]+p2[i]+p3[i]-p4[i])%q for i in range(2))

def is_reynolds(M,q):
    bas=((1,0),(0,1))
    for x,y,z in product(bas,repeat=3):
        Rx,Ry,Rz=mv(M,x,q),mv(M,y,q),mv(M,z,q)
        lhs=bq(Rx,Ry,Rz,q)
        inside=add4(bq(Rx,Ry,z,q),bq(x,Ry,Rz,q),
                    bq(Rx,y,Rz,q),bq(Rx,Ry,Rz,q),q)
        if lhs!=mv(M,inside,q):
            return False
    return True

def mm(A,B,q):
    return tuple(sum(A[2*i+k]*B[2*k+j] for k in range(2))%q
                 for i in range(2) for j in range(2))

def square_zero(M,q):
    return mm(M,M,q)==(0,0,0,0)

def predicted(M,q):
    aa,bb,cc,dd=M
    A=(aa%q==0 and cc%q==0)
    B=(cc%q==0 and dd%q==0)
    C=(cc%q==0 and dd%q==2%q)
    N=square_zero(M,q)
    return A or B or C or N

def rank2(M,q):
    if all(x%q==0 for x in M):
        return 0
    return 2 if (M[0]*M[3]-M[1]*M[2])%q else 1

for q in (3,5,7,11):
    sols=[]
    for M in product(range(q),repeat=4):
        direct=is_reynolds(M,q)
        structural=predicted(M,q)
        assert direct==structural,(q,M,direct,structural)
        if direct:
            sols.append(M)
    assert len(sols)==4*q*q-3*q
    ranks=Counter(rank2(M,q) for M in sols)
    expected_profile=(1,(q-1)*(3*q+1),q*(q-1))
    got=tuple(ranks[i] for i in range(3))
    assert got==expected_profile,(q,got,expected_profile)
    print({"q":q,"operators":len(sols),"rank_profile":got})

print("VERIFY_OK")
