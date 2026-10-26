#!/usr/bin/env python3
"""Independent checks of the triangular-graph minimal-fort classification.

Public reproducibility script for the mathematical statement, with direct
adjacency checks independent of the structural proof and an independent
recurrence for labeled spanning star forests.
"""
from itertools import combinations
from collections import Counter
from math import comb, factorial

def candidate_hist(n):
    # Canonical labeled star-forest recursion: choose block containing 0.
    a = {(0,0): 1}
    for r in range(1,n+1):
        for k in range(r):
            v=0
            for m in range(2,r+1):
                v += comb(r-1,m-1)*(1 if m == 2 else m)*a.get((r-m,k-(m-1)),0)
            if v:
                a[(r,k)]=v
    h=Counter({k:a.get((n,k),0) for k in range(n) if a.get((n,k),0)})
    for k in range(3,n):
        h[k] += comb(n,k)*factorial(k-1)//2
    return h

def is_fort(mask, adj):
    if not mask: return False
    full=(1<<len(adj))-1
    rest=full^mask
    while rest:
        bit=rest & -rest
        v=bit.bit_length()-1
        if (adj[v]&mask).bit_count()==1: return False
        rest^=bit
    return True

def candidate(mask,n,edges):
    if not mask:return False
    deg=[0]*n
    sub_edges=[]
    for i,(u,v) in enumerate(edges):
        if mask&(1<<i):
            deg[u]+=1;deg[v]+=1;sub_edges.append((u,v))
    # Labeled spanning inclusion-minimal edge cover: every edge has a degree-1 endpoint.
    if min(deg)>0 and all(deg[u]==1 or deg[v]==1 for u,v in sub_edges): return True
    # Non-spanning simple cycle: all nonzero degrees equal exactly 2 and connected.
    if 0 in deg and all(d in (0,2) for d in deg):
        active=[i for i,d in enumerate(deg) if d]
        seen={active[0]}; todo=[active[0]]
        while todo:
            w=todo.pop()
            for u,v in sub_edges:
                t=v if u==w else (u if v==w else None)
                if t is not None and t not in seen:
                    seen.add(t);todo.append(t)
        return len(active)==len(seen)
    return False

def run(n):
    edges=list(combinations(range(n),2))
    # Construct adjacency from edge incidence, not from a degree shortcut.
    adj=[sum(1<<j for j,f in enumerate(edges) if j!=i and (e[0] in f or e[1] in f)) for i,e in enumerate(edges)]
    m=len(edges)
    allfort=set()
    for mask in range(1,1<<m):
        if is_fort(mask,adj):allfort.add(mask)
    mine=set()
    for mask in sorted(allfort,key=int.bit_count):
        if not any((f&mask)==f for f in mine):mine.add(mask)
    pred={mask for mask in range(1,1<<m) if candidate(mask,n,edges)}
    assert mine==pred, (n, len(mine),len(pred), next(iter(mine^pred),None))
    actual=Counter(mask.bit_count() for mask in mine)
    assert actual==candidate_hist(n), (n,actual,candidate_hist(n))
    print(f'n={n} vertices={m} subsets={1<<m} all_forts={len(allfort)} minimal={len(mine)} profile={dict(sorted(actual.items()))} VALID')

if __name__=='__main__':
    for n in range(3,7):run(n)
    for n in range(7,15):
        print('recurrence',n,dict(sorted(candidate_hist(n).items())))
    print('VERIFY_OK')
