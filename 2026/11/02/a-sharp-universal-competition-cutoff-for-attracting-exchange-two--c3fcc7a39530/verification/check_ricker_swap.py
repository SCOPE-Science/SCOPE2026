#!/usr/bin/env python3
"""Reproducible numerical and algebraic diagnostics for a symmetric Ricker map.

The universal statements are proved in RESULT.md; numerical sampling here
checks the derived identities and finite illustrative cases, not all parameters.
Requires Python 3 standard library only.
"""
import math
import random


def swap_point(g, z):
    assert 0 <= g < 1 and 0 < z < 1
    A = math.atanh(z) / z
    S = 4 * A / (1 - g)
    u, v = S * (1 + z) / 2, S * (1 - z) / 2
    R = math.exp((1 + g) * S / 2)
    return R, u, v, A, S


def F(R, g, x, y):
    return (R * x * math.exp(-x - g * y),
            R * y * math.exp(-y - g * x))


def one_step_swapped_J(g, u, v):
    return ((-g * u, (u / v) * (1 - v)),
            ((v / u) * (1 - u), -g * v))


def mul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(2))
             for j in range(2)] for i in range(2)]


def jacobian_F(R, g, x, y):
    fx, fy = F(R, g, x, y)
    return [[fx * (1 / x - 1), -g * fx],
            [-g * fy, fy * (1 / y - 1)]]


def schur_conditions(g, z):
    _, u, v, A, S = swap_point(g, z)
    B = one_step_swapped_J(g, u, v)
    tr = B[0][0] + B[1][1]
    det = B[0][0] * B[1][1] - B[0][1] * B[1][0]
    t = (1 - z * z) * A
    # The third condition 1 - trace + determinant is automatically positive.
    c_plus = 4 * A * (1 - (1 + g) / (1 - g) * t)
    c_minus = (1 + g) * S * (1 - t)
    c_det = S * ((1 + g) * t - 1 + (1 - g) / (2 * A))
    assert math.isclose(1 + tr + det, c_plus, abs_tol=3e-9, rel_tol=3e-11)
    assert math.isclose(1 - tr + det, c_minus, abs_tol=3e-9, rel_tol=3e-11)
    assert math.isclose(1 - det, c_det, abs_tol=3e-9, rel_tol=3e-11)
    return c_plus > 0 and c_det > 0 and c_minus > 0, (tr, det, c_plus, c_minus, c_det)


def bisect(f, lo, hi, n=100):
    flo = f(lo)
    assert flo * f(hi) < 0
    for _ in range(n):
        mid = (lo + hi) / 2
        if f(mid) * flo <= 0:
            hi = mid
        else:
            lo, flo = mid, f(mid)
    return (lo + hi) / 2


def thresholds(g):
    def A(z):
        return math.atanh(z) / z
    def t(z):
        return (1 - z * z) * A(z)
    z_flip = bisect(lambda z: t(z) - (1 - g) / (1 + g), 1e-9, 1 - 1e-13)
    z_det = bisect(lambda z: (1 + g) * t(z) + (1 - g) / (2 * A(z)) - 1,
                   1e-9, 1 - 1e-13)
    return z_flip, z_det


def main():
    zstar = bisect(lambda z: (1 - z * z) * math.atanh(z) - z**3,
                   0.2, 0.999999)
    Astar = math.atanh(zstar) / zstar
    gstar = 1 / (1 + 2 * Astar)
    assert 0.75175950 < zstar < 0.75175951
    assert 0.27783903 < gstar < 0.27783905
    print('critical z = %.14f; gamma = %.14f' % (zstar, gstar))

    for g in (0.01, 0.1, 0.25, 0.277, 0.278, 0.30, 0.5):
        zl, zr = thresholds(g)
        assert (zl < zr) == (g < gstar)
        print('gamma %.4f: flip %.12f, determinant %.12f, stable %s' %
              (g, zl, zr, zl < zr))
        for z in (0.001, zl * 0.7, min(0.999, (zl + zr) / 2), zr, min(0.999, zr + 0.015)):
            if z <= 0 or z >= 1: continue
            stable, _ = schur_conditions(g, z)
            if abs(z - zl) > 1e-6 and abs(z - zr) > 1e-6:
                assert stable == (zl < z < zr)

    g, z = 1/10, 3/5
    R, u, v, _, S = swap_point(g, z)
    ell = math.log(2)
    assert math.isclose(u, 160 * ell / 27, rel_tol=2e-14)
    assert math.isclose(v, 40 * ell / 27, rel_tol=2e-14)
    assert math.isclose(R, 2**(110/27), rel_tol=2e-14)
    a, b = F(R, g, u, v)
    assert math.isclose(a, v, rel_tol=1e-14)
    assert math.isclose(b, u, rel_tol=1e-14)
    stable, (tr, det, cp, cm, cd) = schur_conditions(g, z)
    assert stable and cp > 0.44 and cm > 0.0 and cd > 1.04
    assert math.isclose(tr, -20 * ell / 27, rel_tol=2e-14)
    assert math.isclose(det, 200 * ell / 27 - 1 - 704 * ell**2 / 81,
                        abs_tol=2e-14)

    B = one_step_swapped_J(g, u, v)
    B2 = mul(B, B)
    monodromy = mul(jacobian_F(R, g, v, u), jacobian_F(R, g, u, v))
    assert max(abs(B2[i][j] - monodromy[i][j]) for i in range(2) for j in range(2)) < 1e-13
    for j in range(2):
        h = 1e-6
        p = [u, v]
        pp = p.copy(); pp[j] += h
        pm = p.copy(); pm[j] -= h
        rp = F(R, g, *F(R, g, *pp))
        rm = F(R, g, *F(R, g, *pm))
        for i in range(2):
            d = (rp[i] - rm[i]) / (2 * h)
            assert abs(d - B2[i][j]) < 2e-8
    rng = random.Random(20261028)
    for _ in range(300):
        g = rng.uniform(1e-3, 0.95)
        z = rng.uniform(1e-3, 0.98)
        R, u, v, _, _ = swap_point(g, z)
        if R > 1e300: continue
        a, b = F(R, g, u, v)
        assert abs(a/v - 1) < 3e-11 and abs(b/u - 1) < 3e-11
        schur_conditions(g, z)
    print('Exact-form example, monodromy, 300 numerical samples: passed')


if __name__ == '__main__':
    main()
