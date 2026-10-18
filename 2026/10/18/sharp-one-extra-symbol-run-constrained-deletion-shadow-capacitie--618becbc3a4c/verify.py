#!/usr/bin/env python3
"""Independent exhaustive finite checks of a subsequence-deletion extremum."""
from itertools import product
from math import comb

def sizes(w):
    S=[set() for _ in range(len(w)+1)]
    S[0].add(())
    for a in w:
        for k in range(len(w),0,-1):
            S[k].update(x+(a,) for x in S[k-1])
    return [len(S[len(w)-t]) for t in range(len(w)+1)]

def formula(q,r,j,t):
    c=comb(r+1,t)-(comb(r-1,t-1) if t>=1 else 0)
    if t==q:
        c-=max(j-q,0)+max(r-j-q+1,0)
    return c

def run_count(w):
    return 1+sum(w[i]!=w[i-1] for i in range(1,len(w)))

canonical=0
for q in range(2,8):
    for r in range(q, min(q+10,17)):
        for j in range(1,r+1):
            w=tuple((i%q) for i in range(r))
            w=w[:j]+(w[j-1],)+w[j:]
            got=sizes(w)
            for t in range(q+1):
                assert got[t]==formula(q,r,j,t),(q,r,j,t,got[t],formula(q,r,j,t))
            canonical+=1
print('CANONICAL_OK',canonical)
# Exhaustively examine all (q,r)-run words of length r+1 for moderate parameters.
tested=0
for q,rmax in [(2,10),(3,9),(4,7)]:
    for r in range(q,rmax+1):
        best=[0]*(q+1)
        for seq in product(range(q),repeat=r):
            if any(seq[i]==seq[i-1] for i in range(1,r)):
                continue
            for j in range(r):
                w=seq[:j+1]+(seq[j],)+seq[j+1:]
                assert run_count(w)==r
                got=sizes(w)
                for t in range(q+1):
                    if got[t]>best[t]:best[t]=got[t]
                tested+=1
        pred=[max(formula(q,r,j,t) for j in range(1,r+1)) for t in range(q+1)]
        assert best==pred,(q,r,best,pred)
print('GLOBAL_EXHAUSTIVE_OK',tested)
