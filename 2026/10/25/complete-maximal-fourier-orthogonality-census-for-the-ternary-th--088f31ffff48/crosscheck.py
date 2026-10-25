#!/usr/bin/env python3
"""Independent implementation cross-check of the finite Fourier orthogonality census.

Requires the freely available networkx package. This optional check does not
replace the proof of exhaustive enumeration supplied with the main result.
"""
from collections import Counter
from itertools import product
import networkx as nx

V=list(product(range(6),repeat=3))
H=nx.Graph()
H.add_nodes_from(V)
H.add_edges_from((a,b) for i,a in enumerate(V) for b in V[i+1:]
                 if any((x-y)%6 in (2,4) for x,y in zip(a,b)))
counts=Counter(map(len,nx.find_cliques(H)))
assert dict(counts)=={12:34992,13:11664,14:11664,15:34992,27:154952}
print('networkx_version',nx.__version__)
print('vertices',H.number_of_nodes(),'edges',H.number_of_edges())
print('all_maximal_cliques',sum(counts.values()))
print('size_distribution',dict(sorted(counts.items())))
print('Independent graph-enumeration check passed.')
