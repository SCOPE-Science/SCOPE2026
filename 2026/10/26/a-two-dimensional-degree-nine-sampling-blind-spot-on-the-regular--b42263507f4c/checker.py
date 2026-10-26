"""Exact checks for rhombicuboctahedral exact-degree harmonic sampling.
No floating-point rank calculations or external dependencies.
Run: python3 checker.py
"""
from fractions import Fraction as Q
from itertools import product
from functools import reduce
from math import gcd

# Rational quadratic arithmetic Q(sqrt(2)).
ZERO = (Q(0), Q(0))
ONE = (Q(1), Q(0))
ROOT = (Q(0), Q(1))

def add(x, y):
    return x[0]+y[0], x[1]+y[1]

def neg(x):
    return -x[0], -x[1]

def mul(x, y):
    return x[0]*y[0]+2*x[1]*y[1], x[0]*y[1]+x[1]*y[0]

def scale(x, r):
    return x[0]*r, x[1]*r

def inv(x):
    norm=x[0]*x[0]-2*x[1]*x[1]
    assert norm != 0
    return x[0]/norm, -x[1]/norm

def div(x,y):
    return mul(x, inv(y))

A=add(ONE,ROOT)
points=[]
for distinguished in range(3):
    for signs in product((1,-1), repeat=2):
        p=[ZERO,ZERO,ZERO]
        p[distinguished]=A
        indices=[j for j in range(3) if j!=distinguished]
        for j,s in zip(indices,signs):p[j]=scale(ONE,s)
        points.append(tuple(p))
assert len(points)==12
D=add(mul(A,A),scale(ONE,2))
T=[[div(reduce(add,(mul(x[k],y[k]) for k in range(3)),ZERO),D)
    for y in points] for x in points]
assert all(T[i][i]==ONE for i in range(12))

# Exact Legendre polynomial P_9(t), by three-term recurrence.
prev=[[ONE]*12 for i in range(12)]
curr=[r.copy() for r in T]
for ell in range(1,9):
    nex=[[scale(add(scale(mul(T[i][j],curr[i][j]),2*ell+1),
                    neg(scale(prev[i][j],ell))),Q(1,ell+1))
          for j in range(12)] for i in range(12)]
    prev,curr=curr,nex
# The three signed four-point blocks must have identical images under G_9.
w=(1,-1,-1,1)
U=[]
for block in range(3):
    vec=[0]*12
    for j in range(4):vec[4*block+j]=w[j]
    U.append(vec)
for i in (1,2):
    v=[U[0][j]-U[i][j] for j in range(12)]
    for row in curr:
        total=reduce(add,(scale(x,c) for x,c in zip(row,v)), ZERO)
        assert total==ZERO, (i,total)
# The nonzero 3-by-3 signed-block compression is an all-ones matrix.
expected=(Q(160453920,410338673),Q(-84575040,410338673))
for i in range(3):
    for j in range(3):
        total=reduce(add,(scale(curr[4*i+u][4*j+v],w[u]*w[v])
                   for u in range(4) for v in range(4)),ZERO)
        assert scale(total,Q(1,4))==expected
print('Exact Q(sqrt(2)) degree-nine rank-upper-bound checks: PASS')

# A Lucas primality certificate: p-1=2^23*7*17, with primitive root 3.
p=998244353
g=3
assert (p-1)==(2**23)*7*17
assert pow(g,p-1,p)==1
assert all(gcd(pow(g,(p-1)//q,p)-1,p)==1 for q in (2,7,17))
# Since 2,7,17 are prime, the preceding equalities prove p prime.
s=116195171
assert s*s%p==2
amod=(1+s)%p
dmod=(2+amod*amod)%p
assert dmod!=0
invden=pow(dmod,-1,p)
pts=[]
for distinguished in range(3):
    for signs in product((1,-1),repeat=2):
        z=[0]*3
        z[distinguished]=amod
        idx=[j for j in range(3) if j!=distinguished]
        z[idx[0]]=signs[0]%p
        z[idx[1]]=signs[1]%p
        pts.append(z)
t=[[sum(x[k]*y[k] for k in range(3))*invden%p
    for y in pts] for x in pts]

def rank_mod(matrix):
    m=[row[:] for row in matrix]
    n=len(m)
    pivot=0
    for col in range(len(m[0])):
        r=next((j for j in range(pivot,n) if m[j][col]),None)
        if r is None:continue
        m[pivot],m[r]=m[r],m[pivot]
        c=pow(m[pivot][col],-1,p)
        m[pivot]=[(z*c)%p for z in m[pivot]]
        for row in range(pivot+1,n):
            factor=m[row][col]
            if factor:
                m[row]=[(x-factor*y)%p for x,y in zip(m[row],m[pivot])]
        pivot+=1
        if pivot==n:break
    return pivot

p0=[[1]*12 for _ in range(12)]
p1=t
ranks=[rank_mod(p0),rank_mod(p1)]
for ell in range(1,115):
    im=pow(ell+1,-1,p)
    pnext=[[( ((2*ell+1)*t[i][j]*p1[i][j]
             -ell*p0[i][j]) *im)%p for j in range(12)] for i in range(12)]
    ranks.append(rank_mod(pnext))
    p0,p1=p1,pnext
assert len(ranks)==116
assert ranks[:6]==[1,3,5,7,9,11]
assert ranks[6:9]==[12,12,12]
assert ranks[9]==10
assert all(rank==12 for rank in ranks[10:])
print('Modular exact ranks, degrees 0..115: PASS')
print('Degrees 0..5:',ranks[:6],'; degrees 6..8:',ranks[6:9],
      '; degree 9:',ranks[9],'; all degrees 10..115:',set(ranks[10:]))

# Verify the strict-dominance high-degree constants entirely by rationals:
# |t_ij| <= (7+4sqrt(2))/17, and sin(arccos(t)) > 2/3.
# The inequality t_max^2<5/9 reduces to sqrt(2)<179/126.
assert Q(179,126)**2 > 2
# Then at degree 116: 11*sqrt[2/(pi*(116+1/2)*sin)] < 1,
# using pi>157/50 (=3.14), sin>2/3.
assert Q(121*2,1) < Q(157,50)*Q(233,2)*Q(2,3)
print('Global high-degree diagonal-dominance constants: PASS')

# Nonexceptional nearby parameter: rank 12 at degree nine for a=2.
a2=2
pts2=[]
for i in range(3):
    for b in product((1,-1),repeat=2):
        v=[0]*3;v[i]=a2;ids=[j for j in range(3) if j!=i]
        v[ids[0]]=b[0];v[ids[1]]=b[1];pts2.append(v)
T2=[[sum(x[k]*y[k] for k in range(3))*pow(6,-1,p)%p
     for y in pts2] for x in pts2]
x0=[[1]*12 for _ in range(12)];x1=T2
for ell in range(1,9):
    invell=pow(ell+1,-1,p)
    nx=[[( (2*ell+1)*T2[i][j]*x1[i][j]-ell*x0[i][j])*invell%p
         for j in range(12)] for i in range(12)]
    x0,x1=x1,nx
assert rank_mod(x1)==12
print('Parameter-deformation degree-nine rank at a=2: PASS')
print('ALL CHECKS PASSED')
