"""Exact coefficient identities and finite numerical checks for power-law radial weights.

The inequalities in the accompanying proof hold at every point by elementary
complex analysis; the finite checks below are corroborative only.
"""
from fractions import Fraction as Q
from cmath import exp, pi


def c_moment(n, g, q):
    return (n + 1) * (n + g + 1) / ((1 - q) * n + g + 1 - q)


def c_integral(n, g, q):
    p = 1 + g / (1 - q)
    return (n + 1) / (1 - q) * (1 - q * (p - 1) / (n + p))


def c_endpoint(n, g):
    return (n + 1) * (n + g + 1) / g


def verify():
    checks = 0
    for g in (Q(1, 7), Q(1, 2), Q(1), Q(3, 2), Q(7), Q(100)):
        for q in (Q(0), Q(1, 1000), Q(1, 5), Q(1, 2), Q(9, 10), Q(999, 1000)):
            for n in range(100):
                assert c_moment(n, g, q) == c_integral(n, g, q)
                checks += 1
        for n in range(100):
            assert c_moment(n, g, Q(1)) == c_endpoint(n, g)
            checks += 1
    # The pointwise contractivity inequality used in the proof:
    # u |(1-s)/(1-u*s)|^2 <= 1, for 0<=u<=1, |s|<1.
    max_sampled = 0.0
    for u in (0., .01, .25, .5, .75, .99, 1.):
        for rho in (0., .1, .5, .85, .99):
            for j in range(360):
                s = rho * exp(1j * j * pi / 180)
                val = u * abs((1 - s)/(1 - u*s))**2
                assert val < 1 + 1e-10
                max_sampled = max(max_sampled, val)
    # Independent finite-series evaluations of the right-half-plane certificate.
    for g in (.2, 1., 4., 15.):
        for q in (.01, .5, .9, .999):
            for rho in (.1, .35, .65, .9):
                for j in range(45):
                    s = rho * exp(2j * pi * (j / 45))
                    coeffs = [float(c_moment(n, g, q)) for n in range(650)]
                    value = sum(c*s**n for n,c in enumerate(coeffs))
                    assert ((1-s)**2 * value).real > .999999
    print("PASS: %d exact rational coefficient equalities; sampled contractivity max %.12f; finite-series half-plane consistency passed." % (checks, max_sampled))

if __name__ == '__main__':
    verify()
