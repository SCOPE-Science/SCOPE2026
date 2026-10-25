#!/usr/bin/env python3
"""Exact finite discrete-Morse certificate for Ind(K3 x K3 x K4).

Requires Python 3.9+ and no third-party packages. Every nonempty independent
set and every codimension-one containment is enumerated before acyclicity
is tested by a complete topological sort. The empty set is included only
to construct a reduced acyclic matching; it is then deleted, leaving the
matched vertex as the unique ordinary 0-dimensional critical simplex.
"""
from collections import Counter, deque
from itertools import product

vertices = list(product(range(3), range(3), range(4)))
N = len(vertices)
assert N == 36
adjacent = []
for (a, b, c) in vertices:
    adjacent.append(sum(1 << j for j, (x, y, z) in enumerate(vertices)
                        if a != x and b != y and c != z))
assert all(mask.bit_count() == 12 for mask in adjacent)
assert sum(mask.bit_count() for mask in adjacent) // 2 == 216

# Recursion chooses each vertex at most once and in increasing order.
# The remaining bit mask contains the only permitted higher-index vertices.
faces = []
def enumerate_faces(face, remaining):
    faces.append(face)
    while remaining:
        bit = remaining & -remaining
        remaining ^= bit
        i = bit.bit_length() - 1
        enumerate_faces(face | bit, remaining & ~adjacent[i])
enumerate_faces(0, (1 << N) - 1)
assert len(faces) == 30992
assert len(set(faces)) == len(faces)
assert all(not (adjacent[i] & face) for face in faces
           for i in range(N) if face & (1 << i))

f_vector = Counter(f.bit_count() for f in faces)
expected = (1,36,414,2028,4869,6804,6816,5184,3042,1324,396,72,6)
assert tuple(f_vector.get(i, 0) for i in range(13)) == expected
assert max(f.bit_count() for f in faces) == 12
assert sum((-1)**(k-1)*count for k,count in f_vector.items()) == -96

# Canonical lexicographic vertex-toggle matching: at stage i, pair every
# still-unmatched face F omitting i to F union {i}, when both are present.
unpaired = set(faces)
matching = set()
for i in range(N):
    bit = 1 << i
    lower_faces = [f for f in unpaired
                   if not f & bit and (f | bit) in unpaired]
    for lower in lower_faces:
        upper = lower | bit
        assert lower in unpaired and upper in unpaired
        unpaired.remove(lower)
        unpaired.remove(upper)
        matching.add((lower, upper))
assert len(matching) == 15448
assert len(unpaired) == 96
assert Counter(f.bit_count() for f in unpaired) == {4:96}
assert 0 not in unpaired
assert (0, 1) in matching

# Reverse each matched incidence; orient every other face-poset cover
# from the larger simplex to the smaller. A full Kahn sort of the augmented
# face poset certifies absence of every nontrivial closed V path.
outgoing = {f: [] for f in faces}
indegree = {f: 0 for f in faces}
covers = 0
for face in faces:
    bits = face
    while bits:
        bit = bits & -bits
        bits ^= bit
        lower = face ^ bit
        if (lower, face) in matching:
            src, dest = lower, face
        else:
            src, dest = face, lower
        outgoing[src].append(dest)
        indegree[dest] += 1
        covers += 1
assert covers == 178704
queue = deque(f for f in faces if indegree[f] == 0)
visited = 0
while queue:
    f = queue.popleft()
    visited += 1
    for t in outgoing[f]:
        indegree[t] -= 1
        if indegree[t] == 0:
            queue.append(t)
assert visited == len(faces), ('directed cycle', visited)

# Passing from the augmented matching to ordinary discrete Morse theory:
# simply omit (empty, {0}); the zero simplex becomes critical. The
# resulting matching remains acyclic by restriction of the above DAG.
print('VERTICES',N,'GRAPH_EDGES',216)
print('F_VECTOR_BY_CARDINALITY',','.join(str(n) for n in expected))
print('FACES_INCLUDING_EMPTY',len(faces))
print('HASSE_COVERS',covers)
print('MATCHED_PAIRS_AUGMENTED',len(matching))
print('ACYCLIC_DAG_VERTICES',visited)
print('ORDINARY_CRITICAL_DIMENSIONS',dict({0:1,3:96}))
print('IND_K3_K3_K4_WEDGE_96_S3_VERIFIED')
