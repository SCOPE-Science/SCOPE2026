#!/usr/bin/env python3
"""Exact standalone verification of the Pappus path-hypergraph independence complex.

Only the Python standard library is required. All integer assertions are exact.
"""
from collections import Counter, deque
from functools import lru_cache

N = 18
LCF = (5, 7, -7, 7, -7, -5) * 3
edges = {tuple(sorted((i, (i + 1) % N))) for i in range(N)}
edges |= {tuple(sorted((i, (i + LCF[i]) % N))) for i in range(N)}
adj = [0] * N
for a, b in edges:
    assert a != b
    adj[a] |= 1 << b
    adj[b] |= 1 << a
assert len(edges) == 27 and all(a.bit_count() == 3 for a in adj)
# Confirm the graph is connected, bipartite, and has girth six.
dists0 = {0: 0}
queue0 = deque([0])
while queue0:
    u = queue0.popleft()
    for v in range(N):
        if adj[u] & (1 << v) and v not in dists0:
            dists0[v] = dists0[u] + 1
            queue0.append(v)
assert len(dists0) == N
assert all((dists0[a] - dists0[b]) % 2 != 0 for a, b in edges)
girth = N + 1
for origin in range(N):
    dist = {origin: 0}
    parent = {origin: None}
    q = deque([origin])
    while q:
        u = q.popleft()
        for v in range(N):
            if not (adj[u] & (1 << v)):
                continue
            if v not in dist:
                dist[v] = dist[u] + 1
                parent[v] = u
                q.append(v)
            elif parent[u] != v:
                girth = min(girth, dist[u] + dist[v] + 1)
assert girth == 6


def valid(mask):
    return all((adj[v] & mask).bit_count() <= 1
               for v in range(N) if mask & (1 << v))


# Construction A: incremental closure, checking the new vertex and its neighbors.
faces = [0]
for v in range(N):
    bit = 1 << v
    for mask in faces[:]:
        nb = adj[v] & mask
        if nb.bit_count() > 1 or any((adj[w] & mask) for w in range(N) if nb & (1 << w)):
            continue
        faces.append(mask | bit)
face_set = set(faces)
assert len(face_set) == len(faces)
# Construction B: all 2**18 vertex masks, with the direct definition.
brute = {m for m in range(1 << N) if valid(m)}
assert face_set == brute
face_set.remove(0)
assert len(face_set) == 20651
fvector = [sum(m.bit_count() == k for m in face_set) for k in range(1, 11)]
assert fvector == [18, 153, 762, 2394, 4806, 6027, 4428, 1728, 308, 27]

# Deterministic simplex matching. Match all remaining faces by toggling each
# vertex, in the stated increasing order, then remove each pair from the pool.
remaining = set(face_set)
matched = []
for v in range(N):
    bit = 1 << v
    stage = [(f, f | bit) for f in sorted(remaining)
             if not f & bit and f | bit in remaining]
    for lower, upper in stage:
        assert lower in remaining and upper in remaining
        remaining.remove(lower)
        remaining.remove(upper)
    matched.extend(stage)
assert len(matched) == 10320 and len(remaining) == 11
critical5 = sorted(f for f in remaining if f.bit_count() == 6)
critical6 = sorted(f for f in remaining if f.bit_count() == 7)
critical0 = sorted(f for f in remaining if f.bit_count() == 1)
assert len(critical0) == 1 and len(critical5) == 9 and len(critical6) == 1
assert len(remaining) == 11
assert critical5 == [13104, 26146, 39186, 52230, 74340, 100486,
                     135576, 148618, 196812]
assert critical6 == [183554]

# Full directed Hasse graph: ordinary covering relations point from upper to
# lower; matched relations are reversed. Kahn topological sort proves acyclicity.
matched_set = set(matched)
adjacency = {f: [] for f in face_set}
indegree = {f: 0 for f in face_set}
incidences = 0
for upper in face_set:
    bits = [b for b in range(N) if upper & (1 << b)]
    for b in bits:
        lower = upper ^ (1 << b)
        if not lower:  # the empty face is excluded from the ordinary poset
            continue
        assert lower in face_set
        u, v = (lower, upper) if (lower, upper) in matched_set else (upper, lower)
        adjacency[u].append(v)
        indegree[v] += 1
        incidences += 1
