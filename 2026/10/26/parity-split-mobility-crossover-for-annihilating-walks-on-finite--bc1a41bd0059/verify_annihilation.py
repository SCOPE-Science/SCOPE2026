"""Exact checks for hub-dependent annihilating walks on finite stars.
Run: python3 verify_annihilation.py. Standard library only.
"""
from fractions import Fraction as F
from math import log


def harmonic(n):
    return sum((F(1, j) for j in range(1, n + 1)), F(0))


def expected(m, hub_rate, mask):
    assert m >= 1 and hub_rate > 0
    hub = bool(mask & 1)
    k = (mask >> 1).bit_count()
    if (k + hub) < 2:
        return F(0)
    a = F(m) * (1 + hub_rate) / (m + hub_rate)
    b = hub_rate * (m + 1) / (m + hub_rate)
    c = F(m) * hub_rate / (m + hub_rate)

    def amean(j):
        if j == 0:
            return F(0)
        if j % 2 == 0:
            return c * harmonic(j // 2) + (1 - b) * (harmonic(j) - 1) - b / (j + 1)
        return a * harmonic(j) - c * harmonic((j - 1) // 2) - b / (j + 1)

    if hub:
        return amean(k)
    return F(1, k) + amean(k - 1)


def transitions(m, hub_rate, mask):
    ans = []
    hub = mask & 1
    for i in range(1, m + 1):
        leaf = 1 << i
        if mask & leaf:
            if hub:
                ans.append((F(1), mask ^ leaf ^ 1))
            else:
                ans.append((F(1), mask ^ leaf ^ 1))
    if hub:
        for i in range(1, m + 1):
            ans.append((hub_rate / m, mask ^ (1 << i) ^ 1))
    return ans


def gauss(a, b):
    n = len(b)
    aug = [row[:] + [rhs] for row, rhs in zip(a, b)]
    for i in range(n):
        pivot = next(j for j in range(i, n) if aug[j][i] != 0)
        aug[i], aug[pivot] = aug[pivot], aug[i]
        d = aug[i][i]
        aug[i] = [v / d for v in aug[i]]
        for j in range(i + 1, n):
            d = aug[j][i]
            if d:
                aug[j] = [u - d * v for u, v in zip(aug[j], aug[i])]
    x = [F(0)] * n
    for i in reversed(range(n)):
        x[i] = aug[i][n] - sum((aug[i][j] * x[j] for j in range(i + 1, n)), F(0))
    return x


def independent_full_linear_solve(m, gamma):
    transient = [mask for mask in range(1 << (m + 1)) if mask.bit_count() >= 2]
    ix = {mask: i for i, mask in enumerate(transient)}
    n = len(transient)
    mat = [[F(0) for _ in range(n)] for _ in range(n)]
    for i, mask in enumerate(transient):
        for rate, target in transitions(m, gamma, mask):
            mat[i][i] += rate
            if target in ix:
                mat[i][ix[target]] -= rate
    return transient, gauss(mat, [F(1)] * n)


def run():
    residuals = 0
    exact_solves = 0
    for m in range(1, 9):
        for gamma in (F(1, 4), F(1), F(5, 2), F(m), F(2 * m + 1)):
            for mask in range(1 << (m + 1)):
                f = expected(m, gamma, mask)
                if mask.bit_count() <= 1:
                    assert f == 0
                    continue
                trans = transitions(m, gamma, mask)
                lhs = sum((rate * (f - expected(m, gamma, target)) for rate, target in trans), F(0))
                assert lhs == 1, (m, gamma, mask, lhs)
                residuals += 1
            if m <= 4:
                states, solution = independent_full_linear_solve(m, gamma)
                for s, val in zip(states, solution):
                    assert val == expected(m, gamma, s), (m, gamma, s)
                    exact_solves += 1
    for gamma in (F(1, 3), F(1), F(9)):
        for m in (501, 502, 5001, 5002):
            full = expected(m, gamma, (1 << (m + 1)) - 1)
            # Fixed-rate parity constants are evaluated with bounded errors.
            import math
            const = float(full) - log(m) - float(math.euler_gamma if hasattr(math, 'euler_gamma') else 0.5772156649015329)
            target = float(gamma) * (1 - log(2)) - 1 if m % 2 == 0 else float(gamma) * log(2)
            assert abs(const - target) < (0.3 if m < 1000 else 0.04)
    for theta in (F(1, 4), F(1), F(3)):
        for m in (1001, 1002):
            val = float(expected(m, theta * m, (1 << (m + 1)) - 1)) / m
            target = float(theta / (1 + theta)) * (log(2) if m % 2 else 1 - log(2))
            assert abs(val - target) < 0.006
    print('PASS exact generator residuals:', residuals)
    print('PASS independent full-generator linear-system states:', exact_solves)
    print('PASS fixed-speed asymptotic samples: 12')
    print('PASS linearly scaled hub-rate asymptotic samples: 6')


if __name__ == '__main__':
    run()
