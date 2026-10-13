#!/usr/bin/env python3
"""Exact binary truth-table verification for natural-order first-order Reed--Muller codes."""
from collections import Counter

def rank(vectors):
    pivots = {}
    for x in vectors:
        y=x
        while y:
            b=y.bit_length()-1
            if b in pivots: y^=pivots[b]
            else: pivots[b]=y;break
    return len(pivots)

def inspect(m):
    n=1<<m
    weights={}
    for a in range(1<<m):
        for b in (0,1):
            word=[((a&x).bit_count()&1)^b for x in range(n)]
            wt=sum(word[x] or word[(x+1)%n] for x in range(n))
            weights[(a,b)]=wt
    expected={0:1,n:3}
    for j in range(1,n//2): expected[n//2+j]=4
    assert dict(Counter(weights.values()))==expected,(m,Counter(weights.values()),expected)
    for t in range(0,n+1):
        qualifying=[a|(b<<m) for (a,b),w in weights.items() if a or b if 0<w<=t]
        components=1<<(m+1-rank(qualifying))
        if t<n//2+1: target=1<<(m+1)
        else:
            j=t-n//2
            target=1<<max(0,m-2-(j.bit_length()-1))
        assert components==target,(m,t,components,target)
    return m,n,len(expected)

if __name__=='__main__':
    for m in range(2,9):
        r=inspect(m);print(f'm={m} n={r[1]} distinct_pair_weights={r[2]}')
    print('VERIFY_OK')
