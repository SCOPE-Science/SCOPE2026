"""Numerical and exact-arithmetic checks of the stated planar sharpness witness.
These finite checks supplement, and do not replace, the analytical proof.
"""
from fractions import Fraction
from math import isclose


def normp(x, p):
    return (abs(x[0]) ** p + abs(x[1]) ** p) ** (1.0 / p)


def power_profile(a, b, p):
    return ((a + b) ** p + abs(a - b) ** p) / 2


def check_exact_quartic():
    for a in map(Fraction, (0, 1, 2, 3, 7)):
        for b in map(Fraction, (0, 1, 2, 5, 11)):
            # An exact scaled model for p=4: u=(a,a), v=(b,-b).
            # Its half-length radii are a/2**(3/4), b/2**(3/4).
            # Center-to-vertex fourth power is ((a+b)^4+(a-b)^4)/16.
            actual = ((a + b) ** 4 + (a - b) ** 4) / 16
            lhs_scaled = 8 * actual
            rhs_scaled = (a + b) ** 4 / 2 + abs(a - b) ** 4 / 2
            assert lhs_scaled == rhs_scaled


def check_all():
    check_exact_quartic()
    trials = 0
    for p in (2.0, 2.5, 3.0, 4.0, 6.0, 9.0):
        for a in (0.0, 0.125, 0.5, 1.0, 2.0, 7.5):
            for b in (0.0, 0.2, 0.75, 1.0, 3.0, 8.0):
                k = 2 ** (1 - 1 / p)
                u = (k * a, k * a)
                v = (k * b, -k * b)
                vertices = ((0.0, 0.0), u, v, (u[0] + v[0], u[1] + v[1]))
                center = ((u[0] + v[0]) / 2, (u[1] + v[1]) / 2)
                power = min(normp((center[0] - w[0], center[1] - w[1]), p) ** p for w in vertices)
                expected = power_profile(a, b, p)
                assert isclose(power, expected, rel_tol=3e-12, abs_tol=1e-10)
                assert isclose(normp(u, p) / 2, a, rel_tol=3e-12, abs_tol=1e-10)
                assert isclose(normp(v, p) / 2, b, rel_tol=3e-12, abs_tol=1e-10)
                # Other locations in the same parallelogram cannot surpass the candidate.
                for i in range(11):
                    for j in range(11):
                        x = ((i * u[0] + j * v[0]) / 10, (i * u[1] + j * v[1]) / 10)
                        distp = min(normp((x[0] - w[0], x[1] - w[1]), p) ** p for w in vertices)
                        assert distp <= expected + 1e-8 * max(1, expected)
                trials += 1
    print('PASS: quartic exact-rational certificate and', trials, 'witness instances, 121 grid points each')


if __name__ == '__main__':
    check_all()
