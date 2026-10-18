"""Exact character accounting and independent numerical diagnostics for a smooth doubling perturbation."""
from collections import defaultdict
from fractions import Fraction
from math import sin, cos, pi, log


def cosine_sum_coefficients(n, harmonic):
    modulus = (1 << n) - 1
    coeff = defaultdict(Fraction)
    for j in range(n):
        frequency = (harmonic * (1 << j)) % modulus
        coeff[frequency] += Fraction(1, 2)
        coeff[(-frequency) % modulus] += Fraction(1, 2)
    return coeff


def mean_product(a, b, modulus):
    return sum((val * b.get((-freq) % modulus, Fraction(0))
                for freq, val in a.items()), Fraction(0))


def periodic_exponents(n, epsilon):
    modulus = (1 << n) - 1
    result = []
    for k in range(modulus):
        x = k / modulus
        for _ in range(12):
            y = x
            d = 1.0
            for _ in range(n):
                u_prime = 4 * pi * (cos(4 * pi * y) - cos(2 * pi * y))
                d *= 2 + epsilon * u_prime
                y = 2 * y + epsilon * (sin(4 * pi * y) - 2 * sin(2 * pi * y))
            correction = (y - x - k) / (d - 1)
            x -= correction
            if abs(correction) < 2e-15:
                break
        y = x
        ell = 0.0
        for _ in range(n):
            ell += log(2 + epsilon * 4 * pi * (cos(4 * pi * y) - cos(2 * pi * y)))
            y = 2 * y + epsilon * (sin(4 * pi * y) - 2 * sin(2 * pi * y))
        result.append(ell / n)
    return result


def check():
    for n in range(5, 21):
        m = (1 << n) - 1
        a = cosine_sum_coefficients(n, 1)
        b = cosine_sum_coefficients(n, 3)
        assert a.get(0, Fraction()) == b.get(0, Fraction()) == 0
        assert mean_product(a, a, m) == Fraction(n, 2), (n, 'first self')
        assert mean_product(b, b, m) == Fraction(n, 2), (n, 'third self')
        assert mean_product(a, b, m) == 0, (n, 'mixed')
        # Exact variance after extracting the common factor 6*pi*pi/n.
        diff = {j: b.get(j, Fraction()) - a.get(j, Fraction()) for j in set(a) | set(b)}
        assert mean_product(diff, diff, m) == n
    assert mean_product(cosine_sum_coefficients(4, 3),
                        cosine_sum_coefficients(4, 1), 15) == 0
    # Direct nonlinear implicit periodic-point solves, *not* a proof of the theorem.
    leading = 36 * pi ** 4
    for n in (5, 6, 7, 8):
        eps = 0.00075
        values = periodic_exponents(n, eps)
        mean = sum(values) / len(values)
        variance = sum((v - mean)**2 for v in values) / len(values)
        ratio = n * variance / (leading * eps ** 4)
        assert 0.985 < ratio < 1.015, (n, ratio)
    # Distinguish the exact low-period resonance at n=4.
    for n in (3, 4):
        m = (1 << n) - 1
        a = cosine_sum_coefficients(n, 1)
        b = cosine_sum_coefficients(n, 3)
        diff = {j: b.get(j, Fraction()) - a.get(j, Fraction()) for j in set(a) | set(b)}
        obs = mean_product(diff, diff, m)
        if n == 3:
            assert obs == 0
        if n == 4:
            assert obs == 6  # n*V_n coefficient is 54*pi**4
    print('CHECK_OK Fourier equalities n=5..20; nonlinear periodic orbits n=5..8; low-period exceptions n=3,4')


if __name__ == '__main__':
    check()
