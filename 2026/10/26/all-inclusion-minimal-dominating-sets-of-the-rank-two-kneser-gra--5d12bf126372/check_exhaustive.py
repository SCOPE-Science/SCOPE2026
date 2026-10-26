#!/usr/bin/env python3
"""Independent exhaustive subset check for minimal domination in KG(n,2)."""
from itertools import combinations
from collections import Counter
from math import comb

def expected(n):
    return n + comb(n, 3) + 12*comb(n, 5) + 15*comb(n, 6) + comb(n, 2)*comb(n-2, 2)*comb(n-4, 2)

def profile(n, edge_list, mask):
    degrees = [0]*n
    cardinality = 0
    for idx, (u,v) in enumerate(edge_list):
        if mask & (1<<idx):
            degrees[u]+=1; degrees[v]+=1; cardinality += 1
    return cardinality, tuple(sorted(degrees,reverse=True))

def run(n):
    edges = list(combinations(range(n),2))
    closed = [sum((1 << j) for j, e in enumerate(edges)
                  if j==i or (edges[i][0] not in e and edges[i][1] not in e))
              for i in range(len(edges))]
    visited = bytearray(1 << len(edges))
    kinds = Counter()
    for mask in range(1, len(visited)):
        if all(mask & neigh for neigh in closed):
            visited[mask]=1
            if all(not visited[mask^(1<<j)] for j in range(len(edges)) if mask&(1<<j)):
                kinds[profile(n, edges, mask)] += 1
    observed = sum(kinds.values())
    assert observed==expected(n),(n,observed,expected(n))
    return observed,kinds

if __name__=='__main__':
    for n in (5,6,7):
        total,kinds=run(n)
        print('n',n,'minimal',total,'types',sorted(kinds.items(),key=str))
    print('EXHAUSTIVE_CHECK_OK')
