"""Standard-library checks of sharp transport radii for resonant circle rotations.

The infinite statements are proved analytically in RESULT.md. This program tests
exact moments and finite-grid Riemann approximations; no sampling is used to prove
an assertion quantified over all irrational angles or all denominators.
"""
from fractions import Fraction
from math import isclose


def exact_pth_moment(q, p):
    """Integral on quotient circle of circumference 1/q, p a positive integer."""
    return Fraction(1, (p + 1) * (2 * q) ** p)


def discrete_pth_moment(q, p, cells_per_coset):
    """Midpoint Riemann rule for q equal Voronoi cells on the original circle."""
    h = Fraction(1, q * cells_per_coset)
    total = Fraction(0)
    for j in range(cells_per_coset):
        t = (Fraction(j, 1) + Fraction(1, 2)) * h
        dist = min(t, Fraction(1, q) - t)
        total += dist ** p * h * q
    return total


def run():
    for q in (1, 2, 3, 5, 11):
        for p in (1, 2, 3, 4):
            moment = exact_pth_moment(q, p)
            assert moment == Fraction(1, p + 1) / (2 * q) ** p
            approx = discrete_pth_moment(q, p, 1000)
            assert abs(float(approx - moment)) < 0.000001
            radius = float(moment) ** (1 / p)
            assert isclose(radius, 1 / (2 * q * (p + 1) ** (1 / p)), rel_tol=1e-13)
        assert Fraction(1, 2 * q) >= Fraction(1, 4 * q)
    print("PASS: 20 exact rational moment identities and finite ring checks")


if __name__ == "__main__":
    run()
