#!/usr/bin/env python3
"""Direct synchronous one-dimensional counting refinement on pointed grids.
Independently builds an adjacency table; does not use the analytic proof.
"""
from collections import Counter

def partition_depth(m, n):
    vertices = [(i,j) for i in range(m) for j in range(n)]
    index = {v:q for q,v in enumerate(vertices)}
    neigh=[]
    for i,j in vertices:
        neigh.append([index[u] for u in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)) if u in index])
    colors = [int(v == (0,0)) for v in vertices]
    for step in range(m*n):
        sig = [(colors[v], tuple(sorted(Counter(colors[w] for w in neigh[v]).items()))) for v in range(len(vertices))]
        d = {s:q for q,s in enumerate(sorted(set(sig)))}
        new = [d[s] for s in sig]
        if len(set(new)) == len(set(colors)):
            return step, colors, vertices
        colors = new
    raise AssertionError('nontermination')

def expected_orbit(i,j,m,n):
    return tuple(sorted((i,j))) if m == n else (i,j)

pairs=0; max_v=0; max_d=0
for m in range(2,17):
    for n in range(m,32):
        rounds, colors, vertices = partition_depth(m,n)
        expected = n+m//2-2
        if rounds != expected:
            raise AssertionError(('depth',m,n,rounds,expected))
        groups={}
        for v,c in zip(vertices,colors):
            z=expected_orbit(*v,m,n)
            if z in groups and groups[z]!=c:
                raise AssertionError(('orbit split',m,n,z))
            groups[z]=c
        if len(groups)!=len(set(colors)):
            raise AssertionError(('orbit merger',m,n))
        pairs+=1;max_v=max(max_v,len(vertices));max_d=max(max_d,rounds)
print(f'DIRECT_PASS pairs={pairs} max_vertices={max_v} max_rounds={max_d}')
