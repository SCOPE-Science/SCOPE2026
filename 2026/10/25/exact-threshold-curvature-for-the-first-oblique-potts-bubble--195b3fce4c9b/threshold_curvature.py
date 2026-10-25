#!/usr/bin/env python3
"""Reproduce the high-precision threshold-curvature evaluation."""
import mpmath as mp

mp.mp.dps = 50

def G(alpha):
    return mp.besselj(1 - alpha, alpha) + 4 * mp.besselj(-alpha, alpha)

# The sign change brackets the first root corresponding to the reported threshold.
alpha = mp.findroot(G, (mp.mpf("0.90"), mp.mpf("0.91")))
a1 = mp.mpf(4) / (3 * alpha)
Gprime = mp.diff(G, alpha)  # total derivative: order and argument both vary
Jden = mp.besselj(1 - alpha, alpha)
c1 = -(mp.mpf(3) * alpha**2 / 4) * Gprime / Jden
K = mp.mpf(2) * c1**2 / 3

print("alpha_star =", mp.nstr(alpha, 40))
print("a1 =", mp.nstr(a1, 40))
print("G(alpha_star) =", mp.nstr(G(alpha), 8))
print("Gprime =", mp.nstr(Gprime, 40))
print("Jden =", mp.nstr(Jden, 40))
print("c1 =", mp.nstr(c1, 40))
print("K =", mp.nstr(K, 40))
print("Note: these are high-precision floating-point values, not interval certificates.")
