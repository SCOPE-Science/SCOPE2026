#!/usr/bin/env python3
"""Exact affine-polynomial identities for a quartic Cremona representative.

Run with Python 3.9+; uses only the standard library. This finite exact
replay complements, but does not substitute for, the degree-induction proof.
"""

from collections import defaultdict


def atom(i, j, c=1):
    return {(i, j): c} if c else {}


ZERO = {}
ONE = atom(0, 0)
X = atom(1, 0)
Y = atom(0, 1)


def add(*values):
    d = defaultdict(int)
    for v in values:
        for exp, c in v.items():
            d[exp] += c
    return {e: c for e, c in d.items() if c}


def scale(v, k):
    return {e: c * k for e, c in v.items() if c * k}


def mul(u, v):
    d = defaultdict(int)
    for (i, j), a in u.items():
        for (k, l), b in v.items():
            d[(i + k, j + l)] += a * b
    return {e: c for e, c in d.items() if c}


def power(u, n):
    ans = ONE
    while n:
        if n & 1:
            ans = mul(ans, u)
        if n > 1:
            u = mul(u, u)
        n >>= 1
    return ans


def sub(u, v):
    return add(u, scale(v, -1))


def substitute(p, q, coordinates):
    ans = ZERO
    for (i, j), c in coordinates.items():
        ans = add(ans, scale(mul(power(p, i), power(q, j)), c))
    return ans


def compose(f, g):
    return (substitute(g[0], g[1], f[0]), substitute(g[0], g[1], f[1]))


def iterate(f, n):
    value = (X, Y)
    for _ in range(n):
        value = compose(f, value)
    return value


def degree(f):
    return max(sum(e) for polynomial in f for e in polynomial)


def shear():
    return (add(X, power(Y, 2)), Y)


def shear_inverse():
    return (sub(X, power(Y, 2)), Y)


def psi():
    p = add(X, power(Y, 2))
    return (p, add(Y, power(p, 2)))


def diagonal_psi(a, b):
    p, q = psi()
    return (scale(p, a), scale(q, b))


def antidiagonal_psi(a, b):
    p, q = psi()
    return (scale(q, a), scale(p, b))


def henon(a, b):
    return (add(scale(Y, a), scale(power(X, 2), a + b * b)), scale(X, b))


def verify():
    A = shear()
    Ai = shear_inverse()
    assert compose(A, Ai) == (X, Y)
    assert compose(Ai, A) == (X, Y)
    assert compose((X, add(Y, power(X, 2))), A) == psi()
    for a, b in [(1, 1), (2, 1), (-1, 1), (-4, 2), (3, -2)]:
        g = antidiagonal_psi(a, b)
        assert compose(compose(A, g), Ai) == henon(a, b), (a, b)
        if a + b * b:
            assert [degree(iterate(henon(a, b), n)) for n in range(1, 5)] == [2, 4, 8, 16]
        else:
            assert degree(iterate(henon(a, b), 4)) == 1
    for a, b in [(1, 1), (-1, 1), (2, -3)]:
        assert [degree(iterate(diagonal_psi(a, b), n)) for n in (1, 2)] == [4, 16]
    f = antidiagonal_psi(-1, 1)
    assert [degree(iterate(f, n)) for n in range(1, 5)] == [4, 2, 4, 1]
    assert iterate(f, 4) == (X, Y)
    assert iterate(f, 2) != (X, Y)
    print("VERIFIED: shear identity; normal-form conjugacy for five parameter pairs; ")
    print("Hénon exact degrees 2,4,8,16; diagonal exact degrees 4,16; order-four degrees 4,2,4,1")


if __name__ == "__main__":
    verify()
