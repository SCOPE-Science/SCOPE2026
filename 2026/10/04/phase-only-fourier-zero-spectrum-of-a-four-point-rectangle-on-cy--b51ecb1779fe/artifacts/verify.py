#!/usr/bin/env python3
import cmath
import math

TOL = 2e-9

def dft_zero_count(m, n, coeffs):
    a, b, c, d = coeffs
    count = 0
    for k in range(m):
        z = cmath.exp(-2j * math.pi * k / m)
        for ell in range(n):
            w = cmath.exp(-2j * math.pi * ell / n)
            value = a + b*z + c*w + d*z*w
            if abs(value) < TOL:
                count += 1
    return count

def assert_unimodular(coeffs):
    for x in coeffs:
        assert abs(abs(x) - 1.0) < 1e-12

pairs = 0
checks = 0
for m in range(2, 41):
    for n in range(2, 41):
        pairs += 1
        um = cmath.exp(1j * math.pi / (2*m))
        un = cmath.exp(1j * math.pi / (2*n))
        tests = [
            ((1, um, un, um*un), 0),
            ((1, -1, un, -un), n),
            ((1, um, -1, -um), m),
            ((1, -1, -1, 1), m+n-1),
            ((1, 1j, -1j, -1), 2 if (m % 2 == 0 and n % 2 == 0) else 1),
        ]
        for coeffs, expected in tests:
            assert_unimodular(coeffs)
            got = dft_zero_count(m, n, coeffs)
            assert got == expected, (m, n, coeffs, expected, got)
            checks += 1

# Deterministic continuous-torus identity checks for nonfactorable cross phases.
torus_checks = 0
for j in range(1, 80):
    theta = 2 * math.pi * (j + 0.37) / 83
    eta = cmath.exp(1j * theta)
    if abs(eta - 1) < 1e-8:
        continue
    s = cmath.exp(-0.5j * theta)
    for Z, W in ((s, -s), (-s, s)):
        value = 1 + Z + W + eta*Z*W
        assert abs(value) < 1e-10
        assert abs(abs(Z)-1) < 1e-12 and abs(abs(W)-1) < 1e-12
        torus_checks += 1

print(f"VERIFY_OK pairs={pairs} witness_checks={checks} torus_checks={torus_checks}")
