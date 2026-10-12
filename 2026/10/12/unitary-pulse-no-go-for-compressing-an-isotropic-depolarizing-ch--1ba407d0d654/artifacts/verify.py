#!/usr/bin/env python3
"""Finite consistency checks for the depolarizing-channel pulse-control no-go."""
import math
import numpy as np

I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
PAULIS = [I, X, Y, Z]

def depol(rho, p):
    return (1-p)*rho + (p/3)*(X@rho@X + Y@rho@Y + Z@rho@Z)

def dsem(rho, kappa, t):
    a = math.exp(-kappa*t)
    return a*rho + (1-a)*I/2

rng = np.random.default_rng(260516463)
for _ in range(20):
    v = rng.normal(size=2) + 1j*rng.normal(size=2)
    v /= np.linalg.norm(v)
    rho = np.outer(v, v.conj())

    A = rng.normal(size=(2,2)) + 1j*rng.normal(size=(2,2))
    Q, R = np.linalg.qr(A)
    phases = np.diag(R)
    phases = np.where(np.abs(phases) > 0, phases/np.abs(phases), 1)
    U = Q @ np.diag(np.conj(phases))

    for p in (0.01, 0.2, 0.7):
        lhs = depol(U@rho@U.conj().T, p)
        rhs = U@depol(rho, p)@U.conj().T
        assert np.allclose(lhs, rhs, atol=1e-12)

    twirl = sum(P@rho@P.conj().T for P in PAULIS)/4
    assert np.allclose(twirl, I/2, atol=1e-12)

    p = 0.2
    corrected = sum(P.conj().T@depol(P@rho@P.conj().T, p)@P for P in PAULIS)/4
    assert np.allclose(corrected, depol(rho, p), atol=1e-12)

    kappa = 0.37
    s, t = 0.41, 0.73
    assert np.allclose(dsem(dsem(rho, kappa, s), kappa, t),
                       dsem(rho, kappa, s+t), atol=1e-12)

p, gamma = 0.2, 1.7
vals = [p*math.exp(-gamma/f) for f in (1e3, 1e5, 1e7)]
assert abs(vals[-1] - p) < 1e-7
assert vals[0] < vals[1] < vals[2] < p
print("VERIFY_OK")
