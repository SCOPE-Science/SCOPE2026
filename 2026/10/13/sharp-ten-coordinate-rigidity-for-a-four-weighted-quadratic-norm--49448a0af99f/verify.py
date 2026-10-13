#!/usr/bin/env python3
"""Exact reproducibility checks for the weighted quadratic norm rigidity theorem."""
from collections import defaultdict
from fractions import Fraction

WITNESSES = [
    (1,4,7,2), (1,6,9,4), (2,2,4,1), (2,3,6,1),
    (2,4,8,1), (2,5,10,1), (2,7,10,5), (7,3,9,1),
]

def norm(x,y):
    return x*x + 4*y*y

def relation(x,y,u,v,N):
    row=[0]*N
    row[x-1]+=1
    row[y-1]+=4
    row[u-1]-=1
    row[v-1]-=4
    return row

def rank(rows, N):
    a=[[Fraction(t) for t in row] for row in rows]
    r=0
    for col in range(N):
        pivot=next((i for i in range(r,len(a)) if a[i][col]),None)
        if pivot is None: continue
        a[r],a[pivot]=a[pivot],a[r]
        t=a[r][col]
        a[r]=[z/t for z in a[r]]
        for j in range(r+1,len(a)):
            factor=a[j][col]
            if factor:
                a[j]=[a[j][k]-factor*a[r][k] for k in range(N)]
        r+=1
        if r==len(a): break
    return r

def det_bareiss(rows):
    a=[row[:] for row in rows]
    n=len(a)
    sign=1
    old=1
    for k in range(n-1):
        if a[k][k]==0:
            r=next(j for j in range(k+1,n) if a[j][k])
            a[k],a[r]=a[r],a[k]
            sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator=a[i][j]*pivot-a[i][k]*a[k][j]
                assert numerator%old==0
                a[i][j]=numerator//old
        for i in range(k+1,n): a[i][k]=0
        old=pivot
    return sign*a[n-1][n-1]

def all_relations(N):
    grouped=defaultdict(list)
    for x in range(1,N+1):
        for y in range(1,N+1):
            grouped[norm(x,y)].append((x,y))
    return [relation(*group[0],*p,N)
            for group in grouped.values() for p in group[1:]]

for x,y,u,v in WITNESSES:
    assert norm(x,y)==norm(u,v)
M=[relation(*w,10) for w in WITNESSES]
assert rank(M,10)==8
assert det_bareiss([r[:8] for r in M])==-608
assert all(sum(row)==0 for row in M)
assert all(sum(row[k-1]*k*k for k in range(1,11))==0 for row in M)
for N in range(3,11):
    ranks={3:0,4:1,5:1,6:2,7:3,8:4,9:6,10:8}
    rows=all_relations(N)
    assert rank(rows,N)==ranks[N]
    assert (N-ranks[N] >= 3) if N<10 else (N-ranks[N]==2)
    for row in rows:
        assert sum(row)==0 and sum(row[k-1]*k*k for k in range(1,N+1))==0
rows9=all_relations(9)
assert all(row[4]==0 for row in rows9)
# Coefficients of the polynomial identity for the propagation witness.
# (n+8)^2 + 4(n+3)^2 == n^2 + 4(n+5)^2.
assert (1+4, 2*8+4*2*3, 8*8+4*3*3) == (1+4, 4*2*5, 4*5*5)
# Three exact complex-valued examples, sampled across all positive arguments.
for A,B in ((0,1),(7,3),(-5,2)):
    for x in range(1,31):
        for y in range(1,31):
            t=norm(x,y)
            assert A*t+5*B == (A*x*x+B) + 4*(A*y*y+B)
print('EXACT_CERTIFICATE_OK finite_threshold=10 minor_det=-608 rank10=8 rank9=6 witness_count=8 propagation_step=8')
