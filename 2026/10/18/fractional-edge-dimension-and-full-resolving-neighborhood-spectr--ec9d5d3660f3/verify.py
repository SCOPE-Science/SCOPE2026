#!/usr/bin/env python3
"""Independent finite checks for edge-resolving neighborhoods in KG(n,2).

Uses breadth-first search for each distance, independently of the structural
support-intersection proof in the accompanying report. Python >=3.9 stdlib.
"""
from itertools import combinations
from collections import Counter, deque
from math import comb


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def verify(n):
    vertices = list(combinations(range(n), 2))
    adj = [[j for j, B in enumerate(vertices) if i != j and set(A).isdisjoint(B)]
           for i, A in enumerate(vertices)]
    distance = []
    for i in range(len(vertices)):
        d = [-1] * len(vertices)
        d[i] = 0
        q = deque([i])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if d[v] < 0:
                    d[v] = d[u] + 1
                    q.append(v)
        assert all(x >= 0 for x in d)
        distance.append(d)
    edges = [(a, b) for a in range(len(vertices)) for b in adj[a] if a < b]
    assert len(edges) == 3 * choose(n, 4)
    profiles = [tuple(min(distance[v][a], distance[v][b]) for v in range(len(vertices)))
                for a, b in edges]
    actual = Counter()
    refined = Counter()
    for i, j in combinations(range(len(edges)), 2):
        ra = profiles[i]
        rb = profiles[j]
        card = sum(x != y for x, y in zip(ra, rb))
        a, b = edges[i]
        c, d = edges[j]
        union = set(vertices[a]) | set(vertices[b]) | set(vertices[c]) | set(vertices[d])
        actual[card] += 1
        refined[len(union), card] += 1
        U = set(vertices[a]) | set(vertices[b])
        V = set(vertices[c]) | set(vertices[d])
        intersection = U & V
        q = sum((set(S) == set(vertices[a]) or set(S) == set(vertices[b])) !=
                (set(S) == set(vertices[c]) or set(S) == set(vertices[d]))
                for S in vertices if set(S) <= intersection)
        assert card == 12 - 2 * choose(len(intersection), 2) + q
    expected = {
        4: 3 * choose(n, 4),
        6: 30 * choose(n, 5),
        8: 60 * choose(n, 5),
        10: 225 * choose(n, 6),
        11: 180 * choose(n, 6),
        12: 630 * choose(n, 7) + 315 * choose(n, 8),
    }
    expected = Counter({k: v for k, v in expected.items() if v})
    assert actual == expected, (n, actual, expected)
    assert sum(actual.values()) == choose(len(edges), 2)
    assert min(actual) == 4
    assert 3 * choose(n, 4) * 2 == choose(n, 2) * choose(n-2, 2)
    return len(vertices), len(edges), sum(actual.values()), dict(sorted(actual.items()))


def main():
    total = 0
    for n in range(5, 10):
        v, e, p, spectrum = verify(n)
        total += p
        print('n=%d vertices=%d edges=%d edge_pairs=%d spectrum=%s' %
              (n, v, e, p, spectrum))
    print('VERIFICATION_OK cases=5 pairs_checked=%d' % total)

if __name__ == '__main__':
    main()
