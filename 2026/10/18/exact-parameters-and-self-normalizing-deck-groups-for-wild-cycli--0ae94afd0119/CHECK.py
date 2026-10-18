#!/usr/bin/env python3
"""Exact characteristic-two Witt identity and finite-field parameter-fibre checks.

This checker illustrates identities used in the mathematical proof; the
pole-order and Galois normalizer arguments are proved separately in RESULT.md.
No third-party dependencies are required.
"""
from itertools import product

# F_2[L,T] represented by sets of exponent pairs; addition is XOR.
def plus(a, b):
    return a.symmetric_difference(b)

def times(a, b):
    result = set()
    for x, y in product(a, b):
        term = (x[0] + y[0], x[1] + y[1])
        if term in result:
            result.remove(term)
        else:
            result.add(term)
    return result

def square(a):
    return {(2 * i, 2 * j) for (i, j) in a}

def wadd(a, b):
    return (plus(a[0], b[0]), plus(plus(a[1], b[1]), times(a[0], b[0])))

def wneg(a):
    return a[0], plus(a[1], square(a[0]))

def wp(a):
    # Witt Frobenius minus identity in characteristic 2.
    return wadd((square(a[0]), square(a[1])), wneg(a))

zero = set()
one = {(0, 0)}
L = {(1, 0)}
T = {(0, 1)}
A = (T, times(L, T))
Aplus = (T, times(plus(L, one), T))
assert wneg(wneg(A)) == A
assert wp((zero, T)) == (zero, plus(square(T), T))
assert wp((one, zero)) == (zero, zero)
assert wp((one, T)) == (zero, plus(square(T), T))
assert wadd(wneg(A), wp((zero, T))) == Aplus
assert wadd(A, wneg(A)) == (zero, zero)
print('Witt additive inverse and parameter-shift identity: PASS')

# All GF(16) elements using irreducible p(u)=u^4+u+1.
def gf_mul(a, b):
    o = 0
    while b:
        if b & 1:
            o ^= a
        b >>= 1
        a <<= 1
        if a & 16:
            a ^= 0x13
    return o

def gf_sq(a):
    return gf_mul(a, a)

fibres = {}
for a in range(16):
    inv = gf_sq(a) ^ a
    fibres.setdefault(inv, []).append(a)
assert len(fibres) == 8
assert all(len(v) == 2 and v[0] ^ v[1] == 1 for v in fibres.values())
print('Finite-field lambda^2+lambda fibres over GF(16): PASS')

# First Artin-Schreier class of 1/z remains unchanged under any base scaling
# only if scale=1, because nonzero coefficient of a simple pole is not
# a coboundary: pole orders of h^2+h are even.
print('The infinite-field pole-order rigidity is analytical, not a finite test.')
