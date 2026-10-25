#!/usr/bin/env python3
"""Independent group-action certificate for determining sets of the folded 5-cube."""
from itertools import permutations, combinations
from collections import Counter, deque
import json

N = 16
DIRECTIONS = (1, 2, 4, 8, 15)

def maps_of_graph():
    # Quotient F_2^5 / <(1,1,1,1,1)> with fifth coordinate zero.
    maps = []
    for p in permutations(range(5)):
        for t in range(N):
            perm = []
            for x in range(N):
                v = [(x >> i) & 1 for i in range(4)] + [0]
                w = [0] * 5
                for i in range(5):
                    w[p[i]] = v[i]
                if w[4]:
                    w = [z ^ 1 for z in w]
                perm.append(sum(w[i] << i for i in range(4)) ^ t)
            assert len(set(perm)) == N
            assert all(((x ^ y) in DIRECTIONS) == ((perm[x] ^ perm[y]) in DIRECTIONS)
                       for x in range(N) for y in range(N))
            maps.append(tuple(perm))
    assert len(maps) == len(set(maps)) == 1920
    return maps

A = maps_of_graph()
FIX = [0] * N
for j, perm in enumerate(A):
    for i in range(N):
        if perm[i] == i:
            FIX[i] |= 1 << j
ALL = (1 << len(A)) - 1

is_base = [False] * (1 << N)
for mask in range(1 << N):
    stab = ALL
    remaining = mask
    while remaining:
        bit = remaining & -remaining
        remaining -= bit
        stab &= FIX[bit.bit_length() - 1]
    is_base[mask] = stab.bit_count() == 1

minimal = []
for mask in range(1 << N):
    if is_base[mask] and all(not is_base[mask ^ (1 << i)]
                             for i in range(N) if mask & (1 << i)):
        minimal.append(mask)
counts = Counter(m.bit_count() for m in minimal)
assert dict(counts) == {4: 560, 5: 192}
B4 = {m for m in minimal if m.bit_count() == 4}
B5 = {m for m in minimal if m.bit_count() == 5}

def edge_count(mask):
    xs = [i for i in range(N) if mask & (1 << i)]
    return sum((a ^ b) in DIRECTIONS for a, b in combinations(xs, 2))

def is_cycle_five(mask):
    xs = [i for i in range(N) if mask & (1 << i)]
    return len(xs) == 5 and all(sum((x ^ y) in DIRECTIONS for y in xs if x != y) == 2 for x in xs)

assert B4 == {sum(1 << i for i in xs) for xs in combinations(range(N), 4)
              if (lambda m: edge_count(m) == 1 or (edge_count(m) == 0 and (xs[0]^xs[1]^xs[2]^xs[3]) != 0))(sum(1 << i for i in xs))}
assert B5 == {m for m in range(1 << N) if is_cycle_five(m)}

adj = {mask: set() for mask in B4}
for mask in B4:
    for i in range(N):
        if mask & (1 << i):
            for j in range(N):
                if not (mask & (1 << j)):
                    new = mask ^ (1 << i) ^ (1 << j)
                    if new in B4:
                        adj[mask].add(new)
assert sum(map(len, adj.values())) == 11840
assert Counter(map(len, adj.values())) == {20: 480, 28: 80}

layers_by_type = {}
for start in B4:
    dist = {start: 0}
    todo = deque([start])
    while todo:
        x = todo.popleft()
        for y in adj[x]:
            if y not in dist:
                dist[y] = dist[x] + 1
                todo.append(y)
    assert len(dist) == 560 and max(dist.values()) == 4
    t = edge_count(start)
    layer = [sum(v == k for v in dist.values()) for k in range(5)]
    if t in layers_by_type:
        assert layer == layers_by_type[t]
    else:
        layers_by_type[t] = layer
assert layers_by_type == {0: [1,28,126,220,185],1: [1,20,126,244,169]}

def orbit_sizes(subsets):
    pending = set(subsets)
    sizes = []
    while pending:
        mask = next(iter(pending))
        xs = [i for i in range(N) if mask & (1 << i)]
        orbit = {sum(1 << perm[i] for i in xs) for perm in A}
        assert orbit <= subsets
        sizes.append(len(orbit))
        pending -= orbit
    return sorted(sizes)
assert orbit_sizes(B4) == [80,480]
assert orbit_sizes(B5) == [192]

print(json.dumps({
    'graph_vertices':16, 'graph_edges':40, 'automorphisms':len(A),
    'minimum_determining_number':4,
    'inclusion_minimal_size_counts':dict(sorted(counts.items())),
    'four_set_orbit_sizes':[80,480], 'five_set_orbit_sizes':[192],
    'four_set_types':{'independent_nonzero_xor':80,'one_edge':480},
    'five_set_type':'induced_five_cycle',
    'exchange_vertices':len(B4), 'exchange_edges':sum(map(len,adj.values()))//2,
    'exchange_degree_counts':dict(sorted(Counter(map(len,adj.values())).items())),
    'exchange_connected':True, 'exchange_radius':4, 'exchange_diameter':4,
    'exchange_bfs_layers_by_induced_edges':dict(sorted(layers_by_type.items()))
},sort_keys=True))
