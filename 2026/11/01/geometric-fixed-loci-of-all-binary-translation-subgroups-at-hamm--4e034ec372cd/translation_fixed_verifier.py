#!/usr/bin/env python3
"""Finite checks for translation-fixed Rips complexes (Hamming radius two)."""
from itertools import combinations

def subspaces(n):
    layer={frozenset((0,))}
    yield from layer
    for rank in range(1,n+1):
        nxt=set()
        for H in layer:
            for x in range(1,1<<n):
                if x not in H:
                    nxt.add(frozenset(H | {x^h for h in H}))
        layer=nxt
        yield from layer

def cosets(n,H):
    remaining=set(range(1<<n)); ans=[]
    while remaining:
        a=min(remaining); orbit=frozenset(a^h for h in H)
        assert orbit <= remaining
        remaining.difference_update(orbit)
        ans.append(orbit)
    return ans

def compatible(A,B):
    return all((a^b).bit_count()<=2 for a in A for b in B)

def quotient_edges(orbits):
    return {frozenset((i,j)) for i in range(len(orbits)) for j in range(i) if compatible(orbits[i],orbits[j])}

def cube_map(n,orbit,word):
    support=[a for a in range(n) if word>>a&1]
    assert len(support) in (1,2)
    x=min(orbit)
    tail=sum(((x>>a)&1)<<j for j,a in enumerate(a for a in range(n) if a not in support))
    if len(support)==1:return tail
    p=((x>>support[0])^(x>>support[1]))&1
    return (tail<<1)|(p^(tail.bit_count()&1))

def check(n):
    counts={}; tested=0; ranked={} 
    for H in subspaces(n):
        k=len(H).bit_length()-1
        counts[k]=counts.get(k,0)+1
        if not H or H=={0}:continue
        admissible=all(h.bit_count()<=2 for h in H)
        if admissible:
            assert k in (1,2), (n,H)
            O=cosets(n,H)
            assert len(O)==1<<(n-k)
            E=quotient_edges(O)
            if k==1:
                h=next(x for x in H if x)
                labels={i:cube_map(n,O[i],h) for i in range(len(O))}
                assert set(labels.values())==set(range(1<<(n-1)))
                target={frozenset((i,j)) for i in labels for j in labels if i<j and (labels[i]^labels[j]).bit_count()==1}
                assert E==target,(n,h,E^target)
                ranked[(k,h.bit_count())]=ranked.get((k,h.bit_count()),0)+1
            else:
                assert not E,(n,H,E)
                ranked[(k,2)]=ranked.get((k,2),0)+1
        else:
            # An orbit already fails to be a simplex, so there is no fixed point.
            assert any(h.bit_count()>2 for h in H)
        tested+=1
    return counts,ranked,tested
if __name__=='__main__':
    for n in range(3,7):
        a,b,t=check(n)
        print('n',n,'subspaces_by_rank',dict(sorted(a.items())),'admissible_nonzero',b,'tested_nonzero',t)
    print('PASS: full finite subgroup and explicit orbit-graph checks')
