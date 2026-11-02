#!/usr/bin/env python3
"""Reproduce the two-fluctuator Kubo lineshape and three-to-one peak criterion.

Requires Python 3 and numpy. All numerical comparisons use the finite-state
Markov resolvent, independently of the rational closed-form derivation.
"""
import math
import numpy as np


def analytic(v, g, w):
    if not (v > 0 and g > 0):
        raise ValueError("v and g must be positive")
    z = w*w
    return (4*g*v*v*(z+16*g*g+4*v*v)
            / (math.pi*(z+4*g*g)*((z-4*v*v)**2+16*g*g*z)))


def resolvent(v, g, w):
    states = ((-1, -1), (-1, 1), (1, -1), (1, 1))
    Q = np.zeros((4, 4), dtype=float)
    for i, s in enumerate(states):
        for bit in (0, 1):
            t = list(s)
            t[bit] = -t[bit]
            j = states.index(tuple(t))
            Q[i, j] += g
        Q[i, i] -= 2*g
    omega = np.array([v*sum(st) for st in states])
    A = -Q.T.astype(complex) - 1j*np.diag(omega+w)
    return float(np.linalg.solve(A, np.ones(4)/4).sum().real/math.pi)


def P(z, t):
    return (z**3+(34*t+2)*z*z+(320*t*t-48*t-32)*z
            +512*t**3-128*t*t+32*t+32)


def dP(z, t):
    return 3*z*z+2*(34*t+2)*z+(320*t*t-48*t-32)


def test():
    threshold = (24*math.sqrt(15)-53)/343
    assert abs(threshold-0.1164769688308397)<1e-14
    critical_ratio = math.sqrt(threshold)
    assert abs(critical_ratio-0.34128722336301964)<1e-14
    checks = 0
    max_err = 0.0
    for v in (0.7, 1.0, 2.3):
        for ratio in (0.02, 0.07, 0.13, 0.28, 0.34, 0.342, 0.4, 0.7, 1.4, 3.0):
            g = v*ratio
            for s in (-4.0,-3.2,-2.0,-1.4,-1.,-.2,0,.2,1,1.4,2,3.2,4.0):
                a = analytic(v, g, v*s)
                b = resolvent(v, g, v*s)
                err = abs(a-b)/max(1.,abs(a),abs(b))
                assert err < 1.e-11, (v, g, s, a, b, err)
                max_err = max(max_err, err)
                checks += 1
    # Spectral shape polynomial: derivative factorization and minimum factor.
    for t in (0.001, 0.025, 0.1, threshold, 0.2, 0.4, 1.0):
        for z in (0.0, 0.01, 0.5, 1.3, 4., 8., 12.):
            assert abs(dP(z,t)-3*(z+16*t+4)*(z-(8-20*t)/3)) < 1.e-9
        if t < 0.4:
            zmin=(8-20*t)/3
            expect = -32*(t-1)*(343*t*t+106*t-17)/27
            assert abs(P(zmin,t)-expect)<1e-9
    for t in (0.002,0.025,0.1,threshold,0.117,0.2,0.4,1.2):
        roots = np.roots([1.,34*t+2.,320*t*t-48*t-32.,512*t**3-128*t*t+32*t+32.])
        pos = sum(abs(z.imag)<1.e-6 and z.real>1.e-7 for z in roots)
        expected = 2 if t<threshold-1.e-10 else 0
        if abs(t-threshold)>1.e-10:
            assert pos==expected,(t,roots,pos)
        else:
            assert abs(P((8-20*t)/3,t))<1.e-9
    print("Markov-resolvent comparisons:",checks)
    print("Maximum normalized discrepancy:",format(max_err,'.4e'))
    print("Critical switching/amplitude ratio:",format(critical_ratio,'.15f'))
    print("Positive-sideband transition checks: passed")

if __name__=='__main__':
    test()
