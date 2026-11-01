#!/usr/bin/env python3
"""Finite certificate for integral homology of the ordinary four-cut complex of J(6,2).

No external packages or datasets are required. Python 3.9+.
"""
from itertools import combinations
from collections import deque, defaultdict, Counter
from functools import lru_cache
from hashlib import sha256

PAIRS = list(combinations(range(6), 2))
N = len(PAIRS)
assert N == 15
FULL = (1 << N) - 1
ADJ = [0] * N
for i, a in enumerate(PAIRS):
    for j, b in enumerate(PAIRS):
        if i != j and bool(set(a) & set(b)):
            ADJ[i] |= 1 << j


def connected_four(mask):
    visited = mask & -mask
    pending = visited
    while pending:
        vertex = pending & -pending
        pending ^= vertex
        neighbors = ADJ[vertex.bit_length() - 1] & mask & ~visited
        visited |= neighbors
        pending |= neighbors
    return visited == mask


FOURS = [sum(1 << i for i in vertices) for vertices in combinations(range(N), 4)]
DISCONNECTED = [q for q in FOURS if not connected_four(q)]
FACETS = [FULL ^ q for q in DISCONNECTED]
assert len(FACETS) == 390

# Independent descriptions of every face: facet closure and direct complement test.
FACE = bytearray(1 << N)
for facet in FACETS:
    subface = facet
    while True:
        FACE[subface] = 1
        if subface == 0:
            break
        subface = (subface - 1) & facet
for simplex in range(1 << N):
    complement = FULL ^ simplex
    direct = any(q & complement == q for q in DISCONNECTED)
    assert bool(FACE[simplex]) == direct

GROUP = {d: [] for d in range(-1, N)}
for simplex in range(1 << N):
    if FACE[simplex]:
        GROUP[simplex.bit_count() - 1].append(simplex)
F_VECTOR = [len(GROUP[d]) for d in range(11)]
assert F_VECTOR == [15, 105, 455, 1365, 3003, 5005, 6435,
                    6375, 4570, 1935, 390]
assert sum(FACE) == 29654

# Deterministic successive-coordinate matching on the augmented face poset.
ACTIVE = FACE[:]
UP = {}
DOWN = {}
for i in range(N):
    bit = 1 << i
    for a in range(1 << N):
        b = a | bit
        if a & bit == 0 and ACTIVE[a] and ACTIVE[b]:
            ACTIVE[a] = ACTIVE[b] = 0
            UP[a] = b
            DOWN[b] = a
CRITICAL = [a for a in range(1 << N) if ACTIVE[a]]
CRITICAL_GROUP = {d: [a for a in CRITICAL if a.bit_count() - 1 == d]
                  for d in range(-1, 11)}
assert Counter({d: len(v) for d, v in CRITICAL_GROUP.items() if v}) == {
    7: 5, 8: 72, 10: 15
}
assert len(UP) == len(DOWN) == (29654 - 92) // 2
assert all(UP[a] == b and DOWN[b] == a for a, b in UP.items())

# Exhaustive directed Hasse-diagram acyclicity check (not just a matching count).
OUT = [[] for _ in range(1 << N)]
INDEG = [0] * (1 << N)
INCIDENCES = 0
for s in range(1 << N):
    if not FACE[s]:
        continue
    remaining = s
    while remaining:
        bit = remaining & -remaining
        remaining ^= bit
        t = s ^ bit
        if UP.get(t) == s:
            src, dst = t, s
        else:
            src, dst = s, t
        OUT[src].append(dst)
        INDEG[dst] += 1
        INCIDENCES += 1
queue = deque(s for s in range(1 << N) if FACE[s] and INDEG[s] == 0)
visited = 0
while queue:
    s = queue.popleft()
    visited += 1
    for t in OUT[s]:
        INDEG[t] -= 1
        if INDEG[t] == 0:
            queue.append(t)
assert visited == sum(FACE), (visited, sum(FACE))


