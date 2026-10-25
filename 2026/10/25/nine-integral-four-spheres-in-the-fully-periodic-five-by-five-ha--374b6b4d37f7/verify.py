"""Exact finite acyclic-matching certificate for the independence complex of C5 square C5.
Run with CPython 3.9 or later; no optional packages are required.
"""
from collections import Counter, deque

SIDE = 5
SIZE = SIDE * SIDE
neighbors = [0] * SIZE
for row in range(SIDE):
    for col in range(SIDE):
        v = SIDE * row + col
        for r, c in (((row+1)%SIDE, col), ((row-1)%SIDE, col),
                     (row, (col+1)%SIDE), (row, (col-1)%SIDE)):
            neighbors[v] |= 1 << (SIDE*r+c)
assert all(x.bit_count() == 4 for x in neighbors)
assert all((neighbors[i] >> j) & 1 == (neighbors[j] >> i) & 1
           for i in range(SIZE) for j in range(SIZE))

# Generate all independent faces once by the last (greatest) vertex.
faces = [0]
for v in range(SIZE):
    previous = faces[:]
    faces += [face | (1 << v) for face in previous
              if not (neighbors[v] & face)]
assert len(faces) == len(set(faces)) == 25531
assert all(not (neighbors[v] & face)
           for face in faces for v in range(SIZE) if face & (1 << v))
f_vector = Counter(face.bit_count() - 1 for face in faces)
assert [f_vector[d] for d in range(-1, 10)] == [1, 25, 250, 1300, 3850, 6745,
                                              7100, 4450, 1550, 250, 10]

# A matching on the augmented face poset, including the empty face.
# In each stage, match every available pair differing by the pivot vertex.
unused = set(faces)
paired = set()
stages = []
for pivot in range(SIZE):
    bit = 1 << pivot
    candidates = [(face, face | bit) for face in sorted(unused)
                  if not (face & bit) and (face | bit) in unused]
    for lower, upper in candidates:
        assert lower in unused and upper in unused
        paired.add((lower, upper))
        unused.remove(lower)
        unused.remove(upper)
    stages.append(len(candidates))
assert len(paired) == 12761
assert stages == [5682, 3771, 1228, 880, 556, 40, 0, 89, 194, 40,
                  129, 88, 16, 16, 16, 0, 0, 9, 6, 0, 0, 0, 0, 0, 1]
assert len(unused) == 9 and all(face.bit_count() == 5 for face in unused)
assert (0, 1) in paired

# Verify the COMPLETE directed Hasse diagram is acyclic:
# unmatched covering incidences point high->low, matching pairs low->high.
indegree = {face: 0 for face in faces}
successors = {face: [] for face in faces}
for top in faces:
    bits = top
    while bits:
        bit = bits & -bits
        bits ^= bit
        bottom = top ^ bit
        assert bottom in indegree
        if (bottom, top) in paired:
            source, target = bottom, top
        else:
            source, target = top, bottom
        successors[source].append(target)
        indegree[target] += 1
queue = deque(face for face in faces if indegree[face] == 0)
visited = 0
while queue:
    face = queue.popleft()
    visited += 1
    for target in successors[face]:
        indegree[target] -= 1
        if indegree[target] == 0:
            queue.append(target)
assert visited == len(faces)
# Delete the augmented empty-face edge. On the ordinary complex,
# its matched singleton becomes the unique critical 0-cell.
assert all(face != 0 for face in unused)
print('F_VECTOR', [f_vector[d] for d in range(-1, 10)])
print('MATCHED_PAIRS_AUGMENTED', len(paired))
print('MATCHED_PAIRS_NONEMPTY', len(paired) - 1)
print('CRITICAL_ORDINARY_DIMENSIONS', {0: 1, 4: len(unused)})
print('ACYCLIC_VERTICES_VISITED', visited)
print('CRITICAL_FIVE_VERTEX_MASKS', sorted(unused))
print('REDUCED_EULER', sum(1 if face.bit_count() % 2 else -1 for face in faces))
print('VERIFY_OK_TOROIDAL_FIVE_BY_FIVE_NINE_FOUR_SPHERES')
