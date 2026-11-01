#!/usr/bin/env python3
"""Independent graph-automorphism orbit check for minimal product tori.
Requires networkx and verify.py from the same directory.
"""
import networkx as nx
from verify import E,cycles,pairs
G=nx.Graph();G.add_edges_from(E)
a=list(nx.algorithms.isomorphism.GraphMatcher(G,G).isomorphisms_iter())
assert len(a)==96
ci={frozenset(tuple(sorted((u,v))) for u,v in zip(c,c[1:]+c[:1])):j
    for j,c in enumerate(cycles)}
pi={frozenset(p):j for j,p in enumerate(pairs)}
def translate_cycle(g,j):
 c=cycles[j]
 f=frozenset(tuple(sorted((g[u],g[v]))) for u,v in zip(c,c[1:]+c[:1]))
 return ci[f]
left=set(range(60));orbits=[]
while left:
 k=min(left)
 orbit={pi[frozenset((translate_cycle(g,pairs[k][0]),
                      translate_cycle(g,pairs[k][1])))] for g in a}
 assert orbit<=left
 left-=orbit
 orbits.append(orbit)
assert sorted(map(len,orbits))==[12,48]
assert not left
print('FULL_AUTOMORPHISM_GROUP_ORDER 96')
print('DISJOINT_HEXAGON_PAIR_ORBITS 12,48')
print('SYMMETRY_OK')
