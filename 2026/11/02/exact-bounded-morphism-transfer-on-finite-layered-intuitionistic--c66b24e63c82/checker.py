#!/usr/bin/env python3
"""Independent direct tests of exact surjective bounded morphism counts for weak orders."""
from itertools import product
from math import comb, factorial
from functools import lru_cache

@lru_cache(None)
def stirling(n,k):
    if n==0: return 1 if k==0 else 0
    if k==0: return 0
    return k*stirling(n-1,k)+stirling(n-1,k-1)

def onto(n,k):
    return factorial(k)*stirling(n,k)

def optional(n,k):
    return onto(n,k)+onto(n,k+1)

def rec_count(a,b):
    h,k=len(a),len(b)
    # state number j: exactly j bottom target levels still absent; top (k-j) fully covered
    dp={k:1}
    for src in reversed(a):
        nxt={}
        for j,w in dp.items():
            if j<k and b[j]==1:  # frontier (lowest present) singleton
                nxt[j]=nxt.get(j,0)+w
            if j>0:
                v=onto(src,b[j-1])
                if j<k and b[j]==1:
                    v=optional(src,b[j-1])
                nxt[j-1]=nxt.get(j-1,0)+w*v
        dp=nxt
    return dp.get(0,0)

def weak_order(level_sizes):
    L=[]
    for i,s in enumerate(level_sizes):L.extend([i]*s)
    return L

def direct(a,b):
    A=weak_order(a);B=weak_order(b);N=len(A);M=len(B)
    upsA=[tuple(z for z in range(N) if z==x or A[z]>A[x]) for x in range(N)]
    upsB=[frozenset(z for z in range(M) if z==y or B[z]>B[y]) for y in range(M)]
    c=0
    for f in product(range(M),repeat=N):
        if len(set(f))<M:continue
        if all(
            (all((z==x or A[z]>A[x]) <= (f[z]==f[x] or B[f[z]]>B[f[x]]) for z in range(N))
             and all(any((z==x or A[z]>A[x]) and f[z]==y for z in range(N)) for y in upsB[f[x]]))
            for x in range(N)):
            c+=1
    return c

def all_shapes(max_size,max_levels=3):
    for h in range(1,max_levels+1):
        for vals in product(range(1,4), repeat=h):
            if sum(vals)<=max_size:yield vals

def test():
    runs=0
    for a in all_shapes(6):
        for b in all_shapes(5):
            if sum(b)>sum(a):continue
            exp=rec_count(a,b)
            got=direct(a,b)
            assert got==exp,(a,b,exp,got)
            runs+=1
    print('DIRECT_MATCHED',runs)
    for h in range(1,5):
        for a in product(range(2,5),repeat=h):
            for b in product(range(2,5),repeat=h):
                expected=1
                for ai,bi in zip(a,b):expected*=onto(ai,bi)
                assert rec_count(a,b)==expected,(a,b)
            for b in product(range(2,5),repeat=h+1):
                assert rec_count(a,b)==0,(a,b)
    print('THICK_TARGET_TESTS_OK')
    print('SAMPLE',[(a,b,rec_count(a,b)) for a,b in [((2,2),(2,2)),((3,3),(2,2)),((2,2,2),(2,2)),((2,2,2),(1,2)),((2,2,2),(2,1)),((2,2,2),(1,1)),((1,2),(1,1))]])
    print('ALL_CHECKS_OK')
if __name__=='__main__':test()
