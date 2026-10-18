"""Exact moment checks for radial means of Cartesian simplex products.

Run using Python 3.11 or later; no third-party packages required.
"""
from fractions import Fraction
from math import exp, log, log1p
from random import Random


def covariance_coefficients(dims, scales):
    coefficients = [Fraction(1)]
    for degree, scale in zip(dims, scales):
        for _ in range(degree):
            new = [Fraction(0)] * (len(coefficients) + 1)
            for j, coefficient in enumerate(coefficients):
                new[j] += coefficient
                new[j + 1] -= scale * coefficient
            coefficients = new
    return coefficients


def moment_from_polynomial(dims, scales, p):
    coefficients = covariance_coefficients(dims, scales)
    return sum((-j * coefficients[j] / (p + j) for j in range(1, len(coefficients))), Fraction(0))


def beta_moment(d, p):
    result = Fraction(1)
    for j in range(1, d + 1):
        result *= Fraction(j, 1) / (p + j)
    return result


def logarithmic_moment(dims, scales):
    coefficients = covariance_coefficients(dims, scales)
    return sum((coefficients[j] / j for j in range(1, len(coefficients))), Fraction(0))


def harmonic(d):
    return sum((Fraction(1, j) for j in range(1, d + 1)), Fraction(0))


def log_anisotropy(d_small, d_total, p):
    if p == 0:
        return float(harmonic(d_total) - harmonic(d_small))
    return sum(log1p(p / j) for j in range(d_small + 1, d_total + 1)) / p


def critical_profile(lam):
    if lam == 0:
        return log(2)
    return ((2+lam)*log(2+lam) - (1+lam)*log(1+lam) - 2*log(2)) / lam


def main():
    rng = Random(41237)
    p_values = [Fraction(-3, 4), Fraction(-1, 2), Fraction(1, 3), Fraction(1), Fraction(2), Fraction(5)]
    tests = 0
    for dims in ((1, 1), (2, 3), (2, 4, 1), (3, 3), (1, 2, 3)):
        total = sum(dims)
        smallest = min(dims)
        for p in p_values:
            equal = moment_from_polynomial(dims, [Fraction(1)]*len(dims), p)
            assert equal == beta_moment(total, p), (dims,p,equal)
            for i, degree in enumerate(dims):
                if degree != smallest:
                    continue
                scales = [Fraction(0)]*len(dims)
                scales[i] = Fraction(1)
                assert moment_from_polynomial(dims, scales, p) == beta_moment(smallest,p)
            tests += 1
        assert logarithmic_moment(dims, [Fraction(1)]*len(dims)) == -harmonic(total)
        for _ in range(120):
            scales = [Fraction(rng.randint(0,12),12) for _ in dims]
            scales[rng.randrange(len(dims))] = Fraction(1)
            for p in p_values:
                moment = moment_from_polynomial(dims, scales, p)
                lo, hi = beta_moment(total, p), beta_moment(smallest, p)
                if p > 0:
                    assert lo <= moment <= hi, (dims, scales, p, lo, moment, hi)
                else:
                    assert lo >= moment >= hi, (dims, scales, p, lo, moment, hi)
                tests += 1
            ln = logarithmic_moment(dims, scales)
            assert -harmonic(total) <= ln <= -harmonic(smallest)
            tests += 1
    for m,d in ((1,2),(2,5),(3,9),(10,20)):
        pp = [-0.9, -0.5, 0, 0.2, 1, 3, 20, 500]
        values = [log_anisotropy(m,d,p) for p in pp]
        assert all(a>b for a,b in zip(values,values[1:])), (m,d,values)
        assert abs(exp(log_anisotropy(m,d,-0.999999)) - d/m) < 1e-5
    for lam in (0.25, 1.0, 3.0):
        n=12000
        got=log_anisotropy(n,2*n,lam*n)
        expected=critical_profile(lam)
        assert abs(got - expected) < 0.00004, (lam,got,expected)
    for p in (Fraction(-1,2), Fraction(0),Fraction(3),Fraction(20)):
        val=log_anisotropy(12000,24000,float(p))
        assert abs(val-log(2))<0.002, (p,val)
    print('PASS: exact beta endpoints, rational moment sandwich, p=0 bounds, monotonicity and critical scaling; cases:',tests)

if __name__ == '__main__':
    main()
