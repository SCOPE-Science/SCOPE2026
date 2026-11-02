#!/usr/bin/env python3
"""Exact induced-matching and exchange-graph certificate for the Coxeter graph.
Requires only the Python standard library. Run: python verify_fano.py
"""
from itertools import combinations
from collections import Counter, deque


def bits(s):
    while s:
        b = s & -s
        yield b.bit_length() - 1
        s ^= b


def maximal_cliques(neighbors, n):
    """Bron--Kerbosch: outputs every maximal clique exactly once."""
    result = []

    def visit(r, p, x):
        if not (p or x):
            result.append(r)
            return
        pool = p | x
        pivot = max(bits(pool), key=lambda v: (p & neighbors[v]).bit_count())
        for v in list(bits(p & ~neighbors[pivot])):
            b = 1 << v
            visit(r | b, p & neighbors[v], x & neighbors[v])
            p &= ~b
            x |= b

    visit(0, (1 << n) - 1, 0)
    return result


def bfs(adj, source):
    dist = {source: 0}
    queue = deque([source])
    while queue:
        v = queue.popleft()
        for w in adj[v]:
            if w not in dist:
                dist[w] = dist[v] + 1
                queue.append(w)
    return dist


def main():
    lines = {frozenset((i, (i + 1) % 7, (i + 3) % 7)) for i in range(7)}
    triples = [frozenset(t) for t in combinations(range(7), 3) if frozenset(t) not in lines]
    assert len(triples) == 28
    graph = [set() for _ in range(28)]
    for v, w in combinations(range(28), 2):
        if triples[v].isdisjoint(triples[w]):
            graph[v].add(w)
            graph[w].add(v)
    assert {len(s) for s in graph} == {3}
    edges = sorted((v, w) for v in range(28) for w in graph[v] if v < w)
    assert len(edges) == 42

    compat = [0] * 42
    for i, (a, b) in enumerate(edges):
        for j in range(i + 1, 42):
            c, d = edges[j]
            if len({a, b, c, d}) == 4 and all(y not in graph[x] for x in (a, b) for y in (c, d)):
                compat[i] |= 1 << j
                compat[j] |= 1 << i
    maximal = maximal_cliques(compat, 42)
    sizes = Counter(z.bit_count() for z in maximal)
    assert sizes == {4: 84, 5: 924, 6: 3710, 7: 84}, sizes
    maxima = sorted(z for z in maximal if z.bit_count() == 7)
    assert len(maxima) == 84

    distances = [bfs(graph, v) for v in range(28)]
    expected = {}
    for v in range(28):
        sphere3 = {w for w in range(28) if distances[v][w] == 3}
        core = 0
        for k, (a, b) in enumerate(edges):
            if a in sphere3 and b in sphere3:
                core |= 1 << k
        assert core.bit_count() == 6
        assert {sum(1 for w in sphere3 if w in graph[a]) for a in sphere3} == {1}
        for w in graph[v]:
            e = edges.index((min(v, w), max(v, w)))
            candidate = core | (1 << e)
            assert candidate.bit_count() == 7
            expected[candidate] = (v, w)
    assert len(expected) == 84
    assert set(expected) == set(maxima), 'All maxima must equal the distance-three-sphere construction.'

    one = [set() for _ in maxima]
    four = [set() for _ in maxima]
    hist = Counter()
    for i, j in combinations(range(84), 2):
        d = 7 - (maxima[i] & maxima[j]).bit_count()
        hist[d] += 1
        if d == 1:
            one[i].add(j)
            one[j].add(i)
        elif d == 4:
            four[i].add(j)
            four[j].add(i)
    assert hist == {1: 84, 4: 168, 5: 672, 6: 1470, 7: 1092}
    assert {len(n) for n in one} == {2}
    assert {len(n) for n in four} == {4}

    # The edges of the one-exchange graph form 28 disjoint triangles.
    unvisited = set(range(84))
    components = []
    while unvisited:
        v = min(unvisited)
        comp = set(bfs(one, v))
        assert len(comp) == 3
        unvisited -= comp
        components.append(comp)
    assert len(components) == 28
    by_center = {}
    for c in components:
        vs = {expected[maxima[i]][0] for i in c}
        assert len(vs) == 1
        by_center[next(iter(vs))] = c
    assert set(by_center) == set(range(28))

    # Four-exchange between distinct centers iff the centers are distance three,
    # with unique lateral arcs: both tips remain at distance three from the other center.
    four_edges = {frozenset((i, j)) for i in range(84) for j in four[i] if i < j}
    expected_four = set()
    indices = {m: i for i, m in enumerate(maxima)}
    labels = {pair: indices[mask] for mask, pair in expected.items()}
    for v, w in combinations(range(28), 2):
        if distances[v][w] != 3:
            continue
        a = [a for a in graph[v] if distances[w][a] == 3]
        b = [b for b in graph[w] if distances[v][b] == 3]
        assert len(a) == len(b) == 1
        expected_four.add(frozenset((labels[(v, a[0])], labels[(w, b[0])])))
    assert expected_four == four_edges
    assert len(four_edges) == 168

    for adj, shell in ((four, (1, 4, 8, 16, 22, 26, 7)),
                       ([a | b for a, b in zip(one, four)], (1, 6, 24, 45, 8))):
        for v in range(84):
            cnt = Counter(bfs(adj, v).values())
            assert tuple(cnt[d] for d in range(len(shell))) == shell
            assert sum(cnt.values()) == 84

    # Every exact-four edge lies in a unique triangle, giving a 56-vertex cubic graph.
    triangles = [t for t in combinations(range(84), 3) if all(b in four[a] for a, b in combinations(t, 2))]
    assert len(triangles) == 56
    assert all(sum(1 for t in triangles if v in t) == 2 for v in range(84))
    assert all(sum(1 for t in triangles if a in t and b in t) == 1 for a, b in (tuple(edge) for edge in four_edges))
    klein = [set() for _ in triangles]
    for v in range(84):
        t = [i for i, tri in enumerate(triangles) if v in tri]
        assert len(t) == 2
        klein[t[0]].add(t[1]); klein[t[1]].add(t[0])
    assert {len(x) for x in klein} == {3}
    assert sum(map(len, klein)) == 168
    assert len(bfs(klein, 0)) == 56
    assert max(max(bfs(klein, v).values()) for v in range(56)) == 6
    print('FANO_BRON_KERBOSCH_84_MAXIMA_PASS')
    print('SPHERE3_CORE_AND_LATERAL_ARC_LIFT_PASS')
    print('EXCHANGE_ONE_FOUR_SHELLS_AND_56_CUBIC_PASS')


if __name__ == '__main__':
    main()
