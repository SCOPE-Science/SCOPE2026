#!/usr/bin/env python3
"""Algebraic and numerical checks for scalar RMSProp cycle rates.

Uses only the Python standard library. Finite tests are diagnostics, not a proof
of the universal theorem supplied in RESULT.md.
"""
from fractions import Fraction as Q
from cmath import sqrt as csqrt
from math import sqrt, isclose
from random import Random


def F(x, v, h, la, ep, be):
    mem = be * v + (1 - be) * la * la * x * x
    return (x - h * la * x / (sqrt(float(mem)) + ep), mem)


def matrices(h, la, ep, be):
    r = h / 2 - ep / la
    assert r > 0
    a = -1 + 4 * (1 - be) * r / h
    b = 2 * be / (h * la * la)
    c = 2 * (1 - be) * la * la * r
    jp = ((a, b), (c, be))
    jm = ((a, -b), (-c, be))
    return r, jp, jm


def matmul(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)) for i in range(2))


def spectral(h, la, ep, be):
    t = -1 + 3 * be + 4 * (1 - be) * ep / (h * la)
    rt = csqrt(t * t - 4 * be)
    eig = ((t + rt) / 2, (t - rt) / 2)
    return max(abs(u) ** 2 for u in eig), t, tuple(u * u for u in eig)


def test_exact_cases():
    be = Q(1, 25)
    for h in (Q(3), Q(4), Q(8)):
        r = h / 2 - 1
        v = r * r
        # All sqrt(v') are exact rationals at these three points.
        def exactF(x, val):
            nxt = be * val + (1 - be) * x * x
            assert nxt == v
            return x - h * x / (abs(r) + 1), nxt
        assert exactF(r, v) == (-r, v)
        assert exactF(-r, v) == (r, v)
        rr, jp, jm = matrices(h, Q(1), Q(1), be)
        assert rr == r
        t = Q(-1) + 3 * be + 4 * (1 - be) / h
        K = ((-jp[0][0], -jp[0][1]), (jp[1][0], jp[1][1]))
        assert K[0][0] + K[1][1] == t
        assert K[0][0] * K[1][1] - K[0][1] * K[1][0] == be
        M = matmul(jm, jp)
        assert M[0][0] + M[1][1] == t * t - 2 * be
        assert M[0][0] * M[1][1] - M[0][1] * M[1][0] == be * be
        rho, _, _ = spectral(float(h), 1., 1., float(be))
        # Double precision can split an exactly repeated root at a fold by O(sqrt(machine epsilon)).
        assert (t*t <= 4*be)
        assert isclose(rho, float(be), rel_tol=5e-7, abs_tol=5e-7)
    print('EXACT_RATIONAL_CASES_OK 3 4 8')


def test_parameter_grid():
    rng = Random(20261028)
    checked = 0
    for beta in [0.001, 0.01, 0.04, 0.10, 1 / 9, .2, .5, .9, .99]:
        for _ in range(80):
            la = .05 + 5 * rng.random()
            ep = .01 + 3 * rng.random()
            mult = 1.00001 + (10**(5*rng.random()))
            h = mult * 2 * ep / la
            r, jp, jm = matrices(h, la, ep, beta)
            assert r > 0
            xr, v = F(r, la * la * r * r, h, la, ep, beta)
            assert isclose(xr, -r, rel_tol=1e-9, abs_tol=1e-8)
            assert isclose(v, la * la * r * r, rel_tol=1e-9, abs_tol=1e-8)
            rho, t, eig = spectral(h, la, ep, beta)
            m = matmul(jm, jp)
            assert isclose(float(m[0][0] + m[1][1]), t*t - 2*beta, rel_tol=1e-9, abs_tol=1e-9)
            assert isclose(float(m[0][0]*m[1][1]-m[0][1]*m[1][0]), beta*beta, rel_tol=1e-8, abs_tol=1e-9)
            assert rho < 1 and rho + 1e-10 >= beta
            if t*t < 4*beta:
                assert isclose(rho, beta, rel_tol=1e-10, abs_tol=1e-10)
            checked += 1
    assert checked == 720
    print('PARAMETER_GRID_OK', checked)


def test_boundaries():
    for beta in [0.01, .04, .10, 1/9, .2, .5, .9]:
        hi = 4*(1-beta)/(1-3*beta+2*sqrt(beta))
        assert hi > 2
        ri, ti, _ = spectral(hi, 1, 1, beta)
        assert isclose(ti, 2*sqrt(beta), rel_tol=1e-11, abs_tol=1e-11)
        assert isclose(ri, beta, rel_tol=5e-7, abs_tol=5e-7)
        denom = 1 - 3*beta-2*sqrt(beta)
        if beta < 1/9:
            assert denom > 0
            ho = 4*(1-beta)/denom
            assert ho > hi
            ro, to, _ = spectral(ho, 1, 1, beta)
            assert isclose(to, -2*sqrt(beta), rel_tol=1e-9, abs_tol=1e-9)
            assert isclose(ro, beta, rel_tol=5e-7, abs_tol=5e-7)
            assert spectral(ho*2, 1, 1, beta)[0] > beta+1e-10
        else:
            assert denom <= 1e-14
    print('BOUNDARIES_OK')




def test_jacobian_finite_differences():
    checked = 0
    for be in (0.04, 0.20, 0.8):
        for h in (2.5, 3.0, 4.0, 8.0):
            r, jp, jm = matrices(h, 1.0, 1.0, be)
            for x, expected in ((r, jp), (-r, jm)):
                v = r*r
                for k in range(2):
                    dx, dv = ((1e-6, 0.0) if k == 0 else (0.0, 1e-6))
                    forward = F(x+dx, v+dv, h, 1.0, 1.0, be)
                    backward = F(x-dx, v-dv, h, 1.0, 1.0, be)
                    for i in range(2):
                        numerical = (forward[i]-backward[i])/(2e-6)
                        analytical = expected[i][k]
                        assert isclose(numerical, analytical, rel_tol=5e-7, abs_tol=5e-8), (h, be, k, i, numerical, analytical)
            checked += 1
    print('FINITE_DIFFERENCE_JACOBIANS_OK', checked)

if __name__ == '__main__':
    test_exact_cases()
    test_parameter_grid()
    test_boundaries()
    test_jacobian_finite_differences()
    print('VERIFY_OK')
