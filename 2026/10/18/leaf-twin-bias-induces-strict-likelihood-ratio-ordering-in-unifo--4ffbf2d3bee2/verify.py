"""Exact checks for leaf-twin conditional regression in uniform labeled trees.

Run with Python 3. Uses the standard library exclusively. Finite checks corroborate
but cannot replace the general enumeration and Stirling-ratio proof.
"""
from fractions import Fraction
from itertools import product
from math import comb, factorial


def second_kind(max_n):
    S = [[0] * (max_n + 1) for _ in range(max_n + 1)]
    S[0][0] = 1
    for n in range(1, max_n + 1):
        for k in range(1, n + 1):
            S[n][k] = k * S[n - 1][k] + S[n - 1][k - 1]
    return S


def decode_prufer(seq, n):
    d = [1] * n
    for v in seq:
        d[v] += 1
    adj = [[] for _ in range(n)]
    for v in seq:
        u = next(i for i in range(n) if d[i] == 1)
        adj[u].append(v)
        adj[v].append(u)
        d[u] -= 1
        d[v] -= 1
    u, v = [i for i in range(n) if d[i] == 1]
    adj[u].append(v)
    adj[v].append(u)
    return adj


def leaf_twin_pair_count(adj):
    n = len(adj)
    leaves = [i for i in range(n) if len(adj[i]) == 1]
    counts = [0] * n
    for i in leaves:
        counts[adj[i][0]] += 1
    return len(leaves), sum(comb(c, 2) for c in counts)


def verify():
    S = second_kind(100)
    exact_states = 0
    for n in range(4, 9):
        totals = {l: [0, 0] for l in range(2, n)}
        for code in product(range(n), repeat=n - 2):
            l, c = leaf_twin_pair_count(decode_prufer(code, n))
            totals[l][0] += 1
            totals[l][1] += c
            exact_states += 1
        assert sum(v[0] for v in totals.values()) == n ** (n - 2)
        all_cherries = sum(pair[1] for pair in totals.values())
        assert all_cherries == comb(n, 2) * (n - 2) ** (n - 3)
        for l, (population, sum_c) in totals.items():
            k = n - l
            expected = Fraction(comb(l, 2) * S[n - 3][k], S[n - 2][k])
            assert population > 0
            assert Fraction(sum_c, population) == expected, (n, l)
            expected_palm = Fraction(
                comb(n - 2, l - 2) * factorial(n - l) * S[n - 3][n - l],
                (n - 2) ** (n - 3),
            )
            assert Fraction(sum_c, all_cherries) == expected_palm, (n, l)
        print('exhaustive n=', n, 'trees=', n ** (n - 2))
    checks = 0
    for n in range(4, 101):
        regression = []
        for l in range(2, n):
            k = n - l
            v = Fraction(comb(l, 2) * S[n - 3][k], S[n - 2][k])
            regression.append(v)
            checks += 1
        assert regression[0] == 0
        assert all(a < b for a, b in zip(regression, regression[1:])), n
    print('PASS', exact_states, 'enumerated labeled trees;', checks, 'strict-ratio checks')


if __name__ == '__main__':
    verify()
