#!/usr/bin/env python3
"""Finite diagnostics for polar-graph maximal trace-norm packings.

Run: python check.py  (requires numpy)
"""
import numpy as np

def trace_norm(a):
    return float(np.linalg.svd(a, compute_uv=False).sum())

comparisons = 0
checks = 0
for d in range(1, 9):
    n = 2 * d
    rows, cols = np.meshgrid(np.arange(n), np.arange(n), indexing="ij")
    w = np.exp(2j * np.pi * rows * cols / n) / np.sqrt(n)
    v = np.sqrt(2) * w[:d, :]
    u = np.sqrt(2) * w[d:, :]
    assert np.allclose((v.conj().T @ v + u.conj().T @ u) / 2, np.eye(n), atol=1e-12)
    checks += 1
    family = [np.outer(u[:, j], np.conjugate(v[:, j])) for j in range(n)]
    assert np.allclose(np.sum(family, axis=0), 0, atol=1e-12)
    checks += 1
    for j in range(n):
        assert abs(trace_norm(family[j]) - 1) < 1e-11
        checks += 1
        for i in range(j):
            assert abs(trace_norm(family[j] - family[i]) - 2) < 1e-11
            comparisons += 1

for p in range(1, 6):
    for q in range(1, 6):
        k = min(p, q)
        family = []
        for j in range(k):
            a = np.zeros((p, q), dtype=complex)
            a[j, j] = 1
            family.extend([a, -a])
        assert sum(np.linalg.matrix_rank(a) for a in family) == 2 * k
        checks += 1
        for j, a in enumerate(family):
            assert abs(trace_norm(a) - 1) < 1e-12
            checks += 1
            for b in family[:j]:
                assert abs(trace_norm(a-b) - 2) < 1e-12
                comparisons += 1

print(f"PASS: {checks} scalar/check groups and {comparisons} pairwise trace-distance comparisons")
