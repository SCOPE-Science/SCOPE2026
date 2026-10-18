"""Exact integer discrete-Morse certificate for the dominance complex of mu(C5).
Run with Python >= 3.9: python3 verify_grotzsch.py
"""
from collections import Counter, deque
from functools import lru_cache
from hashlib import sha256

NVERT = 11
edges = set()
for j in range(5):
    edges.add(tuple(sorted((j, (j + 1) % 5))))
    for k in ((j - 1) % 5, (j + 1) % 5):
        edges.add(tuple(sorted((5 + j, k))))
    edges.add((5 + j, 10))
assert len(edges) == 20
closed = [1 << j for j in range(NVERT)]
for a, b in edges:
    closed[a] |= 1 << b
    closed[b] |= 1 << a
full = (1 << NVERT) - 1

def dominating(mask):
    covered = 0
    for j in range(NVERT):
        if mask & (1 << j):
            covered |= closed[j]
    return covered == full

faces = {mask for mask in range(1 << NVERT) if dominating(full ^ mask)}
assert len(faces) == 1435 and 0 in faces
assert Counter(s.bit_count()-1 for s in faces if s) == {
    0: 11, 1: 55, 2: 165, 3: 325, 4: 422, 5: 331, 6: 120, 7: 5}
assert all((mask ^ (1 << j)) in faces for mask in faces
           for j in range(NVERT) if mask & (1 << j))

order = (9, 4, 5, 0, 6, 3, 1, 7, 8, 2, 10)
unmatched = faces.copy()
pairs = []
for j in order:
    bit = 1 << j
    for mask in sorted(unmatched):
        partner = mask | bit
        if not mask & bit and partner in unmatched:
            unmatched.remove(mask)
            unmatched.remove(partner)
            pairs.append((mask, partner))
assert len(pairs) == 716 and 0 not in unmatched
assert unmatched == {415, 1071, 1510}
assert (0, 1 << order[0]) in pairs
ordinary_pairs = [(low, high) for low, high in pairs if low != 0]
low_to_high = dict(ordinary_pairs)
nonempty = faces - {0}

# Verify every reversed Hasse edge and the complete DAG, not just a sample.
adjacency = {mask: [] for mask in nonempty}
indegree = {mask: 0 for mask in nonempty}
edges_count = 0
for high in nonempty:
    for j in range(NVERT):
        if high & (1 << j):
            low = high ^ (1 << j)
            if low == 0:
                continue
            a, b = (low, high) if low_to_high.get(low) == high else (high, low)
            adjacency[a].append(b)
            indegree[b] += 1
            edges_count += 1
queue = deque(s for s in nonempty if indegree[s] == 0)
visited = 0
while queue:
    s = queue.popleft()
    visited += 1
    for t in adjacency[s]:
        indegree[t] -= 1
        if indegree[t] == 0:
            queue.append(t)
assert visited == len(nonempty) == 1434
assert all(indegree[s] == 0 for s in nonempty)

# The Morse differential in dimensions 6 -> 5 is a 1x2 integer matrix.
critical5 = [s for s in unmatched if s.bit_count() == 6]
critical6 = sorted(s for s in unmatched if s.bit_count() == 7)
assert critical5 == [1071] and critical6 == [415, 1510]
@lru_cache(None)
def project5(s):
    if s == critical5[0]:
        return 1
    if s not in low_to_high:
        return 0
    high = low_to_high[s]
    assert high.bit_count() == 7 and s.bit_count() == 6
    vertices = tuple(j for j in range(NVERT) if high & (1 << j))
    pivot = (high ^ s).bit_length() - 1
    pivot_sign = (-1) ** vertices.index(pivot)
    return -pivot_sign * sum(((-1) ** k) * project5(high ^ (1 << j))
                             for k, j in enumerate(vertices) if j != pivot)

def signed_morse_entry(critical_top):
    vertices = [j for j in range(NVERT) if critical_top & (1 << j)]
    return sum(((-1) ** k) * project5(critical_top ^ (1 << j))
               for k, j in enumerate(vertices))
morse_boundary = tuple(signed_morse_entry(s) for s in critical6)
assert morse_boundary == (0, 0)
assert max(abs(project5(s)) for s in faces if s.bit_count()==6) <= 3

pair_encoding = ''.join(f'{a:03x}:{b:03x}\n' for a,b in sorted(ordinary_pairs))
print('graph_vertices', NVERT)
print('graph_edges', len(edges))
print('complex_faces_including_empty',len(faces))
print('face_vector', tuple(sum(s.bit_count()==j for s in faces) for j in range(1,9)))
print('ordinary_matched_pairs',len(ordinary_pairs))
print('hasse_arrows',edges_count)
print('dag_vertices_checked', visited)
print('critical_faces_integer_masks', sorted(unmatched))
print('morse_boundary_from_six_to_five', morse_boundary)
print('matching_sha256',sha256(pair_encoding.encode()).hexdigest())
print('VERIFY_OK')
