#!/usr/bin/env python3
"""Finite-dimensional diagnostics for an alternating-adjoint block path."""
import numpy as np


def path(weights):
    n = len(weights) + 1
    a = np.zeros((n, n), dtype=complex)
    for j, w in enumerate(weights):
        a[j, j + 1] = w
    return a


def alternating(core, weights):
    d = core.shape[0]
    n = len(weights) + 1
    a = np.zeros((n * d, n * d), dtype=complex)
    for j, w in enumerate(weights):
        a[j*d:(j+1)*d, (j+1)*d:(j+2)*d] = w * (core if j % 2 == 0 else core.conj().T)
    return a


def opnorm(a):
    return float(np.linalg.svd(a, compute_uv=False)[0])


def check():
    rng = np.random.default_rng(20261018)
    count = 0
    for d in range(1, 5):
        for n in range(2, 8):
            for trial in range(12):
                raw = rng.normal(size=(d, d)) + 1j*rng.normal(size=(d, d))
                if trial == 0:
                    raw[:] = 0.0
                elif trial == 1:
                    raw[:, 1:] = 0.0
                elif trial == 2:
                    raw = np.triu(raw, 1)
                elif trial == 3:
                    raw = np.eye(d)
                scale = opnorm(raw) if np.any(raw) else 1.0
                t = raw / scale
                weights = rng.uniform(.12, 1.8, size=n-1)
                p = path(weights)
                b = alternating(t, weights)
                l = opnorm(t)
                for z in (0.0, 0.15 + .41j, 1.0, -0.8j):
                    lhs = opnorm(np.linalg.inv(np.eye(d*n) - z*b))
                    rhs = opnorm(np.linalg.inv(np.eye(n) - abs(z)*l*p))
                    assert abs(lhs-rhs) < 7e-11 * max(1.0, rhs), (d,n,trial,z,lhs,rhs)
                    count += 1
                # Compare direct k-th powers with the scalar tensor prediction.
                for k in range(1,n):
                    lhs = opnorm(np.linalg.matrix_power(b,k))
                    rhs = opnorm(np.linalg.matrix_power(p,k))*l**k
                    assert abs(lhs-rhs) < 7e-11 * max(1.0, rhs), (d,n,k,lhs,rhs)
                    count += 1
    # Verify the exact discrete-Volterra benchmark at unit scale.
    for n in range(2, 25):
        p = path(np.ones(n-1))
        lhs = opnorm(np.linalg.inv(np.eye(n)-p))
        rhs = 1.0 / (2*np.sin(np.pi / (4*n+2)))
        assert abs(lhs-rhs) < 5e-12 * rhs, (n,lhs,rhs)
        count += 1
    print(f'PASS {count} finite assertions; these are diagnostics, not infinite-dimensional proofs.')

if __name__ == '__main__':
    check()
