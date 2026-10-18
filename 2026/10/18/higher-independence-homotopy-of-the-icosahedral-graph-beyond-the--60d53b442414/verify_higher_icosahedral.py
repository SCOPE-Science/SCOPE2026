#!/usr/bin/env python3
"""Exact finite proof verifier for higher-independence complexes of the icosahedron.

Only the Python standard library is required.  Run with:
    python3 verify_higher_icosahedral.py
"""
from collections import Counter, deque
from itertools import combinations
from math import comb

N = 12
V = tuple(range(N))


def make_edges():
    edges = set()
    # Two poles, two staggered pentagonal rings, and their cross-edges.
    for i in range(5):
        ai, bi = 2 + i, 7 + i
        for u, v in ((0, ai), (1, bi), (ai, 2 + (i + 1) % 5),
                     (bi, 7 + (i + 1) % 5), (ai, bi),
                     (ai, 7 + (i - 1) % 5)):
            edges.add(tuple(sorted((u, v))))
    return edges


E = make_edges()
ADJ = [0] * N
for a, b in E:
    ADJ[a] |= 1 << b
    ADJ[b] |= 1 << a
assert len(E) == 30 and all(a.bit_count() == 5 for a in ADJ)
assert sum(all(tuple(sorted(pair)) in E for pair in combinations(tri, 2))
           for tri in combinations(V, 3)) == 20


def largest_component(mask):
    maximum = 0
    unvisited = mask
    while unvisited:
        bit = unvisited & -unvisited
        connected = bit
        boundary = bit
        while boundary:
            current = boundary & -boundary
            boundary ^= current
            neigh = ADJ[current.bit_length() - 1] & mask & ~connected
            connected |= neigh
            boundary |= neigh
        maximum = max(maximum, connected.bit_count())
        unvisited &= ~connected
    return maximum


def largest_component_union_find(mask):
    """Independent size computation by disjoint-set union on induced edges."""
    parent = list(range(N))
    size = [1] * N

    def root(x):
        while parent[x] != x:
            x = parent[x]
        return x

    for a, b in E:
        if mask & (1 << a) and mask & (1 << b):
            ra, rb = root(a), root(b)
            if ra != rb:
                parent[rb] = ra
                size[ra] += size[rb]
    return max((size[root(v)] for v in V if mask & (1 << v)), default=0)


for mask in range(1 << N):
    assert largest_component(mask) == largest_component_union_find(mask)


def connected(mask):
    return largest_component(mask) == mask.bit_count()


def forbidden_connected_sets(r):
    """The minimal nonfaces have size r+1 and connected induced graph."""
    out = []
    for tup in combinations(V, r + 1):
        mask = sum(1 << v for v in tup)
        if connected(mask):
            out.append(mask)
    return out


def faces_by_components(r):
    return {mask for mask in range(1 << N) if largest_component(mask) <= r}


def faces_by_forbidden(r):
    nonfaces = forbidden_connected_sets(r)
    return {mask for mask in range(1 << N)
            if not any(mask & blocked == blocked for blocked in nonfaces)}


def gf2_rank(columns):
    """Independent binary elimination on ordinary simplicial boundaries."""
    pivots = {}
    for x in columns:
        while x:
            key = x.bit_length() - 1
            if key in pivots:
                x ^= pivots[key]
            else:
                pivots[key] = x
                break
    return len(pivots)


def boundary_ranks(faces):
    by_dim = {j: sorted(m for m in faces if m.bit_count() == j + 1)
              for j in range(max(x.bit_count() for x in faces))}
    ranks = {}
    for d in range(1, len(by_dim)):
        row = {face: i for i, face in enumerate(by_dim[d - 1])}
        cols = []
        for simplex in by_dim[d]:
            col = 0
            for v in V:
                if simplex & (1 << v):
                    col ^= (1 << row[simplex ^ (1 << v)])
            cols.append(col)
        ranks[d] = gf2_rank(cols)
    return ranks