def signed_faces(s):
    rest = s
    while rest:
        bit = rest & -rest
        rest ^= bit
        sign = -1 if (s & (bit - 1)).bit_count() & 1 else 1
        yield s ^ bit, sign


def critical_boundary(upper_dim):
    targets = CRITICAL_GROUP[upper_dim - 1]
    idx = {s: j for j, s in enumerate(targets)}

    @lru_cache(maxsize=None)
    def reduce_lower(s):
        if s in idx:
            return {idx[s]: 1}
        if s in DOWN:
            return {}
        upper = UP.get(s)
        assert upper is not None and upper.bit_count() == s.bit_count() + 1
        incidence = next(c for lower, c in signed_faces(upper) if lower == s)
        result = defaultdict(int)
        for lower, coeff in signed_faces(upper):
            if lower == s:
                continue
            for j, value in reduce_lower(lower).items():
                result[j] -= incidence * coeff * value
        return {j: v for j, v in result.items() if v}

    matrix_columns = []
    for upper in CRITICAL_GROUP[upper_dim]:
        result = defaultdict(int)
        for lower, coeff in signed_faces(upper):
            for j, value in reduce_lower(lower).items():
                result[j] += coeff * value
        matrix_columns.append({j: v for j, v in result.items() if v})
    return matrix_columns

B8 = critical_boundary(8)
B10 = critical_boundary(10)
assert len(B8) == 72 and len(B10) == 15
assert all(not c for c in B10)
assert max(abs(v) for col in B8 for v in col.values()) == 1
# Unit columns give a 5x5 diagonal minor with determinant +/-1.
UNIT_COL = [next(j for j, column in enumerate(B8)
                 if column == {i: 1} or column == {i: -1})
            for i in range(5)]
assert UNIT_COL == [2, 7, 21, 39, 49]
assert len(set(UNIT_COL)) == 5
# With five rows and a unit maximal minor, the nonzero Smith factors are all 1.
# Thus reduced integral homology is Z^67 in dimension 8 and Z^15 in dimension 10.

# Independent full simplicial boundary elimination over F_2, not using matching data.
PREVIOUS = [0]
RANKS = []
for dimension in range(11):
    index = {s: j for j, s in enumerate(PREVIOUS)}
    basis = {}
    for s in GROUP[dimension]:
        boundary = 1 if dimension == 0 else 0
        if dimension:
            for lower, sign in signed_faces(s):
                boundary ^= 1 << index[lower]
        while boundary:
            pivot = boundary.bit_length() - 1
            if pivot in basis:
                boundary ^= basis[pivot]
            else:
                basis[pivot] = boundary
                break
    RANKS.append(len(basis))
    PREVIOUS = GROUP[dimension]
assert RANKS == [1, 14, 91, 364, 1001, 2002, 3003, 3432, 2943, 1560, 375]
BETTI = [F_VECTOR[i] - RANKS[i] - (RANKS[i+1] if i < 10 else 0)
         for i in range(11)]
assert BETTI == [0, 0, 0, 0, 0, 0, 0, 0, 67, 0, 15]

print('GRAPH_VERTICES', N)
print('DISCONNECTED_FOUR_SETS_AND_FACETS', len(FACETS))
print('AUGMENTED_FACES', sum(FACE))
print('FACE_VECTOR', F_VECTOR)
print('MATCHED_PAIRS', len(UP))
print('HASSE_INCIDENCES', INCIDENCES)
print('HASSE_ACYCLIC', visited == sum(FACE))
print('REDUCED_CRITICAL_CELLS', [(d, len(CRITICAL_GROUP[d])) for d in [7,8,10]])
print('MORSE_D8_UNIT_COLUMNS', UNIT_COL)
print('MORSE_D10_ZERO', all(not c for c in B10))
print('F2_BOUNDARY_RANKS', RANKS)
print('F2_REDUCED_BETTI', BETTI)
print('INTEGRAL_REDUCED_HOMOLOGY', 'H8=Z^67,H10=Z^15,others=0')
print('J6_FOUR_CUT_HOMOLOGY_CERTIFICATE_OK')
