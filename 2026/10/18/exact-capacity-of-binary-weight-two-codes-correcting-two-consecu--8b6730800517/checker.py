#!/usr/bin/env python3
"""Reproducibility checks for fixed-weight-two exact two-consecutive-deletion codes."""
from itertools import combinations

def desc(n, pos):
    s = [0] * n
    s[pos[0]] = s[pos[1]] = 1
    return {tuple(s[:i] + s[i+2:]) for i in range(n-1)}

def construction(n):
    pairs = [(0,1)]
    for r in range((n+3)//4+1):
        for p in [(4*r+1,4*r+3),(4*r+2,4*r+4),(4*r+3,4*r+6)]:
            if p[1] < n:
                pairs.append(p)
    return pairs

def independent_alpha(m):
    return ((m+1)//2+1)//2 + (m//2+1)//2

def upper(n):
    m = n-2
    return (m + independent_alpha(m) + 1)//2

def exhaustive(n):
    allpairs = list(combinations(range(n),2))
    outcomes = [desc(n,p) for p in allpairs]
    # independent check of classification of all near and far deletion images
    singleton_occupied = {}
    for p,dset in zip(allpairs,outcomes):
        i,j=p
        singletons = {w.index(1) for w in dset if sum(w)==1}
        expect= ({i} if j-i==1 and i==0 else None)
        if j-i==2: assert singletons == {i}, (n,p,singletons)
        if j-i>=3: assert singletons == {i,j-2}, (n,p,singletons)
        if j-i==1: assert len(singletons)>=1, (n,p,singletons)
    # the claimed forbidden near-near pair conflict
    for i in range(n-4):
        assert desc(n,(i,i+2)) & desc(n,(i+2,i+4)), (n,i)

for n in range(3,301):
    got=construction(n)
    target=3*(n-1)//4
    assert len(got)==target==upper(n), (n,len(got),target,upper(n))
    owned={}
    for p in got:
        for word in desc(n,p):
            assert word not in owned, (n,p,owned.get(word),word)
            owned[word]=p
for n in range(3,35):
    exhaustive(n)
print('WEIGHT_TWO_TWO_BURST_PASS constructive_lengths=3..300 near_far_lemmas_lengths=3..34')
