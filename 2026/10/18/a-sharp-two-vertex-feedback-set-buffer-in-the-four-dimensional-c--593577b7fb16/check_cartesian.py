#!/usr/bin/env python3
"""Independent Cartesian-square model and leaf-pruning certificate."""
from collections import Counter, deque
from itertools import combinations
import json

GRAY = (0, 1, 3, 2)
position = {(a, b): GRAY[a] | (GRAY[b] << 2)
            for a in range(4) for b in range(4)}
neighbors = [set() for _ in range(16)]
for a in range(4):
    for b in range(4):
        v = position[(a, b)]
        for w in (position[((a + 1) % 4, b)],
                  position[(a, (b + 1) % 4)]):
            neighbors[v].add(w)
            neighbors[w].add(v)


def is_forest(keep):
    alive = set(keep)
    while True:
        leaves = [v for v in alive if len(neighbors[v] & alive) <= 1]
        if not leaves:
            return not alive
        alive.difference_update(leaves)


def main():
    catalog = {}
    for k in range(6, 9):
        arr = set()
        for selected in combinations(range(16), k):
            keep = set(range(16)) - set(selected)
            if is_forest(keep):
                arr.add(sum(1 << v for v in selected))
        catalog[k] = arr
    assert len(catalog[6]) == 8
    all_states = set.union(*catalog.values())

    # Build the transition graph from deletion, the opposite direction to checker one.
    graph = {m: set() for m in all_states}
    degree_between_layers = Counter()
    for upper_size in (7, 8):
        for upper in catalog[upper_size]:
            for v in range(16):
                if upper & (1 << v):
                    lower = upper ^ (1 << v)
                    if lower in catalog[upper_size-1]:
                        graph[upper].add(lower)
                        graph[lower].add(upper)
                        degree_between_layers[(upper_size-1,upper_size)] += 1

    def comps(k):
        nodes = {m for layer in catalog for m in catalog[layer] if layer <= k}
        par = {m:m for m in nodes}
        def root(x):
            while par[x] != x:
                par[x] = par[par[x]]
                x = par[x]
            return x
        for m in nodes:
            for nbr in graph[m]:
                if nbr in nodes:
                    a,b = root(m),root(nbr)
                    if a != b: par[a]=b
        counts = Counter(root(x) for x in nodes)
        return dict(sorted(Counter(counts.values()).items()))

    # Check an explicit shortest cross-parity path under the forest constraint.
    walk = sum(1 << v for v in (3, 5, 6, 9, 10, 12))
    for added, vertex in ((True, 2), (True, 7), (False, 6), (True, 4),
                          (False, 5), (True, 11), (False, 3), (True, 8),
                          (False, 10), (True, 13), (False, 9), (False, 12)):
        previous = walk
        assert bool(walk & (1 << vertex)) != added
        walk ^= 1 << vertex
        assert 6 <= walk.bit_count() <= 8
        assert is_forest({v for v in range(16) if not walk & (1 << v)})
        assert walk in graph[previous]
    assert walk == sum(1 << v for v in (2, 4, 7, 8, 11, 13))

    # Distances between all eight optimum sets, using direct vertex-adjacency lists.
    minsets = sorted(catalog[6])
    distances = {'same_parity':Counter(), 'opposite_parity':Counter()}
    for m in minsets:
        dist={m:0}
        todo=deque([m])
        while todo:
            x=todo.popleft()
            for y in graph[x]:
                if y not in dist:
                    dist[y]=dist[x]+1;todo.append(y)
        assert len(dist)==len(all_states)
        for n in minsets:
            if m<n:
                # Disjoint minimum sets use opposite parity classes.
                tag = 'opposite_parity' if not m & n else 'same_parity'
                distances[tag][dist[n]]+=1

    out = {
        'vertices':16,
        'cube_edges':sum(map(len,neighbors))//2,
        'minimum_feedback_size':6,
        'minimum_sets':minsets,
        'layer_counts':{str(k):len(v) for k,v in catalog.items()},
        'tar_edges':{f'{a}-{b}':v for (a,b),v in sorted(degree_between_layers.items())},
        'components_cap_6':{str(a):b for a,b in comps(6).items()},
        'components_cap_7':{str(a):b for a,b in comps(7).items()},
        'components_cap_8':{str(a):b for a,b in comps(8).items()},
        'min_set_pair_distance':{k:dict(sorted(c.items())) for k,c in distances.items()}
    }
    print(json.dumps(out,sort_keys=True))
    print('VERIFY_OK')

if __name__=='__main__':
    main()
