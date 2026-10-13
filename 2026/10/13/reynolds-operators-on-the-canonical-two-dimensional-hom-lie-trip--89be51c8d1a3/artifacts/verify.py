import sympy as sp
from itertools import product
from collections import Counter

a,b,c,d=sp.symbols("a b c d")
T=sp.Matrix([[a,b],[c,d]])
A=sp.diag(1,-1)
e1=sp.Matrix([1,0]); e2=sp.Matrix([0,1])
basis=(e1,e2)

def br(x,y,z):
    return sp.Matrix([sp.expand((x[0]*y[1]-x[1]*y[0])*z[1]),0])

def alpha(x):
    return A*x

for x,y,z in product(basis,repeat=3):
    assert sp.simplify(alpha(br(x,y,z))-br(alpha(x),alpha(y),alpha(z)))==sp.zeros(2,1)
    assert sp.simplify(br(x,y,z)+br(y,x,z))==sp.zeros(2,1)
    assert sp.simplify(br(x,y,z)+br(z,x,y)+br(y,z,x))==sp.zeros(2,1)

for aa,bb,x,y,z in product(basis,repeat=5):
    lhs=br(alpha(aa),alpha(bb),br(x,y,z))
    rhs=(br(br(aa,bb,x),alpha(y),alpha(z))
         +br(alpha(x),br(aa,bb,y),alpha(z))
         +br(alpha(x),alpha(y),br(aa,bb,z)))
    assert sp.simplify(lhs-rhs)==sp.zeros(2,1)

assert sp.simplify(A*T-T*A)==sp.Matrix([[0,2*b],[-2*c,0]])

def defect(x,y,z):
    Tx,Ty,Tz=T*x,T*y,T*z
    inside=br(Tx,Ty,z)+br(x,Ty,Tz)+br(Tx,y,Tz)-br(Tx,Ty,Tz)
    return sp.simplify(br(Tx,Ty,Tz)-T*inside)

red=[]
for x,y,z in product(basis,repeat=3):
    for v in defect(x,y,z):
        v=sp.factor(v.subs({b:0,c:0}))
        if v!=0:
            red.append(v)
target=a*a*d*(d-2)
G=sp.groebner([target],a,d)
assert all(G.reduce(sp.expand(v))[1]==0 for v in red)
G2=sp.groebner(red,a,d)
assert G2.reduce(target)[1]==0

def bq(x,y,z,q):
    return (((x[0]*y[1]-x[1]*y[0])*z[1])%q,0)
def aq(x,q):
    return (x[0]%q,(-x[1])%q)
def mv(M,x,q):
    return ((M[0]*x[0]+M[1]*x[1])%q,(M[2]*x[0]+M[3]*x[1])%q)
def is_rey(M,q):
    bas=((1,0),(0,1))
    for x in bas:
        if mv(M,aq(x,q),q)!=aq(mv(M,x,q),q):
            return False
    for x,y,z in product(bas,repeat=3):
        Tx,Ty,Tz=mv(M,x,q),mv(M,y,q),mv(M,z,q)
        lhs=bq(Tx,Ty,Tz,q)
        p1,p2,p3,p4=bq(Tx,Ty,z,q),bq(x,Ty,Tz,q),bq(Tx,y,Tz,q),bq(Tx,Ty,Tz,q)
        inside=((p1[0]+p2[0]+p3[0]-p4[0])%q,(p1[1]+p2[1]+p3[1]-p4[1])%q)
        if lhs!=mv(M,inside,q):
            return False
    return True
def rank2(M,q):
    if all(x%q==0 for x in M): return 0
    return 2 if (M[0]*M[3]-M[1]*M[2])%q else 1
def mm(X,Y,q):
    return tuple(sum(X[2*i+k]*Y[2*k+j] for k in range(2))%q for i in range(2) for j in range(2))
def inv2(M,q):
    aa,bb,cc,dd=M; det=(aa*dd-bb*cc)%q
    if det==0: return None
    u=pow(det,-1,q)
    return (dd*u%q,-bb*u%q,-cc*u%q,aa*u%q)
def is_aut(P,q):
    if inv2(P,q) is None: return False
    bas=((1,0),(0,1))
    for x in bas:
        if mv(P,aq(x,q),q)!=aq(mv(P,x,q),q): return False
    for x,y,z in product(bas,repeat=3):
        if mv(P,bq(x,y,z,q),q)!=bq(mv(P,x,q),mv(P,y,q),mv(P,z,q),q): return False
    return True
def conj(M,P,q):
    return mm(mm(P,M,q),inv2(P,q),q)

for q in (3,5,7,11):
    sols={M for M in product(range(q),repeat=4) if is_rey(M,q)}
    expected={(0,0,0,dd) for dd in range(q)}
    expected|={(aa,0,0,0) for aa in range(q)}
    expected|={(aa,0,0,2%q) for aa in range(q)}
    assert sols==expected and len(sols)==3*q-2
    ranks=Counter(rank2(M,q) for M in sols)
    assert tuple(ranks[i] for i in range(3))==(1,2*q-2,q-1)

    aut={P for P in product(range(q),repeat=4) if is_aut(P,q)}
    expected_aut={(s,0,0,e) for s in range(1,q) for e in (1,q-1)}
    assert aut==expected_aut
    for M in sols:
        assert {conj(M,P,q) for P in aut}=={M}

    print({"q":q,"operators":len(sols),"rank_profile":tuple(ranks[i] for i in range(3)),
           "automorphisms":len(aut),"conjugacy_classes":len(sols)})

print("VERIFY_OK")
