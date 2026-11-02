#!/usr/bin/env python3
"""Finite checks for the orbit subset-sum and corner coding lemmas."""
from math import comb
from collections import Counter
from itertools import product

def orbit_checks(a):
    blocks = [1]*a + [4]*(a*(a-1)) + [6]*comb(a,2) + [12]*(a*comb(a-1,2)) + [24]*comb(a,4)
    assert sum(blocks)==a**4
    covered=0
    for w in blocks:
        assert w<=covered+1, (a,w,covered)
        covered+=w
    assert covered==a**4
    print('orbit',a,'orbits',len(blocks),'all_numerators',a**4+1)

def grid(m,n):
    adj={}
    for i in range(m):
        for j in range(n):
            adj[(i,j)]={(a,b) for a,b in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)) if 0<=a<m and 0<=b<n}
    return adj

def shortest_counts(adj, c, limit):
    old={c:1}
    seen={c}
    out={0:dict(old)}
    for step in range(1,limit+1):
        nxt={}
        for u,num in old.items():
            for v in adj[u]:
                if v not in seen: nxt[v]=nxt.get(v,0)+num
        old=nxt; seen|=set(nxt); out[step]=nxt
    return out
for a in [4,8,16]:orbit_checks(a)
for m,n in [(5,6),(8,11),(10,10)]:
    g=grid(m,n)
    corners=[u for u in g if len(g[u])==2]
    assert len(corners)==4
    for c in corners:
        counts=shortest_counts(g,c,2*min(3,(min(m,n)-1)//2))
        for j in range(min(3,(min(m,n)-1)//2)+1):
            d=2*j
            k=comb(2*j,j)
            ys=[v for v,z in counts[d].items() if z>=k]
            assert len(ys)==1,(m,n,c,j,ys)
            target=(c[0]+j if c[0]==0 else c[0]-j, c[1]+j if c[1]==0 else c[1]-j)
            assert ys[0]==target
    print('diagonal',m,n,'corners',len(corners),'tested_j',min(3,(min(m,n)-1)//2)+1)
# Classify 4-tuples for a=4 independently from stated multiplicity formulas.
a=4
counts=Counter()
for code in product(range(a),repeat=4):
    mult=tuple(sorted(Counter(code).values(),reverse=True))
    counts[mult]+=1
assert counts=={(4,):4,(3,1):48,(2,2):36,(2,1,1):144,(1,1,1,1):24}
print('four_code_occurrences',dict(counts))
print('ALL_CHECKS_OK')
