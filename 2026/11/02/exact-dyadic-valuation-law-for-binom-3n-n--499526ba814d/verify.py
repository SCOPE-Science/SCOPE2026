#!/usr/bin/env python3
"""Exact checks of the dyadic valuation distribution for choose(3n,n).
Standard library only. The mathematical proof is in RESULT.md.
"""
from collections import Counter
from fractions import Fraction


def add(p, q):
    r = p.copy()
    for k, v in q.items():
        r[k] = r.get(k, 0) + v
    return {k: v for k, v in r.items() if v}


def mul_z(p, j):
    return {k + j: v for k, v in p.items()}


def times(p, scalar):
    return {k: v * scalar for k, v in p.items() if v * scalar}


def next_state(state):
    a, b, c = state
    return (add(a, b), add(a, mul_z(c, 1)), add(mul_z(b, 1), mul_z(c, 1)))


def terminal(state):
    a, b, c = state
    return add(add(a, b), mul_z(c, 1))


def vv(n):
    return 2 * n.bit_count() - (3 * n).bit_count()


state = ({0: 1}, {}, {})
P = []
for r in range(17):
    p = terminal(state)
    assert sum(p.values()) == (1 << r), (r, p)
    assert all(v >= 0 for v in p.values())
    assert p.get(1, 0) == 0
    assert p == dict(Counter(vv(n) for n in range(1 << r))), r
    assert sum(k * v for k, v in p.items()) == \
        Fraction((1 << r) * (r * 3 - 4), 6) + Fraction(3 + (-1)**r, 6), r
    P.append(p)
    state = next_state(state)

assert P[0] == {0: 1}
assert P[1] == {0: 2}
assert P[2] == {0: 3, 2: 1}
for r in range(3, len(P)):
    # D(t,z) = 1-(1+z)t+(z-z^2-1)t^2+(z+z^2)t^3.
    rhs = add(P[r-1], mul_z(P[r-1], 1))
    rhs = add(rhs, add(P[r-2], add(times(mul_z(P[r-2], 1), -1), mul_z(P[r-2], 2))))
    rhs = add(rhs, times(add(mul_z(P[r-3], 1), mul_z(P[r-3], 2)), -1))
    assert P[r] == rhs, r

# Directly verify exact valuation via Kummer carry recursion, including the top terminal carry.
for r in range(14):
    for n in range(1 << r):
        previous = carry = k = 0
        for i in range(r):
            a = (n >> i) & 1
            carry = (a + previous + carry) // 2
            k += carry
            previous = a
        k += (previous + carry) // 2
        assert k == vv(n), (n, r)
print('VERIFY_OK: exact polynomials, 131071 digit-sum valuations, Kummer carries, recurrence and mean formula')
