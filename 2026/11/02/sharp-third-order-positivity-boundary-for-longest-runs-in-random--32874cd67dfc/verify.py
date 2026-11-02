#!/usr/bin/env python3
"""Exact finite census and infinite-family arithmetic for composition maximum kernel.
Standard library only. No floating-point arithmetic.
"""
from itertools import combinations
from functools import lru_cache
from math import comb

@lru_cache(None)
def bounded(n, r, cap):
    if r == 0:
        return int(n == 0)
    if n < r or cap <= 0:
        return 0
    return sum(bounded(n-t, r-1, cap) for t in range(1, min(n, cap)+1))

def count(n, r, m):
    return bounded(n, r, m) - bounded(n, r, m-1)

def det(a):
    if len(a) == 1:
        return a[0][0]
    if len(a) == 2:
        return a[0][0]*a[1][1]-a[0][1]*a[1][0]
    assert len(a)==3
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
            -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
            +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))

def exhaustive_counts(n):
    # Independently enumerate all cut-subsets of {1,...,n-1}.
    a = [[0]*n for _ in range(n)]
    for mask in range(1 << (n-1)):
        cuts = [j for j in range(1, n) if (mask >> (j-1)) & 1]
        parts = [b-a for a,b in zip([0]+cuts, cuts+[n])]
        a[len(parts)-1][n-max(parts)] += 1
    return a

checks = 0
for n in range(1,10):
    a = [[count(n, r, m) for m in range(n,0,-1)] for r in range(1,n+1)]
    assert a == exhaustive_counts(n), f'composition census differs at n={n}'
    checks += 1
    tally={}
    for k in range(1,min(3,n)+1):
        tally[k]=0
        for rows in combinations(range(n),k):
            for cols in combinations(range(n),k):
                v=det([[a[i][j] for j in cols] for i in rows])
                assert v>=0,(n,k,rows,cols,v)
                tally[k]+=1
    checks += sum(tally.values())
    print(f'n={n}: TN3 all minors nonnegative; checked {tally}')

for n in range(10,301):
    q=n//2
    if n%2==0:
        a=[[2,2,1],[3*(q-3),3*(q-2),3*(q-1)],
           [2*(q-3)*(q-4),2*(q-2)*(q-3),2*(q-1)*(q-2)]]
        expected=-6*(q*q-5*q+2)
        maxima=[q+2,q+1,q]
    else:
        a=[[2,2,0],[3*(q-2),3*(q-1),3*(q-1)],
           [2*(q-2)*(q-3),2*(q-1)*(q-2),2*q*(q-1)]]
        expected=-12*(q-4)*(q-1)
        maxima=[q+2,q+1,q]
    b=[[count(n,r,m) for m in maxima] for r in (2,3,4)]
    assert a == b,(n,a,b)
    assert det(a)==expected<0,(n,a,det(a),expected)
    checks += 2
print('PASS:', checks, 'independent matrix comparisons, exact minor inequalities, and family-witness checks')
