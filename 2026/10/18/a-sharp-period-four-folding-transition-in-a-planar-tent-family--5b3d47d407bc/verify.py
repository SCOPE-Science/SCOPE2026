#!/usr/bin/env python3
"""Independent rational checks for the exact four-cycle theorem.

Only the Python standard library is used. The global theorem is established by
symbolic identities in RESULT.md; finite test parameters are not its proof.
"""
from fractions import Fraction as F
from itertools import product

L=((1,1),(1,-1)); R=((-1,1),(-1,-1))

def plus(a,b):
    return (a[0]+b[0],a[1]+b[1])
def times(k,a):
    return (k*a[0],k*a[1])
def apply(t,a,z):
    x,y=z
    if a==0: return (t*(x+y),t*(x-y))
    return (t*(2-x+y),t*(2-x-y))
def matmul(a,b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))
def matvec(a,z):
    return (a[0][0]*z[0]+a[0][1]*z[1],a[1][0]*z[0]+a[1][1]*z[1])
def linear_step(t,a):
    base=L if a==0 else R
    return tuple(tuple(t*u for u in row) for row in base), ((F(0),F(0)) if a==0 else (2*t,2*t))
def orbit_for_word(t,w):
    # Affine symbolic itinerary return z -> Mz+c; solve (I-M)z=c.
    mat=((F(1),F(0)),(F(0),F(1)))
    c=(F(0),F(0))
    for a in w:
        m,d=linear_step(t,a)
        mat=matmul(m,mat)
        c=plus(matvec(m,c),d)
    a,b=1-mat[0][0],-mat[0][1]
    cc,d=-mat[1][0],1-mat[1][1]
    det=a*d-b*cc
    assert det!=0
    x=(d*c[0]-b*c[1])/det
    y=(a*c[1]-cc*c[0])/det
    seed=(x,y)
    seq=[]
    for label in w:
        seq.append(seed)
        seed=apply(t,label,seed)
    assert seed==(x,y)
    return seq,det

def admissible(t,w,seq):
    for label,(x,y) in zip(w,seq):
        if not (0<=x<=2 and 0<=y<=x and y<=2-x): return False
        if (label==0 and x>1) or (label==1 and x<1): return False
    return True

def necklaces(n):
    for w in product((0,1),repeat=n):
        if w == min(w[j:]+w[:j] for j in range(n)):
            yield w

def primitive(seq):
    n=len(seq)
    return all(seq[0]!=seq[d] for d in range(1,n) if n%d==0)

def count(t,n):
    result=[]
    for w in necklaces(n):
        seq,det=orbit_for_word(t,w)
        if admissible(t,w,seq) and primitive(seq):
            result.append((''.join(map(str,w)),seq))
    return result

def p(t): return 4*t**4-2*t-1

def exact_seed_0001(t):
    z=2*t/(4*t**4+1)
    return (z,z)
def exact_seed_0011(t):
    return (2*t*(8*t**5-4*t**4+1)/(16*t**8+1),
            2*t*(4*t**4-2*t+1)/(16*t**8+1))
def exact_seed_0111(t):
    return (2*t/(2*t*t+1), 2*t/(2*t*t+2*t+1))

assert p(F(9175,10000))<0<p(F(918,1000))
assert p(F(9,10))<0<p(F(23,25))

checks=0
for t,expected4 in [(F(89,100),1),(F(9,10),1),(F(23,25),3),
                    (F(19,20),3),(F(1),3)]:
    out1=count(t,1)
    out2=count(t,2)
    out4=count(t,4)
    assert len(out1)==2, (t,out1)
    assert len(out2)==1, (t,out2)
    assert len(out4)==expected4,(t,out4)
    assert {x[0] for x in out4}==({'0001'} if expected4==1 else {'0001','0011','0111'})
    # Nonperiodic length-four words are excluded via exact minimum-period check.
    assert len(out1)+2*len(out2)+4*len(out4)==(8 if expected4==1 else 16)
    for w,seedfun in [('0001',exact_seed_0001),('0011',exact_seed_0011),('0111',exact_seed_0111)]:
        pts,det=orbit_for_word(t,tuple(map(int,w)))
        assert pts[0]==seedfun(t)
        checks+=1
    # Exhaustive binary itineraries up to four, including nonprimitive sequences.
    for n in (1,2,4):
        for w in product((0,1),repeat=n):
            seq,det=orbit_for_word(t,w)
            if admissible(t,w,seq):
                x,y=seq[0]
                z=(x,y)
                for i in range(n):
                    z=apply(t,int(z[0]>1),z)
                assert z==(x,y)
                checks+=1

# Exact polynomial identities behind the switching collision.
for t in (F(89,100),F(9,10),F(23,25),F(19,20),F(1)):
    x1=apply(t,0,exact_seed_0011(t))[0]
    a1=apply(t,0,exact_seed_0111(t))[0]
    assert x1-1==-(2*t*t-1)*(2*t*t-2*t+1)*p(t)/(16*t**8+1)
    assert a1-1==p(t)/((2*t*t+1)*(2*t*t+2*t+1))
    assert exact_seed_0011(t)[0]-exact_seed_0111(t)[0]==-(4*t**3*(2*t*t-2*t+1)*p(t))/((2*t*t+1)*(16*t**8+1))
    assert exact_seed_0011(t)[1]-exact_seed_0111(t)[1]==-(4*t**3*(2*t*t-1)*p(t))/((16*t**8+1)*(2*t*t+2*t+1))
    checks+=4

print('PASS: five exact-rational parameter censuses, all cyclic itineraries,')
print('period reduction, branch membership, algebraic seeds, and collision identities.')
print('Exact verification checks:', checks)
print('The endpoint root and all-parameter sign conclusions are proved analytically in RESULT.md.')
