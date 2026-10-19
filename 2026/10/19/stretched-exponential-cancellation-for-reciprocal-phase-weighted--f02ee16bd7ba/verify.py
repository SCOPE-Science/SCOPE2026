#!/usr/bin/env python3
"""Supplementary numerical check of reciprocal-phase weighted Bergman moments.

Requires mpmath; execute: python verify.py. The asymptotic theorem is proved
analytically, not by the finite evaluations made here.
"""
import mpmath as mp

mp.mp.dps = 70
zeta = mp.exp(-mp.pi*1j/4)


def weighted_moment(n, alpha):
    # The contour 0 -> exp(-pi*i/4) -> 1 is homotopic to (0,1).
    # It damps the oscillatory essential singularity at the origin.
    def f(s):
        return s**alpha * (1-s)**n * mp.exp(1j/s)
    radial = mp.quad(lambda t: zeta*f(zeta*t), [0, .002, .02, .1, .3, 1])
    bridge = mp.quad(lambda t: (1-zeta)*f(zeta+(1-zeta)*t), [0, 1])
    return (radial + bridge)/mp.beta(n+1, alpha+1)


def predicted(n, alpha):
    return (mp.sqrt(mp.pi)/mp.gamma(alpha+1)
        * n**(alpha/2+mp.mpf('0.25'))
        * mp.exp(-mp.sqrt(2*n)*(1-1j))
        * mp.exp(1j*(mp.mpf('0.5')-mp.pi*(2*alpha+1)/8)))


checks = 0
for alpha in [mp.mpf('-0.5'), mp.mpf('0'), mp.mpf('1'), mp.mpf('2')]:
    errors = []
    for n in [50, 200, 800]:
        ratio = weighted_moment(n, alpha)/predicted(mp.mpf(n), alpha)
        err = abs(ratio-1)
        assert err < 4/mp.sqrt(n), (alpha, n, ratio, err)
        errors.append(err)
        checks += 1
    assert errors[2] < errors[1] < errors[0], (alpha, errors)
    checks += 1
print(f'VERIFY_OK {checks} deformed-contour/asymptotic comparisons and decay checks; four weights; n=50,200,800')
