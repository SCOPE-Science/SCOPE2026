#!/usr/bin/env python3
import mpmath as mp

mp.mp.dps = 80

def a(y):
    return mp.mpf("0.5") * mp.log((y**4 + 6*y**2 + 1) / 4)

def b(y):
    return mp.atan(2*y / (1 + y**2))

def N(y):
    return a(y)*y*(y**2 + 3) + b(y)*(1 - y**2)

lo = mp.mpf("0.2241944779358")
hi = mp.mpf("0.2241944779360")
assert N(lo) < 0
assert N(hi) > 0

for _ in range(240):
    mid = (lo + hi) / 2
    if N(mid) < 0:
        lo = mid
    else:
        hi = mid

y = (lo + hi) / 2
lam = mp.sqrt(a(y)**2 + b(y)**2)

assert mp.mpf("0.2241944779359010240194013274") < y
assert y < mp.mpf("0.2241944779359010240194013276")
assert mp.mpf("0.6905440336407464277786112388") < lam
assert lam < mp.mpf("0.6905440336407464277786112390")
assert lam < mp.log(2)

print("VERIFY_OK")
print("y_star =", mp.nstr(y, 60))
print("lambda_uc =", mp.nstr(lam, 60))
print("log2_minus_lambda =", mp.nstr(mp.log(2)-lam, 40))
