#!/usr/bin/env python3
"""Exact finite-state algebra for a three-site open TASEP with local resetting.

Uses only the Python standard library. It verifies polynomial identities over Q[r]
and independently solves the rational stationary equations at test parameters.
"""
from fractions import Fraction as F


def clean(v):
    v=list(v)
    while len(v)>1 and v[-1]==0: v.pop()
    return tuple(v)


def poly(x):
    if isinstance(x, tuple): return x
    return (F(x),)


def add(x,y):
    x,y=poly(x),poly(y)
    return clean([(x[i] if i<len(x) else 0)+(y[i] if i<len(y) else 0)
                  for i in range(max(len(x),len(y)))])


def neg(x): return tuple(-v for v in poly(x))

def sub(x,y): return add(x,neg(y))

def mul(x,y):
    x,y=poly(x),poly(y)
    z=[F(0)]*(len(x)+len(y)-1)
    for i,a in enumerate(x):
        for j,b in enumerate(y): z[i+j]+=a*b
    return clean(z)

def scale(x,c): return mul(poly(x),(F(c),))

def value(x,z):
    s=F(0)
    for a in reversed(poly(x)): s=s*z+a
    return s

R=(F(0),F(1))
H=mul(add(scale(R,3),5),add(add(scale(mul(R,R),6),scale(R,44)),55))
P=scale(H,2)
# Unnormalized probabilities in the bit order 000,001,...,111, denominator P.
weights=[
    scale(add(scale(R,6),5),2),
    (F(15),F(92),F(108),F(36)),
    scale(mul(add(scale(R,3),2),add(scale(R,6),5)),2),
    (F(55),F(144),F(72)),
    scale(add(scale(R,6),5),6),
    scale(mul(add(scale(R,3),1),add(scale(R,3),5)),12),
    scale(add(scale(R,3),5),18),
    scale(add(scale(R,3),5),54)
]
def sum_polys(v):
    s=(F(0),)
    for u in v: s=add(s,u)
    return s

assert sum_polys(weights)==P

# Construct polynomial generator directly from events without assuming any formula.
Q=[[(F(0),) for _ in range(8)] for _ in range(8)]
def move(m,j,rate):
    Q[m][j]=add(Q[m][j],rate)
    Q[m][m]=sub(Q[m][m],rate)
for m in range(8):
    if not m&1: move(m,m|1,(F(1,2),))
    if m&4: move(m,m&~4,(F(1,6),))
    for i in (0,1):
        if m&(1<<i) and not m&(1<<(i+1)):
            move(m,m^(1<<i)^(1<<(i+1)),(F(1),))
    if not m&1:
        for i in (1,2):
            if m&(1<<i): move(m,m^(1<<i)^1,R)
assert all(sum_polys(row)==(F(0),) for row in Q)
assert all(sum_polys([mul(weights[i],Q[i][j]) for i in range(8)])==(F(0),)
           for j in range(8))

quartic=(F(125),F(-125),F(-231),F(18),F(54))
adj12=(F(-2375),F(7070),F(21078),F(17460),F(5832),F(648))
adj23=(F(-125),F(-340),F(354),F(684),F(216))
expected={(0,2):scale(quartic,12),
          (0,1):scale(adj12,-2),
          (1,2):scale(adj23,-18)}
for (i,j),target in expected.items():
    ei=sum_polys([weights[m] for m in range(8) if m&(1<<i)])
    ej=sum_polys([weights[m] for m in range(8) if m&(1<<j)])
    eij=sum_polys([weights[m] for m in range(8) if m&(1<<i) and m&(1<<j)])
    assert sub(mul(eij,P),mul(ei,ej))==target, (i,j)

# Exact root isolation and sign profile. Descartes provides at most two positive roots.
for z,sign in [(F(0),1),(F(532,1000),1),(F(533,1000),-1),
               (F(1),-1),(F(2),-1),(F(2043,1000),-1),
               (F(2044,1000),1),(F(3),1)]:
    assert (value(quartic,z)>0) == (sign==1), z
assert value(adj12,F(1))>0 and value(adj23,F(1))>0
assert all(v>0 for v in adj12[1:])
# For r>=1 the derivative of adj23 is positive, and grows with r.
der_adj23=(adj23[1],2*adj23[2],3*adj23[3],4*adj23[4])
assert value(der_adj23,F(1))>0 and all(v>0 for v in der_adj23[1:])


def stationary_sample(rate):
    # A separate rational Gaussian solver for the actual generator at fixed rate.
    A=[]
    for j in range(8):
        if j==7: A.append([F(1)]*8+[F(1)]);continue
        A.append([value(Q[i][j],rate) for i in range(8)]+[F(0)])
    for k in range(8):
        pivot=next(i for i in range(k,8) if A[i][k])
        A[k],A[pivot]=A[pivot],A[k]
        fac=A[k][k]
        A[k]=[x/fac for x in A[k]]
        for i in range(8):
            if i!=k:
                fac=A[i][k]
                A[i]=[A[i][j]-fac*A[k][j] for j in range(9)]
    observed=[A[i][-1] for i in range(8)]
    analytic=[value(w,rate)/value(P,rate) for w in weights]
    assert observed==analytic
    return observed

for rate in [F(0),F(1,5),F(1,2),F(1),F(2),F(3),F(10),F(100)]:
    stationary_sample(rate)
print('PASS: 8 exact polynomial balance identities, normalization, 3 covariances,')
print('       root bracketing, adjacent negativity and 8 independent rational solves')
