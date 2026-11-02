#!/usr/bin/env python3
"""Reproduce finite checks for a dissipative sine-twist period-doubling theorem."""
import cmath
import math

PI = math.pi
K = 2 * PI

def critical(lam):
    return math.sqrt(2 * (1 + lam * lam))

def step(x, y, lam, t):
    yp = lam * y + (t / K) * math.sin(K * x)
    return ((x + 0.5 + yp) % 1.0, yp)

def eq(u, v, lam, t):
    a, b = 1 + lam, 1 - lam
    return (t / K * math.sin(K * u) + a * u - b * v,
            t / K * math.sin(K * v) - b * u - a * v)

def solve(lam, mu):
    a, b, tc = 1 + lam, 1 - lam, critical(lam)
    s = math.sqrt(6 * mu / (K * K * (tc * tc + a * a) * (tc + a)))
    u, v = s * b, s * (tc + a)
    t = tc + mu
    for _ in range(35):
        f, g = eq(u, v, lam, t)
        j11 = t * math.cos(K * u) + a
        j22 = t * math.cos(K * v) - a
        det = j11 * j22 - b * b
        du = (j22 * f + b * g) / det
        dv = (b * f + j11 * g) / det
        u -= du
        v -= dv
        if abs(du) + abs(dv) < 1e-16:
            break
    assert u > 0 and v > 0
    assert max(abs(x) for x in eq(u, v, lam, t)) < 2e-12
    return u, v, s

def circular_error(a, b):
    return abs(((a - b + 0.5) % 1) - 0.5)

def spectrum2(lam, p, q):
    # p = first phase derivative, q = minus second phase derivative.
    tr = 1 + lam * lam - p * q + (1 + lam) * (p - q)
    disc = cmath.sqrt(tr * tr - 4 * lam * lam)
    return (tr, (tr + disc) / 2, (tr - disc) / 2)

def check():
    checks = 0
    for lam in (0.1, 0.3, 0.5, 0.8, 0.9, 0.98):
        tc = critical(lam)
        for frac in (0.5, 0.95, 1.05, 1.5):
            t = frac * tc
            tr = 1 + lam * lam - t * t
            c1 = 1 - tr + lam * lam
            c2 = 1 + tr + lam * lam
            assert (c1 > 0 and c2 > 0) == (t < tc)
            checks += 1
        tr, e1, e2 = spectrum2(lam, tc, tc)
        assert abs(tr + 1 + lam * lam) < 1e-11
        assert min(abs(e1 + 1), abs(e2 + 1)) < 1e-10
        assert min(abs(e1 + lam * lam), abs(e2 + lam * lam)) < 1e-10
        checks += 3
        for mu in (1e-4, 2e-5, 5e-6):
            u, v, s = solve(lam, mu)
            t = tc + mu
            points = [(u, u+v), (0.5+v, v-u), (-u, -u-v), (0.5-v, u-v)]
            for i in range(4):
                x1, y1 = step(*points[i], lam, t)
                xt, yt = points[(i+1)%4]
                assert circular_error(x1, xt % 1) < 1e-10
                assert abs(y1 - yt) < 1e-10
                checks += 2
            assert abs(math.hypot(u, v) / (s * math.hypot(1-lam, tc+1+lam)) - 1) < 0.003
            checks += 1
            tr, e1, e2 = spectrum2(lam, t*math.cos(K*u), t*math.cos(K*v))
            assert abs((tr + 1 + lam*lam) / mu - 4 * tc) < 0.01
            assert abs(e1) < 1 and abs(e2) < 1
            assert abs(e1*e2 - lam*lam) < 1e-10
            checks += 3
    print('PASS:', checks, 'finite consistency assertions across six damping values')

if __name__ == '__main__':
    check()
