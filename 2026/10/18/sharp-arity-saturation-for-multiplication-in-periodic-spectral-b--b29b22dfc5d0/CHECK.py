#!/usr/bin/env python3
"""Finite, exact-rational diagnostics for polynomially weighted Fourier products.

The exhaustive boxes below are finite consistency tests, not a proof for
unbounded frequencies, arbitrary dimensions, or arbitrary product arity.
"""
from fractions import Fraction
from itertools import product
from collections import defaultdict
from random import Random

assertions = 0

def verify(ok, label):
    global assertions
    assert ok, label
    assertions += 1


def sqnorm(k):
    return sum(t*t for t in k)


def rational_weight_quotient(tup):
    d = len(tup[0]); total = [0]*d; denom = 1
    for k in tup:
        denom *= 1 + sqnorm(k)
        for j in range(d):
            total[j] += k[j]
    return Fraction(1 + sqnorm(total), denom)


def equality_pattern(tup):
    nonzero = [k for k in tup if sqnorm(k) != 0]
    return (len(nonzero) in (2, 3)
            and all(sqnorm(k) == 1 for k in nonzero)
            and all(k == nonzero[0] for k in nonzero))


cases = 0
for dimension, arities, radius in [
    (1, range(2, 8), 2),
    (2, range(2, 5), 1),
    (3, range(2, 4), 1),
]:
    alphabet = list(product(range(-radius, radius+1), repeat=dimension))
    for arity in arities:
        for tup in product(alphabet, repeat=arity):
            q = rational_weight_quotient(tup)
            verify(q <= Fraction(5, 4), (dimension, arity, tup, q))
            verify((q == Fraction(5, 4)) == equality_pattern(tup),
                   ('equality', dimension, arity, tup, q))
            cases += 1

for n in range(2, 51):
    h = Fraction(1+n*n, 2**n)
    verify(h <= Fraction(5, 4), ('h', n))
    verify((h == Fraction(5, 4)) == (n in (2, 3)), ('h_eq', n))

for arity in range(2, 25):
    # Padding the two- and three-character extrema with constant factors.
    base = ((1,), (1,)) + ((0,),) * (arity-2)
    verify(rational_weight_quotient(base) == Fraction(5, 4), arity)
    if arity >= 3:
        tri = ((1,), (1,), (1,)) + ((0,),) * (arity-3)
        verify(rational_weight_quotient(tri) == Fraction(5, 4), arity)


def finite_product(coeffs):
    out = {0: 1}
    for factor in coeffs:
        nxt = defaultdict(int)
        for u, a in out.items():
            for v, b in factor.items():
                nxt[u+v] += a*b
        out = dict(nxt)
    return out


def weighted_norm2(coeff):
    return sum(abs(a)*(1+k*k) for k, a in coeff.items())

rng = Random(271828)
for arity in range(2, 8):
    for case in range(400):
        polys = []
        for _ in range(arity):
            factors = {k: rng.randrange(-2, 3) for k in range(-2, 3)}
            if not any(factors.values()):
                factors[0] = 1
            polys.append(factors)
        lhs = weighted_norm2(finite_product(polys))
        rhs = Fraction(5, 4)
        for f in polys:
            rhs *= weighted_norm2(f)
        verify(lhs <= rhs, (arity, case, lhs, rhs))

for arity in range(2, 25):
    # Normalized near-monochromatic Fourier bumps on R^d approach this ratio.
    analogue = Fraction(arity+1, 1) / Fraction(arity+1, arity)**arity
    verify(analogue > Fraction(5, 4), ('continuous', arity))

print('PASS: %d exact-rational assertions; %d exhaustive frequency configurations' %
      (assertions, cases))
print('scope: finite boxes, sampled coefficient families; not a universal certificate')
