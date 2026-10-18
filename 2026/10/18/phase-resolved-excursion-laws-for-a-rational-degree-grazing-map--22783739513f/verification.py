"""Finite checks for an exact phase-resolved first-return theorem.

Uses only the Python standard library.  The analytic theorem, including
convergence for arbitrary exponents, is not deduced from finite tests.
"""
from fractions import Fraction
from math import floor, log, sqrt


def rational_test(j, a, b):
    """Square-root model: nu=1/2, gamma=1/2, coefficient=1."""
    nu = Fraction(1, 2)
    mu = Fraction(1, 4**j)
    u = Fraction(a * a, b * b)
    assert 0 < u < Fraction(1, 2)
    z = 1 - u
    x0 = mu * z
    assert nu * mu <= x0 <= mu
    # Exact first nonlinear iterate; sqrt(mu*u)=a/(b*2**j).
    y = nu * x0 + Fraction(a, b * 2**j)
    assert y >= nu * mu
    t = 1
    iterate = y
    while iterate > mu:
        iterate = nu * iterate
        t += 1
        assert t < 4 * j + 20
    assert nu * mu <= iterate <= mu
    v = 0.5 * log(1 / float(u), 2)
    assert abs(v - round(v)) > 0.05  # avoid the null-set phase boundaries
    limiting_t = 1 - floor(v)
    limiting_r = 2 ** (-(v - floor(v)))
    assert t - j == limiting_t, (j, a, b, t - j, limiting_t)
    r_actual = float(iterate / mu)
    assert abs(r_actual - limiting_r) < 2.0 * 2**(-j)
    return t - j, r_actual


def finite_tail_probability(j):
    """Finite-j tail P(T-j>=1) via the exactly derived threshold."""
    eps = 2.0 ** (-j - 1)
    lo, hi = 0.0, 0.5
    for _ in range(100):
        mid = (lo + hi) / 2
        if sqrt(mid) + eps * (1.0 - mid) > 0.5:
            hi = mid
        else:
            lo = mid
    root = (lo + hi) / 2
    p = 1.0 - 2 * root
    first_order = 0.5 + 1.5 * eps
    assert abs(p - first_order) <= 2.0 * eps**2
    return p


def main():
    for j in (5, 8, 12):
        for a, b in ((1, 3), (2, 5), (3, 5)):
            rational_test(j, a, b)
        finite_tail_probability(j)

    # Exactly normalized limiting probabilities for nu=gamma=1/2, phase=0.
    # P(J=1)=1/2 and P(J=-k)=(3/8)4^{-k}, k>=0.
    assert Fraction(1, 2) + Fraction(3, 8) * Fraction(4, 3) == 1
    assert Fraction(1, 2) - Fraction(3, 8) * Fraction(4, 9) == Fraction(1, 3)
    # Density g(r)=(8/3)r on (1/2,1) integrates to one.
    assert Fraction(8, 3) * (1 - Fraction(1, 4)) / 2 == 1
    print('EXACT_GRAZING_RETURN_CHECK_OK')


if __name__ == '__main__':
    main()
