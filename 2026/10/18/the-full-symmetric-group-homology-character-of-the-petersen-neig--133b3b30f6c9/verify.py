#!/usr/bin/env python3
"""Exact standalone checks for the Petersen open-neighborhood homology character.
Standard-library Python 3; no external files or network are needed.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations, permutations

POINTS = tuple(range(5))
DUADS = tuple(combinations(POINTS, 2))
NUMBER = {v: k for k, v in enumerate(DUADS)}
VERTICES = tuple((k,) for k in range(10))
ADJACENCY = {i: {j for j, v in enumerate(DUADS) if not (set(u) & set(v))}
             for i, u in enumerate(DUADS)}

# Generate the open-neighborhood complex from its defining common-neighbor rule.
ALL_FACES = set()
for d in range(1, 11):
    for face in combinations(range(10), d):
        if any(set(face) <= neighbors for neighbors in ADJACENCY.values()):
            ALL_FACES.add(face)
EDGES = tuple(sorted(f for f in ALL_FACES if len(f) == 2))
TRIANGLES = tuple(sorted(f for f in ALL_FACES if len(f) == 3))
assert len(ALL_FACES) == 50 and len(EDGES) == 30 and len(TRIANGLES) == 10
assert all(len(f) <= 3 for f in ALL_FACES)
assert {tuple(sorted(NUMBER[t] for t in combinations(A, 2)))
        for A in combinations(POINTS, 3)} == set(TRIANGLES)

# Each edge occurs in just one triangle. Remove one free edge with each 2-simplex.
EDGE_COUNT = Counter(e for t in TRIANGLES for e in combinations(t, 2))
assert set(EDGE_COUNT) == set(EDGES) and set(EDGE_COUNT.values()) == {1}
REMAINING = set(EDGES)
for t in TRIANGLES:
    face = min(combinations(t, 2))
    assert EDGE_COUNT[face] == 1 and face in REMAINING
    REMAINING.remove(face)
assert len(REMAINING) == 20
network = {i: set() for i in range(10)}
for a, b in REMAINING:
    network[a].add(b)
    network[b].add(a)
seen = {0}
queue = deque([0])
while queue:
    for j in network[queue.popleft()]:
        if j not in seen:
            seen.add(j)
            queue.append(j)
assert len(seen) == 10
b1 = len(REMAINING) - len(VERTICES) + 1
assert b1 == 11

# Signed simplicial traces on three chain groups, via exhaustive 120 permutations.
def sgn(values):
    return (-1) ** sum(values[i] > values[j]
                       for i in range(len(values)) for j in range(i+1, len(values)))

def trace(faces, action):
    out = 0
    for f in faces:
        ordered = [action[i] for i in f]
        if tuple(sorted(ordered)) == f:
            out += sgn([f.index(i) for i in ordered])
    return out

def cycle_type(p):
    seen = set()
    parts = []
    for i in POINTS:
        if i in seen:
            continue
        j, size = i, 0
        while j not in seen:
            seen.add(j)
            size += 1
            j = p[j]
        parts.append(size)
    return tuple(sorted(parts, reverse=True))

rows = defaultdict(list)
for p in permutations(POINTS):
    action = tuple(NUMBER[tuple(sorted(p[i] for i in pair))] for pair in DUADS)
    assert len(set(action)) == 10
    assert {tuple(sorted(action[i] for i in tri)) for tri in TRIANGLES} == set(TRIANGLES)
    c0, c1, c2 = trace(VERTICES, action), trace(EDGES, action), trace(TRIANGLES, action)
    top = 1 - c0 + c1 - c2
    fixed = sum(p[i] == i for i in POINTS)
    fixed2 = sum(p[p[i]] == i for i in POINTS)
    fixedduads = sum({p[i], p[j]} == {i, j} for i, j in DUADS)
    exterior = ((fixed - 1) ** 2 - (fixed2 - 1)) // 2
    five = sgn(p) * (fixedduads - fixed)
    assert top == exterior + five
    rows[cycle_type(p)].append((top, exterior, five, c0, c1, c2))

expected = {
    (1,1,1,1,1): (11, 6, 5),
    (2,1,1,1): (-1, 0, -1),
    (2,2,1): (-1, -2, 1),
    (3,1,1): (-1, 0, -1),
    (3,2): (-1, 0, -1),
    (4,1): (1, 0, 1),
    (5,): (1, 1, 0),
}
assert len(rows) == len(expected) == 7
for typ, values in sorted(rows.items(), key=lambda kv:(-len(kv[0]),kv[0])):
    assert all(t == values[0] for t in values)
    assert values[0][:3] == expected[typ]
    print('class', typ, 'size', len(values), 'H1,hook,twisted', values[0][:3],
          'chain', values[0][3:])

def inner(i, j):
    return sum(len(values)*values[0][i]*values[0][j] for values in rows.values())

# Irreducibility follows from integer character norms = |S5|; cross inner product 0.
assert inner(1,1) == 120 and inner(2,2) == 120 and inner(1,2) == 0
assert inner(0,0) == 240
assert sum(len(vals)*vals[0][0] for vals in rows.values()) == 0
print('faces', (10,30,10), 'critical graph', (10,20), 'rankH1', b1,
      'group', sum(map(len, rows.values())))
print('irreducible-character-norms', inner(1,1), inner(2,2), 'cross', inner(1,2))
print('PASS')
