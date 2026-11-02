"""Exact checks for optimal rung weights on a two-rail ladder.

Requires Python 3.9+ standard library only. Finite checks are supplements to
(they do not substitute for) the all-size mathematical proof.
"""
from fractions import Fraction as F
from random import Random


def determinant(a):
    a = [row[:] for row in a]
    n = len(a)
    z, ans = F(0), F(1)
    for k in range(n):
        pivot = next((i for i in range(k, n) if a[i][k]), None)
        if pivot is None:
            return z
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            ans = -ans
        p = a[k][k]
        ans *= p
        for i in range(k + 1, n):
            factor = a[i][k] / p
            if factor:
                for j in range(k + 1, n):
                    a[i][j] -= factor * a[k][j]
                a[i][k] = z
    return ans


def matrix_inverse(a):
    n = len(a)
    a = [row[:] + [F(int(i == j)) for j in range(n)] for i, row in enumerate(a)]
    for k in range(n):
        i = next(i for i in range(k, n) if a[i][k])
        a[k], a[i] = a[i], a[k]
        p = a[k][k]
        a[k] = [v / p for v in a[k]]
        for i in range(n):
            if i != k:
                r = a[i][k]
                a[i] = [v - r * u for v, u in zip(a[i], a[k])]
    return [row[n:] for row in a]


def optimum(n, u):
    assert n >= 2 and u > 0
    a, b = u / 2, u * u / (2 * (1 + u))
    return [a] + [b] * (n - 2) + [a]


def reduced(n, w):
    m = [[F(0) for _ in range(n)] for _ in range(n)]
    for i in range(n - 1):
        m[i][i] += 1
        m[i + 1][i + 1] += 1
        m[i][i + 1] = m[i + 1][i] = F(-1)
    for i in range(n):
        m[i][i] += 2 * w[i]
    return m


def full_ladder(n, w):
    m = [[F(0) for _ in range(2 * n)] for _ in range(2 * n)]
    edges = []
    for rail in range(2):
        for i in range(n - 1):
            edges.append((rail * n + i, rail * n + i + 1, F(1)))
    for i in range(n):
        edges.append((i, n + i, w[i]))
    for i, j, c in edges:
        m[i][i] += c
        m[j][j] += c
        m[i][j] -= c
        m[j][i] -= c
    return m


def ar_covariance(n, u):
    rho = 1 / (1 + u)
    c = rho / (1 - rho * rho)
    return [[c * rho ** abs(i - j) for j in range(n)] for i in range(n)]


def run():
    tests = 0
    rng = Random(20261031)
    for n in range(2, 10):
        for u in [F(1, 20), F(1, 3), F(1, 2), F(1), F(5, 2)]:
            w = optimum(n, u)
            budget = sum(w)
            assert budget == (n * u * u + 2 * u) / (2 * (1 + u))
            tests += 1
            A = reduced(n, w)
            G = ar_covariance(n, u)
            inv = matrix_inverse(A)
            assert inv == G
            tests += 1
            assert all(inv[i][i] == inv[0][0] for i in range(n))
            tests += 1
            expected = u * (u + 2) * (1 + u) ** (n - 2) / 2
            assert determinant(A) / 2 == expected
            tests += 1
            if n <= 7:
                cof = [row[:-1] for row in full_ladder(n, w)[:-1]]
                assert determinant(cof) == expected
                tests += 1
            for _ in range(15):
                # Independent feasible weights, including possible zero rungs.
                raw = [rng.randrange(0, 40) for _ in range(n)]
                if not sum(raw):
                    raw[0] = 1
                z = [budget * F(v, sum(raw)) for v in raw]
                assert sum(z) == budget
                assert determinant(reduced(n, z)) <= 2 * expected
                if determinant(reduced(n, z)) == 2 * expected:
                    assert z == w
                tests += 1
    # A rational budget producing a rational optimizer: n=6, B=2.
    n, u = 6, F(1)
    w = optimum(n, u)
    assert w == [F(1, 2), F(1, 4), F(1, 4), F(1, 4), F(1, 4), F(1, 2)]
    assert sum(w) == 2
    assert determinant(reduced(n, w)) / 2 == 24
    tests += 3
    print(f"PASS: {tests} exact rational checks; determinant, KKT, covariance and full cofactors verified.")


if __name__ == '__main__':
    run()
