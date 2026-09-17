#!/usr/bin/env python3
"""Compact diagnostics for the reversible growth-weighted chemostat theorem.

Requires NumPy. It reproduces the five-species Section 4.2 threshold values from
Alvarez-Latuz--Bayen--Coville and checks the reversible symmetrization/strict
substrate monotonicity on deterministic random test networks.
"""
import numpy as np

# Table 1 Monod coefficients in arXiv:2501.08011.
a = np.array([0.84, 0.46, 0.34, 0.48, 0.76], dtype=float)
b = np.array([0.28, 0.90, 0.11, 0.09, 0.36], dtype=float)
n = len(a)
L = np.zeros((n, n))
for j in range(n):
    L[j, j] = -2.0
    L[(j - 1) % n, j] = 1.0
    L[(j + 1) % n, j] = 1.0

def mu(s):
    return a * s / (b + s)

def perron_symmetric(s, eps):
    d = mu(s)
    root = np.diag(np.sqrt(d))
    S = root @ (np.eye(n) + eps * L) @ root
    return np.linalg.eigvalsh(S)[-1]

print("paper example")
for eps in [0.01, 0.5, 1.0, 5.0, 100.0, 10000.0]:
    grid = np.linspace(0.001, 1.0, 101)
    vals = np.array([perron_symmetric(s, eps) for s in grid])
    assert np.all(np.diff(vals) > 0)
    print(f"eps={eps:g} uc={vals[-1]:.12f}")
print(f"harmonic_limit={n / np.sum(1.0 / mu(1.0)):.12f}")

rng = np.random.default_rng(20260917)
for _ in range(30):
    m = 6
    pi = rng.random(m)
    pi /= pi.sum()
    W = rng.random((m, m))
    W = (W + W.T) / 2.0
    np.fill_diagonal(W, 0.0)
    # Column generator with detailed balance L_ij*pi_j = W_ij = W_ji.
    G = W / pi[None, :]
    for j in range(m):
        G[j, j] = -np.sum(G[:, j])
    assert np.max(np.abs(G.sum(axis=0))) < 1e-10
    R = np.diag(pi ** -0.5)
    A = R @ G @ np.linalg.inv(R)
    assert np.max(np.abs(A - A.T)) < 1e-9
    assert np.linalg.eigvalsh(A).max() < 1e-8

    c = rng.uniform(0.2, 1.2, m)
    k = rng.uniform(0.1, 1.0, m)
    def growth(s):
        return c * s / (k + s)

    for eps in [0.03, 0.7, 7.0, 80.0]:
        rr = []
        for s in np.linspace(0.01, 1.0, 80):
            d = growth(s)
            D = np.diag(d)
            M = (np.eye(m) + eps * G) @ D
            direct = max(np.linalg.eigvals(M).real)
            root = np.diag(np.sqrt(d))
            symmetric = np.linalg.eigvalsh(root @ (np.eye(m) + eps * A) @ root)[-1]
            assert abs(direct - symmetric) < 1e-8
            rr.append(symmetric)
        assert np.min(np.diff(rr)) > 1e-8
print("reversible_random_checks=PASS")
