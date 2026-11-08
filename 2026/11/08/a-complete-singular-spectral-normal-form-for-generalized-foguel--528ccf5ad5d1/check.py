#!/usr/bin/env python3
"""Numerical finite-matrix tests of a positive block spectral decomposition.
Requires numpy. These tests supplement, not replace, the analytic proof.
"""
import numpy as np

rng = np.random.default_rng(20261102)
checks = 0

def close(a, b, tol=1e-9):
    global checks
    a = np.asarray(a)
    b = np.asarray(b)
    assert a.shape == b.shape and np.allclose(a, b, atol=tol, rtol=tol)
    checks += 1

def test(p, q, rank):
    global checks
    left = rng.normal(size=(p, rank)) + 1j * rng.normal(size=(p, rank))
    right = rng.normal(size=(rank, q)) + 1j * rng.normal(size=(rank, q))
    t = left @ right if rank else np.zeros((p, q), dtype=complex)
    ident_p, ident_q = np.eye(p), np.eye(q)
    g = np.block([[ident_p, t], [np.zeros((q, p)), ident_q]])
    gtg = g.conj().T @ g
    sv = np.linalg.svd(t, compute_uv=False)
    sv = sv[:rank]
    phi = (sv + np.sqrt(sv**2 + 4.0)) / 2.0
    pred = np.sort(np.concatenate([phi, 1/phi, np.ones(p+q-2*rank)]))
    actual = np.sqrt(np.maximum(np.linalg.eigvalsh(gtg), 0))
    close(actual, pred)
    assert np.linalg.norm(gtg - np.block([[ident_p,t],[t.conj().T,ident_q+t.conj().T@t]])) < 1e-8
    checks += 1
    for exponent in (0.5, 1.0, 2.0, 3.0):
        lhs = np.sum(abs(actual - 1.0)**exponent)
        rhs = np.sum((phi-1.0)**exponent + (1.0-1.0/phi)**exponent)
        close(lhs, rhs, tol=3e-4 if exponent == 0.5 else 1e-8)
    for extra_zeros in (0, 1, 3):
        exact = np.sort(np.concatenate([actual, np.zeros(extra_zeros)]))
        canonical = np.sort(np.concatenate([pred, np.zeros(extra_zeros)]))
        close(exact, canonical)

for p in range(1, 7):
    for q in range(1, 7):
        for rank in range(min(p,q)+1):
            for _ in range(6):
                test(p,q,rank)
print('FOGUEL_FULL_MODULUS_FINITE_CHECKS_OK', checks)
