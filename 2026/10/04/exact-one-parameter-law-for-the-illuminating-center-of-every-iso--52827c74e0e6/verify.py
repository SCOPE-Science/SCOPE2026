#!/usr/bin/env python3
import math


def root(lam):
    lo, hi = 0.0, 0.5
    for _ in range(180):
        q = (lo + hi) / 2.0
        v = lam * q * math.tan(math.pi * q)
        if v < 1.0:
            lo = q
        else:
            hi = q
    return (lo + hi) / 2.0


def check(lam):
    q = root(lam)
    assert 0.0 < q < 0.5
    lhs = lam * q * math.tan(math.pi * q)
    assert abs(lhs - 1.0) < 2e-14
    angle_geom = 2.0 * math.atan(1.0 / (lam * q))
    angle_area = 2.0 * math.pi * q
    assert abs(angle_geom - angle_area) < 2e-14
    return q

qs = [check(x) for x in (0.25, 0.5, 1.0, 2.0, 4.0)]
assert all(qs[i] > qs[i+1] for i in range(len(qs)-1))
q = qs[2]
t = (1.0 - q) / 2.0
published = 0.3082756986146550422567206
assert abs(t - published) < 3e-16
print('VERIFY_OK')
print('q_lambda_1=%.17g' % q)
print('t_right_isosceles=%.17g' % t)
