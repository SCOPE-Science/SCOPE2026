"""Exact rational and independent Green-kernel checks for a two-refuge cycle."""
from fractions import Fraction as F
from math import acosh, cosh, sinh, isclose


def solve(matrix, rhs):
    n = len(rhs)
    a = [[F(v) for v in row] + [F(rhs[i])] for i, row in enumerate(matrix)]
    for k in range(n):
        pivot = next(i for i in range(k, n) if a[i][k])
        a[k], a[pivot] = a[pivot], a[k]
        z = a[k][k]
        for j in range(k, n + 1):
            a[k][j] /= z
        for i in range(n):
            if i != k:
                z = a[i][k]
                if z:
                    for j in range(k, n + 1):
                        a[i][j] -= z * a[k][j]
    return [a[i][n] for i in range(n)]


def kernel(n, rate, death, distance, shift=F(0)):
    r = [[F(0)] * n for _ in range(n)]
    for i in range(n):
        r[i][i] = 2 * rate + shift + (F(0) if i in (0, distance) else death)
        r[i][(i - 1) % n] = -rate
        r[i][(i + 1) % n] = -rate
    return r


def uniform_protected_laplace(n, rate, death, d, s):
    r = kernel(n, rate, death, d, s)
    z = solve(r, [1] * n)
    vulnerable = [i for i in range(n) if i not in (0, d)]
    return 1 - s * sum(z[i] for i in vulnerable) / (n - 2)


def evaluate(n, rate, death, d):
    r = kernel(n, rate, death, d)
    t = solve(r, [1] * n)
    second = solve(r, [2 * v for v in t])
    v = [i for i in range(n) if i not in (0, d)]
    mean_v = sum(t[i] for i in v) / (n - 2)
    variance_v = sum(second[i] for i in v) / (n - 2) - mean_v * mean_v
    return mean_v, variance_v, sum(t) / n, sum(t)


def base_kernel(n, rate, death, s):
    r = [[F(0)] * n for _ in range(n)]
    for i in range(n):
        r[i][i] = 2 * rate + death + s
        r[i][(i - 1) % n] = -rate
        r[i][(i + 1) % n] = -rate
    return r


def exact_checks():
    cases = 0
    for n in range(4, 11):
        for rate, death in [(F(1), F(1)), (F(3, 2), F(2, 3))]:
            last_var = last_all = None
            last_laps = {}
            for d in range(1, n // 2 + 1):
                mean, variance, mean_all, z = evaluate(n, rate, death, d)
                assert mean == F(n, n - 2) / death
                assert variance > 0
                if last_var is not None:
                    assert last_var > variance and last_all > mean_all
                last_var, last_all = variance, mean_all
                for s in [F(1, 4), F(1), F(5, 2)]:
                    l = uniform_protected_laplace(n, rate, death, d, s)
                    assert 0 < l < 1
                    if s in last_laps:
                        assert last_laps[s] > l
                    last_laps[s] = l
                    b = base_kernel(n, rate, death, s)
                    g = solve(b, [int(i == 0) for i in range(n)])
                    correction = F(2) * death / (death + s) ** 2
                    z_green = F(n) / (death + s) + correction / (1 - death * (g[0] + g[d]))
                    z_direct = sum(solve(kernel(n, rate, death, d, s), [1] * n))
                    assert z_green == z_direct
                    l_green = 1 - F(n) * s / (death * (n - 2)) + s ** 2 * z_green / (death * (n - 2))
                    assert l_green == l
                    theta = acosh(1 + float(death + s) / (2 * float(rate)))
                    g_closed = cosh((n / 2 - d) * theta) / (2 * float(rate) * sinh(theta) * sinh(n * theta / 2))
                    assert isclose(float(g[d]), g_closed, rel_tol=1e-11, abs_tol=1e-11)
                    cases += 1
    n, rate, death = 6, F(1), F(1)
    expected = [(F(17, 9), F(41, 12), F(17, 38)),
                (F(97, 57), F(217, 76), F(107, 248)),
                (F(5, 3), F(11, 4), F(3, 7))]
    for d, (mean_all, var, lap) in enumerate(expected, 1):
        m, v, ma, _ = evaluate(n, rate, death, d)
        assert (ma, v, uniform_protected_laplace(n, rate, death, d, F(1))) == (mean_all, var, lap)
        assert m == F(3, 2)
    print('PASS: %d exact rational resolvent, moment, Laplace and Green checks' % cases)
    print('PASS: all cycle sizes 4..10, all separations, two rate pairs, three Laplace shifts')
    print('PASS: independent hyperbolic-cycle Green identity for all tested cases')
    print('PASS: exact six-site benchmark fractions')


if __name__ == '__main__':
    exact_checks()
