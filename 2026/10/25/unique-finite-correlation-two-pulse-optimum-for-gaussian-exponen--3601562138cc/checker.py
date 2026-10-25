#!/usr/bin/env python3
"""Independent finite numerical tests for two-switch exponential-kernel dephasing.
Run with Python 3 standard library only. Numerical evidence is not the proof.
"""
import math
import random


def quad_recurrence(a, b, c):
    v = 0.0
    q = 0.0
    for ell, sign in ((a, 1), (b, -1), (c, 1)):
        one_minus = -math.expm1(-ell)
        q += 2.0 * (ell + sign * (v - sign) * one_minus)
        v = sign + (v - sign) * math.exp(-ell)
    return q


def quad_independent(a, b, c):
    lengths = [a, b, c]
    signs = [1, -1, 1]
    ans = 2.0 * sum(x + math.expm1(-x) for x in lengths)
    for i in range(3):
        for j in range(i + 1, 3):
            gap = sum(lengths[i + 1:j])
            ans += 2 * signs[i] * signs[j] * (-math.expm1(-lengths[i])) * (-math.expm1(-lengths[j])) * math.exp(-gap)
    return ans


def opt_pulses(L):
    def f(b):
        # log cosh without overflow
        z = b / 2
        logcosh = z + math.log1p(math.exp(-2 * z)) - math.log(2)
        return 2 * b + 2 * logcosh - L
    lo, hi = 0.0, L
    for _ in range(100):
        mid = (lo + hi) / 2
        if f(mid) > 0:
            hi = mid
        else:
            lo = mid
    b = (lo + hi) / 2
    return (L-b)/2, b, (L-b)/2


def run():
    rng = random.Random(420933)
    tests = 0
    for _ in range(800):
        a, b, c = [math.exp(rng.uniform(-4, 2)) for j in range(3)]
        left = quad_recurrence(a, b, c)
        right = quad_independent(a, b, c)
        assert abs(left - right) < 4e-12 * (1 + abs(right)), (a,b,c,left,right)
        tests += 1
    for L in (0.015, 0.1, 0.3, 1, 2, 5, 12, 40, 100):
        a,b,c = opt_pulses(L)
        assert L/3 < b < L/2 and a == c
        optimized = quad_independent(a,b,c)
        cpmg = quad_independent(L/4,L/2,L/4)
        assert optimized < cpmg - 1e-14, (L,optimized,cpmg)
        # At every fixed inner interval, asymmetric outer durations lose.
        for fraction in (0.02, 0.1, 0.3, 0.7, 0.9, 0.98):
            aa = fraction * (L-b)
            cc = L-b-aa
            assert quad_independent(aa,b,cc) > optimized + 1e-14
        # Compare with many unconstrained two-pulse candidates, not just symmetric ones.
        for _ in range(300):
            a2 = rng.uniform(0,L)
            b2 = rng.uniform(0,L-a2)
            c2 = L-a2-b2
            q2 = quad_independent(a2,b2,c2)
            assert q2 >= optimized - 1e-11,(L,a2,b2,c2,q2,optimized)
            tests += 1
        tests += 1
    print('PASS:',tests,'independent block-kernel and optimization comparisons')
    print('L=2 optimized lengths:', tuple(round(x, 10) for x in opt_pulses(2)))
    print('No sampled competitor improved the analytically unique optimizer.')


if __name__=='__main__':
    run()
