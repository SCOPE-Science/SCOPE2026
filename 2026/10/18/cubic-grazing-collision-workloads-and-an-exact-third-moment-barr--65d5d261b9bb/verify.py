#!/usr/bin/env python3
"""Self-contained deterministic numerical cross-checks for a circular specular billiard.

The analytical theorem and moment statements are proved in RESULT.md; numerical
quadrature cannot establish the asymptotic or uniqueness claims.
"""
import math
from fractions import Fraction

PI = math.pi


def simpson(fun, start, stop, intervals=2400):
    assert intervals > 0 and intervals % 2 == 0
    if start == stop:
        return 0.0
    step = (stop - start) / intervals
    acc = fun(start) + fun(stop)
    for j in range(1, intervals):
        acc += (4 if j % 2 else 2) * fun(start + j * step)
    return step * acc / 3


def geom_tail(k, travel, radius=1.0, dim=2):
    """Exact deterministic-speed tail in a Euclidean ball; quadrature."""
    assert k >= 2 and travel >= 0 and radius > 0 and dim >= 2
    ellend = min(2 * radius, travel / (k - 1))
    ellbreak = min(ellend, travel / k)
    if not ellend:
        return 0.0

    vol = PI**(dim/2) / math.gamma(dim/2 + 1)
    sphere = 2 * PI**((dim-1)/2) / math.gamma((dim-1)/2)
    factor = sphere / (4 * vol * radius**dim)
    def integrand(ell, cap):
        return factor * ell * (radius**2 - ell**2 / 4)**((dim-3)/2) * cap

    # Tested cases avoid ell=2R, where changing to angular coordinates is needed.
    assert ellend < 2 * radius
    a = simpson(lambda ell: integrand(ell, ell), 0., ellbreak, 1000)
    b = simpson(lambda ell: integrand(ell, travel - (k - 1) * ell),
                ellbreak, ellend, 1000)
    return a + b


def cubic_coeff(k):
    return Fraction(2 * k - 1, 6 * (k - 1)**2 * k**2)


def asymptotic_geom_tail(k, travel, radius=1.0, dim=2):
    vol = PI**(dim/2) / math.gamma(dim/2 + 1)
    sphere = 2 * PI**((dim-1)/2) / math.gamma((dim-1)/2)
    return float(cubic_coeff(k)) * sphere * travel**3 / (4 * vol * radius**3)


def gaussian_tail(k, h, sigma=1., radius=1.):
    """Exact Maxwellian probability, angular quadrature, no stochastic simulation."""
    a = sigma * h
    def integrand(theta):
        ell = 2 * radius * math.sin(theta)
        inner = a * math.sqrt(PI/2) * (
            math.erf(k * ell / (math.sqrt(2) * a))
            - math.erf((k - 1) * ell / (math.sqrt(2) * a)))
        return (2 / (PI * radius)) * math.sin(theta) * inner
    return simpson(integrand, 0., PI / 2, 6400)


def gaussian_cubic_coeff(k):
    return (2 * k - 1) / (4 * math.sqrt(2 * PI) * k**2 * (k - 1)**2)


def interval_tail(k, h, length=1., sigma=1.):
    z = math.sqrt(2) * sigma * h
    return simpson(lambda u: math.erfc(((k - 1) * length + u) / z),
                   0., length, 10000) / length


def run():
    checks = 0
    # Exact rational telescoping of the coefficients at many integers.
    for k in range(2, 2001):
        term = Fraction(2 * k - 1, k*k*(k-1)**2)
        assert term == Fraction(1, (k-1)**2) - Fraction(1, k*k)
        checks += 1
    for dim in (2, 3, 4, 7):
        for k in (2, 3, 5, 11, 40):
            for travel in (0.02, 0.1, 0.4):
                p = geom_tail(k, travel, dim=dim)
                c = asymptotic_geom_tail(k, travel, dim=dim)
                assert 0 < p
                assert 0.97 < p/c < 1.055
                if dim == 3:
                    assert abs(p/c-1) < 3e-12  # exact cubic law when dim=3
                checks += 2
    for dim in (2, 3, 4, 7):
        vol = PI**(dim/2) / math.gamma(dim/2 + 1)
        sphere = 2 * PI**((dim-1)/2) / math.gamma((dim-1)/2)
        for k in (100, 1000, 5000):
            travel = 0.4
            p = geom_tail(k, travel, dim=dim)
            lim = sphere * travel**3 / (12 * vol)
            assert abs(k**3*p/lim-1) < 0.035
            checks += 1
    for k in (2, 3, 5):
        for eta in (0.07, 0.12):
            p = gaussian_tail(k, eta)
            c = gaussian_cubic_coeff(k) * eta**3
            assert p > 0 and 0.9 < p/c < 1.05
            checks += 2
    for h in (0.08, 0.1):
        p = interval_tail(2, h)
        approx = math.sqrt(2/PI) * h**3 * math.exp(-1/(2*h*h))
        assert 0.95 < p/approx < 1
        checks += 1
    assert Fraction(1,1) - Fraction(1,2000**2) == sum(
        Fraction(2*k-1, k*k*(k-1)**2) for k in range(2,2001))
    checks += 1
    print('PASS:', checks, 'deterministic independent quadrature/rational checks')
    for k in (2,3,5):
        print('Gaussian multi-hit', k, 'h=0.12:', format(gaussian_tail(k, 0.12),'.12g'),
              'cubic leading:', format(gaussian_cubic_coeff(k)*0.12**3,'.12g'))
    print('Tail n=5000:', format(5000**3 * geom_tail(5000,0.4),'.12g'),
          'limit:', format(0.4**3/(6*PI),'.12g'))

if __name__ == '__main__':
    run()
