#!/usr/bin/env python3
"""Finite brute-force checks for edge-open packings in matching-deleted bipartite graphs."""
from itertools import combinations
from math import comb
from collections import Counter

def edges(m,n,t):
    return [(i,j) for i in range(m) for j in range(n) if i!=j or i>=t]

def has_common_edge(e,f,edge_set):
    # Third edge has one endpoint in each selected edge. In bipartite labeling,
    # only the two cross possibilities can be such a third edge.
    i,j=e; k,l=f
    return any(h not in (e,f) for h in [(i,l),(k,j)] if h in edge_set)

def brute(m,n,t):
    E=edges(m,n,t); X=set(E); N=len(E)
    bad=[0]*N
    for a in range(N):
        for b in range(a+1,N):
            if has_common_edge(E[a],E[b],X):
                bad[a]|=1<<b; bad[b]|=1<<a
    pol=Counter(); exceptions=Counter();
    for mask in range(1<<N):
        ok=True
        for a in range(N):
            if mask>>a&1 and mask&bad[a]:
                ok=False;break
        if not ok:continue
        s=[E[i] for i in range(N) if mask>>i&1]
        pol[len(s)]+=1
        if len(s)>=2:
            share_row=len({i for i,j in s})==1
            share_col=len({j for i,j in s})==1
            opp_pair=len(s)==2 and s[0][0]==s[1][1] and s[0][1]==s[1][0] and s[0][0]<t and s[0][1]<t
            assert share_row or share_col or opp_pair, (m,n,t,s)
            if opp_pair:exceptions[len(s)]+=1
    return pol,exceptions

def formula(m,n,t):
    E=m*n-t
    out=Counter({0:1,1:E})
    for k in range(2,max(m,n)+1):
        out[k] = (t*comb(n-1,k) if k<=n-1 else 0)+(m-t)*(comb(n,k) if k<=n else 0) \
                 + (t*comb(m-1,k) if k<=m-1 else 0)+(n-t)*(comb(m,k) if k<=m else 0) \
                 +(comb(t,2) if k==2 else 0)
    return {k:v for k,v in out.items() if v}

def independent_common_edge(e, f, edge_list):
    """Explicitly scan third edges and their endpoint partitions."""
    u = {('A', e[0]), ('B', e[1])}
    v = {('A', f[0]), ('B', f[1])}
    for g in edge_list:
        if g == e or g == f:
            continue
        ends = {('A', g[0]), ('B', g[1])}
        a, b = tuple(ends)
        if (a in u and b in v) or (a in v and b in u):
            return True
    return False

def independent_pair_check():
    tests = 0
    for m in range(2, 6):
        for n in range(2, 6):
            for t in range(min(m, n) + 1):
                E = edges(m, n, t)
                for e, f in combinations(E, 2):
                    assert has_common_edge(e, f, set(E)) == independent_common_edge(e, f, E), (m,n,t,e,f)
                    tests += 1
    return tests

def main():
    cases=0;total_masks=0;valid=0;opp=0
    for m in range(2,5):
        for n in range(2,5):
            for t in range(min(m,n)+1):
                br,ex=brute(m,n,t); fo=formula(m,n,t)
                assert dict(br)==fo,(m,n,t,br,fo)
                cases+=1;total_masks+=1<<(m*n-t);valid+=sum(br.values());opp+=sum(ex.values())
    comparisons=independent_pair_check()
    print('Independent third-edge comparisons:',comparisons)
    print('Exhaustive cases:',cases,'tested subsets:',total_masks,'feasible EOP sets:',valid,'exception-pairs:',opp)
    b,ex=brute(5,5,5)
    assert dict(b)==formula(5,5,5)
    assert dict(ex)=={2:10}
    print('Additional exhaustive crown K_5,5 minus perfect matching:',dict(b),'from 1048576 subsets')
    for m,n,t in [(2,2,0),(2,2,1),(2,2,2),(3,5,2),(4,4,4),(6,9,4),(9,9,9)]:
        print('profile',m,n,t, formula(m,n,t))

if __name__=='__main__':main()
