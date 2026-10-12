#!/usr/bin/env python3
"""Exact finite checks of color-refinement depth and walk moments on grids.

All arithmetic is integer. Run with Python 3.9+; no dependencies.
"""
from collections import defaultdict


def grid_adjacency(m, n):
    a = []
    for i in range(m):
        for j in range(n):
            a.append(tuple(x*n+y for x,y in ((i-1,j),(i+1,j),(i,j-1),(i,j+1))
                           if 0<=x<m and 0<=y<n))
    return a


def orbit_key(m, n, i, j):
    a,b=min(i,m-1-i),min(j,n-1-j)
    return tuple(sorted((a,b))) if m==n else (a,b)


def find_refinement_depth(adj):
    N=len(adj)
    color=[0]*N
    stages=[tuple(color)]
    for t in range(N):
        sig=[(color[v],tuple(sorted(color[w] for w in adj[v]))) for v in range(N)]
        rank={s:k for k,s in enumerate(sorted(set(sig)))}
        nxt=[rank[s] for s in sig]
        if len(set(nxt))==len(set(color)):
            return t, color, stages
        color=nxt
        stages.append(tuple(color))
    raise AssertionError('No finite stabilization')


def walk_signatures(adj, upto):
    N=len(adj); x=[1]*N; signatures=[(1,) for _ in range(N)]
    for k in range(1,upto+1):
        x=[sum(x[w] for w in adj[v]) for v in range(N)]
        signatures=[signatures[v]+(x[v],) for v in range(N)]
    return signatures


def main():
    ncases=0; moment_cases=0; n_vertices=0
    for m in range(2,24):
        for n in range(m,37):
            adj=grid_adjacency(m,n)
            predicted=(m-1)//2 if m==n else max(m-1,(n-1)//2)
            depth, coloring, stages = find_refinement_depth(adj)
            keys=[orbit_key(m,n,i,j) for i in range(m) for j in range(n)]
            assert depth==predicted,(m,n,depth,predicted)
            # Color classes and grid reflection orbits coincide.
            color_to_keys=defaultdict(set);key_to_colors=defaultdict(set)
            for c,key in zip(coloring,keys):
                color_to_keys[c].add(key);key_to_colors[key].add(c)
            assert all(len(x)==1 for x in color_to_keys.values())
            assert all(len(x)==1 for x in key_to_colors.values())
            # Truncated walk-count vectors already separate all orbits at depth R.
            signatures=walk_signatures(adj,predicted)
            sig_to_keys=defaultdict(set);key_to_sigs=defaultdict(set)
            for sig,key in zip(signatures,keys):
                sig_to_keys[sig].add(key);key_to_sigs[key].add(sig)
            assert all(len(x)==1 for x in sig_to_keys.values())
            assert all(len(x)==1 for x in key_to_sigs.values())
            ncases+=1;moment_cases+=1;n_vertices+=m*n
    print('GRID_DEPTH_VERIFIED',ncases,'cases,',n_vertices,'total tested vertices')
    print('WALK_MOMENT_ORBIT_VERIFIED',moment_cases,'cases')
    print('Parameters: 2 <= m <= 23 and m <= n <= 36')


if __name__=='__main__':
    main()
