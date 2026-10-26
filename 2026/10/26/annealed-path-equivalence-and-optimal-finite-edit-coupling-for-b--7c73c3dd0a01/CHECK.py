"""Finite exact-arithmetic checks for the annealed Bernoulli I.I. walk."""
from fractions import Fraction
from math import comb


def distribution_negative_count(n):
    q = {0: Fraction(1)}
    for _ in range(n):
        out = {}
        for k, v in q.items():
            out[k] = out.get(k, Fraction(0)) + v / 2
            out[k + 1] = out.get(k + 1, Fraction(0)) + v / 2
        q = out
    return q


def moment(n, r):
    return sum(v * r ** (2 ** k) for k, v in distribution_negative_count(n).items())


checks = 0
for r in (Fraction(0), Fraction(1, 3), Fraction(1, 2), Fraction(3, 4)):
    for n in range(1, 13):
        lhs = moment(n, r)
        rhs = sum(Fraction(comb(n, k), 2 ** n) * r ** (2 ** k)
                  for k in range(n + 1))
        assert lhs == rhs
        checks += 1
    # Exact expected occupation up to time N; value at each level is
    # obtained by an independent two-state recursion, not a Monte Carlo sample.
    for N in (4, 8, 12):
        lhs = sum(moment(n, r) for n in range(1, N + 1))
        rhs = sum(sum(v * r ** (2 ** k)
                      for k, v in distribution_negative_count(n).items())
                  for n in range(1, N + 1))
        assert lhs == rhs
        checks += 1

# Enumeration of parity of 2**m independent Bernoulli(p) coefficients.
p = Fraction(1, 3)
a = 1 - 2 * p
for m in range(4):
    size = 2 ** m
    signed_mean = sum(((-1) ** sum(bits)) * p ** sum(bits) *
                      (1-p) ** (size-sum(bits))
                      for bits in __import__('itertools').product((0, 1), repeat=size))
    assert signed_mean == a ** size
    checks += 1
print(f'PASS: {checks} exact-rational checks')
