#!/usr/bin/env python3
"""Finite exhaustive checks of the reflexive-core distribution in KD45 frames.

Usage: python3 verify_kd45_core_ldp.py
Uses only the Python standard library. Infinite asymptotics are proved on paper.
"""
from collections import Counter
from itertools import product
from math import comb


def stirling2(n, k):
    d = [[0] * (k + 1) for _ in range(n + 1)]
    d[0][0] = 1
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            d[i][j] = d[i-1][j-1] + j * d[i-1][j]
    return d[n][k]


def theoretical_distribution(n):
    return {m: comb(n, m) * sum(stirling2(m, k) * k ** (n-m)
                for k in range(1, m+1)) for m in range(1, n+1)}


def all_relations_distribution(n):
    result = Counter()
    # Seriality means every row is a nonzero bit mask.
    for rows in product(range(1, 1 << n), repeat=n):
        # Transitivity and right-Euclideanness jointly assert:
        # every edge u->v has identical outgoing rows at u and v.
        if all(rows[u] == rows[v] for u in range(n)
               for v in range(n) if (rows[u] >> v) & 1):
            reflexive = sum((rows[u] >> u) & 1 for u in range(n))
            result[reflexive] += 1
    return dict(result)


def decorated_partition_totals(n):
    d = [0] * (n+1)
    d[0] = 1
    for size in range(1, n+1):
        d[size] = sum(comb(size-1, k-1) * (2**k - 1) * d[size-k]
                      for k in range(1, size+1))
    return d[n]


for n in range(1, 5):
    observed = all_relations_distribution(n)
    formula = theoretical_distribution(n)
    assert observed == formula, (n, observed, formula)
    assert sum(formula.values()) == decorated_partition_totals(n)
    print(f'KD45_EXHAUSTIVE_OK n={n} core_profile={observed}')
for n in range(5, 11):
    formula = theoretical_distribution(n)
    assert sum(formula.values()) == decorated_partition_totals(n)
    print(f'KD45_STIRLING_IDENTITY_OK n={n} total={sum(formula.values())}')
print('KD45_REFLEXIVE_CORE_FORMULAS_OK')
