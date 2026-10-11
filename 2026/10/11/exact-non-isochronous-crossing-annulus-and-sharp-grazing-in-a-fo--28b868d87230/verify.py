#!/usr/bin/env python3
"""Supplementary exact-segment consistency checks for the four-sector relay oscillator.

The universal theorem follows from the analytic proof; this test samples only a finite grid.
"""
from math import acos, asin, cos, sin, sqrt, pi, isclose

def near(a, b, eps=5e-11):
    assert isclose(a, b, rel_tol=eps, abs_tol=eps), (a, b)

def check(k, A):
    assert 0 < k and A > 2*k
    tm = acos(-k/(A-k))
    tp = acos(k/(A+k))
    v = sqrt(A*(A-2*k))
    w = sqrt(A*(A+2*k))
    # First lower branch; next lower branch starts at (0,-v).
    near(k+(A-k)*cos(tm), 0)
    near(-(A-k)*sin(tm), -v)
    near(-k+k*cos(tm)-v*sin(tm), -A)
    near(-k*sin(tm)-v*cos(tm), 0)
    # First upper branch; last upper branch starts at (0,+w).
    near(k-(A+k)*cos(tp), 0)
    near((A+k)*sin(tp), w)
    near(-k+k*cos(tp)+w*sin(tp), A)
    near(-k*sin(tp)+w*cos(tp), 0)
    # Both vector fields cross the y-axis at both turning states.
    assert -A+k < 0 and -A-k < 0
    assert A-k > 0 and A+k > 0
    # The expression is the sum of four positive traversal times.
    period = 2*(tm+tp)
    near(period, 2*acos(-k/(A-k))+2*acos(k/(A+k)))
    assert 2*pi < period < 2*pi+2*acos(1/3)
    deriv = 2*k*(1/((A+k)*sqrt(A*(A+2*k)))-1/((A-k)*sqrt(A*(A-2*k))))
    assert deriv < 0
    # Independently evaluate the trigonometric rewriting of the first term.
    near(tm, pi/2+asin(k/(A-k)))
    near(tp, pi/2-asin(k/(A+k)))

if __name__ == '__main__':
    for k in (0.125, 0.4, 1., 2.5, 20.):
        for ratio in (2.00001, 2.01, 2.1, 2.5, 3., 4., 10., 100.):
            check(k, k*ratio)
        for ratio in (0.2, 0.9, 1.2, 1.99, 2.0):
            A=k*ratio
            assert A*(A-2*k)/2 <= 0
    print('CHECK_OK')
