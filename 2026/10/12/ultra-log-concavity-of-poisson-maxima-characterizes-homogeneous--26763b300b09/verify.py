"""Exact diagnostic checks for finite heterogeneous-Poisson maxima.

The accompanying analytic argument, not finite testing, proves the theorem.
Requires only the Python 3 standard library.
"""
from fractions import Fraction
from math import factorial


def truncated_exp(rate: int, k: int) -> Fraction:
    if k < 0:
        return Fraction(0)
    return sum((Fraction(rate**j, factorial(j)) for j in range(k + 1)), Fraction(0))


def scaled_mass(rates: tuple[int, ...], k: int) -> Fraction:
    # P(M=k) = exp(-sum(rates)) * scaled_mass(rates,k).
    def product_cdf(x):
        v = Fraction(1)
        for rate in rates:
            v *= truncated_exp(rate, x)
        return v
    return product_cdf(k) - product_cdf(k - 1)


def scaled_ulc_defect(rates: tuple[int, ...], k: int) -> Fraction:
    # True ULC defect equals exp(-2 sum(rates)) times this rational.
    f0 = scaled_mass(rates, k)
    return k * f0 * f0 - (k + 1) * scaled_mass(rates, k - 1) * scaled_mass(rates, k + 1)


def main():
    first_failures = {
        (1, 2): 4,
        (1, 1, 2): 5,
        (1, 2, 2): 8,
        (1, 2, 3): 6,
        (1, 1, 2, 2): 7,
    }
    for rates, first in first_failures.items():
        for k in range(1, first):
            assert scaled_ulc_defect(rates, k) >= 0, (rates, k)
        assert scaled_ulc_defect(rates, first) < 0, (rates, first)
    assert scaled_ulc_defect((1, 2), 4) == Fraction(-17, 360)
    for rates in [(1, 1), (1, 1, 1), (2, 2, 2), (1, 1, 1, 1)]:
        for k in range(1, 24):
            assert scaled_ulc_defect(rates, k) >= 0, (rates, k)
    print("PASS: exact-rational ULC diagnostics for five heterogeneous and four homogeneous models")
    print("PASS: first heterogeneous (1,2) failure at k=4, rational defect -17/360")
    print("LIMIT: finite diagnostics do not prove the classification or eventual strictness")


if __name__ == "__main__":
    main()
