#!/usr/bin/env python3
"""Supplementary finite diagnostics for Fourier-cutoff Fock-weight formulas.

These checks are supplementary. The theorem uses analytic Fourier Plancherel,
Gaussian integration, and norm convergence; finite quadratures prove none of
those infinite-dimensional assertions.
"""
from __future__ import annotations
import cmath
import math


def simpson(fun, lo, hi, steps):
    assert steps >= 2 and steps % 2 == 0
    h = (hi - lo) / steps
    acc = fun(lo) + fun(hi)
    for j in range(1, steps):
        acc += (4 if j % 2 else 2) * fun(lo + j * h)
    return acc * h / 3


def g_one_cut(z: complex, eps: float = 0.0) -> complex:
    if abs(z) < 1e-12:
        return 1 - eps
    return (cmath.exp(1j * z) - cmath.exp(1j * eps * z)) / (1j * z)


def gamma_cutoff_hs_squared(lam: float, gamma: float, eps: float) -> float:
    a = 1 - lam * lam
    # u=-log(t) converts t^(2gamma-2) dt to exp(-(2gamma-1)u) du.
    return math.sqrt(2 * math.pi / a) * simpson(
        lambda u: math.exp(-(2*gamma-1)*u + math.exp(-2*u)/(2*a)),
        0.0, -math.log(eps), 10000)


def main():
    lam = .6
    a = 1 - lam*lam
    for y in (0.0, 0.6, 1.5):
        for eps in (0.0, .2):
            numer = simpson(lambda x: abs(g_one_cut(complex(x,y), eps))**2,
                            -300, 300, 60000)
            exact = 2*math.pi * (math.exp(-2*y*eps)-math.exp(-2*y))/(2*y) if y else 2*math.pi*(1-eps)
            assert abs(numer-exact)/exact < .012, (y,eps,numer,exact)
    for gam in (.25,.5,.75,1.0):
        for eps in (.25,.08,.02):
            hs = gamma_cutoff_hs_squared(lam,gam,eps)
            assert hs>0 and math.isfinite(hs)
            if gam == .5:
                ratio = hs/(math.sqrt(2*math.pi/a)*math.log(1/eps))
                assert ratio >=1.0
            if gam < .5:
                assert gamma_cutoff_hs_squared(lam,gam,eps*.5) > hs
    # The singular Hilbert-Schmidt critical exponent has unit residue.
    for delta in (.1,.04,.01):
        gamma = (1 + delta)/2
        hs = math.sqrt(2*math.pi/a) * simpson(
            lambda u: math.exp(-delta*u + math.exp(-2*u)/(2*a)),
            0.0, max(40,32/delta), int(16000/delta)//2*2)
        scaled = delta*hs/math.sqrt(2*math.pi/a)
        assert 1 < scaled < 1.7, (delta, scaled)
    print('PASS: finite Gaussian-Fourier cutoff quadratures, cutoff behavior, and critical residue diagnostics')


if __name__ == '__main__':
    main()
