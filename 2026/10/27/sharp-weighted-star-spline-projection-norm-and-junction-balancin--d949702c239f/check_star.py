"""Exact rational checks of the weighted metric-star spline projection formula.

Usage: python check_star.py
Requires only Python's standard library.
"""
from fractions import Fraction as F
from random import Random


def inverse(A):
    n = len(A)
    T = [[F(v) for v in row] + [F(i == j) for j in range(n)] for i, row in enumerate(A)]
    for i in range(n):
        k = next(j for j in range(i, n) if T[j][i])
        T[i], T[k] = T[k], T[i]
        q = T[i][i]
        T[i] = [v / q for v in T[i]]
        for j in range(n):
            if j != i:
                q = T[j][i]
                T[j] = [a - q * b for a, b in zip(T[j], T[i])]
    return [row[n:] for row in T]


def integral_abs_linear(a, b):
    z = a + b
    if a * z >= 0:
        return abs((a + z) / 2)
    r = -a / b
    assert F(0) < r < F(1)
    return (r * abs(a) + (1-r) * abs(z)) / 2


def compute(measures):
    n = len(measures)
    M = sum(measures)
    G = [[F(0) for _ in range(n+1)] for _ in range(n+1)]
    G[0][0] = M / 3
    for i, mass in enumerate(measures, 1):
        G[0][i] = G[i][0] = mass / 6
        G[i][i] = mass / 3
    GI = inverse(G)
    assert all(sum(G[i][k] * GI[k][j] for k in range(n+1)) == F(i == j)
               for i in range(n+1) for j in range(n+1))
    rows = []
    for v in range(n+1):
        rows.append(sum(mass * integral_abs_linear(GI[v][0], GI[v][j] - GI[v][0])
                        for j, mass in enumerate(measures, 1)))
    return rows


def run():
    rng = Random(4195)
    total = 0
    for n in range(1, 10):
        for case in range(25):
            lengths = [F(rng.randint(1, 60), rng.randint(1, 30)) for _ in range(n)]
            weights = [F(rng.randint(1, 30), rng.randint(1, 15)) for _ in range(n)]
            measures = [a * b for a, b in zip(lengths, weights)]
            rows = compute(measures)
            M = sum(measures)
            expected = [F(5, 3)] + [F(7, 3) - 4*q/(3*(M+q)) for q in measures]
            assert rows == expected, (n, measures, rows, expected)
            sharp = F(7, 3) - 4*min(measures)/(3*(M+min(measures)))
            assert max(rows) == sharp
            if n >= 2:
                assert all(rows[i] > rows[0] for i in range(1, n+1))
            else:
                assert rows[1] == rows[0] == F(5, 3)
            total += 1
    for n in range(2, 13):
        balanced = [F(1)] * n
        rows = compute(balanced)
        assert max(rows) == F(7, 3) - F(4, 3*(n+1))
    for eps in [F(1, 10**j) for j in range(1, 9)]:
        rows = compute([eps, F(1), F(1), F(1)])
        assert max(rows) == F(7, 3) - 4*eps/(3*(3+2*eps))
    print(f"PASS: {total} exact rational weighted cases; balanced and degenerating families checked.")


if __name__ == '__main__':
    run()
