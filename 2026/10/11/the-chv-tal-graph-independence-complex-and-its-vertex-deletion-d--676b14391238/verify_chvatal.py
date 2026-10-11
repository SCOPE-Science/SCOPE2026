"""Exact finite discrete-Morse certificates for a labeled Chvatal graph.

Run: python3 verify_chvatal.py. Only Python's standard library is required.
The graph is specified by the complete edge list below, not by a package graph.
"""
from collections import Counter, deque

N = 12
EDGES = (
    (0, 1), (0, 4), (0, 6), (0, 9),
    (1, 2), (1, 5), (1, 7),
    (2, 3), (2, 6), (2, 8),
    (3, 4), (3, 7), (3, 9),
    (4, 5), (4, 8),
    (5, 10), (5, 11),
    (6, 10), (6, 11),
    (7, 8), (7, 11),
    (8, 10), (9, 10), (9, 11),
)
E = set(EDGES)
assert len(E) == 24 and all(0 <= a < b < N for a, b in E)
NEIGHBORS = [set() for _ in range(N)]
for a, b in E:
    NEIGHBORS[a].add(b)
    NEIGHBORS[b].add(a)
assert all(len(x) == 4 for x in NEIGHBORS)
assert all(not (NEIGHBORS[a] & NEIGHBORS[b]) for a, b in E)

# Two explicit edge-preserving permutations. Their generated vertex orbits
# have sizes four and eight. Independence-set counts distinguish the orbits.
AUTOMORPHISMS = (
    (0, 4, 3, 2, 1, 5, 9, 8, 7, 6, 11, 10),
    (1, 0, 6, 11, 5, 4, 2, 9, 10, 7, 8, 3),
)
for p in AUTOMORPHISMS:
    assert sorted(p) == list(range(N))
    assert {tuple(sorted((p[a], p[b]))) for a, b in E} == E

def orbit(v):
    result = {v}
    while True:
        new = result | {p[x] for p in AUTOMORPHISMS for x in result}
        if new == result:
            return result
        result = new

A = {0, 1, 4, 5}
B = set(range(N)) - A
assert orbit(0) == A and orbit(2) == B

def make_faces(excluded=()):
    permitted = ((1 << N) - 1) ^ sum(1 << v for v in excluded)
    out = set()
    for mask in range(1, 1 << N):
        if mask & ~permitted:
            continue
        if all(not ((mask >> a & 1) and (mask >> b & 1)) for a, b in E):
            out.add(mask)
    return out

def boundary(mask):
    bits = [v for v in range(N) if mask >> v & 1]
    return [(mask ^ (1 << v), (-1) ** j) for j, v in enumerate(bits)]

def morse_certificate(faces, pivot_order=range(N)):
    unmatched = set(faces)
    pairs = []
    for v in pivot_order:
        for low in sorted(unmatched):
            high = low | (1 << v)
            if not (low >> v & 1) and high in unmatched:
                unmatched.remove(low)
                unmatched.remove(high)
                pairs.append((low, high))
    assert 2 * len(pairs) + len(unmatched) == len(faces)
    pairset = set(pairs)
    index = {mask: i for i, mask in enumerate(sorted(faces))}
    adjacency = [[] for _ in faces]
    indegree = [0] * len(faces)
    directed_incidences = 0
    for high in faces:
        for low, _ in boundary(high):
            if low not in faces:
                continue
            src, dst = ((low, high) if (low, high) in pairset
                        else (high, low))
            adjacency[index[src]].append(index[dst])
            indegree[index[dst]] += 1
            directed_incidences += 1
    queue = deque(i for i, x in enumerate(indegree) if x == 0)
    visited = 0
    while queue:
        i = queue.popleft()
        visited += 1
        for j in adjacency[i]:
            indegree[j] -= 1
            if indegree[j] == 0:
                queue.append(j)
    assert visited == len(faces), 'directed gradient cycle'
    critical = {}
    for mask in unmatched:
        critical.setdefault(mask.bit_count() - 1, []).append(mask)
    for cells in critical.values():
        cells.sort()
    return len(pairs), directed_incidences, critical, pairs

def elementary_collapse_certificate(faces, pairs, remaining_vertex):
    """Produce an actual elementary-collapse order from matched pairs."""
    cells = set(faces)
    available = set(pairs)
    moves = 0
    while available:
        free = None
        for low, high in sorted(available, key=lambda x: (-x[1].bit_count(), x[0])):
            if low not in cells or high not in cells:
                continue
            if all(face in (low, high) or (face & low) != low for face in cells):
                free = (low, high)
                break
        assert free is not None, 'no next elementary collapse'
        low, high = free
        cells.remove(low)
        cells.remove(high)
        available.remove(free)
        moves += 1
    assert cells == {remaining_vertex}
    return moves

# Independently check all enumerated link / deletion cardinalities.
whole = make_faces()
assert len(whole) == 126
assert tuple(Counter(x.bit_count() - 1 for x in whole)[d] for d in range(4)) == (12, 42, 52, 20)
for v in range(N):
    deleted = make_faces({v})
    linked = make_faces(NEIGHBORS[v] | {v})
    assert len(deleted) == (99 if v in A else 98)
    assert len(linked) == (26 if v in A else 27)

def colorable(k, removed=()):
    vertices = sorted(set(range(N)) - set(removed),
                      key=lambda v: (-len(NEIGHBORS[v]), v))
    colors = {}
    def assign(index):
        if index == len(vertices):
            return True
        v = vertices[index]
        forbidden = {colors[w] for w in NEIGHBORS[v] if w in colors}
        for c in range(k):
            if c not in forbidden:
                colors[v] = c
                if assign(index+1):
                    return True
                del colors[v]
        return False
    return assign(0)

assert not colorable(3) and colorable(4)
assert all(colorable(3, {v}) and not colorable(2, {v}) for v in range(N))

CASES = {
    'whole': ((), 126, 62, 320, {0: 1, 2: 1}),
    'delete_A': ({0}, 99, 49, 243, {0: 1}),
    'delete_B': ({2}, 98, 48, 239, {0: 1, 2: 1}),
    'link_A': (NEIGHBORS[0] | {0}, 26, 12, 44, {0: 1, 1: 1}),
    'link_B': (NEIGHBORS[2] | {2}, 27, 13, 47, {0: 1}),
}
for name, (excluded, count, expected_pairs, expected_incidences, expected_critical) in CASES.items():
    faces = make_faces(excluded)
    order = ([5] + [v for v in range(N) if v != 5]) if name == 'delete_A' else range(N)
    pairs, incidences, critical, matched = morse_certificate(faces, order)
    dims = {d: len(c) for d, c in critical.items()}
    assert len(faces) == count, (name, len(faces))
    assert pairs == expected_pairs, (name, pairs)
    assert incidences == expected_incidences, (name, incidences)
    assert dims == expected_critical, (name, dims)
    if name in ('delete_A', 'link_B'):
        assert elementary_collapse_certificate(faces, matched, critical[0][0]) == pairs
    print(name, 'faces', len(faces), 'pairs', pairs,
          'incidences', incidences, 'critical', dims)

print('CHVATAL_VERTEX_DICHOTOMY_VERIFY_OK',
      'orbits=4+8', 'chromatic=4_all_vertex_deletions=3', 'whole=S2',
      'delete_A=point', 'link_A=S1',
      'delete_B=S2', 'link_B=point',
      'elementary_collapses=delete_A+link_B')
