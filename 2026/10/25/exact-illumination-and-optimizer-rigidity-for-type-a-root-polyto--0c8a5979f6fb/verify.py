"""Exact finite consistency tests for type-A root-polytope vertex illumination.

The analytic proof, not finite testing, establishes the theorem in all dimensions.
Python standard library only. Execute: python verify.py
"""
from fractions import Fraction
from itertools import product


def illuminate(u, i, j):
    # Exact one-sided l1 derivative at the root e_i-e_j.
    return u[i] - u[j] + sum(abs(u[k]) for k in range(len(u)) if k != i and k != j) < 0


def covers(u):
    m = len(u)
    return {(i, j) for i in range(m) for j in range(m) if i != j and illuminate(u, i, j)}


def check(m):
    roots = {(i, j) for i in range(m) for j in range(m) if i != j}
    outgoing = []
    incoming = []
    for c in range(m):
        o = [1] * m
        o[c] = -(m - 1)
        inc = [-1] * m
        inc[c] = m - 1
        assert sum(o) == 0 and sum(inc) == 0
        assert covers(o) == {(c, j) for j in range(m) if j != c}
        assert covers(inc) == {(i, c) for i in range(m) if i != c}
        outgoing.append(covers(o))
        incoming.append(covers(inc))
    assert set.union(*outgoing) == roots
    assert set.union(*incoming) == roots
    for i, j in roots:
        assert sum((i, j) in s for s in outgoing) == 1
        assert sum((i, j) in s for s in incoming) == 1
    for theta in [Fraction(0), Fraction(2, 7), Fraction(1, 2), Fraction(1)]:
        weight = sum(theta for _ in outgoing) + sum(1 - theta for _ in incoming)
        assert weight == m
        for root in roots:
            received = sum(theta for s in outgoing if root in s) + sum(1 - theta for s in incoming if root in s)
            assert received == 1
    enumerated = 0
    for prefix in product(range(-2, 3), repeat=m - 1):
        u = (*prefix, -sum(prefix))
        if not any(u):
            continue
        enumerated += 1
        illuminated = covers(u)
        assert len(illuminated) <= m - 1
        for i, j in illuminated:
            assert u[i] < 0 and u[j] > 0
        for i, j in illuminated:
            for k, ell in illuminated:
                assert i == k or j == ell
        if len(illuminated) == m - 1:
            neg = sum(c < 0 for c in u)
            pos = sum(c > 0 for c in u)
            assert (neg == 1 and pos == m - 1) or (pos == 1 and neg == m - 1)
    return enumerated


if __name__ == '__main__':
    totals = {m: check(m) for m in range(3, 7)}
    print('EXACT_OK type-A roots; integer-direction profiles:', totals)
