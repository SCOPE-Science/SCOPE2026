#!/usr/bin/env python3
"""Exact, standalone certificate for the stable-triple Schrijver independence complex.

Run with Python 3.9+ using only the standard library. The vertex order is
lexicographic on stable three-subsets of {0,...,8}.
"""
from collections import Counter, deque
from itertools import combinations

N = 9
K = 3
PIVOTS = (3,22,17,15,0,25,4,7,14,16,20,24,12,18,10,13,23,28,
          6,19,8,9,21,5,11,26,2,1,29,27)
EXPECTED_F_VECTOR = (30,297,1311,3054,4212,3639,1974,648,117,9)
EXPECTED_CRITICAL_MASKS = (20768,25559040,134217778,268699664)

# Graph vertices are the stable three-subsets of the cyclic nine-set.
vertices = tuple(c for c in combinations(range(N),K)
                 if all(((x+1)%N) not in c for x in c))
assert len(vertices) == 30 and len(set(vertices)) == len(vertices)
triple_masks = tuple(sum(1<<j for j in c) for c in vertices)
neighbor_masks = tuple(sum(1<<j for j,b in enumerate(triple_masks)
                           if not (a&b)) for a in triple_masks)
assert all((neighbor_masks[i]>>i)&1 == 0 for i in range(30))
assert all(bool(neighbor_masks[i]>>j&1) == bool(neighbor_masks[j]>>i&1)
           for i in range(30) for j in range(30))

# Enumerate every independent set exactly once by increasing indices.
faces = []
def generate(face, available):
    faces.append(face)
    while available:
        bit = available & -available
        available ^= bit
        i = bit.bit_length()-1
        generate(face | bit, available & ~neighbor_masks[i])
generate(0,(1<<len(vertices))-1)
face_set = set(faces)
assert len(faces) == len(face_set) == 15292
assert all(all(not ((face ^ (1<<i)) & neighbor_masks[i])
                   for i in range(30) if face>>i&1) for face in faces)
counts = Counter(face.bit_count()-1 for face in faces if face)
assert tuple(counts[d] for d in range(10)) == EXPECTED_F_VECTOR
assert sum(((-1)**d)*counts[d] for d in counts) == -3

# An independent second generation path, extending partial faces
# one vertex at a time rather than branching through allowed extensions.
by_increasing_vertices = {0}
for i in range(30):
    bit = 1<<i
    additions={x|bit for x in by_increasing_vertices
               if not (x & neighbor_masks[i])}
    by_increasing_vertices.update(additions)
assert by_increasing_vertices == face_set

# At each pivot pair all currently available faces differing by that pivot.
remaining = set(face_set)
matched_lower_to_upper = {}
for i in PIVOTS:
    bit = 1<<i
    lowers = [a for a in remaining if not a&bit and (a|bit) in remaining]
    for a in lowers:
        b = a|bit
        assert a in remaining and b in remaining and a not in matched_lower_to_upper
        remaining.remove(a)
        remaining.remove(b)
        matched_lower_to_upper[a] = b
assert len(matched_lower_to_upper) == 7644
assert 0 in matched_lower_to_upper
assert tuple(sorted(remaining)) == EXPECTED_CRITICAL_MASKS
assert all(c.bit_count()==4 for c in remaining)

# Independently check that the matching is acyclic on the augmented Hasse
# diagram: ordinary covering relations point down except matched ones,
# which point up. Kahn topological sorting rejects ALL directed cycles.
face_index = {f:i for i,f in enumerate(faces)}
indegree = [0]*len(faces)
outgoing = [[] for _ in faces]
incidences = 0
for top in faces:
    remaining_bits = top
    while remaining_bits:
        bit = remaining_bits & -remaining_bits
        remaining_bits ^= bit
        bottom = top^bit
        assert bottom in face_index
        lo,hi = face_index[bottom],face_index[top]
        if matched_lower_to_upper.get(bottom) == top:
            tail,head = lo,hi
        else:
            tail,head = hi,lo
        outgoing[tail].append(head)
        indegree[head] += 1
        incidences += 1
assert incidences == 79812
queue = deque(i for i,x in enumerate(indegree) if x == 0)
processed = 0
while queue:
    v = queue.popleft()
    processed += 1
    for w in outgoing[v]:
        indegree[w] -= 1
        if indegree[w]==0:
            queue.append(w)
assert processed == len(faces), 'The proposed matching is not acyclic'

# Remove the augmented empty-face pair: one critical 0-cell is restored.
# Four critical 3-cells remain; Forman yields a 4-fold S^3 wedge.
assert counts[0]==30
assert len(remaining)==4
assert sum(((-1)**i)*counts[i] for i in range(10))==-3
print('VERIFIED SG(3,3): vertices=30 independent_faces=15292 '
      'matched_augmented_pairs=7644 critical_3=4 '
      'incidences=79812 acyclic_vertices=15292 '
      'ordinary_critical_0=1 homotopy=wedge_4_S3')
