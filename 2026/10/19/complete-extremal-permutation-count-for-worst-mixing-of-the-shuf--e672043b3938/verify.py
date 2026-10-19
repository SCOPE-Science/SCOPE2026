"""Finite corroboration of a Fourier equality classification for shuffled doubling maps.

Dependencies: Python 3.9+ and NumPy 1.20+.
The infinite-parameter statement is established by the accompanying analytic proof;
finite eigenvalue computations in this script do not certify that theorem on their own.
"""
import itertools
import math
import random
import numpy as np


def build(n):
    h = (n - 1) // 2
    A = np.zeros((n, n), dtype=float)
    C = np.zeros((n, n), dtype=float)
    for i in range(n):
        A[i, (2 * i) % n] = 1
        A[i, (2 * i + 1) % n] = 1
        C[i, (i + h) % n] = 1
        C[i, (i - h) % n] = 1
    r = tuple((2 * i - h) % n for i in range(n))
    return A, C, r


def predicted(n):
    h = (n - 1) // 2
    result = {tuple((i + c) % n for i in range(n)) for c in range(n)}
    for a in range(n):
        pairs = []
        for i in range(n):
            j = (a - i) % n
            if i < j:
                pairs.append((i, j))
        assert len(pairs) == h
        for mask in range(1 << h):
            p = list(range(n))
            for b, (i, j) in enumerate(pairs):
                if mask & (1 << b):
                    p[i], p[j] = p[j], p[i]
            result.add(tuple(p))
    assert len(result) == n * (1 << h)
    return result


def subleading_radius(matrix):
    eigenvalues = np.linalg.eigvals(matrix)
    leading = min(range(len(eigenvalues)), key=lambda i: abs(eigenvalues[i] - 1))
    assert abs(eigenvalues[leading] - 1) < 1e-7
    return max(abs(eigenvalues[i]) for i in range(len(eigenvalues)) if i != leading)


def check(n, perms):
    A, C, r = build(n)
    predicted_set = predicted(n)
    R = np.eye(n)[list(r), :]
    expected = math.cos(math.pi / n)
    tested = 0
    for sigma in perms:
        pi = tuple(r[sigma[i]] for i in range(n))
        P = np.eye(n)[list(sigma), :]
        Q = np.eye(n)[list(pi), :]
        assert np.array_equal(P @ R, Q)
        assert np.array_equal(A, R @ C)
        assert np.array_equal(R.T @ (A @ P) @ R, C @ Q)
        radius = subleading_radius(C @ Q / 2.0)
        actual = abs(radius - expected) < 3e-8
        assert (radius <= expected + 1e-8), (n, sigma, radius, expected)
        assert actual == (pi in predicted_set), (n, sigma, pi, radius)
        tested += 1
    return tested


def main():
    for n in (3, 5, 7):
        count = check(n, itertools.permutations(range(n)))
        assert count == math.factorial(n)
        print(f'N={n}: {count} exact permutation configurations checked')
    rng = random.Random(617390)
    n = 9
    sampled = []
    for _ in range(500):
        items = list(range(n))
        rng.shuffle(items)
        sampled.append(tuple(items))
    assert check(n, sampled) == len(sampled)
    print('N=9: 500 random configurations checked')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
