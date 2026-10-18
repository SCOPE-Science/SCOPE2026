#!/usr/bin/env python3
"""Independent mod-two boundary-rank cross-check for the Pappus matching complex."""
from collections import Counter

lcf = (5, 7, -7, 7, -7, -5) * 3
edges = sorted({tuple(sorted((i, j))) for i in range(18)
                for j in ((i + 1) % 18, (i + lcf[i]) % 18)})
assert len(edges) == 27
edge_vertex_masks = [(1 << u) | (1 << v) for u, v in edges]
by_degree = [set() for _ in range(9)]

def enumerate_matchings(i, busy, selected):
    if i == 27:
        if selected:
            by_degree[selected.bit_count() - 1].add(selected)
        return
    enumerate_matchings(i + 1, busy, selected)
    if not (busy & edge_vertex_masks[i]):
        enumerate_matchings(i + 1, busy | edge_vertex_masks[i],
                            selected | (1 << i))

enumerate_matchings(0, 0, 0)
counts = [len(x) for x in by_degree]
assert counts == [27, 297, 1719, 5643, 10557, 10737, 5319, 1026, 42]

rank = []
for d in range(9):
    lower = [0] if d == 0 else sorted(by_degree[d - 1])
    low_index = {simplex: i for i, simplex in enumerate(lower)}
    basis = {}
    for upper in sorted(by_degree[d]):
        col = 0
        edge_indices = [i for i in range(27) if (upper >> i) & 1]
        for i in edge_indices:
            col ^= 1 << low_index[upper ^ (1 << i)]
        while col:
            p = col.bit_length() - 1
            if p in basis:
                col ^= basis[p]
            else:
                basis[p] = col
                break
    rank.append(len(basis))
assert rank == [1, 26, 271, 1448, 4195, 6362, 4335, 984, 42]
assert [counts[d] - rank[d] - (rank[d + 1] if d < 8 else 0)
        for d in range(9)] == [0, 0, 0, 0, 0, 40, 0, 0, 0]
print('VERIFY_OK_PAPPUS_MOD2', 'FACES_35367', 'BETTI5_40',
      'BOUNDARY_RANKS_' + '_'.join(map(str, rank)))
