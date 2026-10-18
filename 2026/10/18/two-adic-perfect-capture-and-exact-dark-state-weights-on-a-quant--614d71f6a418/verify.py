"""Numerical checks for the exact figure-eight sink-survival formulas.

The infinite-family claim is proven analytically in RESULT.md. Numerical tests
here compare two independently implemented constructions on finite graphs.
"""
import math
import numpy as np
from scipy.linalg import expm


def adjacency(m, n):
    assert m >= 3 and n >= 3
    N = m + n - 1
    a = np.zeros((N, N), dtype=float)
    for length, offset in ((m, 0), (n, m - 1)):
        ring = [0] + list(range(offset + 1, offset + length))
        for u, v in zip(ring, ring[1:] + ring[:1]):
            a[u, v] = a[v, u] = 1.0
    return a


def rank_formula(m, n):
    d = math.gcd(m, n)
    same = ((m // d) % 2 == 1 and (n // d) % 2 == 1)
    return (m - 1) // 2 + (n - 1) // 2 + (d // 2 if same else 0)


def survival_formula(m, n, x, branch=0):
    length = m if branch == 0 else n
    assert 1 <= x < length
    s = 0.0 if length % 2 == 0 and x == length // 2 else 0.5
    d = math.gcd(m, n)
    if (m // d) % 2 == 1 and (n // d) % 2 == 1:
        s += (2.0 / (m + n)) * sum(
            math.sin(math.pi * q * x / d) ** 2 for q in range(1, d, 2)
        )
    return s


def dark_projector_by_dense_eigenspaces(a):
    eig, vec = np.linalg.eigh(a)
    result = np.zeros_like(a)
    groups = np.split(np.arange(len(eig)), np.flatnonzero(np.diff(eig) > 1e-8) + 1)
    for indices in groups:
        sub = vec[:, indices]
        at_sink = sub[0, :]
        result += sub @ sub.T
        norm_sq = float(at_sink @ at_sink)
        if norm_sq > 1e-11:
            bright = sub @ at_sink
            result -= np.outer(bright, bright) / norm_sq
    return result


def main():
    rank_tests = 0
    site_tests = 0
    max_error = 0.0
    for m in range(3, 18):
        for n in range(3, 18):
            a = adjacency(m, n)
            projector = dark_projector_by_dense_eigenspaces(a)
            err = abs(np.trace(projector) - rank_formula(m, n))
            max_error = max(max_error, float(err))
            assert err < 2e-8, (m, n, err)
            rank_tests += 1
            for x in range(1, m):
                err = abs(projector[x, x] - survival_formula(m, n, x))
                max_error = max(max_error, float(err))
                assert err < 2e-8, (m, n, x, err)
                site_tests += 1
            for x in range(1, n):
                err = abs(projector[m - 1 + x, m - 1 + x] - survival_formula(m, n, x, 1))
                max_error = max(max_error, float(err))
                assert err < 2e-8, (m, n, 'second', x, err)
                site_tests += 1

    sink_tests = 0
    for m, n, x in ((3, 3, 1), (4, 4, 2), (4, 6, 2), (5, 7, 1), (6, 10, 3)):
        a = adjacency(m, n)
        d = np.zeros(len(a)); d[0] = 1.0
        k = a - 0.5j * np.diag(d)
        propagator = expm(-1j * k * 1400)
        p = float(np.vdot(propagator[:, x], propagator[:, x]).real)
        expected = survival_formula(m, n, x)
        assert abs(p - expected) < 5e-5, (m, n, p, expected)
        sink_tests += 1
    assert abs(survival_formula(4, 6, 2)) < 1e-13
    assert abs(survival_formula(4, 4, 2) - 0.5) < 1e-13
    print(f'VERIFY_OK dense_ranks={rank_tests} site_weights={site_tests} '
          f'nonhermitian_survival={sink_tests} max_projector_error={max_error:.2e}')


if __name__ == '__main__':
    main()
