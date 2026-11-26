"""Exact finite checks for transitions and low-state visitation, not limits."""
from fractions import Fraction
from math import comb, factorial


def stirling(n):
    table = [[0] * (n + 1) for _ in range(n + 1)]
    table[0][0] = 1
    for m in range(1, n + 1):
        for j in range(1, m + 1):
            table[m][j] = table[m - 1][j - 1] + j * table[m - 1][j]
    return table[n]


def transition(n, k, values):
    return {j: Fraction(comb(k, j) * factorial(j) * values[j], k**n)
            for j in range(1, k + 1)}


for n in range(3, 18):
    values = stirling(n)
    p = {k: transition(n, k, values) for k in range(2, n + 1)}
    for k in range(2, n + 1):
        q = 1 - p[k][k]
        assert sum(p[k].values()) == 1
        assert q >= Fraction((k - 1)**n, k**n) > 0
        assert p[k][1] == Fraction(k, k**n)
    assert 1 - p[2][2] == Fraction(2, 2**n)
    assert 1 - p[3][3] == Fraction(3 * (2**n - 1), 3**n)
    for target in range(2, min(4, n) + 1):
        hit = {k: Fraction(int(k == target)) for k in range(1, target + 1)}
        for k in range(target + 1, n + 1):
            hit[k] = (sum(p[k][j] * hit[j] for j in range(1, k))
                      / (1 - p[k][k]))
        assert 0 < hit[n] <= 1
        assert 1 - hit[n] <= n**target * Fraction((target - 1)**n, target**n)

print("Finite transition and visitation checks passed.")
