"""Finite sanity check for the inverse asymptotic bracket, not an infinite proof."""
from math import e, exp, log
GAMMA = 0.5772156649015328606
c = exp(GAMMA)
for k in (10000, 100000, 1000000):
    L = log(k)
    mid = L + log(L) + GAMMA
    left = c*k*(mid - 1.0)
    right = c*k*(mid + 1.0)
    fl = exp(-GAMMA)*left/log(left)
    fr = exp(-GAMMA)*right/log(right)
    assert fl < k < fr, (k, fl, fr)
print("VERIFY_OK", "inversion_brackets=3")
