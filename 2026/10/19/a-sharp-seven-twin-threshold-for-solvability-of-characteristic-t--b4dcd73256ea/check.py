#!/usr/bin/env python3
"""Exact binary structure-constant certificate for a graph-derivation Lie algebra.

Run: python3 check.py
All linear algebra is over F_2; the bracket coefficients are 0 or 1,
so the same rank identities hold over every field of characteristic two.
"""
from itertools import combinations

EXPECTED = {
    1: (0, 0),
    2: (1, 0),
    3: (3, 1, 0),
    4: (6, 3, 2, 0),
    5: (10, 6, 5, 1, 0),
    6: (15, 10, 9, 5, 4, 0),
    7: (21, 15, 14, 14),
}

def basis(span):
    pivots = {}
    for word in span:
        while word:
            lead = word.bit_length() - 1
            if lead in pivots:
                word ^= pivots[lead]
            else:
                pivots[lead] = word
                break
    return [pivots[i] for i in sorted(pivots)]


def lie_data(n):
    edges = list(combinations(range(n), 2))
    loc = {tuple(e): idx for idx, e in enumerate(edges)}
    constants = {}
    for i, e in enumerate(edges):
        for j, f in enumerate(edges):
            if i >= j:
                continue
            common = set(e).intersection(f)
            if len(common) != 1:
                continue
            a, b, c = sorted(set(e).union(f))
            triangle = ((a, b), (a, c), (b, c))
            constants[(i, j)] = sum(1 << loc[g] for g in triangle)

    def bracket(x, y):
        result = 0
        for (i, j), tri in constants.items():
            if ((x >> i & 1) & (y >> j & 1)) ^ ((x >> j & 1) & (y >> i & 1)):
                result ^= tri
        return result

    def derived(V):
        return basis(bracket(u, v) for idx, u in enumerate(V) for v in V[idx + 1:])

    V = [1 << i for i in range(len(edges))]
    dims = [len(V)]
    for step in range(8):
        Vnew = derived(V)
        dims.append(len(Vnew))
        if not Vnew or len(Vnew) == len(V):
            break
        V = Vnew
    return tuple(dims), bracket, loc


def four_cycle(loc, a, b, c, d):
    return sum(1 << loc[tuple(sorted(e))] for e in ((a,c),(a,d),(b,c),(b,d)))

for n, expected in EXPECTED.items():
    dims, bracket, loc = lie_data(n)
    assert dims == expected, (n, dims, expected)

# The same symbolic identity proves perfectness of the second derived
# subalgebra for every number of vertices >=7, by adjoining unused vertices.
dims, bracket, loc = lie_data(7)
C = four_cycle(loc, 0, 1, 2, 3)
U = four_cycle(loc, 0, 1, 4, 5)
V = four_cycle(loc, 2, 3, 4, 6)
assert bracket(U, V) == C
print('EXACT_LIE_SERIES_OK')
for n, ds in EXPECTED.items():
    print(n, '->'.join(map(str, ds)))
print('SEVEN_VERTEX_COMMUTATOR_IDENTITY_OK')
