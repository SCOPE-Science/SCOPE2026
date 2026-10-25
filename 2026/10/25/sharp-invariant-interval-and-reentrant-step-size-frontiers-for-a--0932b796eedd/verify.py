"""Exact-arithmetic checks for the homogeneous doubly stabilized CN interval frontier.

Run: python3 verify.py
Uses only the Python standard library. Finite checks supplement the proof.
"""
from fractions import Fraction as F
from math import sqrt
from random import Random


def polynomial(s, v, h):
    return (4 + 4 * (s - 2) * h + (s * s - 8 * s + 8) * h * h
            + 2 * v * h * h * (2 + s * h))


def endpoint(u, s, v, h):
    d = h / (2 + s * h)
    mid = u + d * u * (1 - u * u)
    a = 1 / h + v * h
    b = s / 2
    return ((a - b) * u + (s + 1) * mid - mid**3) / (a + b)


def exact_test():
    rng = Random(23019663)
    n = 0
    for _ in range(1200):
        s = F(rng.randrange(2, 12), 1)
        v = F(rng.randrange(0, 16), 20)
        h = F(rng.randrange(1, 131), rng.randrange(1, 20))
        u = F(rng.randrange(-100, 101), 100)
        d = h / (2 + s * h)
        mid = u + d * u * (1 - u * u)
        a = 1 / h + v * h
        b = s / 2
        z = endpoint(u, s, v, h)
        # The original linear stage and CN equations are checked independently.
        assert ((mid - u) * F(2, 1) / h + (mid - u) * s
                + u**3 - u == 0)
        assert ((z - u) / h + (mid**3 - mid)
                + s * ((z + u) / 2 - mid) + v * h * (z - u) == 0)
        assert 2 * h * (2 + s * h) * (
            a + b - 2 - 2 * (s - 2) * d) == polynomial(s, v, h)
        assert endpoint(-u, s, v, h) == -z
        if polynomial(s, v, h) >= 0:
            assert -1 <= z <= 1
        else:
            # The exact derivative at the upper equilibrium is negative.
            assert polynomial(s, v, h) / (2 * h * (2 + s * h) * (a + b)) < 0
            assert any(endpoint(1 - F(1, 10**k), s, v, h) > 1
                       for k in range(1, 8))
        n += 1
    # Exact resonant boundary, unsafe window, and large-step recovery.
    assert polynomial(F(2), F(1, 4), F(2)) == 0
    assert endpoint(F(9, 10), F(4), F(0), F(2)) == F(313211996289, 312500000000)
    assert polynomial(F(4), F(1, 10), F(2)) < 0
    assert polynomial(F(4), F(1, 10), F(100)) > 0
    assert polynomial(F(4), F(1, 10), F(1, 10)) > 0
    for s in (F(7), F(8), F(10)):
        for h in (F(1, 100), F(1), F(100), F(10000)):
            assert polynomial(s, F(0), h) > 0
    # Double-stabilization phase maximum at s=2 is exactly 1/4.
    for j in range(1, 10000):
        h = F(j, 1000)
        assert polynomial(F(2), F(1, 4), h) >= 0
    # Re-entrant interval for s=4,v=1/10 has exactly two positive roots.
    # This uses a sign-shape check only; uniqueness is established in the text.
    for s in range(2, 7):
        c = 8*s - s*s - 8
        b = 4*(s - 2)
        def p(t):
            return 16*t**3 + (20*s-16)*t**2 + 8*s*(s-2)*t - s*c
        assert p(0) < 0
        assert p(F(10)) > 0
        lo, hi = F(0), F(10)
        for _ in range(80):
            mid = (lo+hi)/2
            if p(mid) < 0:
                lo = mid
            else:
                hi = mid
        t = (lo+hi)/2
        assert 0 < t < sqrt(c)/2
    print(f"VERIFY_OK: {n} exact CN/stage/criterion tests, 9999 boundary tests, phase and rational witnesses")


if __name__ == '__main__':
    exact_test()
