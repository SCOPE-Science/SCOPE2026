#!/usr/bin/env python3
"""Exact finite replay for odd-hypercube middle-layer actuator construction.
Python 3 standard library only. Analytical proof covers every odd dimension;
finite rank tests are independent consistency checks, not proof by enumeration.
"""
from itertools import combinations
from math import comb

def masks(n,k):
    return [sum(1 << i for i in c) for c in combinations(range(n),k)]

def rank_mod(a, p=1000003):
    a = [[v % p for v in row] for row in a]
    if not a: return 0
    m, cols = len(a), len(a[0])
    rank = 0
    for col in range(cols):
        pivot = next((i for i in range(rank,m) if a[i][col]), None)
        if pivot is None: continue
        a[rank],a[pivot]=a[pivot],a[rank]
        inv=pow(a[rank][col],-1,p)
        a[rank][col:]=[(v*inv)%p for v in a[rank][col:]]
        pivotrow=a[rank]
        for i in range(rank+1,m):
            f=a[i][col]
            if f:
                a[i][col:]=[(x-f*y)%p for x,y in zip(a[i][col:],pivotrow[col:])]
        rank+=1
        if rank==m:return rank
    return rank

def harmonic_pairs_value(mask,t):
    out=1
    for i in range(t):
        a=(mask>>(2*i))&1; b=(mask>>(2*i+1))&1
        out*=a-b
    return out

def alpha(r,t,j):
    q=j-t
    return ((-2)**t)*((-1)**(q//2))*comb(r-t,q//2)

def check():
    asserts=0
    for n in [3,5,7,9]:
        r=n//2; rows=masks(n,r)
        for j in range(r+1):
            cols=masks(n,j)
            matrix=[[(-1 if (x&y).bit_count()%2 else 1) for y in cols] for x in rows]
            actual=rank_mod(matrix)
            expected=len(cols)
            assert actual==expected,(n,j,actual,expected)
            asserts+=1
            for t in range(j+1):
                weight=[harmonic_pairs_value(y,t) for y in cols]
                factor=alpha(r,t,j)
                assert factor!=0
                for ix,x in enumerate(rows):
                    left=sum(v*w for v,w in zip(matrix[ix],weight))
                    right=factor*harmonic_pairs_value(x,t)
                    assert left==right,(n,j,t,x,left,right)
                    asserts+=1
    for r in range(1,51):
        for j in range(r+1):
            for t in range(j+1):
                # coefficient (1-z^2)^(r-t)(1+z) never vanishes for 0 <= j-t <= r-t
                q=j-t
                c=(-1)**(q//2)*comb(r-t,q//2)
                assert c !=0
                asserts+=1
    for n in [2,4,6,8]:
        r=n//2; rows=masks(n,r); cols=masks(n,r)
        assert rank_mod([[(-1 if (x&y).bit_count()%2 else 1) for y in cols] for x in rows]) < len(cols)
        asserts+=1
    print('VERIFICATION_OK assertions=',asserts,'odd ranks n=3,5,7,9; harmonic identities; coefficient nonzero r<=50; even-rank obstruction')

if __name__=='__main__':
    check()
