#!/usr/bin/env python3
"""Exact four-colouring state-graph census for the 5-regular Clebsch graph.

No external packages. Run: python3 verify_core.py
The labelled graph has vertex set 0,...,15 and edges from XOR differences
1,2,4,8,15. Each palette entry is a distinguished color in range(4).
"""
from collections import Counter, deque
from itertools import permutations

V = range(16)
DIFF = (1, 2, 4, 8, 15)
ADJ = [{v ^ d for d in DIFF} for v in V]
EDGES = {tuple(sorted((v, v ^ d))) for v in V for d in DIFF}
assert len(EDGES) == 40

states = []
c = [-1] * 16

def visit(k):
    if k == 16:
        states.append(tuple(c))
        return
    v = max((x for x in V if c[x] < 0),
            key=lambda x: (len({c[y] for y in ADJ[x] if c[y] >= 0}),
                           sum(c[y] < 0 for y in ADJ[x]), -x))
    excluded = {c[y] for y in ADJ[v]}
    for color in range(4):
        if color not in excluded:
            c[v] = color
            visit(k + 1)
    c[v] = -1

# The maximum independent set bounds the chromatic number below by 4.
# This dynamic enumeration examines every one of the 2^16 vertex subsets.
independent = bytearray(1 << 16)
independent[0] = 1
adj_mask = [sum(1 << y for y in ADJ[v]) for v in V]
alpha = 0
for mask in range(1, 1 << 16):
    vertex = mask.bit_length() - 1
    previous = mask ^ (1 << vertex)
    if independent[previous] and not (previous & adj_mask[vertex]):
        independent[mask] = 1
        alpha = max(alpha, mask.bit_count())
assert alpha == 5

visit(0)
where = {state: i for i, state in enumerate(states)}
assert len(where) == len(states) == 28560

neighbors = []
for state in states:
    destinations = []
    for v in V:
        forbidden = {state[u] for u in ADJ[v]}
        for color in range(4):
            if color != state[v] and color not in forbidden:
                nxt = list(state)
                nxt[v] = color
                destinations.append(where[tuple(nxt)])
    neighbors.append(tuple(sorted(destinations)))
assert sum(map(len, neighbors)) == 115200
assert all(i in neighbors[j] for j, row in enumerate(neighbors) for i in row)

degree_dist = Counter(map(len, neighbors))
assert degree_dist == {0: 1680, 2: 3840, 4: 11520, 5: 7680, 6: 3840}

component_id = [-1] * len(states)
components = []
for root in range(len(states)):
    if component_id[root] != -1:
        continue
    queue = [root]
    component_id[root] = len(components)
    for v in queue:
        for w in neighbors[v]:
            if component_id[w] < 0:
                component_id[w] = len(components)
                queue.append(w)
    components.append(queue)
assert Counter(map(len, components)) == {1: 1680, 28: 960}

def distances(seed):
    dist = {seed: 0}
    Q = deque([seed])
    while Q:
        v = Q.popleft()
        for w in neighbors[v]:
            if w not in dist:
                dist[w] = dist[v] + 1
                Q.append(w)
    return dist

active = [ids for ids in components if len(ids) == 28]
for ids in active:
    assert sum(len(neighbors[i]) for i in ids) == 120
    assert max(max(distances(i).values()) for i in ids) == 6

# Vertex automorphisms: one translation, and adjacent permutations of the
# five cube coordinates, descending to antipodal quotient pairs.
vertex_maps = [tuple(x ^ 1 for x in V)]
for t in range(4):
    perm = list(range(5))
    perm[t], perm[t + 1] = perm[t + 1], perm[t]
    remap = []
    for x in V:
        bits = [(x >> i) & 1 for i in range(4)] + [0]
        output = [bits[perm[i]] for i in range(5)]
        if output[4]:
            output = [1 - b for b in output]
        remap.append(sum(output[i] << i for i in range(4)))
    vertex_maps.append(tuple(remap))
for p in vertex_maps:
    assert {tuple(sorted((p[x], p[y]))) for x, y in EDGES} == EDGES
palette_maps = []
for t in range(3):
    p = list(range(4))
    p[t], p[t + 1] = p[t + 1], p[t]
    palette_maps.append(tuple(p))

def images(state):
    for perm in vertex_maps:
        nxt = [None] * 16
        for v in V:
            nxt[perm[v]] = state[v]
        yield where[tuple(nxt)]
    for perm in palette_maps:
        yield where[tuple(perm[c] for c in state)]

# Orbits on recoloring components: transitivity of the 960 nontrivial
# components proves they are isomorphic, rather than relying on graph hashes.
seen = set()
comp_orbits = Counter()
for seed in range(len(components)):
    if seed in seen:
        continue
    seen.add(seed)
    q = [seed]
    for comp in q:
        for j in images(states[components[comp][0]]):
            dest = component_id[j]
            if dest not in seen:
                seen.add(dest)
                q.append(dest)
    comp_orbits[(len(q), len(components[seed]))] += 1
assert comp_orbits == {(960, 28): 1, (1440, 1): 1, (240, 1): 1}

seen = set()
state_orbits = Counter()
for seed in range(len(states)):
    if seed in seen:
        continue
    seen.add(seed)
    q = [seed]
    for j in q:
        for dest in images(states[j]):
            if dest not in seen:
                seen.add(dest)
                q.append(dest)
    state_orbits[(len(q), len(neighbors[seed]))] += 1
assert state_orbits == {(3840, 6): 1, (7680, 5): 1, (7680, 4): 1,
                        (1920, 4): 2, (3840, 2): 1, (1440, 0): 1, (240, 0): 1}
print('VERIFY_OK CORE')
print('independence_number=5 chromatic_number=4')
print('vertices=28560 edges=57600')
print('component_sizes={1:1680,28:960} nontrivial_diameter=6, edges_per_nontrivial=60')
print('degree_histogram={0:1680,2:3840,4:11520,5:7680,6:3840}')
print('component_symmetry_orbits={(960,28):1,(1440,1):1,(240,1):1}')
print('state_symmetry_orbits={(3840,6):1,(7680,5):1,(7680,4):1,(1920,4):2,(3840,2):1,(1440,0):1,(240,0):1}')
