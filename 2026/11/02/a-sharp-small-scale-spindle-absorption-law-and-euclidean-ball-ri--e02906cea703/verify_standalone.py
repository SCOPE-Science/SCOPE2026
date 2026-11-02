"""Standalone standard-library checks of the small-scale spindle absorption formulas.

Run with Python 3.10 or later: python verify_standalone.py
All numerical checks are corroboration, not substitutes for the analytic proof.
"""
from fractions import Fraction
from math import acos, asin, comb, cos, gamma, hypot, pi, sin, sqrt
from random import Random


def unit_ball_volume(d):
    return pi ** (d / 2) / gamma(d / 2 + 1)


def radial_integral(d):
    return sum((Fraction(comb(d - 1, j), (d + j) * (2 * d - 1 - j))
                for j in range(d)), Fraction())


def ball_coefficient(d):
    return (d * unit_ball_volume(d - 1) * float(radial_integral(d))
            / (2 ** (d - 1) * unit_ball_volume(d)))


assert radial_integral(2) == Fraction(1, 3)
assert radial_integral(3) == Fraction(31, 120)
assert radial_integral(4) == Fraction(19, 70)
assert abs(ball_coefficient(2) - 2 / (3 * pi)) < 1e-13
assert abs(ball_coefficient(3) - 93 / 640) < 1e-13
print('EXACT_RADIAL_CONSTANTS_PASSED')


def planar_probability(r):
    return (r * sqrt(4 - r*r) + 2 * (r*r - 2) * asin(r / 2)) / (pi * r*r)

for r in (0.15, 0.1, 0.05):
    assert abs(planar_probability(r) / (r * ball_coefficient(2)) - 1) < 0.002
print('EXACT_DISK_FORMULA_SMALL_SCALE_PASSED')


def d3_probability(eps, n=300):
    # Independent radial integration of the three-dimensional angular law.
    total = 0.0
    for i in range(n):
        t = (i + 0.5) / n
        for j in range(n):
            s = (j + 0.5) / n
            delta = asin(eps*t/2) + asin(eps*s/2)
            total += t*t*s*s*(1-cos(delta))
    return 4.5*total/(n*n)

for r in (0.2, 0.1, 0.04):
    assert abs(d3_probability(r) / (r*r*ball_coefficient(3)) - 1) < 0.005
print('INDEPENDENT_THREE_DIMENSIONAL_QUADRATURE_PASSED')


def radial_ellipse(a, b, theta):
    return 1 / sqrt((cos(theta)/a)**2 + (sin(theta)/b)**2)


def ellipse_moments(a, b, n=16000):
    # Angle-average radial powers; a*b=1 normalizes equal area.
    power5 = 0.0
    power2 = 0.0
    power4 = 0.0
    for j in range(n):
        t=2*pi*(j+0.5)/n
        rho=radial_ellipse(a,b,t)
        power5 += rho**5
        power2 += rho**2
        power4 += rho**4
    return power5/n,power2/n,power4/n

for a in (1.1, 1.5, 2.0):
    m5,m2,m4=ellipse_moments(a,1/a)
    assert abs(m2-1)<1e-10
    assert m5>1
    # Jensen's explicit variance reinforcement, here q=5/2.
    assert m5 >= 1+1.5*(m4-1) - 1e-10
print('STRICT_BALL_OPTIMALITY_AND_RADIAL_VARIANCE_BOUND_PASSED')


def simulated_probability(a,b,eps,n=300000):
    rng=Random(17383)
    count=0
    for _ in range(n):
        t1=sqrt(rng.random()); t2=sqrt(rng.random())
        z1=2*pi*rng.random(); z2=2*pi*rng.random()
        x1,y1=a*t1*cos(z1), b*t1*sin(z1)
        x2,y2=a*t2*cos(z2), b*t2*sin(z2)
        dot=-(x1*x2+y1*y2)/(hypot(x1,y1)*hypot(x2,y2))
        theta=acos(max(-1.,min(1.,dot)))
        if theta<=asin(eps*hypot(x1,y1)/2)+asin(eps*hypot(x2,y2)/2):
            count+=1
    return count/n

for a,b in ((1.,1.),(1.5,2./3.)):
    coeff=ball_coefficient(2)*ellipse_moments(a,b)[0]
    obs=simulated_probability(a,b,0.10)
    assert abs(obs/(0.10*coeff)-1)<0.08
print('INDEPENDENT_POINT_PAIR_MONTE_CARLO_PASSED')
print('ALL_CHECKS_PASSED')
