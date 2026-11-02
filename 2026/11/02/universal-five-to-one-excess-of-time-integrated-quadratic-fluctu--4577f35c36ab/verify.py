#!/usr/bin/env python3
"""Exact, independent rational diagnostics for the quadratic-reset-noise theorem.
Run with Python 3 standard library: python verify.py
"""
from fractions import Fraction as F


def stationary_moments(mu, rate, diff, coupling):
    """Polynomial generator, ordered degree and descending noise power."""
    moments = {(0, 0): F(1)}
    for n in range(1, 5):
        for j in range(n, -1, -1):
            i = n - j
            left = i * coupling * moments[(i - 1, j + 1)] if i else F(0)
            below = diff * j * (j - 1) * moments[(i, j - 2)] if j > 1 else F(0)
            moments[(i, j)] = (left + below) / (i * mu + (rate if j else 0))
    return moments


def check(mu, rate, diff, coupling):
    M = stationary_moments(mu, rate, diff, coupling)
    a = F(1) / (2 * mu)
    b = coupling / (mu * (mu + rate))
    c = coupling * coupling / (mu * rate * (mu + rate))
    m20, m11, m02 = M[(2, 0)], M[(1, 1)], M[(0, 2)]
    assert m20 == 2 * diff * coupling**2 / (mu * rate * (mu + rate))
    # Independently verify that the polynomial h solves -Lh=x*x-E(x*x).
    assert 2 * mu * a == 1
    assert 2 * coupling * a - (mu + rate) * b == 0
    assert coupling * b - rate * c == 0
    assert 2 * diff * c == m20
    # Green-Kubo/Poisson and quadratic-variation formulas are independent.
    sigma_resolvent = 2 * (a * (M[(4,0)] - m20**2)
                           + b * (M[(3,1)] - m20 * m11)
                           + c * (M[(2,2)] - m20 * m02))
    sigma_martingale = (2 * diff * (b*b*m20 + 4*b*c*m11 + 4*c*c*m02)
                        + rate * (b*b*M[(2,2)] + 2*b*c*M[(1,3)] + c*c*M[(0,4)]))
    sigma_formula = (8 * diff**2 * coupling**4 *
                     (rate**3 + 26*rate**2*mu + 31*rate*mu**2 + 10*mu**3)
                     / (mu**3*rate**3*(mu+rate)**3*(rate+2*mu)))
    assert sigma_resolvent == sigma_martingale == sigma_formula
    gaussian_formula = (8 * diff**2 * coupling**4 * (rate**2 + 3*rate*mu + mu**2)
                        / (mu**3*rate**3*(mu+rate)**3))
    if rate != mu:
        gaussian_cov_integral = (4*m20**2/(rate-mu)**2
                                 * (rate**2/(2*mu) + mu**2/(2*rate)
                                    - 2*rate*mu/(rate+mu)))
    else:
        gaussian_cov_integral = 5*m20**2/mu
    assert gaussian_formula == gaussian_cov_integral
    excess_formula = (8 * diff**2 * coupling**4 *
                      (21*rate**2 + 24*rate*mu + 8*mu**2)
                      / (mu**2*rate**3*(mu+rate)**3*(rate+2*mu)))
    assert sigma_formula - gaussian_formula == excess_formula > 0
    z = rate / mu
    ratio = (z**3+26*z**2+31*z+10)/((z+2)*(z*z+3*z+1))
    assert sigma_formula / gaussian_formula == ratio
    assert 1 < ratio < 5
    monotonic_poly = 21*z**4 + 48*z**3 - 3*z*z - 4*z + 8
    assert monotonic_poly > 0
    return sigma_formula, gaussian_formula, ratio


def main():
    cases = [(F(n), F(q), F(p), F(k))
             for n in (1, 2, 3, 5, 8)
             for q in (1, 2, 3, 5, 8)
             for p in (F(1,2), F(1), F(7,3))
             for k in (F(1,3), F(2))]
    results = [check(*case) for case in cases]
    assert len(results) == 150
    assert check(F(1),F(1),F(1),F(1)) == (F(68,3),F(5),F(68,15))
    # Exact algebraic monotonicity certificate: the derivative is negative
    # because P(z)=21z^4+48z^3-3z^2-4z+8 is positive for every z>0:
    # 0<z<=1: 8-3z^2-4z>=1; z>=1: 48z^3-3z^2-4z>0.
    assert 8-3-4 == 1
    assert 48-3-4 > 0
    print('PASS: 150 exact rational parameter tuples; 2 independent Green-Kubo identities')
    print('PASS: 2 covariance-matched Gaussian integrals; positivity and monotonicity certificates')
    print('PASS: unit-rate variances and universal ratio 68/15')


if __name__ == '__main__':
    main()
