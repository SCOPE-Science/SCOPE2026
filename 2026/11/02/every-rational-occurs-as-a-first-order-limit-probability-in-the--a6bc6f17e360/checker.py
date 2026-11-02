#!/usr/bin/env python3
"""Finite independent checks of balanced non-overlapping witnesses."""
from functools import lru_cache
from math import comb

def patterns(b):
    return [tuple([1,1,2]+[2,2]*(i)+[1,2]+[2,2]*(b-i-1)+[2,2]) for i in range(b)]

def comps(n):
    if n==0:
        yield ()
    if n>=1:
        for tail in comps(n-1): yield (1,)+tail
    if n>=2:
        for tail in comps(n-2): yield (2,)+tail

def first_hit(s, ps):
    L=len(ps[0]);lookup={w:i for i,w in enumerate(ps)}
    for t in range(len(s)-L+1):
        i=lookup.get(s[t:t+L]);
        if i is not None:return i
    return None

def finite_counts(b,n):
    p=patterns(b);counts=[0]*b;none=0
    for seq in comps(n):
        i=first_hit(seq,p)
        if i is None: none+=1
        else:counts[i]+=1
    return counts,none

def check():
    for b in range(2,11):
        ps=patterns(b);L=2*b+5
        assert len(set(ps))==b
        assert all(len(w)==L and w.count(1)==3 and w.count(2)==2*b+2 for w in ps)
        for u in ps:
            for v in ps:
                for t in range(1,L):
                    assert u[-t:]!=v[:t], (b,u,v,t)
    print('CROSS_BIFIX_FREE_ALL_B_2_TO_10')
    for b,nlo,nhi in [(2,15,22),(3,19,24),(4,23,26)]:
        for n in range(nlo,nhi+1):
            counts,none=finite_counts(b,n)
            assert len(set(counts))==1, (b,n,counts,none)
            print('COUNTS',b,n,counts[0],none)
    # All valid composition-to-permutation classes are Av(231,312,321)
    from itertools import combinations
    def toperm(s):
        res=[];v=0
        for k in s:
            res.extend(range(v+k,v,-1));v+=k
        return res
    def pat3(a,b,c):
        s=sorted([a,b,c]);return tuple(s.index(v)+1 for v in [a,b,c])
    for n in range(1,11):
        for s in comps(n):
            perm=toperm(s)
            assert all(pat3(*[perm[i] for i in inds]) not in ((2,3,1),(3,1,2),(3,2,1)) for inds in combinations(range(n),3))
            assert len(perm)==n
    print('CLASS_AVOIDANCE_ALL_N_TO_10')
    print('ALL_CHECKS_OK')
if __name__=='__main__': check()
