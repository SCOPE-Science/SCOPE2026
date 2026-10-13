"""Exact finite-state checks for an affine map rounded once to a uniform lattice.

This verifier uses only Python's standard library. The general invariant-law
and global phase claims are proved analytically in RESULT.md; finite tests here
are supplementary.
"""
from fractions import Fraction as Q
from itertools import product
from math import floor


def candidates(z):
    j = z.numerator // z.denominator
    t = z - j
    return {j: Q(1) - t, j + 1: t} if t else {j: Q(1)}


def row(beta, a, j):
    return candidates(a * Q(j) + (1 - a) * beta)


def closed_support(beta, a, initial=(0, 1)):
    states = set(initial)
    for _ in range(100):
        new = states | {t for j in states for t, p in row(beta, a, j).items() if p}
        if new == states:
            return sorted(states)
        states = new
    raise AssertionError('support failed to close')


def moment_distribution(beta, a, steps):
    d = {0: Q(1)}
    for _ in range(steps):
        nd = {}
        for j, mass in d.items():
            for k, p in row(beta, a, j).items():
                nd[k] = nd.get(k, Q(0)) + mass * p
        d = {k: p for k, p in nd.items() if p}
    return d


def w1_kernel_distance(z, w):
    """Integrate |floor(z+U)-floor(w+U)| exactly for uniform U."""
    boundaries = {Q(0), Q(1)}
    for x in (z, w):
        t = x - (x.numerator // x.denominator)
        if t:
            boundaries.add(Q(1) - t)
    b = sorted(boundaries)
    out = Q(0)
    for lo, hi in zip(b, b[1:]):
        mid = (lo + hi) / 2
        out += (hi - lo) * abs((z + mid).numerator // (z + mid).denominator - (w + mid).numerator // (w + mid).denominator)
    return out


checks = 0
for beta in [Q(j, 17) for j in range(1, 17)]:
    ccrit = min(beta / (1 - beta), (1 - beta) / beta)
    for a in [Q(-9, 10), Q(-3, 5), Q(-1, 2), Q(-1, 4), Q(0), Q(1, 4), Q(3, 5), Q(9, 10)]:
        safe = -a <= ccrit
        r0, r1 = row(beta, a, 0), row(beta, a, 1)
        actually_closed = all(k in (0, 1) or not p for r in (r0, r1) for k, p in r.items())
        assert safe == actually_closed
        checks += 1

for a in [Q(-4, 5), Q(-2, 3), Q(-1, 3), Q(0), Q(1, 3), Q(4, 5)]:
    for j, k in product(range(-5, 6), repeat=2):
        beta = Q(1, 4)
        z = a * j + (1 - a) * beta
        w = a * k + (1 - a) * beta
        assert w1_kernel_distance(z, w) == abs(a) * abs(j - k)
        checks += 1

beta = Q(1, 4)
for c in (Q(1, 3), Q(2, 5), Q(1, 2), Q(3, 5)):
    a = -c
    states = closed_support(beta, a)
    assert states == [0, 1] if c == Q(1, 3) else states == [-1, 0, 1]
    p1 = Q(1) / (5 - 3 * c)
    pn = (3 * c - 1) / (4 * (5 - 3 * c))
    p0 = 1 - p1 - pn
    pi = {-1: pn, 0: p0, 1: p1}
    assert sum(pi.values()) == 1
    assert sum(k * p for k, p in pi.items()) == beta
    for k in pi:
        incoming = sum(pi[j] * row(beta, a, j).get(k, Q(0)) for j in pi)
        assert incoming == pi[k]
        checks += 1
    variance = sum((Q(j) - beta) ** 2 * v for j, v in pi.items())
    assert variance == beta * (1 - beta) + (3 * c - 1) / (2 * (5 - 3 * c))
    checks += 1

for c in (Q(1, 4), Q(2, 5), Q(4, 5)):
    d = moment_distribution(beta, -c, 160)
    mean = sum(Q(j) * v for j, v in d.items())
    assert abs(mean - beta) < Q(1, 10**12)
    mse = sum((Q(j) - beta)**2 * v for j, v in d.items())
    if c == Q(1, 4):
        assert abs(mse - beta * (1 - beta)) < Q(1, 10**12)
    elif c == Q(2, 5):
        expected = beta * (1 - beta) + (3 * c - 1) / (2 * (5 - 3 * c))
        assert abs(mse - expected) < Q(1, 10**12)
    else:
        assert mse > beta * (1 - beta)
    checks += 1

print('PASS:', checks, 'exact checks of closure, coupling, and invariant laws; finite-horizon tests supplement the proof.')
