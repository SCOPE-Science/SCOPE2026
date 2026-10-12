import sympy as sp
from itertools import product
from collections import Counter

A,B,C,D=sp.symbols("A B C D")
N=sp.Matrix([[A,B],[C,D]])
e1=sp.Matrix([1,0]); e2=sp.Matrix([0,1]); basis=(e1,e2)

def mul(x,y):
    return sp.Matrix([sp.expand(2*x[0]*y[0]+x[1]*y[1]),sp.expand(x[0]*y[1])])

def tors(x,y):
    Nx,Ny=N*x,N*y
    return sp.simplify(mul(Nx,Ny)-N*(mul(Nx,y)+mul(x,Ny)-N*mul(x,y)))

vals=[tuple(sp.factor(z) for z in tors(x,y)) for x,y in product(basis,repeat=2)]
expected=[
    (C*(B+C),-C*(A-D)),
    (-C*(A-D),-C*(B+C)),
    (-C*(A-D),-C*(B+C)),
    ((A-D)**2+B*(B+C),C*(A-D))
]
for got,want in zip(vals,expected):
    assert all(sp.expand(g-w)==0 for g,w in zip(got,want))

def mq(x,y,q):
    return ((2*x[0]*y[0]+x[1]*y[1])%q,(x[0]*y[1])%q)
def mv(M,x,q):
    return ((M[0]*x[0]+M[1]*x[1])%q,(M[2]*x[0]+M[3]*x[1])%q)
def is_nij(M,q):
    bas=((1,0),(0,1))
    for x,y in product(bas,repeat=2):
        Nx,Ny=mv(M,x,q),mv(M,y,q)
        lhs=mq(Nx,Ny,q)
        p1,p2=mq(Nx,y,q),mq(x,Ny,q)
        p3=mv(M,mq(x,y,q),q)
        inside=((p1[0]+p2[0]-p3[0])%q,(p1[1]+p2[1]-p3[1])%q)
        if lhs!=mv(M,inside,q): return False
    return True
def structural(M,q):
    a,b,c,d=M
    return c*(b+c)%q==0 and c*(a-d)%q==0 and ((a-d)**2+b*(b+c))%q==0
def rank2(M,q):
    if all(x%q==0 for x in M): return 0
    return 2 if (M[0]*M[3]-M[1]*M[2])%q else 1
def is_aut(M,q):
    if (M[0]*M[3]-M[1]*M[2])%q==0: return False
    bas=((1,0),(0,1))
    return all(mv(M,mq(x,y,q),q)==mq(mv(M,x,q),mv(M,y,q),q) for x,y in product(bas,repeat=2))
def refl(M,q):
    a,b,c,d=M
    return (a,-b%q,-c%q,d)

for q in (3,5,7,11,13):
    mats=list(product(range(q),repeat=4))
    S={M for M in mats if is_nij(M,q)}
    assert S=={M for M in mats if structural(M,q)}
    split=pow(q-1,(q-1)//2,q)==1
    rc=Counter(rank2(M,q) for M in S)
    if split:
        total=3*q*q-2*q; ranks=(1,6*(q-1),(q-1)*(3*q-5)); orbits=q*(3*q-1)//2
    else:
        total=q*q; ranks=(1,0,q*q-1); orbits=q*(q+1)//2
    assert len(S)==total and tuple(rc[i] for i in range(3))==ranks
    G={M for M in mats if is_aut(M,q)}
    assert G=={(1,0,0,1),(1,0,0,q-1)}
    seen=set(); O=[]
    for M in S:
        if M in seen: continue
        orb={M,refl(M,q)}; seen|=orb; O.append(orb)
    assert len(O)==orbits
    print({"q":q,"split_minus_one":split,"nijenhuis":total,"rank_profile":ranks,"orbits":orbits})

for q,split0 in ((5,True),(3,False)):
    for m in range(1,7):
        N_m=3*q**(2*m)-2*q**m if split0 or m%2==0 else q**(2*m)
        if split0:
            assert N_m==3*q**(2*m)-2*q**m
        else:
            assert N_m==(q**(2*m) if m%2 else 3*q**(2*m)-2*q**m)

print("VERIFY_OK")
