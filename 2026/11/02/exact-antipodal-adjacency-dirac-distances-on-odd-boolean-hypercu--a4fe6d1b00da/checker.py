"""Reproducibility diagnostics for antipodal Connes distances on odd cubes.

Requires Python 3 and NumPy. These numerical tests supplement the proof.
"""
import math
import random
import numpy as np


def layer_weights(n):
    return np.array([math.sqrt((k + 1) * (n - k)) for k in range(n)])


def jacobi(n, gaps):
    w = layer_weights(n)
    mat = np.zeros((n + 1, n + 1))
    for k in range(n):
        mat[k, k + 1] = mat[k + 1, k] = w[k] * gaps[k]
    return mat


def full_commutator(n, gaps):
    """The real skew commutator in the vertex-subset basis."""
    f = np.concatenate(([0.0], np.cumsum(gaps)))
    levels = [x.bit_count() for x in range(1 << n)]
    mat = np.zeros((1 << n, 1 << n))
    for x in range(1 << n):
        for k in range(n):
            y = x ^ (1 << k)
            mat[x, y] = f[levels[x]] - f[levels[y]]
    return mat


def formula(n):
    assert n >= 1 and n % 2 == 1
    return sum(1 / math.sqrt((k + 1) * (n - k)) for k in range(0, n, 2))


def optimal_gaps(n):
    w = layer_weights(n)
    return np.array([1 / w[k] if k % 2 == 0 else 0.0 for k in range(n)])


def dual_vector(n):
    w = layer_weights(n)
    L = formula(n)
    u = np.empty(n + 1)
    for k in range(0, n, 2):
        u[k] = u[k + 1] = 1 / math.sqrt(2 * L * w[k])
    return u


def run():
    rng = random.Random(19073)
    checks = 0
    for n in (1, 3, 5, 7):
        h = optimal_gaps(n)
        j = jacobi(n, h)
        lam = np.linalg.eigvalsh(j)[-1]
        assert abs(lam - 1) < 5e-13
        assert abs(sum(h) - formula(n)) < 5e-13
        checks += 2
        u = dual_vector(n)
        assert abs(float(u @ u) - 1) < 5e-13
        assert abs(float(u @ j @ u) - 1) < 5e-13
        checks += 2
        for k in range(n):
            basis = np.zeros(n)
            basis[k] = 1
            witness = float(u @ jacobi(n, basis) @ u)
            assert witness >= 1 / formula(n) - 3e-13
            checks += 1
        K = full_commutator(n, h)
        assert abs(np.linalg.norm(K, 2) - 1) < 8e-13
        checks += 1
        for _ in range(16):
            g = np.array([rng.uniform(-1, 1) for _ in range(n)])
            A = full_commutator(n, g)
            J = jacobi(n, np.abs(g))
            assert abs(np.linalg.norm(A, 2) - np.linalg.norm(J, 2)) < 8e-12
            assert sum(abs(float(x)) for x in g) <= formula(n) * np.linalg.norm(J, 2) + 8e-12
            checks += 2
    zeta_half = -0.6048986434216304
    for N in (10, 20, 50, 100, 500, 2000):
        n = 2 * N - 1
        L = formula(n)
        remainder = L - math.pi / 2 - zeta_half / math.sqrt(N)
        assert 0 <= remainder <= 0.06 / N**1.5
        checks += 1
    print('PASS', checks, 'diagnostic assertions')
    print('odd dimensions:', [(n, round(formula(n), 12)) for n in (1, 3, 5, 7, 9)])
    print('Hurwitz zeta coefficient:', zeta_half)


if __name__ == '__main__':
    run()
