#!/usr/bin/env python3
"""Independent numeric diagnostics for first Fourier moments of circular interval windows.
Requires Python 3 and NumPy. This is a finite diagnostic, not a proof."""
import math
import numpy as np


def jacobian(k, rho, phi=0.137):
    """Real (2k-2)x(2k-2) Jacobian in orthonormal mean-zero endpoint coordinates."""
    idx = np.arange(k)
    roots = np.exp(-2j * np.pi * np.outer(np.arange(1, k), idx) / k)
    phases = np.exp(-1j * np.arange(1, k)[:, None] * (phi + 2 * np.pi * rho / k))
    alpha = np.exp(-1j * np.arange(1, k)[:, None] * phi)
    a = -roots * alpha / (2*np.pi)
    b = roots * phases / (2*np.pi)
    # Orthonormal basis for zero-mean real vectors through QR of differences.
    raw = np.eye(k)[:, :-1] - np.eye(k)[:, [-1]]
    Q, _ = np.linalg.qr(raw)
    c = np.hstack((a @ Q, b @ Q))
    return np.vstack((c.real, c.imag))


def moment(k, rho, u, v, phi=0.137):
    j = np.arange(k)
    starts = phi + 2*np.pi*j/k + u
    ends = starts*0 + phi + 2*np.pi*j/k + 2*np.pi*rho/k + v
    m = np.arange(1, k)[:, None]
    return ((np.exp(-1j*m*starts) - np.exp(-1j*m*ends)).sum(axis=1) /
            (2j*np.pi*np.arange(1, k)))


num = 0
rng = np.random.default_rng(204042)
for k in range(2, 14):
    for rho in [0.09, 0.21, 0.37, 0.5, 0.69, 0.87]:
        J = jacobian(k, rho)
        vals = np.linalg.svd(J, compute_uv=False)
        bound_lo = math.sqrt(k)/(2*math.pi)*math.sqrt(1-abs(math.cos(math.pi*rho)))
        bound_hi = math.sqrt(k)/(2*math.pi)*math.sqrt(1+abs(math.cos(math.pi*rho)))
        targets = sorted([bound_lo]*(k-1) + [bound_hi]*(k-1), reverse=True)
        assert np.allclose(vals, targets, rtol=1e-11, atol=5e-14), (k, rho, vals, targets)
        num += 1
        j = np.arange(k)
        u = rng.normal(size=k); u -= np.mean(u)
        v = rng.normal(size=k); v -= np.mean(v)
        h = 1e-6
        numeric = (moment(k, rho, h*u, h*v)-moment(k, rho, -h*u, -h*v))/(2*h)
        formula = (np.exp(-1j*np.arange(1,k)*0.137) *
                   ((np.exp(-2j*np.pi*np.outer(np.arange(1,k),j)/k) @ u) *(-1) +
                    (np.exp(-2j*np.pi*np.outer(np.arange(1,k),j)/k) @ v) *
                     np.exp(-1j*np.arange(1,k)*2*np.pi*rho/k))/(2*np.pi))
        assert np.allclose(numeric, formula, atol=2e-9, rtol=2e-8)
        num += 1
print('PASS', num, 'deterministic singular-spectrum and finite-difference tests')
