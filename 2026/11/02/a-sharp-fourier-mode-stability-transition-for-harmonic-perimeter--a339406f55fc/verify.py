"""Supplementary finite checks for the harmonic perimeter Hessian.

Usage: python verify.py
Only Python's standard library is required. These finite checks do not
replace the analytic proof of the all-frequency statement.
"""
from fractions import Fraction
from math import pi, cos, sin
from cmath import exp


def multiplier(k, r):
    k = abs(k)
    if k == 0:
        return 1 if isinstance(r, int) else r*0+1
    if k == 1:
        return r
    return r**(k-2) * ((k+1)*r*r-(k-1))/2


def direct_perimeter(r, k, eps, n=1536, cutoff=25):
    # Independent discretization: Fourier coefficients of a genuine
    # boundary circle diffeomorphism, then Poisson extension, then arclength.
    samples = [exp(1j*(2*pi*j/n + eps*cos(k*2*pi*j/n))) for j in range(n)]
    coeff = {}
    for freq in range(-cutoff, cutoff+1):
        z = sum(samples[j]*exp(-2j*pi*freq*j/n) for j in range(n))/n
        coeff[freq] = z * (r**abs(freq)) * (1j*freq)
    total = 0.0
    for j in range(n):
        angle = 2*pi*j/n
        deriv = sum(coeff[freq]*exp(1j*freq*angle)
                    for freq in range(-cutoff, cutoff+1))
        total += abs(deriv)
    return 2*pi*total/n


def main():
    # Exact rational comparisons cover a finite sample of radii and modes.
    count = 0
    for r in [Fraction(1, 20), Fraction(1, 5), Fraction(1, 3),
              Fraction(1, 2), Fraction(3, 4), Fraction(99, 100)]:
        d2 = multiplier(2, r)
        bound = max(r*r, d2*d2)
        for k in range(3, 65):
            assert multiplier(k, r)**2 < r*r
            assert multiplier(k, r)**2 < bound
            count += 2
        if r < Fraction(1, 3):
            assert d2*d2 > r*r
        elif r > Fraction(1, 3):
            assert d2*d2 < r*r
        else:
            assert d2*d2 == r*r
        count += 1
    # Compare the quadratic coefficient to the full nonlinear perimeter.
    eps = 0.004
    for r in [0.15, 1/3, 0.72]:
        for k in [1, 2, 3, 5]:
            length = direct_perimeter(r, k, eps)
            numerical = (2*pi*r-length)/(pi*r*eps**2)
            prediction = (1-float(multiplier(k, r))**2)/2
            assert abs(numerical-prediction) < 0.00015, (r,k,numerical,prediction)
            count += 1
    print(f"HARMONIC_PERIMETER_CHECK_OK {count}")


if __name__ == "__main__":
    main()
