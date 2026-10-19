#!/usr/bin/env python3
"""Supplementary finite consistency checks for spherical cap rigidity.

The universal rigidity theorem is proved analytically, not by this script.
Requires only the Python standard library.
"""
from math import pi, sin, cos, hypot, sqrt


def circle_cap_multiplier(m, alpha):
    return sin(m * alpha) / (pi * m)


def discrete_cap_multiplier(m, alpha, samples=32768):
    total = 0j
    for j in range(samples):
        theta = 2*pi*(j + 0.5)/samples - pi
        if abs(theta) < alpha:
            total += complex(cos(m*theta), sin(m*theta))
    return total / samples


def verify_circle_coefficients():
    alpha = pi/sqrt(2)
    for m in range(1, 19):
        analytic = circle_cap_multiplier(m, alpha)
        quadrature = discrete_cap_multiplier(m, alpha, samples=16384)
        assert abs(quadrature-analytic) < 0.00008, (m, quadrature, analytic)
        assert abs(analytic) > 1e-7, m
    return 18


def verify_discontinuous_hemisphere_example():
    # F(eta) = diag(2, 1/2) eta / |diag(2, 1/2) eta|.
    # The maximizing input hemisphere is {eta : u dot F(eta) > 0}.
    samples = 4096
    target_dirs = 192
    F = []
    for j in range(samples):
        th = 2*pi*(j+.5)/samples
        x,y = cos(th),sin(th)
        xx,yy = 2*x,y/2
        norm = hypot(xx,yy)
        F.append((xx/norm, yy/norm))
    total_h = 0.0
    for j in range(target_dirs):
        th = 2*pi*(j+.5)/target_dirs
        ux,uy = cos(th),sin(th)
        h = sum(max(0.0,ux*x+uy*y) for x,y in F)/samples
        total_h += h
    width = 2*total_h/target_dirs
    assert abs(width - 2/pi) < 2e-5, (width,2/pi)
    return width


def main():
    count = verify_circle_coefficients()
    width = verify_discontinuous_hemisphere_example()
    print(f"VERIFY_OK {count} Fourier-cap coefficient comparisons; "
          f"nonorthogonal hemisphere sharpness width {width:.10f}")


if __name__ == '__main__':
    main()
