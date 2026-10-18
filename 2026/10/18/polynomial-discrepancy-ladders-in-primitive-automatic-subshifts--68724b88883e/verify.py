#!/usr/bin/env python3
"""Finite exact checks for the explicit constant-length substitution family.

Run with Python 3 standard library; output counts are diagnostic, not an
infinite mathematical proof.
"""
from itertools import product
from math import comb

checks = 0

def test(condition, label):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(label)


def phi(a, r, d):
    return [a] * r + [min(a + 1, d + 1), 0]


def compose(u, v):
    return tuple(u[t] for t in v)


def powers(r, d, m):
    alphabet = tuple(range(d + 2))
    ident = alphabet
    g = tuple(min(a + 1, d + 1) for a in alphabet)
    c0 = tuple(0 for _ in alphabet)
    maps = [ident] * r + [g, c0]
    level = [ident]
    for _ in range(m):
        level = [compose(f, h) for h in level for f in maps]
    return level


def word(a, r, d, n):
    v = [a]
    for _ in range(n):
        v = [b for z in v for b in phi(z, r, d)]
    return v


for r in range(1, 4):
    for d in range(1, 6):
        alphabet = list(range(d + 2))
        test(all(set(word(a, r, d, d + 3)) == set(alphabet) for a in alphabet),
             ('primitivity', r, d))
        w2 = word(0, r, d, 2)
        test(any((w2[j], w2[j+1]) == (0, 0) for j in range(len(w2)-1)),
             ('adjacent zeros', r, d))
        for m in range(8):
            maps = powers(r, d, m)
            nonconstant = [f for f in maps if len(set(f)) > 1]
            expected = sum(comb(m, j) * r ** (m-j) for j in range(min(d, m)+1))
            test(len(nonconstant) == expected, ('D', r, d, m, len(nonconstant), expected))
            uniquenonconstant = len(set(nonconstant))
            expectednonconstant = min(d, m) + 1
            test(uniquenonconstant == expectednonconstant,
                 ('nonconstant kernel', r, d, m))
            constant_maps = {f for f in maps if len(set(f)) == 1}
            expectedconstant = m if m <= d else d + 2
            test(len(constant_maps) == expectedconstant,
                 ('constant kernel', r, d, m))
            # Direct column inspection independently constructs substituted words.
            if m <= 5 and d <= 4:
                words = [word(a, r, d, m) for a in alphabet]
                actual_maps = [tuple(w[i] for w in words) for i in range((r+2)**m)]
                test(len(actual_maps) == len(maps), ('column length',r,d,m))
                test(actual_maps == maps, ('column maps',r,d,m))
                test(sum(len(set(f)) > 1 for f in actual_maps) == expected,
                     ('column direct',r,d,m))

# Exact rational recurrence and generating-function coefficients.
for r in range(1, 9):
    for d in range(1, 9):
        vals = [sum(comb(m,j)*r**(m-j) for j in range(min(d,m)+1)) for m in range(20)]
        for m in range(1,20):
            test(vals[m] == (r+1)*vals[m-1] - (comb(m-1,d)*r**(m-1-d) if m > d else 0), ('recurrence',r,d,m))

if __name__ == '__main__':
    print(f'PASS: {checks} integer diagnostics of substitution primitivity,')
    print('height witness, exact progression counts, kernel types,')
    print('direct iterated-word columns, and binomial recurrence.')
    print('No finite check substitutes for the proof for all parameters and depths.')
