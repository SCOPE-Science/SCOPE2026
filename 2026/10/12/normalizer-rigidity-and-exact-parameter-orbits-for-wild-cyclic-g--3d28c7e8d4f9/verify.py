#!/usr/bin/env python3
"""Exact GF(16) cross-check of length-two characteristic-two Witt identities.

This checks finite-field instances of the formulas used in the proof. The
no-simple-pole and moduli arguments are proved separately, not enumerated.
"""

MOD = 0b10011  # irreducible polynomial u^4+u+1 over F_2


def mul(a, b):
    z = 0
    while b:
        if b & 1:
            z ^= a
        b >>= 1
        a <<= 1
        if a & 16:
            a ^= MOD
    return z


def add(p, q):
    return tuple(a ^ b for a, b in zip(p, q))


def pmul(p, q):
    z = [0] * 5
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            if i + j < len(z):
                z[i + j] ^= mul(a, b)
    return tuple(z[:3])  # inputs used here have degree at most one


def frob(p):
    z = [0] * 3
    for i, a in enumerate(p):
        if a and 2 * i < len(z):
            z[2 * i] ^= mul(a, a)
    return tuple(z)


zero = (0, 0, 0)
t = (0, 1, 0)
t2 = (0, 0, 1)


def scalar(lam):
    return (0, lam, 0)


def wplus(a, b):
    return (add(a[0], b[0]), add(add(a[1], b[1]), pmul(a[0], b[0])))


def wneg(a):
    return (a[0], add(a[1], pmul(a[0], a[0])))


def wwp(a):
    return wplus((frob(a[0]), frob(a[1])), wneg(a))


def j(lam):
    return mul(lam, lam) ^ lam


assert wwp((zero, t)) == (zero, add(t2, t))
for a in range(16):
    f = (t, scalar(a))
    assert wplus(f, wneg(f)) == (zero, zero)
    assert wneg(f) == (t, add(scalar(a), t2))
    assert j(a) == j(a ^ 1)
    for b in range(16):
        g = (t, scalar(b))
        assert wplus(f, g) == (zero, add(scalar(a ^ b), t2))
        assert wplus(f, wneg(g)) == (zero, scalar(a ^ b))
        assert (j(a) == j(b)) == (b in (a, a ^ 1))
assert len({j(a) for a in range(16)}) == 8
print('VERIFY_OK: Witt identities and eight two-point GF(16) parameter orbits')
