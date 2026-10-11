"""Separate boundary-intersection checks for regular-polygon centroid perimeter splits.

The infinite-degree assertion is proved analytically in RESULT.md; this script checks
finitely many instances and the algebraic identity of the derived tangent formula.
"""
from math import cos, sin, pi, tan, isclose
from fractions import Fraction


def boundary_fraction(n, alpha):
    points = [(cos(2*pi*j/n), sin(2*pi*j/n)) for j in range(n)]
    dx, dy = cos(alpha), sin(alpha)
    crossings = []
    for j in range(n):
        a = points[j]
        b = points[(j+1) % n]
        ex, ey = b[0]-a[0], b[1]-a[1]
        denominator = ex*dy-ey*dx
        if abs(denominator) < 1.e-11:
            continue
        u = -(a[0]*dy-a[1]*dx)/denominator
        if -1.e-10 <= u <= 1+1.e-10:
            crossing = (j+u) % n
            if not any(min(abs(crossing-x), n-abs(crossing-x)) < 1.e-9
                       for x in crossings):
                crossings.append(crossing)
    assert len(crossings) == 2, (n, alpha, crossings)
    arc = (crossings[1]-crossings[0]) % n
    return min(arc, n-arc)/n


def rational_identity():
    # The two expressions for the boundary deficit agree as rational functions
    # with t=tan(alpha), b=tan(beta). Check by exact polynomial arithmetic:
    # t/(2 sin(beta)cos(beta)(1+b*t)) - cot(beta)*t/2
    # = t*(b-t)/(2*(1+b*t)). Put sin(beta)^2=b^2/(1+b^2), etc.
    for numerator_b in (1, 2, 3, 4, 7):
        b = Fraction(numerator_b, 10)
        for numerator_t in range(0, numerator_b+1):
            t = Fraction(numerator_t, 10)
            # sin(2 beta) = 2b/(1+b^2), 1-cos(2 beta)=2b^2/(1+b^2)
            s = 2*b/(1+b*b)
            d = 2*b*b/(1+b*b)
            cot_beta = 1/b
            left = t/(s+d*t)-cot_beta*t/2
            right = t*(b-t)/(2*(1+b*t))
            assert left == right, (b, t)


def verify():
    rational_identity()
    for n in range(3, 38):
        beta = pi/n
        for portion in (1.e-6, .04, .125, .25, .49, .50, .51, .75, .875, .96, 1-1.e-6):
            alpha = beta*portion
            value = boundary_fraction(n, alpha)
            expected = .5 if n % 2 == 0 else .5-tan(alpha)*tan(beta-alpha)/(2*n)
            assert isclose(value, expected, rel_tol=0, abs_tol=4.e-12), (n, alpha, value, expected)
        if n % 2 == 1:
            minimum = .5-tan(pi/(2*n))**2/(2*n)
            assert isclose(boundary_fraction(n, beta/2), minimum,
                           rel_tol=0, abs_tol=4.e-12)
            assert minimum < .5
    assert isclose(.5 - tan(pi/6)**2/6, 4/9, abs_tol=1.e-14)
    print('REGULAR_POLYGON_CENTROID_PERIMETER_CHECKS_OK')

if __name__ == '__main__':
    verify()
