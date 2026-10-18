#!/usr/bin/env python3
"""Supplementary scalar-trace diagnostic; not an infinite-dimensional proof.

Requires Python and mpmath.  Every integral is taken over the full positive
half-line; no finite matrix is used as a certificate.
"""
import mpmath as mp
mp.mp.dps = 35
for beta in (mp.mpf('1.5'), mp.mpf('2.0')):
    leading = mp.gamma(beta-1)/2
    first = mp.euler*mp.gamma(beta)
    for q in (10, 20, 50):
        trace = mp.quad(lambda x: x**(beta-1)*mp.exp(-x)
                        * mp.zeta(1+2*x/q)/q, [0, 1, 10, mp.inf])
        residual_scaled = q**2 * (trace-leading-first/q)
        print('beta=',mp.nstr(beta,3),'q=',q,
              'trace=',mp.nstr(trace,14),
              'q^2 residual=',mp.nstr(residual_scaled,12))
        assert abs(residual_scaled) < 1
print('scalar trace diagnostics: PASS')
