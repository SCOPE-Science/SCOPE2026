#!/usr/bin/env python3
"""Exact rational Hilbert maximal-norm certificate for K_{2,3}."""
from itertools import product
from collections import Counter
from fractions import Fraction

N=5
EDGES=tuple((i,j) for i in range(2) for j in range(2,5))
NEIGH=[set() for _ in range(N)]
for u,v in EDGES: NEIGH[u].add(v);NEIGH[v].add(u)
BALLS=set()
for c in range(N):
    reached={c}; BALLS.add(tuple(sorted(reached)))
    frontier={c}
    while frontier:
        next_front=set().union(*(NEIGH[v] for v in frontier))-reached
        if not next_front:break
        reached|=next_front; BALLS.add(tuple(sorted(reached)));frontier=next_front
BALLS=sorted(BALLS,key=lambda b:(len(b),b))
ROWS=[[(tuple(60//len(b) if j in b else 0 for j in range(N)),b) for b in BALLS if i in b] for i in range(N)]
assert [len(c) for c in ROWS]==[6,6,5,5,5]

def det_bareiss(a):
    n=len(a)
    if n==0:return 1
    a=[list(map(int,row)) for row in a]
    sign=1;den=1
    for k in range(n-1):
        if a[k][k]==0:
            jj=next((r for r in range(k+1,n) if a[r][k]),None)
            if jj is None:return 0
            a[k],a[jj]=a[jj],a[k];sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=a[i][j]*pivot-a[i][k]*a[k][j]
                assert num%den==0
                a[i][j]=num//den
        for i in range(k+1,n):a[i][k]=0
        den=pivot
    return sign*a[-1][-1]

def gram(R):
    return [[sum(r[i]*r[j] for r in R) for j in range(N)] for i in range(N)]

def scalar_poly_on_matrix(G):
    # Check the expected invariant subspaces directly via exact integer arithmetic.
    def apply(v):return [sum(G[i][j]*v[j] for j in range(N)) for i in range(N)]
    oneA=(1,-1,0,0,0)
    bdiff1=(0,0,1,-1,0);bdiff2=(0,0,0,1,-1)
    assert apply(oneA)==[3600*t for t in oneA]
    for v in (bdiff1,bdiff2):assert apply(v)==[400*t for t in v]
    ea=(1,1,0,0,0);eb=(0,0,1,1,1)
    # A^TA on the (a,a,b,b,b) vectors:
    # lambda a = (5 a + b)/3
    # lambda b = (2a+b)/9
    # i.e. integer T^TT has columns 3600*(5/3,2/9), 3600*(1/3,1/9).
    assert apply(ea)==[6000,6000,800,800,800]
    assert apply(eb)==[1200,1200,400,400,400]

special=(0,0,1,1,1)
assert [ROWS[i][special[i]][1] for i in range(N)]==[(0,),(1,),(0,1,2),(0,1,3),(0,1,4)]
strict=0;checked=0;min_first=10**30
for config in product(*(range(len(rs)) for rs in ROWS)):
    R=[ROWS[i][config[i]][0] for i in range(N)]
    G=gram(R)
    if config==special:
        scalar_poly_on_matrix(G)
        continue
    P=[[6156*(i==j)-G[i][j] for j in range(N)] for i in range(N)]
    for k in range(1,N+1):
        d=det_bareiss([row[:k] for row in P[:k]])
        if d<=0:raise AssertionError(('nonpositive Sylvester determinant',config,k,d))
    strict+=1
    min_first=min(min_first,P[0][0])
    checked+=1
assert strict==4499
# Exact witness ratio: x=(1,1,b,b,b), b=(sqrt(55)-7)/3, is positive;
# squared norm root (8+sqrt(55))/9.
# Rational separation: sqrt(55)>739/100 because 55*(10000)>739^2.
assert 550000>739**2
print('CERTIFICATE_OK selections=4500 strict=4499 exceptional=1 threshold=171/100 root=(8+sqrt55)/9')
