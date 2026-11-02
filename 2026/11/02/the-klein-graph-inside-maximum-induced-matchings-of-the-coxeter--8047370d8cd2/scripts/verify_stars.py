#!/usr/bin/env python3
"""Independent finite certificate using the three-seven-cycles-and-stars Coxeter model.
Pure Python standard library. The named Klein comparison uses an explicit
adjacency encoding attributed to the SageMath named-graph generator.
"""
from collections import Counter, deque
from itertools import combinations


def vertices(mask):
    while mask:
        v = (mask & -mask).bit_length() - 1
        yield v
        mask &= mask - 1


def exact_cliques(k, compatible):
    """Lexicographically enumerate every k-clique, without relying on maximality."""
    found = []

    def visit(chosen, available, length):
        if length == k:
            found.append(chosen)
            return
        while available and length + available.bit_count() >= k:
            b = available & -available
            i = b.bit_length() - 1
            available ^= b
            visit(chosen | b, available & compatible[i], length + 1)

    visit(0, (1 << len(compatible)) - 1, 0)
    return found


def shortest_paths(g, source):
    d = {source: 0}
    q = deque([source])
    while q:
        u = q.popleft()
        for v in g[u]:
            if v not in d:
                d[v] = d[u] + 1
                q.append(v)
    return d


def decode_sparse6(source):
    """Decode sparse6 for graphs of fewer than 63 vertices, using 6-bit groups."""
    assert source.startswith(':')
    words = [ord(c) - 63 for c in source[1:]]
    assert all(0 <= t <= 63 for t in words)
    bits = ''.join(format(t, '06b') for t in words)
    n = words[0]
    assert n == 56
    # sparse6: after six bits encoding n, pairs (b,x) of width k+1,
    # with k=ceil(log2(n))=6; as specified by Brendan McKay's format.
    k = 6
    v = 0
    out = [set() for _ in range(n)]
    rest = bits[6:]
    for pos in range(0, len(rest) - k, k + 1):
        chunk = rest[pos:pos + k + 1]
        if len(chunk) < k + 1:
            break
        b, x = int(chunk[0]), int(chunk[1:], 2)
        if b:
            v += 1
        if x > v:
            v = x
        elif v < n:
            if x != v:
                out[v].add(x)
                out[x].add(v)
        if v >= n:
            break
    return out


def main():
    graph = [set() for _ in range(28)]

    def edge(a, b):
        graph[a].add(b)
        graph[b].add(a)

    for offset, order in ((0, (1, 2, 3, 4, 5, 6, 0)),
                          (7, (4, 6, 1, 3, 5, 0, 2)),
                          (14, (3, 6, 2, 5, 1, 4, 0))):
        for x, y in zip(order, order[1:] + order[:1]):
            edge(offset + x, offset + y)
    for x in range(7):
        for y in (x, x + 7, x + 14):
            edge(21 + x, y)
    assert all(len(t) == 3 for t in graph)
    e = sorted((i, j) for i in range(28) for j in graph[i] if i < j)
    assert len(e) == 42

    valid = [0] * 42
    for i, (u, v) in enumerate(e):
        for j, (x, y) in enumerate(e):
            if i == j:
                continue
            # A pair of edges is simultaneously induced iff its four endpoints
            # induce exactly those two edges.
            endpoints = {u, v, x, y}
            if len(endpoints) == 4 and sum(int(b in graph[a]) for a, b in combinations(endpoints, 2)) == 2:
                valid[i] |= 1 << j
    assert exact_cliques(8, valid) == [], 'No induced matching of eight edges.'
    maxima = sorted(exact_cliques(7, valid))
    assert len(maxima) == 84
    assert len(set(maxima)) == 84

    dist = [shortest_paths(graph, v) for v in range(28)]
    candidates = {}
    for v in range(28):
        sphere3 = {w for w in range(28) if dist[v][w] == 3}
        assert len(sphere3) == 12
        core = 0
        for k, (a, b) in enumerate(e):
            if a in sphere3 and b in sphere3:
                core |= 1 << k
        assert core.bit_count() == 6
        for w in graph[v]:
            idx = e.index((min(v, w), max(v, w)))
            candidates[core | (1 << idx)] = (v, w)
    assert set(maxima) == set(candidates)

    adj1, adj4 = ([set() for _ in range(84)] for _ in range(2))
    distances = Counter()
    for i, j in combinations(range(84), 2):
        d = 7 - (maxima[i] & maxima[j]).bit_count()
        distances[d] += 1
        if d == 1:
            adj1[i].add(j); adj1[j].add(i)
        if d == 4:
            adj4[i].add(j); adj4[j].add(i)
    assert distances == {1: 84, 4: 168, 5: 672, 6: 1470, 7: 1092}

    adj = [adj1[v] | adj4[v] for v in range(84)]
    assert all(Counter(shortest_paths(adj, v).values()) == {0:1,1:6,2:24,3:45,4:8} for v in range(84))
    assert all(Counter(shortest_paths(adj4, v).values()) == {0:1,1:4,2:8,3:16,4:22,5:26,6:7} for v in range(84))

    triangles = [tuple(t) for t in combinations(range(84),3)
                 if all(b in adj4[a] for a,b in combinations(t,2))]
    assert len(triangles) == 56
    inverse = {v:[] for v in range(84)}
    for i,t in enumerate(triangles):
        for v in t: inverse[v].append(i)
    assert all(len(t) == 2 for t in inverse.values())
    cubic = [set() for _ in range(56)]
    for i, j in inverse.values():
        cubic[i].add(j);cubic[j].add(i)
    assert {len(x) for x in cubic} == {3}
    assert all(len(shortest_paths(cubic,i))==56 for i in range(56))

    # The canonical SageMath Klein3RegularGraph sparse6 encoding (see
    # https://github.com/sagemath/sage/blob/develop/src/sage/graphs/generators/smallgraphs.py).
    sparse6 = (':w`_GKWDBap`CMWFCpWsQUNdBwwuXPHrg`U`RIqypehVLqgHupYcFJyAv^Prk]'
               'EcarHwIVHAKh|\\tLVUxT]`ZDTJ{Af[o_AuKs{r_?ef')
    reference = decode_sparse6(sparse6)
    assert len(reference) == 56 and sum(map(len, reference)) == 168

    # An independently fixed vertex bijection witnesses an exact isomorphism;
    # it is checked against every edge, not just the graph's invariants.
    isomorphism = (0, 3, 55, 27, 35, 1, 42, 53, 28, 33, 52, 34, 32, 23, 40, 18, 4, 39, 49, 37, 14, 15, 17, 48, 13, 16, 43, 36, 44, 10, 45, 20, 51, 6, 2, 54, 25, 26, 5, 11, 50, 47, 19, 24, 31, 30, 9, 8, 29, 21, 22, 46, 7, 12, 41, 38)
    assert len(isomorphism) == 56 and set(isomorphism) == set(range(56))
    assert all({isomorphism[j] for j in cubic[i]} == reference[isomorphism[i]]
               for i in range(56))
    print('STARS_7_AND_8_EXACT_CLIQUE_EXHAUSTION_PASS')
    print('STARS_84_MAXIMA_AND_METRIC_PASS')
    print('KLEIN_F056B_SAGE_GRAPH_EXACT_ISOMORPHISM_PASS')

if __name__ == '__main__':
    main()
