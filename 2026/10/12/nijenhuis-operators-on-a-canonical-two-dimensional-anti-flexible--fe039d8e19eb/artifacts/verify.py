import sympy as sp
from itertools import product
from collections import Counter

a,b,c,d=sp.symbols("a b c d")
N=sp.Matrix([[a,b],[c,d]])
e1=sp.Matrix([1,0]); e2=sp.Matrix([0,1])
basis=(e1,e2)

def mul(x,y):
    return sp.Matrix([sp.expand((x[0]+x[1])*y[0]),sp.expand(x[1]*y[1])])

# Anti-flexible identity.
for x,y,z in product(basis,repeat=3):
    ass1=mul(mul(x,y),z)-mul(x,mul(y,z))
    ass2=mul(mul(z,y),x)-mul(z,mul(y,x))
    assert sp.simplify(ass1-ass2)==sp.zeros(2,1)

def ndef(x,y):
    Nx,Ny=N*x,N*y
    inside=mul(Nx,y)+mul(x,Ny)-N*mul(x,y)
    return sp.simplify(mul(Nx,Ny)-N*inside)

vals=[]
for x,y in product(basis,repeat=2):
    vals.append(tuple(sp.factor(z) for z in ndef(x,y)))
expected=[
    (b*c,-c*(a-d)),
    (0,-b*c),
    (0,-b*c),
    (b*b,0),
]
assert vals==expected,(vals,expected)

def mq(x,y,q):
    return (((x[0]+x[1])*y[0])%q,(x[1]*y[1])%q)

def mv(M,x,q):
    return ((M[0]*x[0]+M[1]*x[1])%q,
            (M[2]*x[0]+M[3]*x[1])%q)

def is_nij(M,q):
    bas=((1,0),(0,1))
    for x,y in product(bas,repeat=2):
        Nx,Ny=mv(M,x,q),mv(M,y,q)
        lhs=mq(Nx,Ny,q)
        p1=mq(Nx,y,q); p2=mq(x,Ny,q); p3=mv(M,mq(x,y,q),q)
        inside=((p1[0]+p2[0]-p3[0])%q,(p1[1]+p2[1]-p3[1])%q)
        if lhs!=mv(M,inside,q):
            return False
    return True

def is_rb0(M,q):
    bas=((1,0),(0,1))
    for x,y in product(bas,repeat=2):
        Rx,Ry=mv(M,x,q),mv(M,y,q)
        lhs=mq(Rx,Ry,q)
        p1=mq(Rx,y,q); p2=mq(x,Ry,q)
        inside=((p1[0]+p2[0])%q,(p1[1]+p2[1])%q)
        if lhs!=mv(M,inside,q):
            return False
    return True

def rank2(M,q):
    if all(z%q==0 for z in M): return 0
    return 2 if (M[0]*M[3]-M[1]*M[2])%q else 1

def is_aut(M,q):
    if rank2(M,q)!=2: return False
    bas=((1,0),(0,1))
    for x,y in product(bas,repeat=2):
        if mv(M,mq(x,y,q),q)!=mq(mv(M,x,q),mv(M,y,q),q):
            return False
    return True

for q in (2,3,5,7):
    mats=list(product(range(q),repeat=4))
    nij={M for M in mats if is_nij(M,q)}
    predicted={M for M in mats if M[1]%q==0 and (M[2]*(M[0]-M[3]))%q==0}
    assert nij==predicted
    assert len(nij)==2*q*q-q
    ranks=Counter(rank2(M,q) for M in nij)
    assert tuple(ranks[i] for i in range(3))==(1,3*(q-1),2*(q-1)**2)

    aut={M for M in mats if is_aut(M,q)}
    assert aut=={(1,0,0,1)}

    rb={M for M in mats if is_rb0(M,q)}
    expected_rb={(0,0,t,0) for t in range(q)}
    assert rb==expected_rb

    print({"q":q,"nijenhuis":len(nij),
           "rank_profile":tuple(ranks[i] for i in range(3)),
           "automorphisms":len(aut),"rb0":len(rb)})

print("VERIFY_OK")
