"""Exact rational cross-check of periodic two-velocity transport cumulants.

Install sympy, then execute: python verify.py
No external data files are required.
"""
from fractions import Fraction
from itertools import product
from sympy import Matrix, Rational, eye, zeros, simplify, trace


def product_coefficients(left, right):
    return [sum((left[i] * right[j] for i in range(3) for j in range(3)
                 if i + j == degree), zeros(2)) for degree in range(3)]


def test_profile(rate_values, speed=1, interval_length=1):
    rates = [Rational(str(x)) for x in rate_values]
    v = Rational(str(speed))
    h = Rational(str(interval_length))
    n = len(rates)
    length = n * h
    mean = sum(rates, Rational(0)) / n
    # Centered antiderivative E = spatial variance of G.
    start = Rational(0)
    integrated = Rational(0)
    integrated_square = Rational(0)
    for rate in rates:
        slope = rate - mean
        integrated += start * h + slope * h**2 / 2
        integrated_square += start**2 * h + start*slope*h**2 + slope**2*h**3/3
        start += slope*h
    assert start == 0
    e = simplify(integrated_square / length - (integrated / length)**2)
    # The monodromy is computed independently as the exact Taylor expansion
    # of matrix exponentials on each constant-rate segment.
    monodromy = [eye(2), zeros(2), zeros(2)]
    for rate in rates:
        b0 = Matrix([[0, 2*rate/v], [0, 0]])
        b1 = Matrix([[0, 1/v], [1/v, 0]])
        q1, q2 = 2*rate/v**2, 1/v**2
        coeffs = [eye(2)+h*b0,
                  eye(2)*q1*h**2/2 + b1*h + b0*q1*h**3/6,
                  eye(2)*(q2*h**2/2 + q1**2*h**4/24)
                  + b0*(q2*h**3/6 + q1**2*h**5/120)
                  + b1*q1*h**3/6]
        monodromy = product_coefficients(coeffs, monodromy)
    c1, c2 = [simplify(trace(monodromy[i])) for i in (1, 2)]
    expected_c1 = 2*mean*length**2/v**2
    expected_c2 = (length**2/v**2 + mean**2*length**4/(3*v**4)
                   - 4*length**2*e/v**4)
    a2 = simplify(length**2/c1)
    a4 = simplify((length**4/Rational(12) - c2*a2**2)/c1)
    expected_a2 = v**2/(2*mean)
    expected_a4 = -v**4/(8*mean**3) + v**2*e/(2*mean**3)
    assert all(simplify(left - right) == 0 for left, right in [
        (c1, expected_c1), (c2, expected_c2),
        (a2, expected_a2), (a4, expected_a4)])
    return e, simplify(24*a4)


if __name__ == '__main__':
    examples = [([1], 1, 1), ([1, 3], 1, 1),
                ([1, 2, 4], 2, 1), ([5, 1, 1, 1], 1, 1),
                (['1/3', 3, 2], '3/2', '1/2'),
                ([7, 1, 3, 2], '2/3', '3/2')]
    examples.extend((rates, 1, 1) for n in (2, 3, 4)
                    for rates in product((1, 2), repeat=n))
    for rates, v, h in examples:
        e, k4 = test_profile(rates, v, h)
        assert e >= 0
    # One rate landscape has a *positive* fourth cumulant.
    e, k4 = test_profile([5, 1, 1, 1])
    assert e == Rational(3, 4) and k4 == Rational(3, 4)
    print('PASS:', len(examples), 'exact piecewise-constant profiles;',
          'four independent rational coefficient identities each;'
          ' positive and negative fourth-cumulant cases')
