#!/usr/bin/env python3
import math

c = 3.0 ** (4.0 / 3.0)

def f(t):
    return c * (1.0 + t) ** 2 - t * ((1.0 + t) ** 2 + 8.0)

lo, hi = 2.0, 3.0
assert f(lo) > 0.0 and f(hi) < 0.0
for _ in range(200):
    mid = (lo + hi) / 2.0
    if f(mid) > 0.0:
        lo = mid
    else:
        hi = mid
tau = (lo + hi) / 2.0

r0 = 3.0 ** (-4.0 / 3.0)
A = (9.0 / 8.0) ** (2.0 / 3.0)
B = 1.0 / (4.0 * r0)
assert abs(A - B) < 1e-14

d2 = (8.0 + (1.0 + tau) ** 3) ** (2.0 / 3.0) / (c + tau * tau)
d = math.sqrt(d2)

assert 2.76673988007869 < tau < 2.76673988007872
assert 1.29958204360102 < d2 < 1.29958204360106
assert 1.13999212435920 < d < 1.13999212435924

print("VERIFY_OK")
print("tau=%.17g" % tau)
print("d2=%.17g" % d2)
print("d=%.17g" % d)
