#!/usr/bin/env python3
"""Supplementary direct finite Fourier checks for quadratic-residue phase multipliers.

The checks are floating-point consistency checks, not an infinite proof.
"""
import cmath
import math


def primes_under(n):
    out = []
    for p in range(3, n):
        if all(p % d for d in range(2, math.isqrt(p) + 1)):
            out.append(p)
    return out


def fourier_kernel(p, theta):
    qr = {pow(t, 2, p) for t in range(1, p)}
    mult = [0j] + [1+0j if xi in qr else cmath.exp(1j * theta) for xi in range(1, p)]
    return [sum(mult[j] * cmath.exp(2j * math.pi * x * j / p)
                for j in range(p)) / p for x in range(p)]


def analytic_norm(p, theta):
    c, s = abs(math.cos(theta / 2)), abs(math.sin(theta / 2))
    return (p - 1) / p * (c + (math.sqrt(c*c + p*s*s)
                                      if p % 4 == 1 else max(c, math.sqrt(p)*s)))


checks = 0
for p in primes_under(200):
    for theta in (0.0, math.pi / 9, math.pi / 3, 2 * math.pi / 3, math.pi,
                  -math.pi / 5, math.pi * 1.707):
        k = fourier_kernel(p, theta)
        direct = sum(abs(z) for z in k)
        expected = analytic_norm(p, theta)
        assert abs(direct - expected) < 3e-10, (p, theta, direct, expected)
        assert abs(sum(z.real*z.real + z.imag*z.imag for z in k)
                   - (p-1)/p) < 4e-10
        checks += 2
    if p % 4 == 1:
        theta = math.acos((3-p)/(p-1))
        best = math.sqrt(p-1)
        k = fourier_kernel(p, theta)
        assert abs(sum(abs(z) for z in k) - best) < 3e-10
        assert max(abs(abs(z) - best/p) for z in k) < 3e-10
        checks += 2
    else:
        phase = math.acos((1-p)/(1+p))
        target = (p-1)/p * max(2, math.sqrt(p+1))
        assert abs(analytic_norm(p, phase)-target) < 3e-10
        if p == 3:
            assert abs(analytic_norm(3, 0)-4/3) < 3e-10
        else:
            assert target < math.sqrt(p-1)
        checks += 2
# C5: spectral definition on positive eigenvalues, zero on constants.
small = (5 - math.sqrt(5))/2
large = (5 + math.sqrt(5))/2
h = math.log(large/small)
for gamma in (0.0, 0.1, -1.0, 2 * math.pi / (3*h), 4*math.pi/h):
    m = [0j, cmath.exp(1j * gamma * math.log(small)),
         cmath.exp(1j * gamma * math.log(large)),
         cmath.exp(1j * gamma * math.log(large)),
         cmath.exp(1j * gamma * math.log(small))]
    k = [sum(m[j] * cmath.exp(2j * math.pi * x * j / 5)
             for j in range(5))/5 for x in range(5)]
    x = math.cos(gamma*h)
    formula = (2/5) * (math.sqrt(2+2*x)+2*math.sqrt(3-2*x))
    assert abs(sum(abs(z) for z in k)-formula)<3e-10
    checks += 1
assert abs(analytic_norm(5, 0) - 8/5) < 3e-10
assert abs(analytic_norm(5, 2*math.pi/3) - 2) < 3e-10
checks += 2
print(f'CHECK_OK primes={len(primes_under(200))} comparisons={checks}')
