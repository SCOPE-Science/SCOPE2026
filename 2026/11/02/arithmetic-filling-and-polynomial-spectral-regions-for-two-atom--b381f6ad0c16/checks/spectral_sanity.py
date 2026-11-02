#!/usr/bin/env python3
"""Finite checks of simple semigroup and spectral-symbol identities; not a proof."""
import cmath
import math

checks = 0

def check(ok):
    global checks
    assert ok
    checks += 1

for u, v in [(0.35, 0.49), (0.2, 0.7), (0.4, 0.16)]:
    for n in range(1, 25):
        for z in [0j, 0.25 + 0.17j, -0.3 + 0.06j]:
            # Compose the affine maps z -> (1-t)+t*z.
            psi = lambda t, w: 1 - t + t * w
            check(abs(psi(u, psi(v, z)) - psi(u * v, z)) < 1e-12)
            check(abs(psi(v, psi(u, z)) - psi(u * v, z)) < 1e-12)
            a, b = 1.15, 0.78
            x = -n / 25.0
            y = 0.27 * n
            lam = x + 1j * y
            check(abs(a * u ** (-lam) + b * v ** (-lam)) <= a / u + b / v + 1e-12)

q = 0.45
a, b = 1.15, 0.78
M = a / q + b / q**2
for j in range(721):
    theta = 2 * math.pi * j / 720
    z = cmath.exp(1j * theta) / q
    w = a * z + b * z * z
    check(abs(w) <= M + 1e-10)
    if j == 360:
        check(abs(w + M) > 0.01)

print(f"{checks} finite consistency assertions passed; this does not certify the theorem.")
