#!/usr/bin/env python3
"""Reproduce finite-energy consistency tests for the stated cubic Hamiltonian.

Python standard library only. Finite quadrature is not a proof of asymptotic claims.
"""
from fractions import Fraction
from math import cos, sin, pi, sqrt, log, fsum


def q(x, a, k):
    return 1 + 2*a*x + k*x*x


def V(x, a, k):
    return x*x/2 - a*x*x*x/3 + k*x*x*x*x/4


def check_conservation():
    for a, k in ((Fraction(0), Fraction(1)),
                 (Fraction(2, 5), Fraction(1)),
                 (Fraction(-1, 2), Fraction(3))):
        for x in (Fraction(-3, 2), Fraction(0), Fraction(5, 3)):
            for y in (Fraction(-2, 3), Fraction(1), Fraction(7, 4)):
                qp = 2*a + 2*k*x
                vp = x - a*x*x + k*x*x*x
                xdot = q(x, a, k)*y
                ydot = -vp - qp*y*y/2
                hx = vp + qp*y*y/2
                hy = q(x, a, k)*y
                assert hx*xdot + hy*ydot == 0


def negative_turning_point(E, a, k, A):
    left = -2*A
    while V(left, a, k) < E:
        left *= 2
    right = 0.0
    for _ in range(100):
        middle = (left+right)/2
        if V(middle, a, k) > E:
            left = middle
        else:
            right = middle
    return (left+right)/2


def period(A, a, k, n=30000):
    E = V(A, a, k)
    B = negative_turning_point(E, a, k, A)
    radius = (A-B)/2
    center = (A+B)/2
    step = pi/n
    terms = []
    for i in range(n):
        theta = (i+0.5)*step
        x = center + radius*cos(theta)
        denom = q(x,a,k)*(E-V(x,a,k))
        assert denom > 0
        terms.append(radius*sin(theta)/sqrt(denom))
    return sqrt(2)*step*fsum(terms)


def main():
    check_conservation()
    for a,k,A in ((0.0,1.0,35.0),(0.4,1.0,35.0),
                  (-0.4,1.0,35.0),(1.0,3.0,35.0)):
        E = V(A,a,k)
        actual = period(A,a,k)
        observed = actual*sqrt(k*E/2) - log(4*E/k)/2
        predicted = log(8*k*k/(k-a*a))
        assert abs(observed-predicted) < 0.003, (a,k,observed,predicted)
    print('CHECK_OK')

if __name__ == '__main__':
    main()
