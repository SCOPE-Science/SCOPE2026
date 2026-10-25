#!/usr/bin/env python3
"""Small exact-arithmetic checks for the orthotope section-radius lemma.
The proof of the asymptotic is analytic and is given in RESULT.md; these tests
check representative finite-dimensional edge-intersection identities only.
"""
from fractions import Fraction as F
from itertools import product
from math import gamma, pi, isclose, sqrt
import math


def max_section_vertex_radius_sq(a, u):
    """Maximum squared norm among generic hyperplane/box edge intersections."""
    n = len(a)
    best = None
    for i in range(n):
        js = [j for j in range(n) if j != i]
        if u[i] == 0:
            continue
        for signs in product((-1, 1), repeat=n - 1):
            numerator = sum((u[j] * a[j] * s for j, s in zip(js, signs)), F(0))
            if abs(numerator) <= a[i] * abs(u[i]):
                xi = -numerator / u[i]
                norm_sq = xi * xi + sum((a[j] * a[j] for j in js), F(0))
                if best is None or norm_sq > best:
                    best = norm_sq
    if best is None:
        raise AssertionError('no section vertices found')
    return best


def main():
    a = (F(3), F(2), F(1))
    r0_sq = sum(x*x for x in a[1:])
    gap = a[0]*a[0] - a[1]*a[1]
    # In the dominant-edge cone, the exact maximal radius is R0^2+(S/|u1|)^2.
    dominant = ((F(10), F(1), F(1)), (F(10), F(2), F(-1)), (F(17), F(-1), F(2)), (F(20), F(2), F(1)))
    for u in dominant:
        S = sum(a[j] * abs(u[j]) for j in range(1, 3))
        assert a[0]*abs(u[0]) > S
        got = max_section_vertex_radius_sq(a, u)
        expected = r0_sq + (S/abs(u[0]))**2
        assert got == expected, (u, got, expected)
    # Away from the dominant-edge cone, some non-long-axis edge crosses the plane;
    # its vertex radius is at least R0^2+(a1^2-a2^2).
    non_dominant = (F(1), F(2), F(4))
    S = sum(a[j] * abs(non_dominant[j]) for j in range(1, 3))
    assert S > a[0]*abs(non_dominant[0])
    got = max_section_vertex_radius_sq(a, non_dominant)
    assert got >= r0_sq + gap, (got, r0_sq + gap)
    # In dimension three the general leading coefficient reduces to R0/(pi*a2*a3).
    R0 = math.sqrt(float(r0_sq))
    general = (2**2 * gamma(1.5) * R0) / (2 * pi**1.5 * float(a[1]*a[2]))
    special = R0 / (pi * float(a[1]*a[2]))
    assert isclose(general, special, rel_tol=1e-14, abs_tol=1e-14)
    print('ORTHOTOPE_TAIL_CHECK_OK')
    print('dominant_edge_cases=4 exact_fraction_checks=passed')
    print('non_dominant_gap_check=passed')
    print('dimension_3_coefficient_reduction=passed')


if __name__ == '__main__':
    main()