queue = deque(f for f, d in indegree.items() if d == 0)
visited = 0
while queue:
    u = queue.popleft()
    visited += 1
    for v in adjacency[u]:
        indegree[v] -= 1
        if indegree[v] == 0:
            queue.append(v)
assert visited == len(face_set)
assert all(d == 0 for d in indegree.values())

# Exact signed integral algebraic Morse boundary, calculated by recursively
# resolving every matched (dimension 5,dimension 6) unit-incidence pair.
low_to_high = dict(matched)
high_to_low = {up: lo for lo, up in matched}
critical5_index = {f: i for i, f in enumerate(critical5)}


def boundary(simplex):
    vertices = [v for v in range(N) if simplex & (1 << v)]
    return [(simplex ^ (1 << v), 1 if j % 2 == 0 else -1)
            for j, v in enumerate(vertices)]


@lru_cache(None)
def project_degree5(face):
    assert face.bit_count() == 6
    if face in critical5_index:
        return {critical5_index[face]: 1}
    if face in high_to_low:
        assert high_to_low[face].bit_count() == 5
        return {}
    upper = low_to_high[face]
    assert upper.bit_count() == 7
    upper_bd = dict(boundary(upper))
    incidence = upper_bd[face]
    assert incidence in (-1, 1)
    out = Counter()
    for other, coef in upper_bd.items():
        if other == face:
            continue
        for i, n in project_degree5(other).items():
            out[i] -= incidence * coef * n
    return {i: n for i, n in out.items() if n}


morse = Counter()
for f, coef in boundary(critical6[0]):
    for i, n in project_degree5(f).items():
        morse[i] += coef * n
integral_column = [morse[i] for i in range(9)]
assert integral_column == [0] * 9

# Independent mod-two homology calculation on the full original simplicial
# boundary matrices, rather than on the discrete Morse matched complex.
levels = {k: sorted(m for m in face_set if m.bit_count() == k)
          for k in range(1, 11)}
ranks = {1: 0}
for k in range(2, 11):
    index = {m: j for j, m in enumerate(levels[k - 1])}
    pivots = {}
    for upper in levels[k]:
        column = 0
        for v in range(N):
            if upper & (1 << v):
                column ^= 1 << index[upper ^ (1 << v)]
        while column:
            p = column.bit_length() - 1
            if p not in pivots:
                pivots[p] = column
                break
            column ^= pivots[p]
    ranks[k] = len(pivots)
assert [ranks[k] for k in range(2, 11)] == [17, 136, 626, 1768,
                                            3038, 2980, 1447, 281, 27]
mod2_betti = [len(levels[k]) - ranks[k] - ranks.get(k + 1, 0)
              for k in range(1, 11)]
assert mod2_betti == [1, 0, 0, 0, 0, 9, 1, 0, 0, 0]

print('graph_vertices=18 graph_edges=27 all_degrees=3 girth=6 bipartite=True')
print(f'nonempty_faces={len(face_set)} fvector={fvector}')
print(f'matched_pairs={len(matched)} critical_counts=(1@0,9@5,1@6)')
print('hasse_incidences=', incidences, 'toposort_visited=', visited, sep='')
print('critical5_masks=', critical5, sep='')
print('critical6_mask=', critical6, sep='')
print('integral_morse_boundary_6_to_5=', integral_column, sep='')
print('gradient_projection_states=', project_degree5.cache_info().currsize, sep='')
print('mod2_boundary_ranks_dimensions_1_to_9=',
      [ranks[k] for k in range(2, 11)], sep='')
print('mod2_unreduced_betti_dimensions_0_to_9=', mod2_betti, sep='')
print('ALL_CHECKS_PASS')
