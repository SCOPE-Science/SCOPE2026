#!/usr/bin/env python3
"""Finite numerical checks for the one-defect Hadamard Schur multiplier theorem.

The analytical proof, not these finite tests, establishes the result for all
admissible Hadamard orders. Requires NumPy; standard IEEE double precision.
"""
import math
import numpy as np


def sylvester(order):
    H = np.array([[1]], dtype=float)
    while H.shape[0] < order:
        H = np.block([[H, H], [H, -H]])
    assert H.shape == (order, order)
    return H


def paley(q):
    assert q % 4 == 3
    quadratic = {i * i % q for i in range(1, q)}
    C = np.zeros((q, q))
    for i in range(q):
        for j in range(q):
            if i != j:
                C[i, j] = 1 if (j - i) % q in quadratic else -1
    H = np.ones((q + 1, q + 1))
    H[1:, 1:] = C - np.eye(q)
    return H


def normalize(H):
    H = H.copy()
    H *= H[[0], :]
    H *= H[:, [0]]
    return H


def constant(n):
    return ((n - 2) * math.sqrt(n) + 2 * (n - 1) * math.sqrt(n + 2)) / (3 * n - 2)


def weights(n):
    b = (1 + 2 * math.sqrt(n / (n + 2))) / (3 * n - 2)
    return 1 - (n - 1) * b, b


def certificate(n):
    t, b = weights(n)
    R = math.sqrt((t - b) ** 2 + 4 * (n - 1) * t * b)
    X = np.eye(n) * math.sqrt(n)
    u = np.ones(n - 1) / math.sqrt(n - 1)
    k00 = (t + (2 * n - 3) * b) / R
    k01 = -(t + b) * math.sqrt(n - 1) / R
    k11 = (b + (2 * n - 3) * t) / R
    X[0, 0] = k00
    X[0, 1:] = X[1:, 0] = k01 * u
    X[1:, 1:] += (k11 - math.sqrt(n)) * np.outer(u, u)
    return X


def check():
    rng = np.random.default_rng(246813579)
    count = 0
    for n in range(4, 201):
        c = constant(n)
        t, b = weights(n)
        assert 0 < t < 1 and 0 < b < 1
        exact_defect = 2 / (n * math.sqrt(n) + (n - 1) * math.sqrt(n + 2))
        assert math.isclose(math.sqrt(n) - c, exact_defect, rel_tol=1e-9, abs_tol=1e-12)
        count += 1
    orders = [(4, sylvester(4)), (8, sylvester(8)),
              (12, paley(11)), (16, sylvester(16)),
              (20, paley(19)), (32, sylvester(32))]
    for n, H in orders:
        H = normalize(H)
        assert np.max(np.abs(H @ H.T - n * np.eye(n))) < 1e-9
        B = H.copy()
        B[0, 0] *= -1
        c = constant(n)
        t, b = weights(n)
        p = np.array([t] + [b] * (n - 1))
        D = np.diag(np.sqrt(p))
        M = D @ B @ D
        U, singular, Vt = np.linalg.svd(M)
        assert abs(sum(singular) - c) < 2e-10
        A = U @ Vt
        assert np.linalg.norm(A, 2) < 1 + 1e-10
        witness = np.linalg.norm(B * A, 2)
        assert witness >= c - 1e-9
        X = certificate(n)
        assert min(np.linalg.eigvalsh(X)) > 1e-8
        assert np.max(np.abs(np.diag(X) - c)) < 2e-9
        assert np.max(np.abs(B.T @ np.linalg.solve(X, B) - X)) < 2e-9
        assert abs(witness - c) < 2e-9
        count += 6
        for _ in range(48):
            rp = rng.dirichlet(np.ones(n) * rng.uniform(.2, 4))
            rq = rng.dirichlet(np.ones(n) * rng.uniform(.2, 4))
            trial = np.sqrt(rp)[:, None] * B * np.sqrt(rq)[None, :]
            assert np.linalg.svd(trial, compute_uv=False).sum() <= c + 2e-9
            count += 1
        print('order=%d norm=%.12f defect=%.9g certificate_and_witness=OK' % (n, c, math.sqrt(n)-c))
    print('PASS %d numerical and scalar assertions' % count)


if __name__ == '__main__':
    check()
