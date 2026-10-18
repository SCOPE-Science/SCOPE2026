#!/usr/bin/env python3
"""Independent dodecahedral anti-forcing census using bit-mask matching tests.

Run: python verify_direct.py
The graph is generated from the classical LCF notation, not Petersen coordinates.
"""
from collections import Counter
from itertools import combinations
# An independent LCF presentation of the dodecahedral graph.
LCF = [10, 7, 4, -4, -7, 10, -4, 7, -7, 4] * 2
E = sorted({tuple(sorted((v, (v + 1) % 20))) for v in range(20)}
           | {tuple(sorted((v, (v + LCF[v]) % 20))) for v in range(20)})
assert len(E) == 30
# Explicit vertex bijection checks that this LCF presentation is the same
# graph as the usual generalized-Petersen description GP(10,2).
TO_GP = (0, 1, 11, 19, 17, 15, 13, 3, 2, 12,
         10, 18, 16, 14, 4, 5, 6, 7, 8, 9)
GP_EDGES = {tuple(sorted((i, (i + 1) % 10))) for i in range(10)}
GP_EDGES |= {(i, 10 + i) for i in range(10)}
GP_EDGES |= {tuple(sorted((10 + i, 10 + (i + 2) % 10)))
             for i in range(10)}
assert len(set(TO_GP)) == 20 and len(GP_EDGES) == 30
assert {tuple(sorted((TO_GP[u], TO_GP[v]))) for u, v in E} == GP_EDGES
INDEX = {e: k for k, e in enumerate(E)}
NEIGH_LIST = [[] for _ in range(20)]
for u, v in E:
    NEIGH_LIST[u].append(v)
    NEIGH_LIST[v].append(u)
NEIGH = [tuple(sorted(x)) for x in NEIGH_LIST]
assert all(len(x) == 3 for x in NEIGH)
BITEDGE = [(1 << u) | (1 << v) for u, v in E]

# A second perfect-matching enumeration, using integer bit masks for vertices.
def extend(available, used):
    if not available:
        yield used
        return
    vb = available & -available
    v = vb.bit_length() - 1
    for w in NEIGH[v]:
        wb = 1 << w
        if available & wb:
            j = INDEX[tuple(sorted((v, w)))]
            yield from extend(available & ~vb & ~wb, used | (1 << j))

PMS = sorted(set(extend((1 << 20) - 1, 0)))
assert len(PMS) == 36

# For each fixed matching M every alternative N produces the forbidden-edge
# constraint S intersection (N minus M) nonempty. Test those constraints
# directly, independently of the alternating-cycle or orbit methods.

def run_match(m):
    available_ids = [j for j in range(30) if not (m >> j) & 1]
    forbidden = [n & ~m for n in PMS if n != m]
    # Only set-minimal constraints are needed to decide hitting.
    forbidden = [c for c in forbidden if not any(d != c and (d & c) == d
                                                    for d in forbidden)]
    ordinary = None
    disjoint = None
    for k in range(0, 9):
        count_ordinary = 0
        count_disjoint = 0
        # Explicitly enumerate ALL subsets of this size (no nonexhaustive sampling).
        for comb in combinations(available_ids, k):
            s = 0
            used_vertices = 0
            indep = True
            for j in comb:
                s |= 1 << j
                if indep and used_vertices & BITEDGE[j]:
                    indep = False
                used_vertices |= BITEDGE[j]
            if not all(s & c for c in forbidden):
                continue
            count_ordinary += 1
            if indep:
                count_disjoint += 1
        if ordinary is None and count_ordinary:
            ordinary = (k, count_ordinary)
        if disjoint is None and count_disjoint:
            disjoint = (k, count_disjoint)
        if ordinary is not None and disjoint is not None:
            break
    assert ordinary and disjoint
    return ordinary + disjoint

RESULTS = [run_match(m) for m in PMS]
COUNTS = Counter(RESULTS)
assert COUNTS == {(4, 8, 8, 4): 30, (5, 22, 8, 5): 6}, COUNTS
print('GRAPH POLYHEDRAL_DODECAHEDRON n=20 m=30')
print('PERFECT_MATCHINGS', len(PMS))
for row, count in sorted(COUNTS.items()):
    print('PROFILE ordinary_min={} ordinary_witnesses={} '
          'disjoint_min={} disjoint_witnesses={} multiplicity={}'.format(*row, count))
print('TOTAL_MINIMUM_WITNESSES', sum(row[1] * c for row, c in COUNTS.items()))
print('TOTAL_MINIMUM_DISJOINT_WITNESSES', sum(row[3] * c for row, c in COUNTS.items()))
print('INDEPENDENT_VERIFY_OK')
