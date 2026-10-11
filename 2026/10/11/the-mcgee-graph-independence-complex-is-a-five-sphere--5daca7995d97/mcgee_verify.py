"""Finite acyclic discrete-Morse certificate for the McGee graph independence complex.

Run with CPython 3, using the standard library only. Vertices are 0,...,23.
The graph is specified by the Hamiltonian cycle plus repeated LCF offsets.
"""
from collections import Counter, deque

N = 24
LCF = (12, 7, -7) * 8
edges = set()
for u in range(N):
    edges.add(tuple(sorted((u, (u + 1) % N))))
    edges.add(tuple(sorted((u, (u + LCF[u]) % N))))
assert len(edges) == 36
adj = [0] * N
for u, v in edges:
    assert u != v
    adj[u] |= 1 << v
    adj[v] |= 1 << u
assert all(a.bit_count() == 3 for a in adj)

# Graph girth: for each root, check every non-tree edge of its breadth-first tree.
girth = N + 1
for root in range(N):
    dist = [-1] * N
    par = [-1] * N
    dist[root] = 0
    q = deque([root])
    while q:
        u = q.popleft()
        for v in range(N):
            if not (adj[u] >> v & 1):
                continue
            if dist[v] < 0:
                dist[v], par[v] = dist[u] + 1, u
                q.append(v)
            elif par[u] != v:
                girth = min(girth, dist[u] + dist[v] + 1)
assert girth == 7, girth

# The 9-cycle below is induced, excluding no-3-divisible-induced-cycle
# hypotheses of general graph independence-complex sphere theorems.
induced_nine = (0, 1, 8, 7, 6, 18, 17, 16, 23)
assert len(set(induced_nine)) == 9
nine_mask = sum(1 << v for v in induced_nine)
for j, u in enumerate(induced_nine):
    expected = (1 << induced_nine[(j - 1) % 9]) | (1 << induced_nine[(j + 1) % 9])
    assert adj[u] & nine_mask == expected

# Construct the *entire* augmented face poset in increasing vertex order.
faces = [0]
for v in range(N):
    bit = 1 << v
    additions = [face | bit for face in faces if not face & adj[v]]
    faces.extend(additions)
assert len(faces) == 34305
assert len(set(faces)) == len(faces)
f_vector = Counter(face.bit_count() for face in faces)
assert [f_vector[i] for i in range(11)] == [1, 24, 240, 1304, 4212, 8328, 10024, 7072, 2668, 424, 8]
index = {face: i for i, face in enumerate(faces)}

# At stage v pair currently unmatched faces F and F+v whenever both exist.
# This fully specifies the finite matching, without an external pair table.
mate = [-1] * len(faces)
for v in range(N):
    bit = 1 << v
    for i, face in enumerate(faces):
        if mate[i] >= 0 or face & bit:
            continue
        j = index.get(face | bit)
        if j is not None and mate[j] < 0:
            mate[i] = j
            mate[j] = i

assert mate[0] == index[1] and mate[index[1]] == 0
# Pass to the ordinary nonempty face poset: the former empty/0 pair is omitted.
mate[0] = -1
mate[index[1]] = -1
critical = [face for i, face in enumerate(faces) if face and mate[i] < 0]
assert set(critical) == {1, sum(1 << v for v in (2, 5, 12, 14, 17, 21))}, critical
pair_count = sum(face != 0 and mate[i] >= 0 for i, face in enumerate(faces)) // 2
assert pair_count == 17151, pair_count
for i, j in enumerate(mate):
    if i and j >= 0:
        assert j and mate[j] == i
        assert (faces[i] ^ faces[j]).bit_count() == 1
        assert (faces[i] & faces[j]) in (faces[i], faces[j])

# Directed incidence graph: each ordinary covering points from coface to face,
# except matched incidences, which are reversed. Kahn's algorithm checks *all*
# vertices and edges of this graph, not merely sampled gradient paths.
outgoing = [[] for _ in faces]
indegree = [0] * len(faces)
incidences = 0
for i, face in enumerate(faces):
    if not face:
        continue
    x = face
    while x:
        bit = x & -x
        x ^= bit
        lower = face ^ bit
        if not lower:
            continue
        j = index[lower]
        if mate[i] == j:
            src, dst = j, i
        else:
            src, dst = i, j
        outgoing[src].append(dst)
        indegree[dst] += 1
        incidences += 1
assert incidences == 197768
queue = deque(i for i, face in enumerate(faces) if face and indegree[i] == 0)
visited = 0
while queue:
    u = queue.popleft()
    visited += 1
    for v in outgoing[u]:
        indegree[v] -= 1
        if indegree[v] == 0:
            queue.append(v)
assert visited == len(faces) - 1 == 34304, (visited, len(faces) - 1)

# Exactly one critical 0-cell and one critical 5-cell gives the homotopy S^5.
assert [face.bit_count() - 1 for face in critical] == [0, 5] or sorted(face.bit_count() - 1 for face in critical) == [0, 5]
print('MCGEE_MORSE_VERIFY_OK',
      'vertices=24 edges=36 girth=7',
      'nonempty_faces=34304',
      'matched_pairs=17151',
      'critical_dimensions=0,5',
      'incidences=197768',
      'acyclic_vertices=34304', 'induced_nine_cycle=verified')
