#!/usr/bin/env python3
"""Verify trivariate rank coefficients for commuting idempotent full transformations.
Use Python 3 standard library: python3 verify.py
"""
from itertools import product
from collections import Counter
from math import factorial, comb


def enumerate_pairs(n):
    idempotents = [f for f in product(range(n), repeat=n)
                   if all(f[f[i]] == f[i] for i in range(n))]
    distribution = Counter()
    for f in idempotents:
        a = len(set(f))
        for g in idempotents:
            if all(f[g[x]] == g[f[x]] for x in range(n)):
                b = len(set(g))
                c = len({f[g[x]] for x in range(n)})
                distribution[(a, b, c)] += 1
    return distribution, len(idempotents)


def formula(n):
    """Independent species recurrence using weighted labeled one-root blocks."""
    blocks = [Counter() for _ in range(n + 1)]
    for m in range(1, n + 1):
        for p in range(m):
            for q in range(m - p):
                r = m - 1 - p - q
                weight = (m * factorial(m - 1) //
                          (factorial(p) * factorial(q) * factorial(r)))
                weight *= (p + 1)**r * (q + 1)**r
                blocks[m][(p + 1, q + 1, 1)] += weight
    distributions = [Counter() for _ in range(n + 1)]
    distributions[0][(0, 0, 0)] = 1
    for j in range(1, n + 1):
        for m in range(1, j + 1):
            choose = comb(j - 1, m - 1)
            for (a, b, c), x in blocks[m].items():
                for (aa, bb, cc), y in distributions[j - m].items():
                    distributions[j][(a + aa, b + bb, c + cc)] += choose*x*y
    return distributions[n]


def main():
    expected_totals = [1, 7, 58, 601, 7616]
    for n in range(1, 6):
        direct, count_idempotents = enumerate_pairs(n)
        theoretical = formula(n)
        assert direct == theoretical, f'Rank distribution mismatch at n={n}'
        assert sum(direct.values()) == expected_totals[n - 1]
        assert count_idempotents == sum(comb(n, k)*k**(n-k) for k in range(1, n+1))
        for a, b, k in direct:
            assert 1 <= k <= min(a, b) and a + b - k <= n
        for a in range(1, n+1):
            for b in range(1, n+1):
                for k in range(1, n+1):
                    expected_support = k <= min(a,b) and a+b-k <= n
                    assert ((a,b,k) in theoretical) == expected_support, (n,a,b,k)
        print(f'PASS n={n} idempotents={count_idempotents} commuting_pairs={sum(direct.values())} rank_cells={len(direct)}')
    print('VERIFY_OK_COMMUTING_IDEMPOTENT_TRIRANK')

if __name__ == '__main__':
    main()
