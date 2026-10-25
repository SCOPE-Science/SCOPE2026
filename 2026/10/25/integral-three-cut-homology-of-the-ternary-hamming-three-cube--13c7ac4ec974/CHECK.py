#!/usr/bin/env python3
"""Exact integral homology checker for the 3-cut complex of H(3,3).

Pure Python 3 standard library. Builds the combinatorial Alexander dual,
uses integer elementary column operations, and checks unit Smith reductions.
No floating-point arithmetic or external data are needed.
"""
from collections import defaultdict
from itertools import combinations, product

vertices = list(product(range(3), repeat=3))
n = len(vertices)
assert n == 27


def adjacent(i, j):
    return sum(x != y for x, y in zip(vertices[i], vertices[j])) == 1


def face_connected_triple(t):
    return sum(adjacent(i, j) for i, j in combinations(t, 2)) >= 2


faces = {
    0: [(i,) for i in range(n)],
    1: list(combinations(range(n), 2)),
    2: [t for t in combinations(range(n), 3) if face_connected_triple(t)],
}
for k in (3, 4):
    earlier = set(faces[k - 1])
    faces[k] = [
        s for s in combinations(range(n), k + 1)
        if all(s[:j] + s[j + 1:] in earlier for j in range(k + 1))
    ]
assert tuple(len(faces[k]) for k in range(5)) == (27, 351, 351, 81, 0)

# The combinatorial Alexander dual has the complete 1-skeleton, so its
# integer 1-cycle group is freely based on the 325 non-star edges.
nonstar = [e for e in faces[1] if 0 not in e]
row_number = {e: j for j, e in enumerate(nonstar)}
assert len(nonstar) == 325
triangles = faces[2]
triangle_index = {f: j for j, f in enumerate(triangles)}

# The boundary in the nonstar edge coordinates is the signed boundary:
# [a,b,c] -> [b,c] - [a,c] + [a,b].
b2 = []
for t in triangles:
    entries = {}
    for j, edge in enumerate(combinations(t, 2)):
        if 0 not in edge:
            entries[row_number[edge]] = (1, -1, 1)[j]
    b2.append(entries)

# Check that every oriented 3-face has integral boundary squared zero
# using the FULL edge boundary, without the nonstar projection.
full_edge_number = {e: j for j, e in enumerate(faces[1])}

def boundary_triangle(t):
    return {
        full_edge_number[(t[1], t[2])]: 1,
        full_edge_number[(t[0], t[2])]: -1,
        full_edge_number[(t[0], t[1])]: 1,
    }

for tet in faces[3]:
    totals = defaultdict(int)
    for j in range(4):
        t = tet[:j] + tet[j + 1:]
        for edge, val in boundary_triangle(t).items():
            totals[edge] += (-1 if j % 2 else 1) * val
    assert all(val == 0 for val in totals.values())


def unit_column_reduction(columns, count_rows):
    """Integer column elimination without row operations.

    Every used pivot is +1 or -1. Returned unpivoted column labels
    form a freely generated kernel *when* every residual column is zero.
    All column operations are integral/unimodular.
    """
    cols = [dict(c) for c in columns]
    active = set(range(len(cols)))
    pivot_count = 0
    while True:
        row_terms = defaultdict(list)
        for col in active:
            for row, value in cols[col].items():
                assert 0 <= row < count_rows and value != 0
                row_terms[row].append((col, value))
        choices = []
        for row, terms in row_terms.items():
            for col, val in terms:
                if abs(val) == 1:
                    choices.append(((len(terms) - 1) * (len(cols[col]) - 1),
                                    len(terms), len(cols[col]), row, col, val))
        if not choices:
            break
        _, _, _, row, pivot_col, pivot_value = min(choices)
        pivot = cols[pivot_col]
        assert pivot[row] == pivot_value and abs(pivot_value) == 1
        for col, entry in row_terms[row]:
            if col == pivot_col:
                continue
            factor = entry * pivot_value
            for r, val in pivot.items():
                newval = cols[col].get(r, 0) - factor * val
                if newval:
                    cols[col][r] = newval
                else:
                    cols[col].pop(r, None)
        active.remove(pivot_col)
        pivot_count += 1
    assert all(not cols[col] for col in active), 'Unreduced nonzero column'
    return pivot_count, sorted(active)


rank_b2, free_triangle_columns = unit_column_reduction(b2, len(nonstar))
assert rank_b2 == 217 and len(free_triangle_columns) == 134

# After unimodular elimination of b2, the 134 nonpivot triangle basis
# vectors span ker(b2). Since pivots only modify other columns by adding
# pivot columns, the coordinates along nonpivot triangles stay unchanged.
free_index = {col: j for j, col in enumerate(free_triangle_columns)}
b3_onto_cycles = []
for tet in faces[3]:
    entries = {}
    for j in range(4):
        tri = tet[:j] + tet[j + 1:]
        col = triangle_index[tri]
        if col in free_index:
            entries[free_index[col]] = 1 if j % 2 == 0 else -1
    b3_onto_cycles.append(entries)
rank_b3, unused = unit_column_reduction(b3_onto_cycles, 134)
assert rank_b3 == 81 and not unused

# Reduced integral homology of dual:
# H_1 = Z^(325-217), H_2 = Z^(134-81); no torsion, other positive H zero.
h1, h2 = 325 - rank_b2, 134 - rank_b3
assert (h1, h2) == (108, 53)
assert 27 - 351 + 351 - 81 - 1 == -h1 + h2

# Integral combinatorial Alexander duality, on n=27 vertices:
# reduced H_i(Delta_3; Z) = reduced H^(24-i)(dual; Z).
# The dual homology is free, so universal coefficients introduce no Ext.
assert 27 - 22 - 3 == 2 and 27 - 23 - 3 == 1
print('PASS: face vector (27,351,351,81), no 5-vertex face')
print('PASS: exact integral chain condition d2*d3=0')
print('PASS: unit-pivot ranks d2=217, d3=81 and torsion-free cokernels')
print('PASS: reduced dual integral H1=Z^108, H2=Z^53')
print('PASS: reduced three-cut integral H22=Z^53, H23=Z^108')