# Explicit sequences of elementary vertex toggles (discrete-Morse pairs).
# The one critical 0-cell plus top-dimensional critical cells gives each wedge.
ORDERS = {
    3: (0, 9, 4, 8, 6, 3, 2, 10, 7, 5, 1, 11),
    4: (0, 4, 5, 8, 7, 3, 1, 10, 9, 11, 2, 6),
    5: (1, 9, 8, 5, 10, 2, 3, 7, 4, 0, 11, 6),
    6: (1, 9, 8, 5, 10, 2, 3, 7, 4, 0, 11, 6),
}
EXPECTED = {
    3: dict(faces=(1, 12, 66, 220, 285, 120, 10),
            critical={0: 1, 3: 10}, ranks=(11, 55, 165, 110, 10)),
    4: dict(faces=(1, 12, 66, 220, 495, 300, 40),
            critical={0: 1, 3: 70}, ranks=(11, 55, 165, 260, 40)),
    5: dict(faces=(1, 12, 66, 220, 495, 792, 112),
            critical={0: 1, 4: 350}, ranks=(11, 55, 165, 330, 112)),
    6: dict(faces=(1, 12, 66, 220, 495, 792, 924, 12),
            critical={0: 1, 5: 450}, ranks=(11, 55, 165, 330, 462, 12)),
}


def morse_and_acyclicity(faces, order):
    assert set(order) == set(V) and len(order) == N
    unmatched = set(faces) - {0}
    matched = []
    for vertex in order:
        for low in sorted(unmatched):
            high = low | (1 << vertex)
            if low in unmatched and not (low & (1 << vertex)) and high in unmatched:
                unmatched.remove(low)
                unmatched.remove(high)
                matched.append((low, high))
    rev = set(matched)
    adjacency = {mask: [] for mask in faces if mask}
    indegree = {mask: 0 for mask in adjacency}
    incidences = 0
    for high in adjacency:
        for v in V:
            if not (high & (1 << v)):
                continue
            low = high ^ (1 << v)
            if low == 0:
                continue
            tail, head = (low, high) if (low, high) in rev else (high, low)
            adjacency[tail].append(head)
            indegree[head] += 1
            incidences += 1
    q = deque(mask for mask in adjacency if indegree[mask] == 0)
    visited = 0
    while q:
        mask = q.popleft()
        visited += 1
        for neighbor in adjacency[mask]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)
    assert visited == len(adjacency), 'The oriented Hasse diagram has a directed cycle'
    return Counter(mask.bit_count() - 1 for mask in unmatched), len(matched), incidences


for r in range(3, 7):
    faces = faces_by_components(r)
    # This is independent of the component bound implementation: connected
    # induced (r+1)-vertex subsets are precisely the minimal forbidden faces.
    assert faces == faces_by_forbidden(r)
    sizes = Counter(mask.bit_count() for mask in faces)
    expected = EXPECTED[r]
    assert tuple(sizes[k] for k in range(len(expected['faces']))) == expected['faces']
    assert max(sizes) == len(expected['faces']) - 1
    critical, pairs, incidences = morse_and_acyclicity(faces, ORDERS[r])
    assert dict(critical) == expected['critical'], (r, critical)
    assert pairs * 2 + sum(critical.values()) == len(faces) - 1
    ranks = boundary_ranks(faces)
    assert tuple(ranks[k] for k in sorted(ranks)) == expected['ranks'], (r, ranks)
    print('r=', r, 'simplices=', len(faces)-1,
          'matching_pairs=', pairs, 'critical=', dict(critical),
          'hasse_edges=', incidences, 'boundary_ranks=', list(ranks.values()))

# Graph vertex-connectivity >=5: deleting any <=4 vertices leaves the rest connected.
for k in range(5):
    for subset in combinations(V, k):
        complement = ((1 << N) - 1) ^ sum(1 << v for v in subset)
        assert connected(complement)

# Hence every induced set with at least eight vertices is connected.
# For 7 <= r <= 11, the complex is the (r-1)-skeleton of the full simplex;
# vertex-0 toggles give one critical vertex and C(11,r) top-dimensional cells.
for r in range(7, 12):
    f = faces_by_components(r)
    assert f == {m for m in range(1 << N) if m.bit_count() <= r}
    reduced_top_betti = comb(11, r)
    assert reduced_top_betti > 0
    print('r=', r, 'skeleton_dimension=', r-1, 'top_sphere_count=', reduced_top_betti)

assert len(faces_by_components(12)) == 1 << N
print('ICOSAHEDRAL_HIGHER_INDEPENDENCE_STAGES_VERIFIED')
