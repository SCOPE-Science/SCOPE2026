"""Independent finite linear-algebra and simulation checks for odd-cycle caps.

Requires NumPy. This is a diagnostic, not a proof of the limiting law.
"""
import math
import numpy as np


def alternating_inverse(y):
    """Invert y_i = 1 - x_i - x_{i+1}, with cyclic indices."""
    n = len(y)
    assert n >= 5 and n % 2 == 1
    v0 = -0.5 * sum((-1) ** (i + 1) * y[i] for i in range(n))
    v = [v0]
    for i in range(n - 1):
        v.append(v[-1] + (-1) ** (i + 1) * y[i])
    return np.array([0.5 + (-1) ** (i + 1) * v[i] for i in range(n)])


def cap_sample(n, rng):
    e = rng.exponential(size=n + 1)
    y = e[:n] / e.sum()
    x = alternating_inverse(y)
    assert np.min(x) >= -1e-12 and np.max(x) <= 1 + 1e-12
    assert np.max(abs(1 - x - np.roll(x, -1) - y)) < 1e-11
    assert x.sum() > (n - 1) / 2
    return x


def unsigned_euler_even(two_m):
    vals = [1]
    for k in range(1, two_m // 2 + 1):
        a = -sum(math.comb(2 * k, 2 * j) * vals[j] for j in range(k))
        vals.append(a)
    return abs(vals[-1])


def run():
    rng = np.random.default_rng(11739)
    for n in (5, 7, 11, 19):
        a = np.eye(n) + np.roll(np.eye(n), -1, axis=1)
        assert abs(abs(np.linalg.det(a)) - 2) < 1e-10
        for j in range(n):
            y = np.zeros(n)
            y[j] = 1
            x = alternating_inverse(y)
            assert np.max(np.abs(x - np.rint(x))) < 1e-12
            assert abs(x.sum() - (n - 1) / 2) < 1e-12
        x = alternating_inverse(np.zeros(n))
        assert np.max(abs(x - 0.5)) < 1e-12
    assert unsigned_euler_even(4) == 5
    assert unsigned_euler_even(6) == 61
    assert unsigned_euler_even(8) == 1385
    print('Finite inverse, determinant and simplex-vertex checks: PASS')
    for n in (5, 9, 31, 101, 501):
        samples = 2000 if n < 501 else 1000
        q = np.array([np.sum((cap_sample(n, rng) - 0.5) ** 2)
                      for _ in range(samples)])
        exact_mean = n / (4 * (n + 2))
        laplace = np.mean(np.exp(-q))
        limit_laplace = 1 / math.cosh(math.sqrt(0.5))
        print(f'n={n:3d}, sample mean Q={q.mean():.6f}, '
              f'exact mean={exact_mean:.6f}, '
              f'sample Laplace(1)={laplace:.6f}, '
              f'limiting Laplace(1)={limit_laplace:.6f}')
    print('All algebraic assertions passed. Monte Carlo is diagnostic only.')


if __name__ == '__main__':
    run()
