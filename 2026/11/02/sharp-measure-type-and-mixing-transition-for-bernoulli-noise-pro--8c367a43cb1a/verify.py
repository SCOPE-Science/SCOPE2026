#!/usr/bin/env python3
"""Exact-rational consistency checks for Bernoulli-noise proximal-gradient dynamics.

These tests validate sample parameter identities and a finite-word regeneration
example. The general measure-theoretic results follow from the written proof.
"""
from fractions import Fraction as Q
from collections import defaultdict


def soft(x, t):
    if x > t:
        return x - t
    if x < -t:
        return x + t
    return Q(0)


def phi(x, q, b, t, sign):
    return soft(q * x + sign * b, t)


def check(q, t, b):
    assert Q(0) < q < 1 and Q(0) < t < b
    c = b - t
    B = c / (1 - q)
    assert phi(B, q, b, t, 1) == B
    assert phi(-B, q, b, t, -1) == -B
    lo_plus = phi(-B, q, b, t, 1)
    hi_minus = phi(B, q, b, t, -1)
    assert hi_minus == -lo_plus
    assert -B <= lo_plus <= B
    if q < Q(1, 2):
        gap = c * (1 - 2 * q) / (1 - q)
        assert lo_plus == gap and gap > 0
        assert hi_minus == -gap
        for x in (-B, Q(0), B):
            assert phi(x, q, b, t, 1) == q * x + c
            assert phi(x, q, b, t, -1) == q * x - c
    elif q == Q(1, 2):
        assert lo_plus == hi_minus == 0
        assert B == 2 * c
        assert c * c / (1 - q * q) == B * B / 3
    else:
        assert lo_plus <= 0 <= hi_minus
        # Exact nonempty interior for the interval of inputs killed by +.
        jlo = max(-B, (-b - t) / q)
        jhi = min(B, (-b + t) / q)
        assert jlo < jhi
    return B


for q in [Q(1, 5), Q(1, 3), Q(1, 2), Q(2, 3), Q(3, 4), Q(9, 10)]:
    for t, c in [(Q(1, 7), Q(1, 4)), (Q(1), Q(2)), (Q(5), Q(7))]:
        check(q, t, t + c)

q, t, b = Q(2, 3), Q(1), Q(2)
B = check(q, t, b)
assert B == 3
# Four '-' innovations followed by '+' reset EVERY initial state in [-3,3].
left, right = -B, B
for _ in range(4):
    left = phi(left, q, b, t, -1)
    right = phi(right, q, b, t, -1)
assert left == -3 and right == -Q(19, 9)
assert phi(left, q, b, t, 1) == 0
assert phi(right, q, b, t, 1) == 0
# Monotonicity gives reset for the full interval, with probability 1/32.

# Propagate the exact rational law from zero for ten iterations.
dist = {Q(0): Q(1)}
for _ in range(10):
    nxt = defaultdict(Q)
    for x, p in dist.items():
        for sign in (-1, 1):
            nxt[phi(x, q, b, t, sign)] += p / 2
    dist = dict(nxt)
    assert sum(dist.values()) == 1
assert Q(0) in dist and dist[Q(0)] > 0
print('VERIFY_OK interval-regimes=18, exact-reset-word=----+, reset_probability>=1/32, exact-distribution-steps=10, mass_zero=',dist[Q(0)], 'states=',len(dist))
