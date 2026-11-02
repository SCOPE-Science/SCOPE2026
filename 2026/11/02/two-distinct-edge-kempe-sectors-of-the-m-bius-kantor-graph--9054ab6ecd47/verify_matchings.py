#!/usr/bin/env python3
"""Exhaustive perfect-matching verification of a finite edge-Kempe classification."""
from collections import Counter, deque
from itertools import permutations

N = 8
edges = sorted({tuple(sorted(pair)) for i in range(N)
                for pair in [(i, (i+1) % N), (i, N+i),
                             (N+i, N+(i+3) % N)]})
assert len(edges) == 24
inc = [[j for j, e in enumerate(edges) if v in e] for v in range(16)]
assert all(len(row) == 3 for row in inc)
FULL = (1 << 24) - 1
matchings = []

def enumerate_matchings(used, chosen):
    if used == (1 << 16) - 1:
        matchings.append(chosen)
        return
    v = next(x for x in range(16) if not (used >> x) & 1)
    for ei in inc[v]:
        a, b = edges[ei]
        w = b if a == v else a
        if not (used >> w) & 1:
            enumerate_matchings(used | (1 << v) | (1 << w), chosen | (1 << ei))

enumerate_matchings(0, 0)
assert len(matchings) == 33 and len(set(matchings)) == 33
mset = set(matchings)
colors = [(a, b, FULL ^ (a | b)) for a in matchings for b in matchings
          if not (a & b) and FULL ^ (a | b) in mset]
assert len(colors) == 120 and len(set(colors)) == 120
ids = {s: i for i, s in enumerate(colors)}

# The union of any two perfect matchings is a 2-factor of alternating cycles.
def alternating_cycles(mask):
    pending = {i for i in range(24) if (mask >> i) & 1}
    components = []
    while pending:
        start = pending.pop()
        stack, submask = [start], 1 << start
        while stack:
            ei = stack.pop()
            for v in edges[ei]:
                for ej in inc[v]:
                    if ej in pending:
                        pending.remove(ej)
                        stack.append(ej)
                        submask |= 1 << ej
        components.append(submask)
    return components

adj = [set() for _ in colors]
patterns = []
for ci, triple in enumerate(colors):
    sig = []
    for a, b in ((0, 1), (0, 2), (1, 2)):
        cycles = alternating_cycles(triple[a] | triple[b])
        assert sum(t.bit_count() for t in cycles) == 16
        sig.append(tuple(sorted(t.bit_count() for t in cycles)))
        for cycle in cycles:
            updated = list(triple)
            updated[a] ^= cycle
            updated[b] ^= cycle
            j = ids[tuple(updated)]
            assert j != ci
            adj[ci].add(j)
    patterns.append(tuple(sorted(sig)))
assert all(i in adj[j] for j, row in enumerate(adj) for i in row)
assert sum(map(len, adj)) // 2 == 342
assert Counter(map(len, adj)) == {4: 18, 6: 102}

seen, components = set(), []
for start in range(len(colors)):
    if start in seen:
        continue
    queue = [start]
    seen.add(start)
    for v in queue:
        for w in adj[v]:
            if w not in seen:
                seen.add(w)
                queue.append(w)
    components.append(queue)
components.sort(key=len)
assert [len(c) for c in components] == [24, 96]
small, large = components
assert Counter(patterns[v] for v in small) == {
    ((8, 8), (16,), (16,)): 18,
    ((8, 8), (8, 8), (8, 8)): 6,
}
assert Counter(patterns[v] for v in large) == {
    ((6, 10), (6, 10), (6, 10)): 96,
}

# Exhaustive breadth-first search establishes radius, diameter, and profiles.
summary = {}
for comp in components:
    counts = Counter()
    for v in comp:
        dist = {v: 0}
        todo = deque([v])
        while todo:
            u = todo.popleft()
            for w in adj[u]:
                if w not in dist:
                    dist[w] = dist[u] + 1
                    todo.append(w)
        assert len(dist) == len(comp)
        layer = Counter(dist.values())
        counts[tuple(layer[k] for k in range(max(layer)+1))] += 1
    summary[len(comp)] = counts
assert summary[24] == {(1, 4, 15, 4): 18, (1, 6, 15, 2): 6}
assert summary[96] == {(1, 6, 27, 42, 20): 96}

# Proper two-colouring criterion is checked separately in each component.
def bipartite(comp):
    sign = {}
    for start in comp:
        if start in sign:
            continue
        sign[start] = 0
        todo = deque([start])
        while todo:
            u = todo.popleft()
            for v in adj[u]:
                if v not in sign:
                    sign[v] = sign[u] ^ 1
                    todo.append(v)
                elif sign[v] == sign[u]:
                    return False
    return True

assert not bipartite(small) and bipartite(large)
assert sum(len(adj[v]) for v in small) // 2 == 54
assert sum(len(adj[v]) for v in large) // 2 == 288

# Four explicit graph symmetries generate a group of 96 automorphisms.
r = tuple((i+1) % 8 if i < 8 else 8+(i-8+1) % 8 for i in range(16))
s = tuple(-i % 8 if i < 8 else 8+(-(i-8)) % 8 for i in range(16))
t = tuple(8+(3*i) % 8 if i < 8 else (3*(i-8)) % 8 for i in range(16))
w = (0, 1, 9, 12, 4, 5, 13, 8, 7, 2, 14, 15, 3, 6, 10, 11)
generators = [r, s, t, w]
edge_id = {e: i for i, e in enumerate(edges)}
assert all({tuple(sorted((p[u], p[v]))) for u, v in edges} == set(edges)
           for p in generators)
identity = tuple(range(16))
group = {identity}
queue = [identity]
for p in queue:
    for gen in generators:
        new = tuple(p[gen[i]] for i in range(16))
        if new not in group:
            group.add(new)
            queue.append(new)
assert len(group) == 96

def permute_coloring(c, p):
    mapping = [edge_id[tuple(sorted((p[u], p[v])))] for u, v in edges]
    return tuple(sum(1 << mapping[j] for j in range(24) if (m >> j) & 1) for m in c)

anchor = colors[large[0]]
images = {ids[permute_coloring(anchor, p)] for p in group}
assert len(images) == 96 and images == set(large)
# This is a free transitive action of a group of order 96: a Cayley graph.
assert all(ids[permute_coloring(anchor, p)] in large for p in group)
# For the other component, the action has four six-element orbits.
todo = set(small)
orbits = []
while todo:
    root = colors[next(iter(todo))]
    orbit = {ids[permute_coloring(root, p)] for p in group}
    assert orbit <= todo
    todo -= orbit
    orbits.append(len(orbit))
assert sorted(orbits) == [6, 6, 6, 6]
# Each neighbor of a reference Cayley-graph vertex comes from an involution.
neighbor_generators = [p for p in group if ids[permute_coloring(anchor, p)] in adj[ids[anchor]]]
assert len(neighbor_generators) == 6
assert all(tuple(p[p[i]] for i in range(16)) == identity for p in neighbor_generators)
print('MATCHING_ENUM_33_MATCHINGS_120_NAMED_COLORINGS_PASS')
print('KEMPE_COMPONENTS_24_96_EDGES_54_288_PASS')
print('CYCLE_SIGNATURES_8_PLUS_8_VERSUS_6_PLUS_10_PASS')
print('DISTANCES_SMALL_3_LARGE_4_AND_BIPARTITE_CONTRAST_PASS')
print('AUTOMORPHISM_GROUP_96_REGULAR_CAYLEY_SECTOR_PASS')
