"""Exhaustive integral discrete-Morse certificate for a cyclic order-23 neighborhood complex.

Requires Python 3.9+ standard library only. Execute: python verify_paley23.py
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

P = 23
ORDER = (22, 21, 5, 13, 18, 20, 4, 11, 0, 16, 17, 12,
         9, 1, 6, 19, 2, 7, 10, 8, 14, 15, 3)
Q = {a * a % P for a in range(1, P)}
assert sorted(Q) == [1, 2, 3, 4, 6, 8, 9, 12, 13, 16, 18]

def boundary(face, faces):
    j = 0
    for v in range(P):
        if face & (1 << v):
            subface = face ^ (1 << v)
            if subface in faces:
                yield subface, (1 if j % 2 == 0 else -1)
            j += 1

# The facets are exactly the 23 translates of the quadratic residues.
faces = set()
for v in range(P):
    facet = sum(1 << ((v + r) % P) for r in Q)
    subface = facet
    while subface:
        faces.add(subface)
        subface = (subface - 1) & facet
f_vector = Counter(face.bit_count() - 1 for face in faces)
assert [f_vector[d] for d in range(11)] == [23, 253, 1771, 6325, 10373,
                                               10626, 7590, 3795, 1265, 253, 23]
assert len(faces) == 42297

# Elementary simplicial collapses, always selecting the least free face.
# A degree-one face has a unique codimension-one coface in the current complex;
# in a simplicial complex the coface is automatically maximal.
degree = {}
for face in faces:
    degree[face] = sum((face | (1 << v)) in faces
                       for v in range(P) if not face & (1 << v))
queue = [face for face in faces if degree[face] == 1]
heapq.heapify(queue)
collapse_count = 0
while queue:
    low = heapq.heappop(queue)
    if low not in faces or degree[low] != 1:
        continue
    uppers = [low | (1 << v) for v in range(P)
              if not low & (1 << v) and (low | (1 << v)) in faces]
    assert len(uppers) == 1
    high = uppers[0]
    faces.remove(low)
    faces.remove(high)
    for face in (low, high):
        for v in range(P):
            if face & (1 << v):
                subface = face ^ (1 << v)
                if subface in faces:
                    degree[subface] -= 1
                    if degree[subface] == 1:
                        heapq.heappush(queue, subface)
    collapse_count += 1
assert collapse_count == 19184 and len(faces) == 3929
assert Counter(face.bit_count() - 1 for face in faces) == {0: 23, 1: 253,
                                                            2: 1180, 3: 1815, 4: 658}
for high in faces:
    assert all(low in faces for low, _ in boundary(high, faces))

# Forman matching on the surviving subcomplex, with a fixed pivot order.
unmatched = set(faces)
pairs = []
for v in ORDER:
    bit = 1 << v
    for low in sorted(unmatched):
        if low & bit:
            continue
        high = low | bit
        if high in unmatched:
            unmatched.remove(low)
            unmatched.remove(high)
            pairs.append((low, high))
critical = unmatched
assert len(pairs) == 1856
assert Counter(face.bit_count() - 1 for face in critical) == {0: 1, 3: 212, 4: 4}
mate = {}
for low, high in pairs:
    assert low.bit_count() + 1 == high.bit_count()
    mate[low], mate[high] = high, low
assert len(mate) == len(faces) - len(critical)

# Explicit acyclicity certificate: the entire reversed Hasse graph is a DAG.
adj = defaultdict(list)
in_degree = {face: 0 for face in faces}
edge_count = 0
for high in faces:
    for low, _ in boundary(high, faces):
        source, target = (low, high) if mate.get(low) == high else (high, low)
        adj[source].append(target)
        in_degree[target] += 1
        edge_count += 1
queue = deque(face for face in faces if in_degree[face] == 0)
visited = 0
while queue:
    source = queue.popleft()
    visited += 1
    for target in adj[source]:
        in_degree[target] -= 1
        if in_degree[target] == 0:
            queue.append(target)
assert (visited, edge_count) == (3929, 14596)

# Integral gradient-path evaluation of the degree-4 -> degree-3 Morse boundary.
# In degree 3, a cell paired upward with a 4-cell is replaced by the signed
# remaining 3-faces of that 4-cell; one paired downward with a 2-cell maps to 0.
upward = {low: high for low, high in pairs if low.bit_count() == 4}

@lru_cache(None)
def reduce_3(face):
    if face in critical:
        return {face: 1}
    if face not in upward:
        return {}
    high = upward[face]
    signed = dict(boundary(high, faces))
    pivot = signed[face]
    assert abs(pivot) == 1
    answer = defaultdict(int)
    for other, sign in signed.items():
        if other != face:
            for target, coeff in reduce_3(other).items():
                answer[target] -= pivot * sign * coeff
    return {target: coeff for target, coeff in answer.items() if coeff}

critical_3 = sorted(face for face in critical if face.bit_count() == 4)
critical_4 = sorted(face for face in critical if face.bit_count() == 5)
columns = []
for top in critical_4:
    col = defaultdict(int)
    for low, sign in boundary(top, faces):
        for target, coeff in reduce_3(low).items():
            col[target] += sign * coeff
    columns.append({target: coeff for target, coeff in col.items() if coeff})
assert [len(col) for col in columns] == [26, 27, 55, 26]
assert max(abs(coeff) for col in columns for coeff in col.values()) == 1

# Column relation c0-c1-c2+c3=0 establishes rank <=3.
for row in critical_3:
    assert columns[0].get(row, 0) - columns[1].get(row, 0) \
           - columns[2].get(row, 0) + columns[3].get(row, 0) == 0
# A primitive 3x3 minor establishes rank >=3 and all nonzero Smith factors 1.
rows = (8724, 133252, 270360)
assert all(row in critical_3 for row in rows)
a = [[columns[j].get(row, 0) for j in range(3)] for row in rows]
det = (a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
       - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
       + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0]))
assert abs(det) == 1
print('PASS: 42,297 faces; 19,184 simplicial collapses; acyclic matching;')
print('      critical cells (0:1, 3:212, 4:4), integral Morse rank 3,')
print('      primitive rank-3 image; homotopy wedge of 209 S^3 and one S^4.')
