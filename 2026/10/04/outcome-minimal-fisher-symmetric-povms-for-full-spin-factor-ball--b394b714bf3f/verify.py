#!/usr/bin/env python3
from fractions import Fraction as Q


def check(d, r):
    assert d >= 2
    assert Q(0) <= r < Q(1)
    Delta = Q(d + 1) - Q(d - 1) * r
    p0 = (Q(1) + r) / Delta
    p1 = (Q(1) - r) / Delta
    c = (Q(d - 1) * r - Q(1)) / Q(d)

    # Normalization and axial mean of the spherical support.
    assert p0 + Q(d) * p1 == Q(1)
    assert p0 + Q(d) * p1 * c == r

    # Exact transverse and axial second moments.  These two identities,
    # together with the regular-simplex tensor identity and vanishing cross
    # terms, are exactly Cov(z)=(1-r^2) I/d.
    transverse = Q(d) * p1 * (Q(1) - c*c) / Q(d - 1)
    axial_second = p0 + Q(d) * p1 * c*c
    target = (Q(1) - r*r) / Q(d)
    assert transverse == target
    assert axial_second == r*r + target

    # Positivity of probabilities and admissibility of c.
    assert p0 > 0 and p1 > 0
    assert -1 < c < 1
    return p0, p1, c


def main():
    radii = [Q(0), Q(1, 7), Q(1, 3), Q(3, 5), Q(9, 10), Q(99, 100)]
    for d in range(2, 10):
        for r in radii:
            check(d, r)

    # Five-parameter Gamma^5 example: the construction has 6 outcomes,
    # while randomizing 5 binary spectral measurements yields 10 labeled
    # outcomes.  The theorem's lower bound is d+1=6.
    d = 5
    assert d + 1 == 6
    assert 2*d == 10
    assert d + 1 < 2*d
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
