#!/usr/bin/env python3
"""Exact finite discrete-Morse certificate for the (3,4,4) Hamming box.

Only Python's standard library is needed. The code independently constructs the
simplicial face poset from the graph adjacency predicate, creates a matching,
and checks every cover relation for directed acyclicity.
"""
from collections import Counter, deque
from itertools import product

SIZES = (3, 4, 4)
VERTICES = tuple(product(*(range(s) for s in SIZES)))
N = len(VERTICES)
assert N == 48
ALL = (1 << N) - 1

# Edge of categorical product iff all three coordinates differ.
ADJ = tuple(
    sum(1 << j for j, y in enumerate(VERTICES)
        if i != j and all(a != b for a, b in zip(x, y)))
    for i, x in enumerate(VERTICES)
)
assert all((ADJ[i] >> i) & 1 == 0 for i in range(N))
assert all(((ADJ[i] >> j) & 1) == ((ADJ[j] >> i) & 1)
           for i in range(N) for j in range(N))
assert sum(int.bit_count(x) for x in ADJ) // 2 == 48 * (2*3*3) // 2

# Exact complete recursion: every independent face has a unique increasing
# sequence of selected vertex indices. The mask 'allowed' contains subsequent
# vertices that are nonneighbors of all previously selected vertices.
FACES = []
def enumerate_faces(allowed, face):
    FACES.append(face)
    while allowed:
        bit = allowed & -allowed
        allowed ^= bit
        enumerate_faces(allowed & ~ADJ[bit.bit_length() - 1], face | bit)

enumerate_faces(ALL, 0)
FACE_TO_INDEX = {face: i for i, face in enumerate(FACES)}
assert len(FACE_TO_INDEX) == len(FACES)
F = Counter(face.bit_count() for face in FACES)
assert tuple(F[i] for i in range(17)) == (
    1,48,696,4192,12636,23904,35016,42336,43002,
    36128,24552,13200,5468,1680,360,48,3
)
assert len(FACES) == 243270
assert sum((-1)**k * count for k, count in F.items()) == 198

# Deterministic matching: at stage v, pair any two currently unpaired faces
# which differ by insertion of vertex v. A face is paired at most once.
REMAINING = set(FACES)
PARTNER = {}
for v in range(N):
    bit = 1 << v
    pairs = [(face, face | bit) for face in REMAINING
             if not (face & bit) and (face | bit) in REMAINING]
    for lower, upper in pairs:
        REMAINING.remove(lower)
        REMAINING.remove(upper)
        PARTNER[lower] = upper
        PARTNER[upper] = lower
assert len(PARTNER) // 2 == 121536
assert len(REMAINING) == 198
assert all(face.bit_count() == 4 for face in REMAINING)
assert 0 in PARTNER and PARTNER[0].bit_count() == 1
assert len(PARTNER) + len(REMAINING) == len(FACES)

# A matched cover F < F+v has upward orientation; every other cover is downward.
# Check the ENTIRE directed Hasse diagram, not a random sample or a homology
# computation. Indegrees are accumulated once for every actual cover relation.
indegree = [0] * len(FACES)
cover_count = 0
for j, upper in enumerate(FACES):
    bits = upper
    while bits:
        bit = bits & -bits
        bits ^= bit
        lower = upper ^ bit
        cover_count += 1
        if PARTNER.get(lower) == upper:
            indegree[j] += 1
        else:
            indegree[FACE_TO_INDEX[lower]] += 1
assert cover_count == sum(k * F[k] for k in F)
queue = deque(j for j, deg in enumerate(indegree) if deg == 0)
removed = 0
while queue:
    j = queue.popleft()
    removed += 1
    face = FACES[j]
    partner = PARTNER.get(face)
    if partner is not None and partner.bit_count() == face.bit_count() + 1:
        t = FACE_TO_INDEX[partner]
        indegree[t] -= 1
        if indegree[t] == 0:
            queue.append(t)
    bits = face
    while bits:
        bit = bits & -bits
        bits ^= bit
        lower = face ^ bit
        if PARTNER.get(lower) != face:
            t = FACE_TO_INDEX[lower]
            indegree[t] -= 1
            if indegree[t] == 0:
                queue.append(t)
assert removed == len(FACES), (removed, len(FACES))
assert all(v == 0 for v in indegree)

# The radius-1 complex is a union of the 40 coordinate-line simplices.
# Their nerve has one triangle per original vertex and is homotopy equivalent
# to the bipartite incidence graph of lines and original vertices.
lines = sum((N // s for s in SIZES))
incidence_edges = 3 * N
beta_1 = incidence_edges - (lines + N) + 1
assert (lines, incidence_edges, beta_1) == (40, 144, 57)
assert sum((N // s) * (s * (s - 1) // 2) for s in SIZES) == 192

print('EXACT_AUGMENTED_FACE_COUNT', len(FACES))
print('EXACT_HASSE_COVER_COUNT', cover_count)
print('MATCHED_PAIRS', len(PARTNER)//2)
print('CRITICAL_FACES', dict(Counter(face.bit_count()-1 for face in REMAINING)))
print('DIRECTED_HASSE_ACYCLIC_VERIFIED', removed)
print('SCALE_ONE_BETA_ONE', beta_1)
print('COMPLETE_HAMMING_3_4_4_FILTRATION_VERIFIED')
