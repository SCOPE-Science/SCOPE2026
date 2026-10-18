#!/usr/bin/env python3
"""Independent finite-matrix checks for flux estimation on a uniform magnetic cycle.

Requires numpy and scipy. Finite-dimensional numerical corroboration does not prove
any all-size or zero-time-asymptotic statement.
"""
import math
import numpy as np
from scipy.linalg import expm

checks = 0

def check(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)


def data(n, phi, t, J=1.0):
    shift = np.zeros((n, n), dtype=complex)
    for j in range(n):
        shift[(j + 1) % n, j] = 1
    u = np.exp(1j * phi / n)
    H = J * (u * shift + u.conjugate() * shift.conj().T)
    Hp = (1j * J / n) * (u * shift - u.conjugate() * shift.conj().T)
    initial = np.eye(n, dtype=complex)[:, 0]
    psi = expm(-1j * t * H) @ initial
    dpsi = -1j * t * (Hp @ psi)
    p = np.abs(psi) ** 2
    dp = 2 * np.real(dpsi * np.conjugate(psi))
    classical = sum(float(dp[k] ** 2 / p[k]) for k in range(n) if p[k] > 1e-25)
    quantum = 4 * (np.vdot(dpsi, dpsi).real - abs(np.vdot(psi, dpsi)) ** 2)
    return H, Hp, psi, p, dp, classical, quantum


def asymptotic(n, phi, t, J=1.0):
    x = J * t
    if n % 2 == 0:
        return 4 * (x ** n) * (math.sin(phi / 2) ** 2) / math.factorial(n // 2) ** 2
    return 8 * (x ** (n + 1)) * (math.cos(phi) ** 2) / math.factorial((n + 1) // 2) ** 2

for n in range(3, 11):
    for phi in (0.17, 0.61, 1.15, 2.4):
        for t in (0.10, 0.18, 0.36, 0.91):
            H, Hp, psi, p, dp, FI, QFI = data(n, phi, t)
            check(abs(sum(p) - 1) < 2e-12, 'probability normalization')
            check(abs(sum(dp)) < 3e-12, 'score normalization')
            check(abs(QFI - 8 * t * t / (n * n)) < 3e-12, 'exact quantum information')
            check(FI <= QFI + 2e-10, 'classical/quantum ordering')
            if t == 0.91:
                # Independent diagonalization of the Hermitian generator.
                lam, v = np.linalg.eigh(H)
                independent = (v * np.exp(-1j * t * lam)) @ v.conj().T[:, 0]
                check(np.linalg.norm(psi - independent) < 2e-12, 'spectral versus exponential')
                h = 1e-5
                plus = data(n, phi+h, t)[3]
                minus = data(n, phi-h, t)[3]
                check(np.max(np.abs(dp - (plus-minus)/(2*h))) < 2e-8, 'derivative versus finite difference')
        # Asymptotic formula including the exact leading constant.
        t = 0.14
        FI = data(n, phi, t)[5]
        leading = asymptotic(n, phi, t)
        check(abs(FI/leading - 1) < 0.04, 'nonzero first information coefficient')

for n in range(3, 12):
    blinded = [0.0, math.pi] if n % 2 == 0 else [math.pi / 2, 3 * math.pi / 2]
    for phi in blinded:
        for t in (0.23, 0.77, 1.63):
            _, _, _, p, dp, FI, QFI = data(n, phi, t)
            check(np.max(np.abs(dp)) < 3e-12, 'exact symmetry point')
            check(FI < 3e-18, 'zero score information at symmetry point')
            check(QFI > 0, 'pure-state model still changes in fixed gauge')

# The two farthest sites on odd cycles, and the antipode on even cycles,
# contribute the asserted asymptotic classical-information constants.
for n in range(3, 10):
    phi = .76
    t = .125
    _, _, _, p, dp, FI, _ = data(n, phi, t)
    indices = [n//2] if n % 2 == 0 else [n//2, n-n//2]
    far_info = sum(float(dp[k]**2 / p[k]) for k in indices)
    leading = asymptotic(n, phi, t)
    check(abs(far_info/leading - 1) < .04, 'farthest-vertex leading coefficient')
    check(abs((FI-far_info)/leading) < .04, 'other vertices are higher order')

print(f'VERIFY_OK {checks} finite probability, Fisher, symmetry and leading-coefficient checks')
