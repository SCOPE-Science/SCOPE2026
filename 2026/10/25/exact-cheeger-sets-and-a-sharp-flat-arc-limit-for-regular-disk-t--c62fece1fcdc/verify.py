#!/usr/bin/env python3
"""Reproducible numerical and symbolic checks for a family of disk triangles.

Requires Python >= 3.10. Optional: SymPy for symbolic series check.
Run: python verify.py
"""
from math import pi, sqrt, sin, asin, cos


def parameters(width, radius):
    assert 0 < width <= radius
    vertex = (sqrt((4 * radius**2 - (radius - width)**2) / 3) - (radius - width)) / 2
    inrad = width - vertex
    return vertex, inrad, radius - inrad


def inner_geometry(width, radius, erosion):
    vertex, rho, center = parameters(width, radius)
    assert 0 <= erosion <= rho
    small_radius = radius - erosion
    v = (sqrt(max(0, 4 * small_radius**2 - 3 * center**2)) - center) / 2
    v = max(0.0, v)
    alpha = 2 * asin(max(0.0, min(1.0, sqrt(3) * v / (2 * small_radius))))
    area = 3 * sqrt(3) * v**2 / 4 + 3 * small_radius**2 * (alpha - sin(alpha)) / 2
    return area, alpha, v


def cheeger_radius(width, radius):
    _, rho, _ = parameters(width, radius)
    lo, hi = 0.0, rho
    for _ in range(85):
        mid = (lo + hi) / 2
        if inner_geometry(width, radius, mid)[0] > pi * mid**2:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def angular_area(width, radius, erosion, steps=24000):
    # Independent geometric integration: intersect the three disks along rays,
    # with the ray endpoint determined by the most restrictive disk.
    _, rho, c = parameters(width, radius)
    assert erosion < rho
    rr = radius - erosion
    angles = (0.0, 2*pi/3, 4*pi/3)

    def square_radius(theta):
        possible = []
        for a in angles:
            ct = cos(theta-a)
            t = c*ct + sqrt(max(0.0, rr**2-c**2*(1-ct**2)))
            possible.append(t)
        return min(possible)**2

    # Trapezoidal quadrature is superconvergent on each smooth periodic segment.
    return pi * sum(square_radius(2*pi*k/steps) for k in range(steps)) / steps


def run():
    for width, rad in ((1.,1.), (1.,1.6), (1.,4.), (1.,15.), (2.2,4.4)):
        v, rho, c = parameters(width, rad)
        assert abs(rad**2 - (c*c + c*v + v*v)) < 1e-10
        assert abs(v + rho - width) < 1e-11
        for proportion in (0., 0.2, 0.5, 0.85):
            er = rho*proportion
            exact, alpha, _ = inner_geometry(width, rad, er)
            independent = angular_area(width, rad, er)
            assert abs(exact-independent) < 4e-7*max(1,width*width), (rad, er, exact, independent)
        s = cheeger_radius(width, rad)
        exact, alpha, _ = inner_geometry(width, rad, s)
        assert abs(exact-pi*s*s) < 3e-11*max(1,width**2)
        # Cheeger set is the outer offset of the inner parallel set.
        perimeter = 3*(rad-s)*alpha + 2*pi*s
        area_C = exact + s*3*(rad-s)*alpha + pi*s*s
        assert abs(perimeter/area_C - 1/s) < 1e-10
        assert 0 < alpha < pi/3 + 1e-12
    H = 3+sqrt(pi*sqrt(3))
    K = (H*H+6*H-9)/(6*H)
    diffs = []
    for rad in (100., 200., 400., 800.):
        sr = cheeger_radius(1., rad)
        diffs.append(abs(rad*(H-1/sr)-K))
    assert diffs[-1] < 0.002 and all(a>b for a,b in zip(diffs,diffs[1:])), diffs
    try:
        import sympy as sp
    except ImportError:
        print('SymPy not installed: symbolic check skipped')
    else:
        x,w,s=sp.symbols('x w s',positive=True)
        R=1/x
        v=(sp.sqrt((4*R**2-(R-w)**2)/3)-(R-w))/2
        c=R-w+v
        vs=(-c+sp.sqrt(4*(R-s)**2-3*c**2))/2
        series=sp.series(vs,x,0,2).removeO().expand()
        expected=2*w/3-2*s+x*(-w**2/9+2*w*s-3*s**2)
        assert sp.simplify(series-expected)==0
        t0=2*w/3-2*s
        t1=-w**2/9+2*w*s-3*s**2
        B=3*sp.sqrt(3)/4*(2*t0*t1+t0**3)
        assert sp.simplify(B - sp.sqrt(3)*(w-3*s)*(w*w+6*w*s-9*s*s)/9)==0
    print('CHEEGER_DISK_TRIANGLE_CHECKS_OK')


if __name__=='__main__':
    run()
