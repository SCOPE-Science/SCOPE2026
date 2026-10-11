"""Exact finite binomial identities for an Aluthge-iterate example.

The analytical convergence and divergence assertions are proved separately;
this script only checks finite coefficients, the interpolation construction,
and the stated concentration-bound arithmetic at sample indices.
"""
from fractions import Fraction
from math import comb, exp, log2


def sign(j):
    assert isinstance(j, int) and j >= 0
    return (-1) ** ((j + 1).bit_length() - 1)


def primitive(j):
    """Integer values of the 1-Lipschitz interpolant F."""
    return sum(sign(k) for k in range(j))


def binomial_exponent(n):
    numerator = sum(sign(j) * comb(n, j) for j in range(n + 1))
    return Fraction(numerator, 1 << n)


for j in range(64):
    assert primitive(j + 1) - primitive(j) == sign(j)
    assert abs(primitive(j)) <= j

# The coefficients for one or two steps follow the polar-decomposition formula.
assert binomial_exponent(0) == 1
assert binomial_exponent(1) == 0
assert binomial_exponent(2) == Fraction(-1, 2)

for ell in range(4, 10):
    n = 3 * 2**ell
    ex = binomial_exponent(n)
    desired = 1 if ell % 2 == 0 else -1
    # Direct exact evaluation exhibits the targeted parity regime.
    assert ex * desired > Fraction(9, 10)
    # The analytic proof uses Hoeffding's inequality at t=2**(ell-2).
    concentration_error_bound = 4 * exp(-2**ell / 24)
    assert abs(float(ex) - desired) <= concentration_error_bound + 1e-14

print('MONOMIAL_COMPOSITION_ALUTHGE_BINOMIAL_IDENTITIES_OK')
