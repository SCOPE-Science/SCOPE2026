#!/usr/bin/env python3
import itertools
import sympy as sp


def elem(vals, k):
    return sp.expand(sum(sp.prod(c) for c in itertools.combinations(vals, k)))


t, s = sp.symbols("t s")
u2, u3, u4, u5 = sp.symbols("u2 u3 u4 u5")

roots32 = [2*t, 2*t, 2*t, -3*t, -3*t]
roots41 = [s, s, s, s, -4*s]
inv32 = [sp.factor(elem(roots32, k)) for k in range(2, 6)]
inv41 = [sp.factor(elem(roots41, k)) for k in range(2, 6)]
assert inv32 == [-15*t**2, -10*t**3, 60*t**4, 72*t**5]
assert inv41 == [-10*s**2, -20*s**3, -15*s**4, -4*s**5]

# Eliminate the normalization parameters. Put the parameter first for lexicographic elimination.
G32 = sp.groebner([
    u2 + 15*t**2,
    u3 + 10*t**3,
    u4 - 60*t**4,
    u5 - 72*t**5,
], t, u5, u4, u3, u2, order="lex")
I32 = {sp.factor(p.as_expr()) for p in G32.polys if not p.as_expr().has(t)}
expected32 = {
    -12*u2*u3 + 25*u5,
    -4*u2**2 + 15*u4,
    4*u2**3 + 135*u3**2,
}
assert I32 == expected32

G41 = sp.groebner([
    u2 + 10*s**2,
    u3 + 20*s**3,
    u4 + 15*s**4,
    u5 + 4*s**5,
], s, u5, u4, u3, u2, order="lex")
I41 = {sp.factor(p.as_expr()) for p in G41.polys if not p.as_expr().has(s)}
expected41 = {
    u2*u3 + 50*u5,
    3*u2**2 + 20*u4,
    2*u2**3 + 5*u3**2,
}
assert I41 == expected41

# Each ideal eliminates u4,u5 and leaves a plane cusp with exponents 2 and 3.
assert sp.factor((4*u2**3 + 135*u3**2).subs({u2:-15*t**2,u3:-10*t**3})) == 0
assert sp.factor((2*u2**3 + 5*u3**2).subs({u2:-10*s**2,u3:-20*s**3})) == 0

# Compute the scheme-theoretic local intersection ideal.
Gsum = sp.groebner(list(expected32 | expected41), u5, u4, u3, u2, order="lex")
sum_basis = [sp.factor(p.as_expr()) for p in Gsum.polys]
assert sum_basis == [u5, u4, u3**2, u2*u3, u2**2]

# Standard monomials are 1, u2, u3, so the quotient length is 3.
standard = [sp.Integer(1), u2, u3]
for m in standard:
    _, rem = Gsum.reduce(m)
    assert sp.expand(rem - m) == 0
for m in [u2**2, u2*u3, u3**2, u4, u5]:
    _, rem = Gsum.reduce(m)
    assert rem == 0

print("VERIFY_OK")
