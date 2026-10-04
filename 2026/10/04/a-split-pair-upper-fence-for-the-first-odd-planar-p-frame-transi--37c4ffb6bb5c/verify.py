#!/usr/bin/env python3
import math


def fp_from_angles(angles, p):
    total = 0.0
    for i, a in enumerate(angles):
        for j, b in enumerate(angles):
            if i != j:
                total += abs(math.cos(a-b))**p
    return total


def split_angles(k, alpha):
    return [0.0]*k + [math.pi/2]*(k-1) + [math.pi/2-alpha, math.pi/2+alpha]


def perp_angles(k):
    return [0.0]*(k+1) + [math.pi/2]*k


def F(k, p, alpha):
    c = math.cos(alpha)
    s = math.sin(alpha)
    d = math.cos(2*alpha)
    return 2*(k-1)*c**p + 2*k*s**p + d**p - (2*k-1)


def root(k, alpha):
    lo, hi = 0.0, 2.0
    for _ in range(100):
        mid = (lo+hi)/2
        if F(k, mid, alpha) > 0:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2


def asymptotic_constant(alpha):
    c = math.cos(alpha)
    s = math.sin(alpha)
    d = math.cos(2*alpha)
    return (1 - 2*c*c + d*d)/(2*(c*c*math.log(c) + s*s*math.log(s)))


for k in range(2, 13):
    for alpha in (math.pi/9, math.pi/8, math.pi/7):
        for p in (1.2, 1.7, 1.95):
            direct = (fp_from_angles(split_angles(k, alpha), p)
                      - fp_from_angles(perp_angles(k), p))/2
            assert abs(direct - F(k, p, alpha)) < 2e-10
        assert F(k, 1e-9, alpha) > 0
        assert F(k, 2.0, alpha) < 0
        q = root(k, alpha)
        assert 0 < q < 2
        assert abs(F(k, q, alpha)) < 2e-12

c8 = asymptotic_constant(math.pi/8)
assert abs(c8 - 0.49726051282860247) < 2e-15
for k in (100, 1000, 10000):
    q = root(k, math.pi/8)
    assert abs(k*(2-q) - c8) < 0.003

q5 = root(2, math.pi/7)
assert abs(q5 - 1.7776626430852609) < 2e-15
print('VERIFY_OK pair_count_cases=108 roots=33 asymptotic_k=100,1000,10000 q5_pi7=%.15f C8=%.15f' % (q5, c8))
