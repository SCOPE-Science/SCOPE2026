#!/usr/bin/env python3
"""Standalone finite tests for the stated two-dimensional rook-graph theorem."""
from itertools import product, combinations
from collections import Counter

def expected(m,n):
    return 2*m, (13 if m==n==2 else (m+n if m==n else n))

def good(cfg, adj):
    return all((sum(cfg[j]==2 for j in adj[i])==1 if v==0 else any(cfg[j]!=0 for j in adj[i])) for i,v in enumerate(cfg))

def graph_adj(m,n):
    return [tuple(j for j in range(m*n) if j!=i and (j//n==i//n or j%n==i%n)) for i in range(m*n)]

def brute(m,n):
    adj=graph_adj(m,n); mn=m*n
    best=mn+1; count=0
    for cfg in product(range(3),repeat=mn):
        wt=sum(cfg)
        if wt>best: continue
        if not good(cfg,adj):continue
        if wt<best:best=wt;count=0
        count+=1
    return best,count

def bounded_optimized(m,n):
    # Enumerate every assignment with weight at most the explicit upper bound 2m.
    adj=graph_adj(m,n);nn=m*n;bound=2*m
    ans=Counter()
    # Without 2's, only the all-one assignment can be admissible.
    if nn<=bound and good([1]*nn,adj):ans[nn]+=1
    for k in range(1,m+1):
        for Ttup in combinations(range(nn),k):
            T=set(Ttup)
            forced={p for p in range(nn) if p not in T and sum(q in T for q in adj[p])!=1}
            remaining=bound-2*k-len(forced)
            if remaining<0:continue
            free=[p for p in range(nn) if p not in T and p not in forced]
            for j in range(remaining+1):
                for extra in combinations(free,j):
                    P=forced|set(extra)|T
                    if all(any(q in P for q in adj[p]) for p in P):
                        ans[2*k+len(forced)+j]+=1
    return (min(ans),ans[min(ans)]) if ans else (None,0)

def main():
    exhaustive=[(2,2),(2,3),(2,4),(2,5),(2,6),(3,3),(3,4)]
    for m,n in exhaustive:
        actual=brute(m,n);assert actual==expected(m,n),(m,n,actual)
        print('direct',m,n,actual,flush=True)
    bounded=[(2,7),(3,5),(3,6),(4,4),(4,5),(5,5)]
    for m,n in bounded:
        actual=bounded_optimized(m,n);assert actual==expected(m,n),(m,n,actual)
        print('support enumeration',m,n,actual,flush=True)
    print('PASS: all 13 independent parameter instances')
if __name__=='__main__':main()
