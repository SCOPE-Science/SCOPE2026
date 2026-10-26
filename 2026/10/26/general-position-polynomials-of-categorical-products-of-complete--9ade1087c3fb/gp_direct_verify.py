#!/usr/bin/env python3
"""Independent finite tests for position-set enumeration in products of complete graphs."""
from collections import Counter, deque
from itertools import combinations
from math import comb, factorial


def expected(p, q):
    c = Counter({0: 1, 1: p * q})
    for k in range(2, max(p, q) + 1):
        c[k] += p * comb(q, k) if k <= q else 0
        c[k] += q * comb(p, k) if k <= p else 0
    rectangles = comb(p, 2) * comb(q, 2)
    c[2] += 2 * rectangles
    c[3] += 4 * rectangles
    c[4] += rectangles
    for k in range(3, min(p, q) + 1):
        c[k] += comb(p, k) * comb(q, k) * factorial(k)
    return +c


def expected_maximal(p, q):
    c = Counter()
    c[q] += p
    c[p] += q
    c[4] += comb(p, 2) * comb(q, 2)
    r = min(p, q)
    c[r] += comb(max(p, q), r) * factorial(r)
    return +c


def distances(adj, n):
    ans = []
    for v in range(n):
        d = [-1] * n
        d[v] = 0
        queue = deque([v])
        while queue:
            x = queue.popleft()
            for y in range(n):
                if d[y] == -1 and (adj[x] >> y) & 1:
                    d[y] = d[x] + 1
                    queue.append(y)
        assert set(d) <= {0, 1, 2}, (n, v, d)
        ans.append(d)
    return ans


def shape(mask, vertices, adjacency):
    selected = [i for i in range(len(vertices)) if mask >> i & 1]
    size = len(selected)
    if size == 0: return 'empty'
    if size == 1: return 'single'
    degrees = {i:sum(bool(adjacency[i] >> j & 1) for j in selected) for i in selected}
    if max(degrees.values()) == 0:
        rows = {vertices[i][0] for i in selected}
        cols = {vertices[i][1] for i in selected}
        assert len(rows) == 1 or len(cols) == 1
        return 'layer'
    if all(degrees[i] == size - 1 for i in selected):
        assert len({vertices[i][0] for i in selected}) == size
        assert len({vertices[i][1] for i in selected}) == size
        return 'edge' if size == 2 else 'clique'
    if size in (3, 4) and sum(degrees.values()) == (2 if size == 3 else 4):
        rows = {vertices[i][0] for i in selected}
        cols = {vertices[i][1] for i in selected}
        assert len(rows) == len(cols) == 2
        return 'edge-and-single' if size == 3 else 'rectangle'
    raise AssertionError(('unexpected GP shape', selected, degrees))


def exhaustive(p, q):
    v = [(i, j) for i in range(p) for j in range(q)]
    n = len(v)
    adj = [sum(1 << b for b, (u, w) in enumerate(v) if i != u and j != w)
           for i, (i, j) in enumerate(v)]
    d = distances(adj, n)
    bad = []
    for i, j, k in combinations(range(n), 3):
        # Direct original shortest-path criterion, without assuming a cluster graph.
        forbidden = any(d[a][c] == d[a][b] + d[b][c]
                        for a, b, c in [(i, j, k), (j, i, k), (i, k, j)])
        induced_edges = sum(int(bool(adj[a] >> b & 1))
                            for a, b in [(i, j), (j, k), (i, k)])
        assert forbidden == (induced_edges == 2)
        if forbidden: bad.append((1 << i) | (1 << j) | (1 << k))
    valid = bytearray(1 << n)
    distribution = Counter()
    shapes = Counter()
    for m in range(1 << n):
        ok = all((m & b) != b for b in bad)
        valid[m] = ok
        if ok:
            distribution[m.bit_count()] += 1
            shapes[shape(m, v, adj)] += 1
    maximal = Counter()
    for m in range(1 << n):
        if not valid[m]: continue
        if all(not valid[m | (1 << i)] for i in range(n) if (m >> i & 1) == 0):
            maximal[m.bit_count()] += 1
    assert +distribution == expected(p, q), (p, q, distribution, expected(p, q))
    assert +maximal == expected_maximal(p, q), (p, q, maximal, expected_maximal(p, q))
    rect = comb(p, 2) * comb(q, 2)
    assert shapes['rectangle'] == rect
    assert shapes['edge-and-single'] == 4 * rect
    print(f'{p}x{q}: subsets={1<<n}; GP={dict(sorted(distribution.items()))}; '
          f'maximal={dict(sorted(maximal.items()))}; shapes={dict(sorted(shapes.items()))}')


def valley():
    for p in range(4, 51):
        q = 2*p+4
        c = expected(p, q)
        assert c[p] > c[p+1] < c[p+2]
        assert factorial(p) * comb(q, p) > p * comb(q, p+1)
        assert c[p+1] == p * comb(q, p+1)
        assert c[p+2] == p * comb(q, p+2)
    for p in (4,5,6,10):
        q=2*p+4;c=expected(p,q)
        print(f'valley {p}x{q}: ({c[p]}, {c[p+1]}, {c[p+2]}) at degrees ({p},{p+1},{p+2})')
    print('Exact-integer spot checks of valley inequalities: p=4..50.')

if __name__ == '__main__':
    for p, q in [(3,3),(3,4),(3,5),(3,6),(4,4)]: exhaustive(p,q)
    valley()
    print('All independent finite checks passed.')
