import sympy as sp
from itertools import product
from collections import Counter

a,b,c,d=sp.symbols("a b c d")
R=sp.Matrix([[a,b],[c,d]])
e=sp.Matrix([1,0])
f=sp.Matrix([0,1])

def br(x,y):
    return sp.Matrix([0, sp.expand(x[0]*y[1]-x[1]*y[0])])

def defect(x,y):
    Rx=R*x
    Ry=R*y
    return sp.simplify(br(Rx,Ry)-R*(br(Rx,y)+br(x,Ry)-br(Rx,Ry)))

vals=[]
for x in (e,f):
    for y in (e,f):
        vals.extend(sp.factor(z) for z in defect(x,y) if z!=0)

E1=sp.factor(b*(a*d-a-b*c-d))
E2=sp.factor(d*d*(a-1)-b*c*(d+1))
G=sp.groebner([E1,E2],a,b,c,d,order="grevlex")
for z in vals:
    assert G.reduce(z)[1]==0
G2=sp.groebner(vals,a,b,c,d,order="grevlex")
for z in (E1,E2):
    assert G2.reduce(z)[1]==0

def bracket_mod(x,y,p):
    return (0,(x[0]*y[1]-x[1]*y[0])%p)

def mv(M,x,p):
    return ((M[0]*x[0]+M[1]*x[1])%p,(M[2]*x[0]+M[3]*x[1])%p)

def is_reynolds(M,p):
    bas=((1,0),(0,1))
    for x in bas:
        for y in bas:
            Rx=mv(M,x,p); Ry=mv(M,y,p)
            lhs=bracket_mod(Rx,Ry,p)
            q1=bracket_mod(Rx,y,p); q2=bracket_mod(x,Ry,p); q3=bracket_mod(Rx,Ry,p)
            inside=((q1[0]+q2[0]-q3[0])%p,(q1[1]+q2[1]-q3[1])%p)
            if lhs!=mv(M,inside,p):
                return False
    return True

def equations(M,p):
    aa,bb,cc,dd=M
    return bb*(aa*dd-aa-bb*cc-dd)%p==0 and (dd*dd*(aa-1)-bb*cc*(dd+1))%p==0

def branch(M,p):
    aa,bb,cc,dd=M
    return (
        (bb%p==0 and dd%p==0)
        or (bb%p==0 and dd%p!=0 and aa%p==1)
        or (bb%p!=0 and (dd+aa)%p==0 and (bb*cc+aa*aa)%p==0)
    )

def rank2(M,p):
    aa,bb,cc,dd=M
    if all(x%p==0 for x in M):
        return 0
    return 2 if (aa*dd-bb*cc)%p else 1

for p in (2,3,5,7):
    ranks=Counter(); n=0
    for M in product(range(p),repeat=4):
        r=is_reynolds(M,p)
        assert r==equations(M,p)==branch(M,p)
        if r:
            n+=1
            ranks[rank2(M,p)]+=1
    expected=3*p*p-2*p
    profile=(1,2*p*p-p-1,p*(p-1))
    assert n==expected
    assert tuple(ranks[i] for i in range(3))==profile
    print({"q":p,"total":n,"ranks":profile})

print("VERIFY_OK")
