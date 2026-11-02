"""Finite consistency checks for two-circle rational-angle polynomial examples.

The analytic proof, not these sampled evaluations, establishes the theorem.
Run: python3 CHECK.py
"""
import cmath
import math

assertions = 0
max_rel_error = 0.0
for q in range(2, 10):
    theta = math.pi / q
    delta = 2.0 * math.sin(theta / 2.0)
    a = complex(delta / 2.0, math.sqrt(1.0 - delta * delta / 4.0))
    b = a.conjugate()
    z0 = -1.0 + 0j
    w0 = (z0 - a) / (z0 - b)
    gamma = (w0.conjugate() / abs(w0)) ** q
    for center in (0.0, delta):
        for j in range(721):
            phi = 2.0 * math.pi * j / 721
            z = center + complex(math.cos(phi), math.sin(phi))
            za = gamma * (z - a) ** q
            zb = 1j * (z - b) ** q
            P, Q = za + zb, za - zb
            error = abs(abs(P) ** 2 - abs(Q) ** 2) / (1.0 + abs(P) ** 2 + abs(Q) ** 2)
            max_rel_error = max(max_rel_error, error)
            assert error < 1e-10, (q, j, center, error)
            assertions += 1
    # Nonproportionality: the quotients at the distinct intersection points are opposite.
    Pa, Qa = 1j * (a-b)**q, -1j * (a-b)**q
    Pb, Qb = gamma * (b-a)**q, gamma * (b-a)**q
    assert abs(Pa / Qa - Pb / Qb) > 1.0
    assertions += 1
print(f"PASS: {assertions} numerical consistency assertions; max relative error {max_rel_error:.3e}")
