#!/usr/bin/env python3
"""Numerical corroboration for the strict-unimodality theorem.

The global monotonicity proof is analytic and appears in RESULT.md.  This
script only reproduces the decimal root and maximum quoted there.
"""
import mpmath as mp

mp.mp.dps = 60

def H(p):
    p = mp.mpf(p)
    L = mp.log(mp.beta(mp.mpf("0.5"), p-mp.mpf("0.5")))
    Lp = mp.digamma(p-mp.mpf("0.5")) - mp.digamma(p)
    return mp.log(2/(p-1)) - L + p*Lp

def A(p):
    p = mp.mpf(p)
    loga = (mp.log(p)
            + ((p-1)/p)*mp.log(2/(p-1))
            + mp.log(mp.beta(mp.mpf("0.5"), p-mp.mpf("0.5")))/p)
    return mp.e**loga

root = mp.findroot(H, (mp.mpf("1.2"), mp.mpf("1.4")))
assert mp.mpf("1.31709") < root < mp.mpf("1.31710")
assert H(mp.mpf("1.31")) > 0
assert H(mp.mpf("1.32")) < 0
peak = A(root)
assert abs(peak-mp.mpf("3.8219877526570496723")) < mp.mpf("1e-18")
print("VERIFY_OK p_star=%s peak=%s H_1.31=%s H_1.32=%s" %
      (mp.nstr(root, 18), mp.nstr(peak, 18), mp.nstr(H(mp.mpf("1.31")), 8), mp.nstr(H(mp.mpf("1.32")), 8)))
