#!/usr/bin/env python3
"""Exact-rational checks for the pointwise Delta constant on finite real cubes.

No third-party dependencies. The proof is analytic; these checks independently
exercise constructive convex witnesses and strict separating functionals.
"""
from fractions import Fraction as F
from itertools import product

ZERO, ONE = F(0), F(1)


def capacities(x, r):
    """Opposite-face weights, valid above b_* = max(1-x_i)."""
    assert r > 0 and all(ZERO <= a <= ONE for a in x)
    return [((ONE - a) / (r + ONE - a)
             if r <= ONE + a else ZERO) for a in x]


def full_capacities(x, r):
    """All signed far faces, including the low-radius regime."""
    ans = ZERO
    for a in x:
        if r <= ONE - a:
            ans += (ONE + a) / (r + ONE + a)
        if r <= ONE + a:
            ans += (ONE - a) / (r + ONE - a)
    return ans


def witness(x, r):
    """Return rational far points and barycentric weights if feasible."""
    n = len(x)
    bstar = max(ONE - a for a in x)
    if r <= bstar:
        i = next(i for i, a in enumerate(x) if ONE - a == bstar)
        p = list(x); m = list(x)
        p[i] = ONE; m[i] = 2 * x[i] - ONE
        return [(F(1, 2), p), (F(1, 2), m)]
    c = capacities(x, r)
    total = sum(c, ZERO)
    if total < ONE:
        return None
    lam = [z / total for z in c]
    out = []
    for j in range(n):
        if lam[j] == 0:
            continue
        v = []
        for i in range(n):
            if i == j:
                v.append(x[i] - r)
            else:
                v.append(x[i] + (lam[i] * r) / (ONE - lam[i]))
        out.append((lam[j], v))
    return out


def test(x, r):
    global checks, constructions, separations
    bstar = max(ONE - a for a in x)
    expected = full_capacities(x, r) >= 1
    cert = witness(x, r)
    assert (cert is not None) == expected, (x, r, cert, expected)
    if cert is not None:
        assert sum((lam for lam, _ in cert), ZERO) == 1
        for i, ai in enumerate(x):
            assert sum((lam * v[i] for lam, v in cert), ZERO) == ai
        for lam, v in cert:
            assert lam > 0
            assert all(-1 <= a <= 1 for a in v)
            assert max(abs(v[i] - x[i]) for i in range(len(x))) >= r
        constructions += 1
    else:
        assert r > bstar
        active = [i for i, a in enumerate(x) if r <= ONE + a]
        total = sum(capacities(x, r), ZERO)
        assert total < ONE
        f = [ONE / (r + ONE - a) if i in active else ZERO
             for i, a in enumerate(x)]
        at_x = sum((f[i] * a for i, a in enumerate(x)), ZERO)
        cap_bound = sum(f, ZERO) - ONE
        assert at_x - cap_bound == ONE - total > ZERO
        separations += 1
    checks += 1


def symmetric_expected(a, n):
    if n == 1:
        return ONE - a
    return min(ONE + a, (n - 1) * (ONE - a))


checks = constructions = separations = 0
vals = [F(k, 5) for k in range(6)]
radii = [F(k, 10) for k in range(1, 21)]
for n in range(1, 5):
    for x in product(vals, repeat=n):
        for r in radii:
            test(x, r)

# Explicit rational boundary checks for every equal-coordinate cube.
for n in range(1, 9):
    for a in vals:
        d = symmetric_expected(a, n)
        x = (a,) * n
        if d > 0:
            test(x, d)
        if d < 2:
            test(x, min(2, d + F(1, 100)))

# Sharp unit-sphere extremum and the equality witnesses, including n=3.
for n in range(3, 13):
    d = 2 - F(2, n - 1)
    a = ONE - F(2, n - 1)
    x = (ONE,) + (a,) * (n - 1)
    test(x, d)
    if d < 2:
        test(x, min(2, d + F(1, 1000)))

# The two-dimensional source result and three-dimensional sharp cutoff.
for a in vals:
    for b in vals:
        x = (a, b)
        d = ONE - min(a, b)
        if d > 0:
            test(x, d)
        if d < 2:
            test(x, min(2, d + F(1, 100)))
        x3 = (ONE, a, b)
        if max(a, b) > 0:
            test(x3, F(101, 100))

print('VERIFY_OK exact_rational_checks=%d constructive=%d separating=%d dimensions=1..12' %
      (checks, constructions, separations))
