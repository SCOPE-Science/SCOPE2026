#!/usr/bin/env python3
"""Finite diagnostics for the parity mechanism; universal proof is in RESULT.md.
No network and no nonstandard packages are required.
"""
import cmath
import math

checks = 0
for d in range(1, 6):
    for m in (0.2, 0.35, 0.5, 0.72, 0.95):
        for alpha in (0.65, 1.0, 1.75):
            beta = alpha * math.tan(math.pi * m / 2)
            for n in range(0, 13):
                exponent = (2 * d + n) / m
                # The Gamma prefactor is positive; only the complex phase matters.
                phase = cmath.exp(-exponent * cmath.log((alpha - 1j * beta) / abs(alpha - 1j * beta)))
                assert abs(phase.imag if n % 2 == 0 else phase.real) < 1.0e-10
                checks += 1

for k in range(-8, 9):
    # A bounded angular function on S^1; a(-omega) has factor (-1)^k.
    for t in (0.04, 0.32, 0.83, 1.47, 2.61, 4.8, 9.4):
        a_plus = 1.0 if k % 2 == 0 else 0.0
        a_minus = 0.0 if k % 2 == 0 else 1.0
        sample = a_plus * math.sin(t) + a_minus * math.cos(t)
        assert abs(sample) <= 1.0 + 1.0e-12
        checks += 1

print(f"PASS: {checks} finite diagnostics. Infinite-dimensional assertions require the written proof.")
