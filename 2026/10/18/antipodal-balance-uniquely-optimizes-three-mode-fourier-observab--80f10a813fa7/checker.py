#!/usr/bin/env python3
"""Finite checks only: the universal identities are established analytically."""
from math import pi, sin, cos, sqrt, isclose
from itertools import product

def data(a, theta):
    t = 2*a/pi
    c = 2*sin(a)/pi
    d = sin(2*a)/pi
    u = cos(theta)
    v = d*(2*u*u-1)
    w = c*u
    h = sqrt(v*v+8*w*w)
    matrix = [[t, w, v], [w, t, w], [v, w, t]]
    eig = sorted([t-v, t+(v-h)/2, t+(v+h)/2])
    ideal = t-d
    deficit = ideal - eig[0]
    exact_gap = 4*u*u*(c*c-d*d)/(h+v+2*d)
    trace = sum(matrix[j][j] for j in range(3))
    det = (t-v)*(t*(t+v)-2*w*w)
    assert isclose(sum(eig),trace,rel_tol=1e-11,abs_tol=1e-11)
    assert isclose(eig[0]*eig[1]*eig[2],det,rel_tol=1e-9,abs_tol=1e-11)
    assert eig[0]>-1e-11
    assert deficit>-1e-11
    assert isclose(deficit,exact_gap,rel_tol=1e-8,abs_tol=1e-11)
    return eig[0], ideal, deficit

def main():
    for a in (0.03,0.1,0.4,0.8,1.2,1.53):
        opt, ideal, gap = data(a, pi/2)
        assert isclose(opt, ideal,abs_tol=1e-12)
        assert abs(gap)<1e-12
        for j in range(101):
            theta = a + (pi-2*a)*j/100
            mineig, target, loss = data(a, theta)
            assert mineig<=target+1e-12
        eps=1e-3
        curvature = 4*sin(a)**3/(pi*cos(a))
        _,_,loss = data(a,pi/2+eps)
        assert abs(loss/eps**2/curvature-1)<2e-3
    print("Finite calculations pass; analytic proof handles all admissible parameters.")

if __name__ == "__main__":
    main()
