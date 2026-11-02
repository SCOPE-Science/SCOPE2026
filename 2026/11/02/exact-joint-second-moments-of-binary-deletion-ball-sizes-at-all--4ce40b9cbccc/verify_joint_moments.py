#!/usr/bin/env python3
"""Exact all-deletion, all-length bivariate moment generating-function check.

Uses only Python's standard library. A 9-state rational linear representation
and a degree-13 polynomial certificate prove the generating-function identity
for infinitely many lengths and all pairs of deletion counts.
"""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import combinations

# Polynomial monomials: (length degree, first deletion degree, second deletion degree).
def const(x):
    return {(0, 0, 0): Q(x)} if x else {}

def var(i):
    key = [0, 0, 0]; key[i] = 1
    return {tuple(key): Q(1)}

def add(*ps):
    v = defaultdict(Q)
    for p in ps:
        for k, a in p.items(): v[k] += a
    return {k: a for k, a in v.items() if a}

def neg(p):
    return {k: -a for k, a in p.items()}

def mul(*ps):
    v = const(1)
    for p in ps:
        u = defaultdict(Q)
        for (n, a, b), x in v.items():
            for (m, c, d), y in p.items(): u[n+m, a+c, b+d] += x*y
        v = {k: x for k, x in u.items() if x}
    return v

def scalar(c, p):
    return {k: Q(c)*v for k, v in p.items()}

x, z, w = var(0), var(1), var(2)
xzw = mul(x, z, w)
R = add(
    const(8),
    scalar(-4, mul(x, add(z, w))),
    scalar(-8, xzw),
    scalar(4, mul(x, x, z, w, add(z, w))),
    scalar(2, mul(x, x, z, z, w, w)),
    neg(mul(x, x, x, z, z, w, w, add(z, w, const(4))))
)
S = add(const(4), scalar(-4, x), scalar(-2, mul(x, add(z, w))),
        scalar(-2, xzw), mul(x, x, z, w, add(z, w)))
NUM = mul(add(const(2), neg(xzw)), R)
DEN = mul(add(const(1), neg(xzw)),
          add(const(2), neg(xzw), scalar(-2, mul(x, w))),
          add(const(2), neg(xzw), scalar(-2, mul(x, z))), S)
assert max(k[0] for k in NUM) <= 4
assert max(k[0] for k in DEN) <= 5
assert NUM[0, 0, 0] == DEN[0, 0, 0] == 16

# The matrix K(z,w) has dimension 3 x 3 = 9. Its coefficient of
# x^n from (I-xK)^-1 is K^n. We compare all n=0,...,13.
# If DEN*F-NUM were nonzero, Cramer's rule implies its numerator
# over det(I-xK) has length degree at most max(5+8, 4+9)=13.
# Vanishing of its first 14 coefficients proves that numerator zero.
v = {(None, None, 0, 0): 1}
series = {}
for n in range(14):
    counts = defaultdict(int)
    for (s, t, a, b), multiplicity in v.items():
        counts[a, b] += multiplicity
    for (a, b), mass in counts.items():
        series[n, a, b] = Q(mass, 2**n)
    nxt = defaultdict(int)
    for (s, t, a, b), mass in v.items():
        for symbol in (0, 1):
            o1 = [(symbol, 0)]
            if s is None or s != symbol: o1.append((s, 1))
            o2 = [(symbol, 0)]
            if t is None or t != symbol: o2.append((t, 1))
            for ns, da in o1:
                for nt, db in o2:
                    nxt[ns, nt, a+da, b+db] += mass
    v = nxt

residual = add(mul(DEN, series), neg(NUM))
assert not [((n,a,b),v) for (n,a,b),v in residual.items() if n <= 13]

# Independently check the underlying canonical-subsequence counts by
# exhaustive deletion-mask enumeration at every length through 8.
def greedy_deck(word):
    dp = {(None, 0): 1}
    for bit in word[::-1]:
        nxt = defaultdict(int)
        for (s, d), v in dp.items():
            nxt[bit, d] += v
            if s is None or s != bit: nxt[s, d+1] += v
        dp = nxt
    ans = defaultdict(int)
    for (s, d), v in dp.items(): ans[d] += v
    return ans

for n in range(9):
    for raw in range(1 << n):
        word = tuple((raw >> k) & 1 for k in range(n))
        deck = greedy_deck(word)
        for d in range(n + 1):
            truth = len({tuple(word[i] for i in range(n) if i not in omit)
                         for omit in combinations(range(n), d)})
            assert deck[d] == truth, (n, word, d, deck[d], truth)

print('CLOSED_RATIONAL_JOINT_MOMENT_IDENTITY_OK')
print('NINE_STATE_DEGREE_13_CERTIFICATE_OK n=0..13, all z,w coefficients')
print('DIRECT_ALL_DELETION_SPECTRA_OK word_length=0..8')
print('NUMERATOR_TERMS', len(NUM), 'DENOMINATOR_TERMS', len(DEN))
