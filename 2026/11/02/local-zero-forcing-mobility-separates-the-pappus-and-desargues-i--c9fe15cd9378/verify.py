#!/usr/bin/env python3
"""Exhaustive finite certificate for local zero-forcing reconfiguration."""
from collections import Counter, deque
from itertools import combinations

PAPPUS_LINES = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 4, 6), (3, 1, 6), (0, 5, 7),
    (3, 2, 7), (1, 5, 8), (4, 2, 8),
)

def add_edge(adj, a, b):
    assert a != b
    adj[a] |= 1 << b
    adj[b] |= 1 << a

def pappus():
    adj = [0] * 18
    for j, triple in enumerate(PAPPUS_LINES):
        for point in triple:
            add_edge(adj, point, 9 + j)
    assert sum(a.bit_count() for a in adj) == 54
    assert all(a.bit_count() == 3 for a in adj)
    return adj

def desargues():
    # Bipartite double cover of the Petersen graph KG(5,2).
    verts = list(combinations(range(5), 2))
    adj = [0] * 20
    for i, a in enumerate(verts):
        for j, b in enumerate(verts):
            if set(a).isdisjoint(b):
                add_edge(adj, i, 10 + j)
    assert sum(a.bit_count() for a in adj) == 60
    assert all(a.bit_count() == 3 for a in adj)
    return adj

def forcing_closure(adj, start):
    # Simultaneous legal forces, with the old blue set frozen in each round.
    all_vertices = (1 << len(adj)) - 1
    blue = start
    while blue != all_vertices:
        newer = blue
        for v in range(len(adj)):
            if blue & (1 << v):
                white_neighbors = adj[v] & ~blue
                if white_neighbors and white_neighbors.bit_count() == 1:
                    newer |= white_neighbors
        if newer == blue:
            break
        blue = newer
    return blue

def minima(adj):
    n = len(adj)
    all_vertices = (1 << n) - 1
    checked = 0
    for k in range(n + 1):
        result = []
        for sel in combinations(range(n), k):
            checked += 1
            mask = sum(1 << i for i in sel)
            if forcing_closure(adj, mask) == all_vertices:
                result.append(mask)
        if result:
            return k, result, checked
    raise AssertionError('No forcing set')

def exchange(bases, adj, sliding):
    n = len(adj)
    loc = {m: i for i, m in enumerate(bases)}
    graph = [[] for _ in bases]
    for i, mask in enumerate(bases):
        for a in range(n):
            if not mask & (1 << a):
                continue
            destinations = adj[a] if sliding else ((1 << n) - 1)
            for b in range(n):
                if mask & (1 << b) or not destinations & (1 << b):
                    continue
                candidate = mask ^ (1 << a) ^ (1 << b)
                j = loc.get(candidate)
                if j is not None:
                    graph[i].append(j)
    assert all(len(v) == len(set(v)) for v in graph)
    assert all(i in graph[j] for j, row in enumerate(graph) for i in row)
    return graph

def components(gr):
    seen = set()
    cc = []
    for v in range(len(gr)):
        if v in seen:
            continue
        queue = [v]
        seen.add(v)
        for a in queue:
            for b in gr[a]:
                if b not in seen:
                    seen.add(b)
                    queue.append(b)
        cc.append(len(queue))
    return Counter(cc)

def all_eccentricities(gr):
    N = len(gr)
    count = Counter()
    for root in range(N):
        distances = [-1] * N
        distances[root] = 0
        queue = deque([root])
        while queue:
            v = queue.popleft()
            for w in gr[v]:
                if distances[w] < 0:
                    distances[w] = distances[v] + 1
                    queue.append(w)
        assert all(d >= 0 for d in distances)
        count[max(distances)] += 1
    return count

def main():
    pa, de = pappus(), desargues()
    kp, bp, cp = minima(pa)
    kd, bd, cd = minima(de)
    assert (kp, len(bp), cp) == (7, 6912, sum(__import__('math').comb(18,i) for i in range(8)))
    assert (kd, len(bd), cd) == (8, 13520, sum(__import__('math').comb(20,i) for i in range(9)))
    print('MINIMA_OK Pappus', kp, len(bp), 'Desargues', kd, len(bd), 'checked', cp, cd)
    pts = exchange(bp, pa, True)
    dts = exchange(bd, de, True)
    assert Counter(map(len, pts)) == Counter({2:1080,3:3564,4:2268})
    assert sum(map(len, pts)) // 2 == 10962
    assert components(pts) == Counter({6912:1})
    assert sum(map(len, dts)) == 0
    assert components(dts) == Counter({1:13520})
    print('SLIDE_OK Pappus', 'edges', 10962, 'degrees', sorted(Counter(map(len,pts)).items()), 'connected', True,
          'Desargues isolated',len(bd))
    ecc = all_eccentricities(pts)
    assert ecc == Counter({16:648,17:4968,18:1296})
    print('DISTANCE_OK Pappus', 'radius', min(ecc), 'diameter', max(ecc), 'ecc', sorted(ecc.items()))
    dtj = exchange(bd, de, False)
    assert sum(map(len,dtj)) // 2 == 178560
    assert components(dtj) == Counter({13520:1})
    print('JUMP_OK Desargues', 'edges', 178560, 'connected', True)
    print('FULL_CERTIFICATE_OK')
if __name__ == '__main__':
    main()
