"""Exact diagram-matching checks for the first singular Brauer stratum.

Run: python3 verify_brauer_clique.py
No third-party dependencies. The infinite-index argument uses the
five-label support reduction, proved in RESULT.md; this finite check
exhausts every five-label configuration, rather than extrapolating data.
"""
from collections import Counter
from itertools import combinations, permutations
from math import factorial


def normalize(pairs):
    return tuple(sorted(tuple(sorted(pair)) for pair in pairs))


def perfect_matchings(points):
    if not points:
        yield ()
        return
    a = points[0]
    for j in range(1, len(points)):
        b = points[j]
        for rest in perfect_matchings(points[1:j] + points[j + 1:]):
            yield ((a, b),) + rest


def product(first, second, n):
    """Concatenate perfect matchings, erase middle-only loops."""
    parents = list(range(3 * n))

    def root(x):
        while parents[x] != x:
            parents[x] = parents[parents[x]]
            x = parents[x]
        return x

    def union(x, y):
        x, y = root(x), root(y)
        if x != y:
            parents[y] = x

    # First has points 0..n-1 (top) and n..2n-1 (middle).
    for i, j in first:
        union(i, j)
    # Second has points n..2n-1 (middle) and 2n..3n-1 (bottom).
    for i, j in second:
        union(i + n, j + n)

    boundary = {}
    for x in list(range(n)) + list(range(2 * n, 3 * n)):
        value = x if x < n else x - n
        boundary.setdefault(root(x), []).append(value)
    assert all(len(pair) == 2 for pair in boundary.values())
    return normalize(boundary.values())


def propagating_rank(diagram, n):
    return sum(i < n <= j for i, j in diagram)


def candidates(n):
    """Each pair support gives one projection; each triple six arrows."""
    for a, b in combinations(range(n), 2):
        pair = ((a, b), (a + n, b + n))
        vertical = ((j, j + n) for j in range(n) if j not in (a, b))
        yield frozenset((a, b)), normalize((*pair, *vertical))
    for a, b, c in permutations(range(n), 3):
        pair = ((a, b), (b + n, c + n), (c, a + n))
        vertical = ((j, j + n) for j in range(n) if j not in (a, b, c))
        yield frozenset((a, b, c)), normalize((*pair, *vertical))


def expected_coefficients(n):
    coeff = [0] * (n // 2 + 1)
    for a in range(n // 2 + 1):
        for b in range((n - 2 * a) // 3 + 1):
            coeff[a + b] += factorial(n) // (
                (2 ** a) * factorial(a) * factorial(b) * factorial(n - 2 * a - 3 * b)
            )
    return coeff


def independent_clique_count(n):
    """Enumerate vertex sets in the disjoint-support graph, not partitions."""
    supports = [s for s, _ in candidates(n)]
    counts = [0] * (n // 2 + 1)

    def recurse(possible, size):
        counts[size] += 1
        for i, v in enumerate(possible):
            next_possible = [w for w in possible[i + 1:] if supports[v].isdisjoint(supports[w])]
            recurse(next_possible, size + 1)

    recurse(list(range(len(supports))), 0)
    return counts


def main():
    # Independently find EVERY idempotent from ALL perfect matchings
    # in rank n-2 for n=2,3,4,5, and compare to explicit candidates.
    for n in range(2, 6):
        all_diagrams = (normalize(x) for x in perfect_matchings(tuple(range(2 * n))))
        real = {d for d in all_diagrams if propagating_rank(d, n) == n - 2 and product(d, d, n) == d}
        proposed = list(candidates(n))
        assert len(proposed) == len({d for _, d in proposed})
        assert {d for _, d in proposed} == real
        assert len(real) == n * (n - 1) // 2 + n * (n - 1) * (n - 2)
        print('FULL_IDEMPOTENTS', n, len(real))

    # The union of the two supports has <=5 vertices when they intersect.
    # Thus this complete B5 test settles every overlapping case in Bn.
    n = 5
    elements = list(candidates(n))
    witnessed = Counter()
    for i, (support1, a) in enumerate(elements):
        for support2, b in elements[i + 1:]:
            intersect = len(support1 & support2)
            kind = (len(support1), len(support2))
            kind = tuple(sorted(kind))
            commute = product(a, b, n) == product(b, a, n)
            assert commute == (intersect == 0)
            witnessed[(kind, intersect, commute)] += 1
    expect = {
        ((2, 2), 0, True): 15, ((2, 2), 1, False): 30,
        ((2, 3), 0, True): 60, ((2, 3), 1, False): 360,
        ((2, 3), 2, False): 180,
        ((3, 3), 1, False): 540, ((3, 3), 2, False): 1080,
        ((3, 3), 3, False): 150,
    }
    assert dict(witnessed) == expect, (witnessed, expect)
    assert sum(witnessed.values()) == 70 * 69 // 2
    print('ALL_B5_COMMUTATION_PAIRS', sum(witnessed.values()), 'PASS')

    # Exhaustively enumerate cliques of the support compatibility graph.
    # This is independent of the analytic exponential formula.
    for n in range(2, 9):
        observed = independent_clique_count(n)
        assert observed == expected_coefficients(n), (n, observed, expected_coefficients(n))
        print('CLIQUES', n, *observed)
    print('VERIFY_OK_BRAUER_CORANK_TWO_CLIQUES')


if __name__ == '__main__':
    main()
