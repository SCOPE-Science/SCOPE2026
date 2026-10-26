#!/usr/bin/env python3
"""Exact independent enumerations for the square-switch reconfiguration of Hamilton cycles in Q4."""
from collections import Counter, deque
from itertools import combinations, permutations

D = 4
V = range(1 << D)
NB = {u: tuple(u ^ (1 << i) for i in range(D)) for u in V}
E = tuple((u, v) for u in V for v in NB[u] if u < v)
EDGE_ID = {e: i for i, e in enumerate(E)}

def bit(u, v):
    return 1 << EDGE_ID[tuple(sorted((u, v)))]

# Enumeration A: Every undirected Hamilton cycle, anchored at vertex zero,
# has exactly two orientations; keep the one whose second vertex is smaller.
def via_paths():
    out = set()
    def dfs(path, visited):
        u = path[-1]
        if len(path) == len(V):
            if 0 in NB[u] and path[1] < u:
                edges = zip(path, path[1:] + [0])
                out.add(sum(bit(a, b) for a, b in edges))
            return
        for v in NB[u]:
            if not (visited & (1 << v)):
                dfs(path + [v], visited | (1 << v))
    dfs([0], 1)
    return out

# Enumeration B: Every Hamilton cycle is the union of precisely its two
# alternating perfect matchings. Enumerate *all* matchings recursively.
def all_matchings():
    def dfs(left, mask):
        if not left:
            yield mask
            return
        u = (left & -left).bit_length() - 1
        for v in NB[u]:
            if left & (1 << v):
                yield from dfs(left ^ (1 << u) ^ (1 << v), mask | bit(u, v))
    return tuple(dfs((1 << len(V)) - 1, 0))

def is_cycle(mask):
    nb = [[] for _ in V]
    for i, (u, v) in enumerate(E):
        if mask & (1 << i):
            nb[u].append(v)
            nb[v].append(u)
    if any(len(row) != 2 for row in nb):
        return False
    seen = {0}
    todo = [0]
    while todo:
        for y in nb[todo.pop()]:
            if y not in seen:
                seen.add(y)
                todo.append(y)
    return len(seen) == len(V)

def via_matchings():
    matchings = all_matchings()
    assert len(matchings) == 272 and len(set(matchings)) == 272
    out = set()
    for a, b in combinations(matchings, 2):
        if not a & b and is_cycle(a | b):
            out.add(a | b)
    return out

def face_masks():
    ans = []
    for i, j in combinations(range(D), 2):
        for base in V:
            if base & ((1 << i) | (1 << j)):
                continue
            x = base ^ (1 << i)
            y = base ^ (1 << j)
            z = base ^ (1 << i) ^ (1 << j)
            ans.append(bit(base, x) | bit(base, y) | bit(x, z) | bit(y, z))
    assert len(ans) == 24 and len(set(ans)) == 24
    return set(ans)

def adjacency_by_flips(cycles, faces):
    idx = {c: i for i, c in enumerate(cycles)}
    graph = [set() for _ in cycles]
    for i, c in enumerate(cycles):
        for f in faces:
            if (c & f).bit_count() == 2:
                j = idx.get(c ^ f)
                if j is not None:
                    graph[i].add(j)
    assert all(i in graph[j] for i, row in enumerate(graph) for j in row)
    return graph

def adjacency_by_pair_differences(cycles, faces):
    graph = [set() for _ in cycles]
    for i, j in combinations(range(len(cycles)), 2):
        if (cycles[i] ^ cycles[j]) in faces:
            graph[i].add(j)
            graph[j].add(i)
    return graph

def components(g):
    unseen = set(range(len(g)))
    parts = []
    while unseen:
        start = min(unseen)
        component = {start}
        todo = [start]
        unseen.remove(start)
        while todo:
            for nxt in g[todo.pop()]:
                if nxt in unseen:
                    unseen.remove(nxt)
                    component.add(nxt)
                    todo.append(nxt)
        parts.append(component)
    return parts

def all_distances(g, giant):
    ecc = Counter()
    pairs = Counter()
    for u in giant:
        dist = {u: 0}
        q = deque([u])
        while q:
            x = q.popleft()
            for y in g[x]:
                if y not in dist:
                    dist[y] = dist[x] + 1
                    q.append(y)
        assert len(dist) == len(giant)
        ecc[max(dist.values())] += 1
        for y, d in dist.items():
            if y > u:
                pairs[d] += 1
    return ecc, pairs

def symmetric_orbits(cycles):
    idx = {m: i for i, m in enumerate(cycles)}
    maps = []
    for axes in permutations(range(D)):
        for translation in V:
            vmap = [translation ^ sum(((v >> i) & 1) << axes[i] for i in range(D)) for v in V]
            maps.append(tuple(EDGE_ID[tuple(sorted((vmap[a], vmap[b])))] for a,b in E))
    assert len(maps) == 384 and len(set(maps)) == 384
    seen = set()
    orbits = []
    for c in cycles:
        i = idx[c]
        if i in seen:
            continue
        orbit = set()
        for ep in maps:
            moved = 0
            for j in range(len(E)):
                if c & (1 << j):
                    moved |= 1 << ep[j]
            orbit.add(idx[moved])
        assert not orbit & seen
        seen |= orbit
        orbits.append(orbit)
    assert len(seen) == len(cycles)
    return orbits

def main():
    first = via_paths()
    second = via_matchings()
    assert first == second and len(first) == 1344
    cycles = sorted(first)
    faces = face_masks()
    graph = adjacency_by_flips(cycles, faces)
    check = adjacency_by_pair_differences(cycles, faces)
    assert graph == check
    degrees = Counter(len(row) for row in graph)
    assert degrees == {0:240, 1:384, 2:192, 4:288, 8:240}
    assert sum(degrees[d] * d for d in degrees) // 2 == 1920
    comp = components(graph)
    assert sorted(map(len, comp)) == [1]*240 + [1104]
    giant = next(p for p in comp if len(p) == 1104)
    eccentricity, distance_pairs = all_distances(graph, giant)
    assert eccentricity == {10:96, 11:192, 12:816}
    assert [distance_pairs[d] for d in range(1, 13)] == [1920, 7488, 14208, 41232, 47424, 112080, 81408, 152736, 54912, 79488, 7488, 8472]
    assert sum(distance_pairs.values()) == 1104*1103//2
    orbits = symmetric_orbits(cycles)
    orbit_degrees = sorted((len(o), len(graph[next(iter(o))])) for o in orbits)
    assert orbit_degrees == [(48,0),(48,8),(96,0),(96,0),(96,4),(192,2),(192,4),(192,8),(384,1)]
    print('VERIFY_OK')
    print('Hamiltonian cycles:',len(cycles),'matching pairs:',len(all_matchings()),'squares:',len(faces))
    print('square-switch graph: vertices=1344 edges=1920 components=241 isolated=240 giant=1104')
    print('degrees:',sorted(degrees.items()),'orbits:',orbit_degrees)
    print('giant: radius=10 diameter=12 eccentricities:',sorted(eccentricity.items()))
    print('distance pairs:',sorted(distance_pairs.items()))
if __name__ == '__main__':
    main()
