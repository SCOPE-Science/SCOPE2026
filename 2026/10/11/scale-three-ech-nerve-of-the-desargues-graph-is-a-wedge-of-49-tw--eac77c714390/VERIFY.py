"""Reconstruct the intrinsic scale-three graph Cech nerve of GP(10,3).

Requires only Python 3 standard library; checks the entire discrete Morse gradient.
The input is defined internally by an explicitly specified finite graph.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations
from random import Random

N = 10
EDGES = set()
def edge(u, v):
    EDGES.add(tuple(sorted((u, v))))
for i in range(N):
    edge(i, (i + 1) % N)
    edge(10 + i, 10 + (i + 3) % N)
    edge(i, 10 + i)
assert len(EDGES) == 30
vertices = tuple(range(20))
closed = {v: {v} for v in vertices}
for u, v in EDGES:
    closed[u].add(v)
    closed[v].add(u)
assert all(len(s) == 4 for s in closed.values())

facets = [closed[u] | closed[v] for u, v in sorted(EDGES)]
assert len(facets) == 30 and all(len(s) == 6 for s in facets)
complex_faces = set()
for F in facets:
    for d in range(1, 7):
        for S in combinations(sorted(F), d):
            complex_faces.add(sum(1 << j for j in S))
assert Counter(x.bit_count()-1 for x in complex_faces) == {
    0: 20, 1: 150, 2: 440, 3: 410, 4: 180, 5: 30
}
assert len(complex_faces) == 1230

# Exhaustive elementary free-face collapse, sorted to remove nondeterminism.
remaining = set(complex_faces)
first_pairs = []
while True:
    upper = defaultdict(list)
    for tau in remaining:
        if tau.bit_count() < 2:
            continue
        for v in vertices:
            if tau & (1 << v):
                upper[tau ^ (1 << v)].append(tau)
    possibilities = []
    for sigma, sup in upper.items():
        if sigma in remaining and len(sup) == 1:
            possibilities.append((sup[0].bit_count(), sup[0], sigma))
    if not possibilities:
        break
    _, tau, sigma = max(possibilities)
    assert len(upper[sigma]) == 1 and upper[sigma][0] == tau
    assert tau in remaining and sigma in remaining
    remaining.remove(tau)
    remaining.remove(sigma)
    first_pairs.append((sigma, tau))
assert len(first_pairs) == 472
assert Counter(x.bit_count()-1 for x in remaining) == {0: 20, 1: 118, 2: 148}

# Build a spanning tree, then a matching of tree vertices to tree edges.
rng = Random(1)
onefaces = sorted(s for s in remaining if s.bit_count() == 2)
rng.shuffle(onefaces)
parent = list(vertices)
def root(x):
    while parent[x] != x:
        x = parent[x]
    return x
spanning = set()
for s in onefaces:
    u, v = (j for j in vertices if s & (1 << j))
    a, b = root(u), root(v)
    if a != b:
        parent[a] = b
        spanning.add(s)
assert len(spanning) == 19
adj = defaultdict(list)
for s in spanning:
    u, v = (j for j in vertices if s & (1 << j))
    adj[u].append((v, s))
    adj[v].append((u, s))
visit = {0}
q = deque([0])
tree_pairs = []
while q:
    u = q.popleft()
    for v, s in adj[u]:
        if v not in visit:
            visit.add(v)
            q.append(v)
            tree_pairs.append((1 << v, s))
assert len(visit) == 20 and len(tree_pairs) == 19

# Match each non-tree edge with a triangle only after all the other
# boundary edges have already been matched or belong to the tree.
unmatched_edges = set(onefaces) - spanning
triangles = sorted(s for s in remaining if s.bit_count() == 3)
unmatched_triangles = set(triangles)
triangle_pairs = []
while True:
    choices = []
    for t in triangles:
        if t not in unmatched_triangles:
            continue
        possible = [e for e in unmatched_edges if (t & e) == e]
        if len(possible) == 1:
            choices.append((possible[0], t))
    if not choices:
        break
    s, t = rng.choice(choices)
    assert s in unmatched_edges and t in unmatched_triangles
    unmatched_edges.remove(s)
    unmatched_triangles.remove(t)
    triangle_pairs.append((s, t))
assert len(triangle_pairs) == 99
assert not unmatched_edges and len(unmatched_triangles) == 49

pairs = first_pairs + tree_pairs + triangle_pairs
matched = {}
for low, high in pairs:
    assert low not in matched and high not in matched
    assert low & high == low and high.bit_count() == low.bit_count()+1
    matched[low] = high
    matched[high] = low
assert len(pairs) == 590 and len(matched) == 1180
critical = complex_faces - matched.keys()
assert Counter(s.bit_count()-1 for s in critical) == {0: 1, 2: 49}
assert critical & {1} == {1}

# Complete directed Hasse graph: unmatched incidences higher -> lower,
# matched incidences lower -> higher. Topological sort proves acyclicity.
indegree = {s: 0 for s in complex_faces}
forward = defaultdict(list)
arc_count = 0
for high in complex_faces:
    if high.bit_count() == 1:
        continue
    for v in vertices:
        if high & (1 << v):
            low = high ^ (1 << v)
            assert low in complex_faces
            u, w = (low, high) if matched.get(low) == high else (high, low)
            forward[u].append(w)
            indegree[w] += 1
            arc_count += 1
q = deque(s for s in complex_faces if indegree[s] == 0)
seen = 0
while q:
    u = q.popleft()
    seen += 1
    for w in forward[u]:
        indegree[w] -= 1
        if indegree[w] == 0:
            q.append(w)
assert seen == 1230, (seen, len(complex_faces))
assert arc_count == sum(s.bit_count() for s in complex_faces if s.bit_count()>1)

# Independent mod-two chain ranks of the remaining 2-complex.
def gf2_rank(vectors):
    basis = {}
    for v in vectors:
        while v:
            k = v.bit_length() - 1
            if k not in basis:
                basis[k] = v
                break
            v ^= basis[k]
    return len(basis)
def boundary_rank(d):
    lower = sorted(s for s in remaining if s.bit_count() == d)
    higher = sorted(s for s in remaining if s.bit_count() == d + 1)
    lower_id = {s: i for i, s in enumerate(lower)}
    cols = []
    for high in higher:
        col = 0
        for v in vertices:
            if high & (1 << v):
                col ^= 1 << lower_id[high ^ (1 << v)]
        cols.append(col)
    return gf2_rank(cols)
assert boundary_rank(1) == 19
assert boundary_rank(2) == 99
print('VERIFY_OK', 'facets=30 faces=1230 simplicial_collapses=472',
      'gradient_pairs=590 critical_0=1 critical_2=49',
      'Hasse_arcs='+str(arc_count), 'mod2_boundary_ranks=19,99')
