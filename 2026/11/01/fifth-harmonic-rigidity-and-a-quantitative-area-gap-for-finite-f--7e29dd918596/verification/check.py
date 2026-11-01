#!/usr/bin/env python3
"""Deterministic checks for the fifth-mode area gap of constant-width ovals.

All universal claims in the accompanying proof are analytic. This script independently
checks Fourier integration, several exact extremal identities, and finitely many samples.
It uses only Python's standard library and performs no external requests.
"""
import math
import random
from fractions import Fraction

PI = math.pi


def area_formula(w, a, b, c, d):
    return PI*w*w/4 - 4*PI*(a*a + b*b) - 12*PI*(c*c + d*d)


def radius(w, a, b, c, d, t):
    return w/2 - 8*(a*math.cos(3*t) + b*math.sin(3*t)) - 24*(c*math.cos(5*t) + d*math.sin(5*t))


def support(w, a, b, c, d, t):
    return w/2 + a*math.cos(3*t) + b*math.sin(3*t) + c*math.cos(5*t) + d*math.sin(5*t)


def dh(w, a, b, c, d, t):
    return -3*a*math.sin(3*t) + 3*b*math.cos(3*t) - 5*c*math.sin(5*t) + 5*d*math.cos(5*t)


def trapezoid_area(w, a, b, c, d, count=4096):
    # Exact for degree at most 10 with 4096 evenly spaced nodes in infinite precision.
    return sum((support(w, a, b, c, d, 2*PI*i/count)**2 -
                dh(w, a, b, c, d, 2*PI*i/count)**2)
               for i in range(count)) * PI / count


def main():
    checks = 0
    # The algebraic split used in the proof is tested with exact rational arithmetic.
    for i in range(25):
        for j in range(25):
            R, S = Fraction(i, 11), Fraction(j, 11)
            bound = max(R+S/2, S-R, S) if R == 0 else max(R+S/2, S-R)
            assert bound*bound >= R*R + S*S/2
            checks += 1

    # Triple cosine sampling inequality, independent of the phase of the fifth mode.
    rng = random.Random(1975)
    for _ in range(250):
        R, S, phi = 2*rng.random(), 2*rng.random(), 2*PI*rng.random()
        at_extrema = [R + S*math.cos(phi+2*PI*k/3) for k in range(3)]
        assert max(at_extrema) + 1e-12 >= R+S/2
        checks += 1

    # Exact extremal area and curvature non-negativity at the boundary.
    for w in (Fraction(1), Fraction(2), Fraction(7,3)):
        # pi factors cancel in the algebraic identities.
        a = w/16
        area_over_pi = w*w/4 - 4*a*a
        assert area_over_pi == 15*w*w/64
        for i in range(128):
            assert radius(float(w), float(a), 0.0, 0.0, 0.0,
                          2*PI*i/128) >= -1e-13
        checks += 129

    # For each random real-phase pair, scale coefficients into the convex regime
    # using the rigorous triangle bound on absolute curvature amplitudes.
    for _ in range(140):
        w = 0.25 + 3*rng.random()
        a, b, c, d = [rng.uniform(-1, 1) for k in range(4)]
        amplitude = 8*math.hypot(a, b) + 24*math.hypot(c, d)
        scale = (w/2) * rng.uniform(.05, .9) / amplitude
        a, b, c, d = [scale*z for z in (a, b, c, d)]
        assert min(radius(w, a, b, c, d, 2*PI*i/192) for i in range(192)) > 0
        A = area_formula(w, a, b, c, d)
        assert A + 1e-11 >= 15*PI*w*w/64 + 6*PI*(c*c + d*d)
        A_quad = trapezoid_area(w, a, b, c, d)
        assert abs(A-A_quad) < 2e-10*(1+A)
        checks += 3

    print(f"PASS: {checks} deterministic checks; analytic proof controls all angles.")

if __name__ == '__main__':
    main()
