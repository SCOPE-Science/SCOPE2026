"""Independent numerical consistency checks for exact circular-lens rectangle formulas.

All claims for the continuum of parameters are established analytically in RESULT.md.
These checks compare independently formulated feasibility and area calculations.
"""
from math import acos, cos, isclose, pi, sin, sqrt
from random import Random


def optimizer(c):
    b = (sqrt(c*c+8)-3*c)/4
    a = sqrt(b*(b+c))
    return a, b


def area_unit(c):
    a, b = optimizer(c)
    return 4*a*b


def unit_feasible(c, a, b, theta):
    horizontal = a*abs(cos(theta))+b*abs(sin(theta))
    return a*a+b*b+2*c*horizontal+c*c <= 1+1e-12


def scale_to_feasible(c, a, b, theta):
    horizontal = a*abs(cos(theta))+b*abs(sin(theta))
    s = (1-c*c)/(c*horizontal + sqrt(c*c*horizontal*horizontal + (a*a+b*b)*(1-c*c)))
    assert unit_feasible(c, s*a, s*b, theta)
    return s


def check():
    rng = Random(1729)
    for c in [0, 1e-4, .02, .10, .25, .50, .75, .90, .99, .999]:
        a, b = optimizer(c)
        assert isclose(2*b*b+3*c*b+c*c, 1, abs_tol=4e-14)
        assert isclose(a*a, b*(b+c), abs_tol=2e-14)
        assert unit_feasible(c, a, b, pi/2)
        r = a/b
        if c > 0:
            assert a > b
            assert isclose(c, (r*r-1)/(r*sqrt(r*r+1)), abs_tol=8e-12)
        s = (sqrt(2-c*c)-c)/2
        max_area = 4*a*b
        if c > 0:
            assert max_area > 4*s*s
        else:
            assert isclose(max_area, 2, abs_tol=1e-14)
        # Area cannot improve upon the theorem by rotating or changing aspect.
        for j in range(1200):
            x = .01 + rng.random()*1.3
            y = .01 + rng.random()*1.3
            theta = pi*rng.random()/2
            scale = scale_to_feasible(c, x, y, theta)
            sampled = 4*scale*scale*x*y
            assert sampled <= max_area + 3e-12, (c, sampled, max_area)
        # Independently compare the exact stationary root against a 1D mesh.
        for j in range(300):
            v = j*(1-c)/300
            if v+c < 1:
                candidate = 4*v*sqrt(1-(v+c)**2)
                assert candidate <= max_area + 4e-12
    for c in [.001, .0005]:
        b_sq=(sqrt(2-c*c)-c)/2
        delta=area_unit(c)-4*b_sq*b_sq
        assert abs(delta/(c*c)-.5)<.003
    for eps in [1e-3, 1e-4, 1e-5]:
        c=1-eps
        m=area_unit(c)
        b_sq=(sqrt(2-c*c)-c)/2
        assert abs(m/eps**1.5-8*sqrt(6)/9)<.005
        assert abs(4*b_sq*b_sq/eps**2-4)<.012
        lens=2*acos(c)-2*c*sqrt(1-c*c)
        assert abs(m/lens-1/sqrt(3))<.001
    print('ALL_CHECKS_PASSED')


if __name__ == '__main__':
    check()
