#!/usr/bin/env python3
"""Finite checks for exact cycle heat-flow Lipschitz formulas.

Requires only Python's standard library. These checks corroborate, but do not
replace, the all-order analytic argument in RESULT.md.
"""
import math


def graph_distance(j, n):
    return min(j, n - j)


def heat_row(n, t):
    # Exact spectral formula evaluated in floating point.
    eigenvalues = [4.0 * math.sin(math.pi * m / n) ** 2 for m in range(n)]
    multipliers = [math.exp(-t * x) for x in eigenvalues]
    return [sum(multipliers[m] * math.cos(2 * math.pi * m * j / n)
                for m in range(n)) / n for j in range(n)]


def expression(n, p):
    r = n // 4
    tail = lambda d: sum(p[j] for j in range(n) if graph_distance(j, n) > d)
    if n % 4 == 0:
        return 1 - 2 * p[r] - 2 * tail(r)
    if n % 4 == 1:
        return 1 - p[r] - 2 * tail(r)
    if n % 4 == 2:
        return 1 - 2 * tail(r)
    return 1 - 3 * p[r + 1] - 2 * tail(r + 1)


def independent_dual(n, p):
    # Linear-programming dual with integral edge slopes. A vertex of
    # [-1,1]^n intersect sum(g_j)=0 has all slopes in {-1,0,1}.
    # DP imposes sum(g_j)=0 without using the median formula.
    dp = {0: 0.0}
    for pj in p:
        new = {}
        for s, value in dp.items():
            for g in (-1, 0, 1):
                k = s + g
                candidate = value + g * pj
                if k not in new or candidate > new[k]:
                    new[k] = candidate
        dp = new
    return dp[0]


def coefficient(n):
    if n % 2:
        a = math.pi / (2 * n)
        return 2 / n * (1 / math.sin(a) - math.sin(a))
    if n % 4 == 0:
        return 4 / (n * math.tan(math.pi / n))
    return 4 / (n * math.sin(math.pi / n))


def exact_taylor():
    count = 0
    for n in range(3, 81):
        r, residue = divmod(n, 4)
        expected_order = r + (residue >= 2)
        expected_numerator = -(2, 1, 4, 3)[residue]
        # Integer coefficients of exp(t Q) delta_0, with Q=-L.
        q = [[0] * n for _ in range(n)]
        for v in range(n):
            q[v][v] = -2
            q[v][(v - 1) % n] += 1
            q[v][(v + 1) % n] += 1
        weights = []
        for j in range(n):
            d = graph_distance(j, n)
            if residue == 0:
                w = 1 if d < r else 0 if d == r else -1
            elif residue == 1:
                w = 1 if d < r else 0 if d == r else -1
                if j == r:
                    w = 1
            elif residue == 2:
                w = 1 if d <= r else -1
            else:
                w = 1 if d < r + 1 else 0 if d == r + 1 else -1
                if j == r + 1:
                    w = -1
            weights.append(w)
        assert sum(weights) == 0
        v = [0] * n
        v[0] = 1
        for j in range(expected_order + 1):
            numerator = sum(w * a for w, a in zip(weights, v))
            if j == 0:
                assert numerator == 1
            elif j < expected_order:
                assert numerator == 0, (n, j, numerator)
            else:
                assert numerator == expected_numerator, (n, j, numerator)
            v = [sum(q[x][y] * v[y] for y in range(n)) for x in range(n)]
            count += 1
    return count


def main():
    num = 0
    for n in range(3, 25):
        for t in (0.0, 0.17, 0.5, 1.0, 3.0, 8.0):
            p = heat_row(n, t)
            median = sorted(p)[n // 2]
            median_distance = sum(abs(x - median) for x in p)
            from_formula = expression(n, p)
            from_dual = independent_dual(n, p)
            assert abs(median_distance - from_formula) < 5e-12, (n, t, "formula")
            assert abs(median_distance - from_dual) < 5e-12, (n, t, "dual")
            assert abs(sum(p) - 1) < 5e-12
            assert 0 <= from_formula < 1 + 5e-12
            num += 1
    harmonics = 0
    for n in range(3, 81):
        cosine = [math.cos(2 * math.pi * j / n) for j in range(n)]
        median = sorted(cosine)[n // 2]
        c_direct = (2 / n) * sum(abs(x - median) for x in cosine)
        assert abs(c_direct - coefficient(n)) < 1e-12
        harmonics += 1
    taylors = exact_taylor()
    print("CHECK_OK cycle_sizes=78 spectral_coefficients=78 heat_dual_instances=%d exact_Taylor_coefficients=%d" %
          (num, taylors))


if __name__ == "__main__":
    main()
