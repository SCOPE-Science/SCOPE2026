#!/usr/bin/env python3
"""Exact 2-token Petersen resistance-and-orbit verification; Python 3 standard library."""
from collections import Counter, deque
from fractions import Fraction
from itertools import combinations, permutations

PAIR_LABELS = tuple(combinations(range(5), 2))
BASE_INDEX = {p: i for i, p in enumerate(PAIR_LABELS)}
TOKEN_STATES = tuple(combinations(range(10), 2))
STATE_INDEX = {p: i for i, p in enumerate(TOKEN_STATES)}
N = len(TOKEN_STATES)
DEN = 95760
# (canonical pair of token-state indices, size, resistance numerator / 95760,
#  shortest two-token distance); each state index refers to TOKEN_STATES.
EXPECTED = (
    ((0, 4), 60, 32257, 1),
    ((0, 38), 60, 36730, 2),
    ((0, 8), 60, 37967, 1),
    ((0, 36), 30, 38189, 2),
    ((0, 3), 30, 38756, 2),
    ((0, 1), 60, 38981, 2),
    ((0, 23), 60, 39584, 3),
    ((0, 19), 120, 40483, 3),
    ((0, 17), 15, 41562, 4),
    ((0, 37), 60, 46283, 2),
    ((0, 6), 120, 46801, 2),
    ((0, 34), 30, 49083, 3),
    ((0, 20), 120, 49447, 3),
    ((0, 18), 60, 50441, 4),
    ((6, 7), 30, 55076, 2),
    ((6, 13), 60, 58156, 3),
    ((6, 12), 15, 59360, 4),
)


def make_graph():
    edges = {(i, j) for i in range(10) for j in range(i + 1, 10)
             if set(PAIR_LABELS[i]).isdisjoint(PAIR_LABELS[j])}
    # Construct GP(5,2) independently and verify that the two definitions agree.
    outer = [BASE_INDEX[tuple(sorted((i, (i + 2) % 5)))] for i in range(5)]
    inner = [BASE_INDEX[tuple(sorted(((i + 3) % 5, (i + 4) % 5)))] for i in range(5)]
    assert len(set(outer + inner)) == 10
    gp_edges = set()
    for i in range(5):
        for u, v in ((outer[i], outer[(i + 1) % 5]),
                     (inner[i], inner[(i + 2) % 5]), (outer[i], inner[i])):
            gp_edges.add(tuple(sorted((u, v))))
    assert edges == gp_edges and len(edges) == 15
    neighbors = [set() for _ in range(N)]
    # Build the token graph from edge moves, not from its full matrix.
    for i, s in enumerate(TOKEN_STATES):
        for u in s:
            v = next(x for x in s if x != u)
            for z in range(10):
                if z == v or tuple(sorted((u, z))) not in edges:
                    continue
                j = STATE_INDEX[tuple(sorted((v, z)))]
                neighbors[i].add(j)
    assert all(i in neighbors[j] for i in range(N) for j in neighbors[i])
    assert len(neighbors[0]) == 6
    assert Counter(map(len, neighbors)) == {6: 30, 4: 15}
    assert sum(map(len, neighbors)) // 2 == 120
    return edges, neighbors


def exact_inverse(a):
    # Exact Gauss-Jordan elimination; pivot and product identities are checked.
    n = len(a)
    b = [[Fraction(a[i][j]) for j in range(n)] +
         [Fraction(int(i == j)) for j in range(n)] for i in range(n)]
    for k in range(n):
        pivot = next((i for i in range(k, n) if b[i][k]), None)
        assert pivot is not None
        b[pivot], b[k] = b[k], b[pivot]
        row = b[k]
        p = row[k]
        row[k:] = [t / p for t in row[k:]]
        for i in range(n):
            if i == k:
                continue
            fac = b[i][k]
            if fac:
                for j in range(k, 2 * n):
                    b[i][j] -= fac * row[j]
    inv = [r[n:] for r in b]
    for i in range(n):
        for j in range(n):
            assert sum(a[i][k] * inv[k][j] for k in range(n)) == (i == j)
    return inv


def graph_distances(neighbors):
    ds = []
    for start in range(N):
        d = [-1] * N
        d[start] = 0
        todo = deque([start])
        while todo:
            i = todo.popleft()
            for j in neighbors[i]:
                if d[j] < 0:
                    d[j] = d[i] + 1
                    todo.append(j)
        assert min(d) >= 0
        ds.append(d)
    return ds


def main():
    edges, neighbors = make_graph()
    assert N == 45
    lap = [[-int(j in neighbors[i]) + (len(neighbors[i]) if i == j else 0)
            for j in range(N)] for i in range(N)]
    red = [row[1:] for row in lap[1:]]
    inv = exact_inverse(red)
    assert inv == [list(col) for col in zip(*inv)]

    def resistance(i, j):
        a = inv[i - 1][i - 1] if i else Fraction(0)
        b = inv[j - 1][j - 1] if j else Fraction(0)
        cross = inv[i - 1][j - 1] if i and j else Fraction(0)
        return a + b - 2 * cross

    perms = []
    for p in permutations(range(5)):
        a = [BASE_INDEX[tuple(sorted((p[x], p[y])))] for x, y in PAIR_LABELS]
        q = tuple(STATE_INDEX[tuple(sorted((a[x], a[y])))] for x, y in TOKEN_STATES)
        assert all({q[j] for j in neighbors[i]} == neighbors[q[i]] for i in range(N))
        perms.append(q)
    assert len(set(perms)) == 120
    unused = set(combinations(range(N), 2))
    table = []
    while unused:
        i, j = min(unused)
        orbit = {tuple(sorted((p[i], p[j]))) for p in perms}
        assert orbit <= unused
        unused -= orbit
        res = {resistance(a, b) for a, b in orbit}
        assert len(res) == 1
        x = next(iter(res)) * DEN
        assert x.denominator == 1
        table.append(((i, j), len(orbit), int(x)))
    distances = graph_distances(neighbors)
    results = sorted(((pair, size, numerator, distances[pair[0]][pair[1]])
                      for pair, size, numerator in table), key=lambda row: row[2])
    assert tuple(results) == EXPECTED
    assert sum(size for _, size, _, _ in results) == N * (N - 1) // 2 == 990
    counts = Counter(distances[i][j] for i in range(N) for j in range(i + 1, N))
    assert dict(counts) == {1: 120, 2: 390, 3: 390, 4: 90}
    assert sum(Fraction(numerator * size, DEN) for _, size, numerator, _ in results) == Fraction(486429, 1064)
    # Two graph-distance levels overlap in resistance: a distance-2 pair can
    # have less resistance than a distance-1 pair.
    assert Fraction(36730, DEN) < Fraction(37967, DEN)
    assert len({x[2] for x in results}) == 17
    print('VERIFY_OK; 45 vertices; 120 edges; 990 unordered pairs; 17 orbits and 17 distinct resistances')


if __name__ == '__main__':
    main()
