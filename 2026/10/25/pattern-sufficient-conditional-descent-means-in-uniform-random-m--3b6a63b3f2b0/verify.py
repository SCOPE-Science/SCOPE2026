"""Exact finite checks for pattern-conditional descent identities in matchings."""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations


def perfect_matchings(vertices):
    if not vertices:
        yield ()
        return
    first = vertices[0]
    for pos in range(1, len(vertices)):
        second = vertices[pos]
        for rest in perfect_matchings(vertices[1:pos] + vertices[pos + 1:]):
            yield ((first, second),) + rest


def descent_number(partners):
    return sum(partners[i] > partners[i + 1] for i in range(len(partners) - 1))


def chord_type(edge1, edge2):
    (a, b), (c, d) = edge1, edge2
    x = sorted((a, b, c, d))
    induced = {v: i for i, v in enumerate(x)}
    u, v = sorted((induced[a], induced[b]))
    if (u, v) == (0, 1) or (u, v) == (2, 3):
        return 'alignment'
    if (u, v) == (0, 2) or (u, v) == (1, 3):
        return 'crossing'
    return 'nesting'


def check(n):
    N = 2 * n
    pattern_totals = [defaultdict(lambda: [0, 0]) for _ in range(n)]
    joint = defaultdict(int)
    sums = defaultdict(int)
    matching_count = 0
    for edges in perfect_matchings(tuple(range(N))):
        matching_count += 1
        pi = [0] * N
        for a, b in edges:
            pi[a], pi[b] = b, a
        desc = descent_number(pi)
        pair_counts = defaultdict(int)
        for edge1, edge2 in combinations(edges, 2):
            pair_counts[chord_type(edge1, edge2)] += 1
        sums['D'] += desc
        for typ in ('crossing', 'nesting', 'alignment'):
            sums[typ] += pair_counts[typ]
            joint[typ] += desc * pair_counts[typ]
        for k in range(1, n + 1):
            for subset in combinations(edges, k):
                endpoints = sorted(x for a, b in subset for x in (a, b))
                rank = {v: i for i, v in enumerate(endpoints)}
                tau = [0] * (2 * k)
                for a, b in subset:
                    tau[rank[a]], tau[rank[b]] = rank[b], rank[a]
                total, count = pattern_totals[k - 1][tuple(tau)]
                pattern_totals[k - 1][tuple(tau)] = [total + desc, count + 1]
    assert Fraction(sums['D'], matching_count) == n
    for k in range(1, n + 1):
        for tau, (total, count) in pattern_totals[k - 1].items():
            expectation = Fraction(n) + Fraction(k, n) * (descent_number(tau) - k)
            assert Fraction(total, count) == expectation, (n, k, tau, total, count)
    if n >= 2:
        expected = {'crossing': Fraction(-(n - 1), 3),
                    'nesting': Fraction(n - 1, 3),
                    'alignment': Fraction(0)}
        for typ in expected:
            covariance = Fraction(joint[typ], matching_count) - Fraction(sums['D'] * sums[typ], matching_count**2)
            assert covariance == expected[typ], (n, typ, covariance, expected[typ])
    print(f'PASS n={n}, matchings={matching_count}, all marked patterns and pair-type covariances')


if __name__ == '__main__':
    for n in range(1, 6):
        check(n)
