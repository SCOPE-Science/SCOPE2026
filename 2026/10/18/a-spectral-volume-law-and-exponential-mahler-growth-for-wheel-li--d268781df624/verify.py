"""Exact finite-dimensional checks for the wheel Lipschitz-polar volume theorem.

Requires Python 3, numpy, and sympy. No external documents or data files.
The analytic infinite-dimensional spectral argument is in RESULT.md, not this checker.
"""
from fractions import Fraction
from math import comb, factorial
import numpy as np
import sympy as sy


def integer_lattice_points(m, dilation):
    """Independently count lattice points of dilated wheel polar via a finite transfer matrix."""
    k = dilation
    size = 2*k + 1
    transition = np.array([[int(abs(i-j) <= k) for j in range(size)]
                           for i in range(size)], dtype=object)
    power = np.linalg.matrix_power(transition, m)
    return sum(int(power[i, i]) for i in range(size))


def ehrhart_volume(m):
    """Leading coefficient of integral m-polytope's Ehrhart polynomial, by differences."""
    top_diff = sum((-1)**(m-j)*comb(m, j)*integer_lattice_points(m, j)
                   for j in range(m+1))
    return Fraction(top_diff, factorial(m))


def from_closed_generating_function(max_m):
    z = sy.symbols('z')
    tangent = sy.tan(z/2)
    generating = (tangent/z)*(5/(1-3*tangent)+1/(1-tangent))
    truncation = sy.series(generating, z, 0, max_m-1).removeO().expand()
    return [Fraction(sy.Rational(truncation.coeff(z, m-2)))
            for m in range(2, max_m+1)]


def known_primal_normalized_volume(m):
    root3 = sy.sqrt(3)
    return int(sy.expand((1+root3)**m+(1-root3)**m-(2 if m%2==0 else 0)))


def main():
    max_m = 8
    coefficients = from_closed_generating_function(max_m)
    for m in range(3, max_m+1):
        volume_from_lattice = ehrhart_volume(m)
        volume_from_spectrum = coefficients[m-2]
        assert volume_from_lattice == volume_from_spectrum, (m, volume_from_lattice,
                                                              volume_from_spectrum)
        positive_integer = known_primal_normalized_volume(m)
        assert positive_integer > 0
        normalized_mahler = Fraction(positive_integer, 4**m)*volume_from_spectrum
        assert normalized_mahler > 1
        print(f'm={m} exact polar volume={volume_from_lattice}; '
              f'normalized Mahler product={normalized_mahler}; PASS')
    assert coefficients[0] == 3  # Formal trace-square value; no two-vertex wheel is claimed.
    print('ALL SIX INDEPENDENT EHRHART-VOLUME / SPECTRAL-COEFFICIENT CHECKS PASSED')


if __name__ == '__main__':
    main()
