#!/usr/bin/env python3
import math


def p_source(m, x):
    a = 2 ** (m - 1)
    if x == 0.0:
        return 0.5
    num = math.exp(-(a - 1) * x) * (
        math.sinh((3 * a - 1) * x) - math.sinh((a - 1) * x)
    )
    den = 2 * math.sinh(2 * a * x)
    return num / den


def p_simple(m, x):
    a = 2 ** (m - 1)
    return 0.5 * (1 + math.exp(-2 * (2 * a - 1) * x)) / (1 + math.exp(-2 * a * x))


def F(a, q):
    return (2 * a - 1) * q ** (a - 1) + (a - 1) * q ** (2 * a - 1) - a


def root_q(a):
    lo, hi = 0.0, 1.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if F(a, mid) < 0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def main():
    checks = 0
    for m in range(2, 8):
        for x in (0.01, 0.03, 0.07, 0.15, 0.3, 0.6, 1.0):
            a = 2 ** (m - 1)
            # Avoid direct sinh overflow in this modest test range.
            if (3 * a - 1) * x < 700:
                ps = p_source(m, x)
                pq = p_simple(m, x)
                assert abs(ps - pq) < 2e-12 * max(1.0, abs(ps), abs(pq))
                checks += 1

    prev_scaled = None
    prev_min = None
    for m in range(2, 15):
        a = 2 ** (m - 1)
        q = root_q(a)
        assert 0 < q < 1
        assert F(a, q * (1 - 1e-8)) < 0
        assert F(a, min(1.0, q * (1 + 1e-8))) > 0
        x = -0.5 * math.log(q)
        pm = p_simple(m, x)
        eps = min(1e-5, x / 10)
        assert p_simple(m, x - eps) > pm
        assert p_simple(m, x + eps) > pm
        scaled = (2 ** m) * x
        if m >= 5 and prev_scaled is not None:
            assert abs(scaled - math.asinh(1.0)) < abs(prev_scaled - math.asinh(1.0))
        if m >= 5 and prev_min is not None:
            assert abs(pm - (math.sqrt(2) - 1)) < abs(prev_min - (math.sqrt(2) - 1))
        prev_scaled, prev_min = scaled, pm

    m = 14
    a = 2 ** (m - 1)
    q = root_q(a)
    x = -0.5 * math.log(q)
    pm = p_simple(m, x)
    print('VERIFY_OK')
    print('identity_checks=', checks)
    print('limit_scaled_location=', math.asinh(1.0))
    print('limit_minimum=', math.sqrt(2) - 1)
    print('limit_uniform_defect=', 1.5 - math.sqrt(2))
    print('m14_scaled_location=', (2 ** m) * x)
    print('m14_minimum=', pm)


if __name__ == '__main__':
    main()
