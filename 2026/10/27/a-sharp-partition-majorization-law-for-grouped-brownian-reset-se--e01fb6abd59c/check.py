#!/usr/bin/env python3
"""Exact moment-order tests and a Brownian reset-schedule illustration.

Requires Python 3 standard library only. Numeric tests illustrate, not replace, the proof.
"""
from fractions import Fraction
from math import erf, sqrt


def partitions(n, maximum=None):
    if maximum is None:
        maximum = n
    if n == 0:
        yield ()
        return
    for a in range(min(n, maximum), 0, -1):
        for rest in partitions(n - a, a):
            yield (a,) + rest


def moment(m):
    # Equally weighted two-point common-survival environment.
    return (Fraction(1, 4) ** m + Fraction(3, 4) ** m) / 2


def survival(part):
    result = Fraction(1)
    for m in part:
        result *= moment(m)
    return result


def balanced(n, k):
    a, b = divmod(n, k)
    return (a + 1,) * b + (a,) * (k - b)


def most_uneven(n, k):
    return (n - k + 1,) + (1,) * (k - 1)


def dominates(a, b):
    assert len(a) == len(b) and sum(a) == sum(b)
    aa, bb = sorted(a, reverse=True), sorted(b, reverse=True)
    return all(sum(aa[:j]) >= sum(bb[:j]) for j in range(1, len(a) + 1))


checks = 0
for n in range(2, 13):
    parts = list(partitions(n))
    for k in range(1, n + 1):
        b, e = balanced(n, k), most_uneven(n, k)
        candidates = [p for p in parts if len(p) == k]
        for p in candidates:
            assert survival(b) <= survival(p) <= survival(e)
            if p != b:
                assert survival(b) < survival(p)
            if p != e:
                assert survival(p) < survival(e)
            checks += 1
        for x in candidates:
            for y in candidates:
                if dominates(x, y):
                    assert survival(x) >= survival(y)
                    if x != y:
                        assert survival(x) > survival(y)
                    checks += 1
    for p in parts:
        if len(p) < 2:
            continue
        merged = tuple(sorted((p[0] + p[1],) + p[2:], reverse=True))
        assert survival(merged) > survival(p)
        checks += 1

# The Brownian survival q_0(t)=erf(x0/sqrt(4Dt)) is non-exponential:
# a schedule with one early reset gives distinct conditional survival.
t, u = 1.0, 0.05
q = lambda v: erf(0.5 / sqrt(v)) if v > 0 else 1.0
no_reset = q(t)
with_reset = q(u) * q(t - u)
assert with_reset > no_reset
checks += 1

# Exact, positive covariance under common schedules for a two-point law.
assert moment(2) - moment(1)**2 == Fraction(1, 16)
checks += 1

print(f"Exact checks passed: {checks}")
print("Seven searchers, three independent clocks:")
for p in [(3, 2, 2), (4, 2, 1), (5, 1, 1)]:
    print(f"  partition={p}, exact toy-law all-survival={survival(p)}")
print(f"Brownian q(1)={no_reset:.12f}, q(0.05)q(0.95)={with_reset:.12f}")
print("All theoretical comparisons use exact rational arithmetic or direct analytic identities.")
