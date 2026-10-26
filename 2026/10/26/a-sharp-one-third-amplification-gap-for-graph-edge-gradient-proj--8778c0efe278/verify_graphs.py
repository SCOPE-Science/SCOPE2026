#!/usr/bin/env python3
"""Independent numerical finite-graph check of the stated graph-projection theorem.

Requires numpy and networkx (standard NetworkX graph atlas).
Finite sampling cannot establish the theorem for arbitrary graph sizes.
"""
import numpy as np
import networkx as nx

counts = {}
for n in range(3, 8):
    total = equal = 0
    for g in nx.graph_atlas_g():
        if g.number_of_nodes() != n or not nx.is_connected(g) or nx.is_tree(g):
            continue
        total += 1
        m = g.number_of_edges()
        b = np.zeros((m, n), dtype=float)
        for j, (u, v) in enumerate(g.edges()):
            b[j, u] = 1.0
            b[j, v] = -1.0
        lap = b.T @ b
        proj = b @ np.linalg.pinv(lap, hermitian=True) @ b.T
        val = float(np.max(np.sum(np.abs(proj), axis=1)))
        tri_cactus = True
        for block in nx.biconnected_components(g):
            subgraph = g.subgraph(block)
            if len(block) not in (2, 3):
                tri_cactus = False
                break
            if len(block) == 3 and subgraph.number_of_edges() != 3:
                tri_cactus = False
                break
        if val < 4.0 / 3.0 - 1.0e-7:
            raise AssertionError((n, sorted(g.edges()), 'gap', val))
        is_equal = abs(val - 4.0 / 3.0) < 1.0e-7
        if is_equal != tri_cactus:
            raise AssertionError((n, sorted(g.edges()), 'classification', val, tri_cactus))
        equal += int(is_equal)
    counts[n] = (total, equal)
print('Connected cyclic graphs; equality graphs by vertex count:', counts)
assert counts == {3:(1,1),4:(4,1),5:(18,4),6:(106,10),7:(842,30)}
print('All finite checks passed. No claim of exhaustive infinite verification.')
