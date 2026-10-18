"""Exact finite checks for a frozen-cardinality bootstrap random walk.

Run with Python 3.11 or later. No external dependencies.
"""
from itertools import product
from math import comb
from fractions import Fraction

checks = 0

def check(condition, description):
    global checks
    if not condition:
        raise AssertionError(description)
    checks += 1


def pascal_signs(bits):
    """Image under the binary Pascal triangle, followed by sign encoding."""
    return tuple(1 if sum(comb(s, k) * bits[k] for k in range(s + 1)) % 2 == 0
                 else -1 for s in range(len(bits)))


# The lower-triangular Pascal map is an exact permutation of all binary words.
for m in range(0, 10):
    words = set()
    for bits in product((0, 1), repeat=m + 1):
        words.add(pascal_signs(bits))
    check(len(words) == 2 ** (m + 1), f'not bijective at m={m}')
    check(words == set(product((-1, 1), repeat=m + 1)), f'not onto at m={m}')


# Direct sum over both environment bits and walk increments for finite moments.
for n in range(1, 8):
    nout = 0
    first = 0
    second = 0
    qfirst = 0
    qsecond = 0
    for bits in product((0, 1), repeat=n):
        f = pascal_signs(bits)
        for xi in product((-1, 1), repeat=n):
            s = 0
            c = 0
            for x in xi:
                c += f[s]
                if x == -1:
                    s += 1
            first += c
            second += c * c
            q = c - f[0] + 1
            qfirst += q
            qsecond += q * q
            nout += 1
    check(first == 0, f'nonzero mean at n={n}')
    exact = Fraction(second, nout)
    predicted = Fraction(3 * n - 4) + Fraction(4, 2 ** n)
    check(exact == predicted, f'variance mismatch at n={n}: {exact}, {predicted}')
    check(Fraction(qfirst, nout) == 1, f'predictable bracket mean at n={n}')
    qvar = Fraction(qsecond, nout) - 1
    qpred = 0 if n == 1 else Fraction(3*n-7)+Fraction(8,2**n)
    check(qvar == qpred, f'predictable bracket variance at n={n}')


# For every fixed environment the transformed increments are again iid fair.
# Verifies triangular bijection (not a substitute for the general proof).
for n in range(1, 8):
    for bits in product((0, 1), repeat=n):
        signs = pascal_signs(bits)
        outputs = set()
        for xi in product((-1, 1), repeat=n):
            out = []
            s = 0
            for j, x in enumerate(xi):
                multiplier = 1 if j == 0 else signs[s]
                out.append(multiplier * x)
                if x == -1:
                    s += 1
            outputs.add(tuple(out))
        check(len(outputs) == 2 ** n, f'walk recycling not bijective at n={n}, bits={bits}')

print(f'PASS: {checks} exact assertions')
