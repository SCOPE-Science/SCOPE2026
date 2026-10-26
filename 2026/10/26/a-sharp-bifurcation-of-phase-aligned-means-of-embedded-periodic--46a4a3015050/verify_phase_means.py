"""Finite checks of exact phase-alignment identities for two-lobed periodic curves.

Requires Python 3 standard library only. Universal mathematical assertions
are derived analytically in RESULT.md, not certified by finite sampling.
"""
import cmath
import math
from fractions import Fraction


def corr(eps, k, theta):
    return math.cos(theta) * (1 - eps * eps * math.cos(k * theta) / 2)


def curve(sign, eps, k, theta):
    return (1 + sign * eps * math.cos(k * theta)) * cmath.exp(1j * theta)


def quadrature_corr(eps, k, phase, n=4096):
    acc = 0.0
    for j in range(n):
        t = 2 * math.pi * j / n
        acc += (curve(+1, eps, k, t) * curve(-1, eps, k, t + phase).conjugate()).real
    return acc / n


# Exact rational polynomial and zero-slope threshold identities.
for num, den in [(1, 10), (2, 5), (1, 2), (9, 10)]:
    a = Fraction(num, den)
    for x in [Fraction(0), Fraction(1, 4), Fraction(1, 2), Fraction(3, 4), Fraction(1)]:
        P = (1 + a / 2) * x - a * x ** 3
        assert P == x * (1 + a / 2 - a * x ** 2)
    assert Fraction(1) + a / 2 - 3 * a == 1 - 5 * a / 2
assert Fraction(1) - 5 * Fraction(2, 5) / 2 == 0
print('EXACT_TWO_LOBE_POLYNOMIAL_IDENTITIES_PASS 21')

count = 0
for k, eps in [(2, 0.2), (2, 0.8), (5, 0.6), (20, 0.09), (100, 0.02)]:
    for phase in [0.0, 0.2, 0.5, 1.2]:
        error = abs(quadrature_corr(eps, k, phase) - corr(eps, k, phase))
        assert error < 2e-12, (k, eps, phase, error)
        count += 1
print('FOURIER_CORRELATION_QUADRATURE_PASS', count)

for a in [0.1, 0.4, 0.5, 0.7, 0.95]:
    if a <= 0.4:
        optimum_phase = 0.0
        optimum = 1 - a / 2
    else:
        t = math.sqrt((2 + a) / (6 * a))
        optimum_phase = math.acos(t)
        optimum = 2 * a * t ** 3
        assert abs((1 + a / 2) - 3 * a * t ** 2) < 1e-14
    samples = [corr(math.sqrt(a), 2, 2 * math.pi * j / 8192) for j in range(8192)]
    assert 0 <= optimum - max(samples) < 3e-7, (a, optimum - max(samples))
    if a > 0.4:
        assert abs(corr(math.sqrt(a), 2, optimum_phase) - optimum) < 1e-14
print('TWO_LOBE_COMPLETE_PHASE_SCANS_PASS 5')

for k, eps in [(20, 0.09), (100, 0.02), (500, 0.005)]:
    assert 0 < eps < 1
    assert eps * eps > 2 / (k * k + 1)
    assert -1 + eps * eps * (k * k + 1) / 2 > 0
    theta = 0.25 / k
    assert corr(eps, k, theta) > corr(eps, k, 0)
print('HIGH_HARMONIC_LOCAL_MAXIMUM_OBSTRUCTION_PASS 3')

# Mode 1 fixes the putative identification phase; mode -1 contradicts it.
a = 0.7
eps = math.sqrt(a)
theta = math.acos(math.sqrt((2 + a) / (6 * a)))
c1_pos = (1 + cmath.exp(1j * theta)) / 2
c1_neg = (1 + cmath.exp(-1j * theta)) / 2
alpha = -theta
assert abs(c1_neg - c1_pos * cmath.exp(1j * alpha)) < 1e-14
cminus_pos = eps * (1 - cmath.exp(-1j * theta)) / 4
cminus_neg = eps * (1 - cmath.exp(1j * theta)) / 4
assert abs(cminus_neg - cminus_pos * cmath.exp(-1j * alpha)) > 1e-3
print('SUPERCRITICAL_MEANS_NOT_SHIFT_EQUIVALENT_PASS')
print('UNBOUNDED_CLASSIFICATION_AND_EXISTENCE_REQUIRE_ANALYTICAL_PROOF')
