"""Independent finite-dimensional checks of exact sampling resonances.

Requirements: Python 3, NumPy, SciPy. Run: python CHECK.py.
These numerical checks corroborate, but do not replace, the all-size proof.
"""
import math
import numpy as np
from scipy.linalg import expm
from scipy.optimize import linear_sum_assignment


def generator(n, a, b):
    q = np.zeros((n, n), float)
    for i in range(n):
        q[i, (i + 1) % n] += a
        q[i, (i - 1) % n] += b
        q[i, i] -= a + b
    return q


def resonance(n, a, b, m):
    if n in (3, 6):
        return 2 * m * math.pi / (math.sqrt(3) * abs(a - b))
    if n == 4:
        return m * math.pi / abs(a - b)
    raise ValueError('The theorem predicts no resonance for this n')


def entropy_rate(a, b):
    return (a - b) * math.log(a / b)


def sampled_asymmetry(p):
    return np.max(np.abs(p - p.T))


def main():
    count = 0
    for a, b in ((2.0, 1.0), (3.0, 1.0)):
        assert entropy_rate(a, b) > 0
        count += 1
        for n in (3, 4, 6):
            q = generator(n, a, b)
            qs = generator(n, (a + b) / 2, (a + b) / 2)
            assert np.max(np.abs(q - q.T)) > 0
            count += 1
            for m in (1, 2):
                t = resonance(n, a, b, m)
                p = expm(q * t)
                assert sampled_asymmetry(p) < 1e-12, (n, a, b, m)
                assert np.max(np.abs(np.sum(p, axis=1) - 1)) < 1e-12
                assert np.min(p) > 0
                count += 3
                eigs = np.linalg.eigvalsh((p + p.T) / 2)
                if m % 2:
                    assert np.min(eigs) < -1e-10, (n, a, b, m, eigs)
                    count += 1
                else:
                    assert np.min(eigs) > -2e-14  # near-underflow modes may round to zero
                    assert np.max(np.abs(p - expm(qs * t))) < 1e-12
                    count += 2
        for n in (5, 7, 8, 9, 10, 11, 12, 13, 14, 15):
            q = generator(n, a, b)
            for t in (0.21, 0.63, 1.17):
                p = expm(q * t)
                assert sampled_asymmetry(p) > 1e-9, (n, a, b, t)
                count += 1
                freq = np.exp(t * ((a + b) * (np.cos(2 * np.pi * np.arange(n) / n) - 1) + 1j * (a - b) * np.sin(2 * np.pi * np.arange(n) / n)))
                eig = np.linalg.eigvals(p)
                cost = np.abs(freq[:, None] - eig[None, :])
                rows, cols = linear_sum_assignment(cost)
                assert np.max(cost[rows, cols]) < 1e-10, (n, a, b, t)
                count += 1
    # The argument that 2cos(2pi/n) is an algebraic integer is exact,
    # and is independent of these finite numerical comparisons.
    print(f'PASS: {count} independent numerical assertions; no all-n proof inferred from sampling.')


if __name__ == '__main__':
    main()
