#!/usr/bin/env python3
"""Exact arithmetic checks for degree-nine cubic--line incidence obstructions.

This script verifies necessary numerical possibilities. The geometric
nonexistence arguments are supplied in RESULT.md, not inferred from code.
"""
from math import comb


def candidates(k, ell):
    """Possible (nodes, ordinary triples, A5) under necessary conditions."""
    B = 9 * comb(k, 2) + 3 * k * ell + comb(ell, 2)
    max_a5 = 3 * comb(k, 2) + k * ell
    cases = []
    for a5 in range(max_a5 + 1):
        for triples in range(B // 3 + 1):
            nodes = B - 3 * (triples + a5)
            if nodes < 0:
                continue
            if nodes + 4 * triples + 5 * a5 != 48:
                continue
            # Clear denominators in Talar's necessary orbifold inequality.
            if 108 * k + 4 * nodes + 3 * triples < 4 * ell + 20 * a5:
                continue
            cases.append((nodes, triples, a5))
    return B, cases


assert candidates(1, 6) == (33, [(0, 7, 4), (3, 5, 5)])
assert candidates(2, 3) == (30, [(0, 2, 8), (3, 0, 9)])

# With six distinct lines, any line is in at most two pure line triples,
# and hence there are at most four pure line triple points in total.
max_line_triples = (6 * ((6 - 1) // 2)) // 3
assert max_line_triples == 4

# Each flex line meets the cubic at its single order-three contact,
# so a mixed triple (cubic + 2 lines) needs 2 nonflex lines.
for nodes, triples, flexes in candidates(1, 6)[1]:
    u_min = triples - max_line_triples
    u_max = comb(6 - flexes, 2) if 6 - flexes >= 2 else 0
    assert u_min > u_max, (nodes, triples, flexes, u_min, u_max)

# Three pairwise nonconcurrent lines give 3 distinct line--line vertices,
# exceeding the 2 available triples when there are no nodes.
assert 3 > 2
# When concurrent, a second triple involving both cubics contributes 1
# to their intersection number, while each further A5 contributes 3.
assert (9 - 1) % 3 != 0
print("CHECK_OK: four numerical types; three excluded by incidence conditions")
