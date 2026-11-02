"""Reproducible finite checks for the anisotropic Bergman companion theorem.

Uses only the Python standard library. Tests exact monomial norms and
matrix shift coefficients plus illustrative finite Schatten sums.
Finite tests do not certify the asymptotic theorem.
"""
from fractions import Fraction
from math import factorial, exp, gamma, log


def bergman_norm_sq(u, v):
    # Normalized volume of the complex unit ball in dimension two.
    return Fraction(2 * factorial(u) * factorial(v), factorial(u + v + 2))


def shift_coefficient_sq(u, v, k, r1, r2):
    m = u + v
    if m == 0:
        return Fraction(0)
    # The integral of t**(m+k-1) from 0 to 1 is 1/(m+k).
    raw_coefficient = r1**u * r2**v * Fraction(m, m + k)
    return raw_coefficient**2 * bergman_norm_sq(u, v + k) / bergman_norm_sq(u, v)


def rising_formula_sq(u, v, k, r1, r2):
    m = u + v
    if m == 0:
        return Fraction(0)
    ratio = Fraction(1)
    for j in range(1, k + 1):
        ratio *= Fraction(v + j, m + 2 + j)
    return (r1**(2*u) * r2**(2*v) * Fraction(m*m, (m+k)*(m+k)) * ratio)


assert bergman_norm_sq(0, 0) == 1
checks = 0
rational_radii = [(Fraction(1, 2), Fraction(3, 5)),
                  (Fraction(5, 7), Fraction(7, 9)),
                  (Fraction(9, 10), Fraction(4, 5))]
for k in range(1, 7):
    for u in range(0, 22):
        for v in range(0, 22):
            for r1, r2 in rational_radii:
                a = shift_coefficient_sq(u, v, k, r1, r2)
                b = rising_formula_sq(u, v, k, r1, r2)
                assert a == b, (u, v, k, r1, r2)
                checks += 1
print('EXACT_MONOMIAL_AND_SHIFT_CHECK_OK', checks)


def finite_schatten_power(epsilon, a, k, p, u_max=1500, v_max=500):
    # Explicit finite partial sum, not a limit certificate.
    delta = epsilon**a
    result = 0.0
    for v in range(v_max + 1):
        fac_v = exp(-p * delta * v)
        for u in range(u_max + 1):
            m = u + v
            if m == 0:
                continue
            ratio = 1.0
            for j in range(1, k+1):
                ratio *= (v+j)/(m+2+j)
            w = m/(m+k) * (ratio**0.5)
            result += exp(-p*epsilon*u)*fac_v*(w**p)
    return result

# Illustrative computational check: all values finite and below or equal to
# the infinite sums. A separate analytic argument proves the asymptotics.
for k, p in [(1, 1.0), (2, 1.0), (4, 1.0)]:
    q = k*p/2
    a = 0.5
    for eps in (0.04, 0.02):
        finite = finite_schatten_power(eps, a, k, p)
        assert finite > 0
        assert finite == finite and finite != float('inf')
        if q < 1:
            predicted_constant = gamma(1-q)*gamma(1+q)/(p*p)
            exponent = 1+a-(1-a)*q
            scaled = finite*eps**exponent
        elif q == 1:
            predicted_constant = (1-a)/(p*p)
            scaled = finite*eps**(2*a)/log(1/eps)
        else:
            predicted_constant = 1/(p*p*(q-1))
            scaled = finite*eps**(2*a)
        print('FINITE_PARTIAL_SUM', k, p, eps, round(scaled, 7),
              'asymptotic_constant', round(predicted_constant, 7))
print('FINITE_PARTIAL_SUM_CHECK_OK')
