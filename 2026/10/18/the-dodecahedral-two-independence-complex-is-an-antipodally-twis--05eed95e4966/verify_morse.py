"""Exact finite Morse certificate for the two-independence complex of GP(10,2).

Python 3 standard library only. Every simplex, matching pair, Hasse cover,
and directed gradient step is enumerated. The integer boundary uses oriented
simplices with increasing vertex labels.
"""
from collections import Counter, deque
from itertools import permutations

N = 20
adj = [0] * N
for i in range(10):
    for u, v in ((i, (i + 1) % 10), (i, 10 + i),
                 (10 + i, 10 + ((i + 2) % 10))):
        adj[u] |= 1 << v
        adj[v] |= 1 << u
assert all(x.bit_count() == 3 for x in adj)

# Recursively enumerate *all* faces, including the empty face.
faces = [0]
for v in range(N):
    for face in tuple(faces):
        nbor = face & adj[v]
        if nbor.bit_count() > 1:
            continue
        if nbor and (face & adj[nbor.bit_length() - 1]):
            continue
        faces.append(face | (1 << v))
face_set = set(faces)
assert len(faces) == len(face_set) == 63143
f_vector = dict(sorted(Counter(s.bit_count()-1 for s in faces).items()))
assert list(f_vector.values()) == [1, 20, 190, 1080, 3985, 9772,
                                   15870, 16640, 10770, 4000, 750, 60, 5]
facets = [s for s in faces if s and all((s | (1 << v)) not in face_set
                                          for v in range(N) if not ((s >> v) & 1))]
facet_counts = dict(sorted(Counter(s.bit_count() - 1 for s in facets).items()))
assert len(facets) == 510
assert facet_counts == {7: 25, 8: 60, 9: 420, 11: 5}

# Greedy vertex-toggle matching: at pivot v pair every still-unmatched
# face s avoiding v with the available upper face s union {v}.
mate = {}
for v in range(N):
    bit = 1 << v
    for s in faces:
        t = s | bit
        if not (s & bit) and s not in mate and t in face_set and t not in mate:
            mate[s] = t
            mate[t] = s
assert mate.get(0) == 1
# Use the ordinary, nonaugmented face poset: leave vertex 0 critical.
del mate[0]
del mate[1]
assert len(mate) == 63130
critical = [s for s in faces if s and s not in mate]
critical_counts = dict(sorted(Counter(s.bit_count()-1 for s in critical).items()))
assert critical_counts == {0: 1, 5: 1, 6: 6, 7: 4}
assert len(critical) == 12

# An unmatched Hasse cover points downward; a matched cover points upward.
# A topological traversal of all vertices and covers establishes acyclicity.
indegree = {s: 0 for s in faces if s}
out = {s: [] for s in faces if s}
covers = 0
for t in faces:
    bits = t
    while bits:
        bit = bits & -bits
        bits -= bit
        s = t ^ bit
        if not s:  # omit empty-face covers
            continue
        x, y = (s, t) if mate.get(s) == t else (t, s)
        out[x].append(y)
        indegree[y] += 1
        covers += 1
queue = deque(s for s in indegree if indegree[s] == 0)
visited = 0
while queue:
    s = queue.popleft()
    visited += 1
    for t in out[s]:
        indegree[t] -= 1
        if indegree[t] == 0:
            queue.append(t)
assert visited == len(faces) - 1 == 63142
assert covers == 410500


def signed_boundary(mask):
    """Return boundary (facet, ±1), in increasing-vertex orientation."""
    bits = mask
    j = 0
    while bits:
        bit = bits & -bits
        bits -= bit
        yield mask ^ bit, 1 if j % 2 == 0 else -1
        j += 1


def morse_boundary(k):
    """Return integral differential from critical k-cells to critical (k-1)-cells.

    Algebraic cancellation is evaluated along the DAG of gradient paths:
    for a lower face a matched upward to b, the normal form satisfies
    NF(a)=-[b:a] sum_{v != a}[b:v] NF(v). Upper-matched lower faces
    contribute zero. Thus the computation uses integer arithmetic only.
    """
    lower = [s for s in faces if s.bit_count() == k]
    crit_lower = [s for s in lower if s not in mate]
    positions = {s: i for i, s in enumerate(crit_lower)}
    successors = {}
    incoming = {s: 0 for s in lower}
    for s in lower:
        t = mate.get(s)
        if t is None or t.bit_count() != k + 1:
            continue
        eps = dict(signed_boundary(t))[s]
        row = [(v, -e * eps) for v, e in signed_boundary(t) if v != s]
        successors[s] = row
        for v, _ in row:
            incoming[v] += 1
    queue = deque(s for s, c in incoming.items() if c == 0)
    order = []
    while queue:
        s = queue.popleft()
        order.append(s)
        for v, _ in successors.get(s, []):
            incoming[v] -= 1
            if incoming[v] == 0:
                queue.append(v)
    assert len(order) == len(lower)
    normal_form = {}
    for s in reversed(order):
        outrow = [0] * len(crit_lower)
        if s in positions:
            outrow[positions[s]] = 1
        else:
            for v, e in successors.get(s, []):
                for j, coeff in enumerate(normal_form[v]):
                    outrow[j] += e * coeff
        normal_form[s] = outrow
    crit_upper = [s for s in faces if s.bit_count() == k + 1 and s not in mate]
    columns = []
    for s in crit_upper:
        col = [0] * len(crit_lower)
        for v, eps in signed_boundary(s):
            for j, coeff in enumerate(normal_form[v]):
                col[j] += eps * coeff
        columns.append(col)
    return crit_upper, crit_lower, columns

up6, low5, d6_columns = morse_boundary(6)
up7, low6, d7_columns = morse_boundary(7)
assert d6_columns == [[0], [0], [-1], [0], [1], [0]]
assert d7_columns == [[1, 0, 0, 0, 0, 0],
                      [1, 0, 1, -1, 1, 0],
                      [0, 0, 0, 1, 0, -1],
                      [0, -1, 0, 0, 0, 0]]
assert up6 == low6
D6 = [c[0] for c in d6_columns]
assert all(sum(D6[j] * c[j] for j in range(6)) == 0 for c in d7_columns)

# A unit four-by-four minor proves that d7 has rank four and primitive image.
# Columns here are critical 7-cells, rows critical 6-cells indexed 0..3.
a = [[d7_columns[col][row] for col in range(4)] for row in range(4)]
def sign(p):
    return -1 if sum(p[i] > p[j] for i in range(len(p))
                     for j in range(i + 1, len(p))) % 2 else 1
unit_minor = sum(sign(p) * a[0][p[0]] * a[1][p[1]] * a[2][p[2]] * a[3][p[3]]
                 for p in permutations(range(4)))
assert abs(unit_minor) == 1
assert 1 in [abs(v) for v in D6]
print('graph_vertices=20 graph_edges=30')
print('face_vector(-1..11)=', list(f_vector.values()))
print('nonempty_faces=63142 matching_pairs=31565')
print('facet_counts=', facet_counts)
print('hasse_covers=410500 directed_vertices=63142 acyclic_topological_sort=63142')
print('critical_cells=', critical_counts)
print('d6_columns=', d6_columns)
print('d7_columns=', d7_columns)
print('d7_unimodular_minor_rows_0_1_2_3=', unit_minor)
print('reduced_integral_homology_H6=Z_all_others=0')
print('simplicial_Morse_WC_homotopy_type=S6')
