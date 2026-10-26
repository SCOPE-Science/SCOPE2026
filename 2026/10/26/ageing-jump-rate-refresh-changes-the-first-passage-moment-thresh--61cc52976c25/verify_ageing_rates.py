#!/usr/bin/env python3
"""Standalone numerical and exact-parameter checks for ageing-rate first passage.

Python standard library only. Finite quadratures check the analytic spectral formula;
the asymptotic theorem requires the separate proof, not numerical extrapolation.
"""
from fractions import Fraction
from math import cos, sin, pi, log, log1p, exp, sqrt, gamma


def exponents(alpha, beta, delta):
    power = (1 + alpha * beta) / (2 * alpha * (1 + beta))
    slow = delta * (power - Fraction(1, 2))
    return power, slow


def integral_survival_one(alpha, beta, delta, n, mesh=4000):
    """P(T>t_n), x0=1, from an exact nonnegative spectral integral."""
    assert mesh % 2 == 0
    lengths = [(j ** float(beta)) * log(2.718281828459045 * j) ** float(delta)
               for j in range(1, n + 1)]
    powers = [u ** float(alpha) for u in lengths]
    scale = sum(powers) ** (1.0 / float(alpha))

    def at(y):
        theta = pi * y**4
        q = 2.0 * sin(theta / 2.0)**2
        z = q ** float(alpha)
        return 4.0 * y**3 * (1.0 + cos(theta)) * exp(-sum(log1p(z * w) for w in powers))

    h = 1.0 / mesh
    total = at(0) + at(1)
    for i in range(1, mesh):
        total += (4 if i % 2 else 2) * at(i*h)
    survival = total * h / 3.0
    coefficient = sqrt(2.0) * gamma(1.0/(2.0*float(alpha))) / (float(alpha)*pi)
    return survival, scale, survival * sqrt(scale) / coefficient


def main():
    expected = [
        (Fraction(1,3), Fraction(1), Fraction(-3), Fraction(1), Fraction(-3,2), True),
        (Fraction(1,3), Fraction(1), Fraction(-2), Fraction(1), Fraction(-1), False),
        (Fraction(2,5), Fraction(0), Fraction(0), Fraction(5,4), Fraction(0), True),
        (Fraction(2,5), Fraction(1), Fraction(0), Fraction(7,8), Fraction(0), False),
        (Fraction(1), Fraction(1), Fraction(-5), Fraction(1,2), Fraction(0), False),
    ]
    for a,b,d,claimed_power,claimed_log,mean_finite in expected:
        power, slow = exponents(a,b,d)
        assert (power,slow) == (claimed_power,claimed_log)
        assert ((power > 1) or (power == 1 and slow < -1)) == mean_finite

    cases = [(Fraction(2,5),0,0,200), (Fraction(2,5),1,0,200),
             (Fraction(1,3),1,-3,300), (Fraction(1,3),1,-2,300)]
    for a,b,d,n in cases:
        survival, scale, ratio = integral_survival_one(a,b,d,n)
        assert 0 < survival < 1, (a,b,d,n,survival)
        assert abs(ratio - 1.0) < 0.035, (a,b,d,n,ratio)
        print(f"alpha={a} beta={b} delta={d} n={n} survival={survival:.12g} "
              f"normalization={scale:.9g} ratio_to_stable_limit={ratio:.8f}")
    print('CHECK_OK exact_parameter_cases=5 spectral_quadratures=4')

if __name__ == '__main__':
    main()
