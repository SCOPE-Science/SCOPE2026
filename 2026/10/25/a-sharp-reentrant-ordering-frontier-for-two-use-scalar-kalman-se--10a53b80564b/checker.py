"""Exact-rational reproducibility checks for a two-slot scalar sensing order theorem.

The mathematical proof of the universal classifications is in RESULT.md.
This script checks the independent covariance and information-form recurrences.
"""
from fractions import Fraction as F
from random import Random
from math import sqrt, isclose


def posterior(v, precision):
    return v / (1 + precision * v)


def final_variance(p, first, last, t, q):
    return posterior(q + t * posterior(p, first), last)


def information_difference(p, strong, weak, t, q):
    return 1 / final_variance(p, strong, weak, t, q) - 1 / final_variance(p, weak, strong, t, q)


def factored_difference(p, strong, weak, t, q):
    C, D = 1 + p * strong, 1 + p * weak
    return (strong - weak) * (t*p*p / ((t*p + q*C)*(t*p + q*D)) - 1)


def comparison_polynomial(p, strong, weak, t, q):
    C, D, nu = 1 + p*strong, 1 + p*weak, q/p
    return t*t + (nu*(C+D)-1)*t + nu*nu*C*D


checks = 0
rng = Random(43729)
for _ in range(5000):
    p = F(rng.randint(1, 20), rng.randint(1, 20))
    r = F(rng.randint(2, 20), rng.randint(1, 20))
    s = F(rng.randint(1, 20), rng.randint(1, 20))
    if r == s:
        r += F(1, 2)
    strong, weak = max(r, s), min(r, s)
    q = F(rng.randint(1, 30), rng.randint(1, 50))
    t = F(rng.randint(0, 30), rng.randint(1, 30))
    actual = information_difference(p, strong, weak, t, q)
    assert actual == factored_difference(p, strong, weak, t, q)
    checks += 1
    # A negative polynomial is precisely the strong-first-optimal regime.
    poly = comparison_polynomial(p, strong, weak, t, q)
    assert (actual > 0) == (poly < 0)
    checks += 1

p, strong, weak, q = F(1), F(3), F(1), F(1, 100)
for t, expected in [(F(0), -1), (F(1,4), 1), (F(2), -1)]:
    d = information_difference(p, strong, weak, t, q)
    assert (d > 0) - (d < 0) == expected
    checks += 1

assert final_variance(p, strong, weak, F(0), q) == F(1, 101)
checks += 1
assert final_variance(p, weak, strong, F(0), q) == F(1, 103)
checks += 1
assert final_variance(p, strong, weak, F(1,4), q) == F(29, 429)
checks += 1
assert final_variance(p, weak, strong, F(1,4), q) == F(27, 281)
checks += 1
assert final_variance(p, strong, weak, F(2), q) == F(51, 151)
checks += 1
assert final_variance(p, weak, strong, F(2), q) == F(101, 403)
checks += 1

C, D = 1 + float(p*strong), 1 + float(p*weak)
nu_star = 1/(sqrt(C) + sqrt(D))**2
assert q < nu_star
checks += 1
nu = float(q/p)
B = 1 - nu*(C+D)
disc = B*B - 4*nu*nu*C*D
assert disc > 0
checks += 1
lo = (B-sqrt(disc))/2
hi = (B+sqrt(disc))/2
assert 0 < lo < hi
checks += 1
for t in [0, lo/2, (lo+hi)/2, 2*hi]:
    # Independent direct floating-point application of the filter.
    u = 1/(1 + float(p)*float(strong))
    v = 1/(1 + float(p)*float(weak))
    pf = 1/(float(weak)+1/(float(q) + t*float(p)*u))
    pl = 1/(float(strong)+1/(float(q) + t*float(p)*v))
    assert (pf < pl) == (lo < t < hi)
    checks += 1

print(f'PASS: {checks} exact-rational and independent boundary checks')
