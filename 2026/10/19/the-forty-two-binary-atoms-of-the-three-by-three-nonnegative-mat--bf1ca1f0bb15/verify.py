#!/usr/bin/env python3
"""Exact, self-contained audit of the 3x3 0/1 prime-matrix classification.
All arithmetic is over nonnegative integers, not the Boolean semiring.
"""
from itertools import product, permutations

N = 3
MATRICES = list(product((0, 1), repeat=N*N))
PERMS = tuple(permutations(range(N)))

def matmul(a, b):
    return tuple(sum(a[3*i+k] * b[3*k+j] for k in range(3))
                 for i in range(3) for j in range(3))

def det(a):
    return (a[0] * (a[4]*a[8]-a[5]*a[7])
            - a[1] * (a[3]*a[8]-a[5]*a[6])
            + a[2] * (a[3]*a[7]-a[4]*a[6]))

def reindex(a, p, q):
    return tuple(a[3*p[i]+q[j]] for i in range(3) for j in range(3))

def orbit(a):
    return {reindex(a, p, q) for p in PERMS for q in PERMS}

def matrix(rows):
    return tuple(v for row in rows for v in row)

UNITS = {tuple(int(j == p[i]) for i in range(3) for j in range(3))
         for p in PERMS}
assert len(UNITS) == 6
SHEAR = matrix(((1,1,0), (0,1,0), (0,0,1)))
TRIANGLE = matrix(((0,1,1), (1,0,1), (1,1,0)))
assert len(orbit(SHEAR)) == 36
assert len(orbit(TRIANGLE)) == 6
PRIMES = orbit(SHEAR) | orbit(TRIANGLE)
assert len(PRIMES) == 42 and PRIMES.isdisjoint(UNITS)

# Directly check all 512^2 candidate binary products. This search is
# exhaustive for non-singular binary products by Lemma 1 in RESULT.md.
NONUNITS = [m for m in MATRICES if m not in UNITS]
FACTOR = {}
for b in NONUNITS:
    for c in NONUNITS:
        a = matmul(b, c)
        if a in PRIMES:
            raise AssertionError('the proposed prime has nonunit factors')
        if a in MATRICES and a not in FACTOR:
            FACTOR[a] = (b, c)
assert len(FACTOR) == 464, len(FACTOR)
assert len(PRIMES) + len(FACTOR) + len(UNITS) == 512
assert set(FACTOR) == set(MATRICES) - PRIMES - UNITS

sing = {a for a in MATRICES if det(a) == 0}
nonsing = set(MATRICES) - sing
assert len(sing) == 338 and len(nonsing) == 174
# Singular matrices admit an explicit singular factor on one side:
# if a row is zero, delete it; if two rows agree, duplicate the row;
# otherwise apply the analogous operation to columns.
for a in sing:
    rows = [tuple(a[3*i+j] for j in range(3)) for i in range(3)]
    cols = [tuple(a[3*i+j] for i in range(3)) for j in range(3)]
    assert any(not any(r) for r in rows) or len(set(rows)) < 3 or \
           any(not any(c) for c in cols) or len(set(cols)) < 3
    assert a in FACTOR

# Independent row/column permutation orbit partition of nonsingular support.
seen = set()
data = []
for a in sorted(nonsing):
    if a in seen:
        continue
    o = orbit(a)
    assert o <= nonsing and not (o & seen)
    seen |= o
    primal = 'prime' if a in PRIMES else ('unit' if a in UNITS else 'composite')
    assert all((m in PRIMES) == (a in PRIMES) for m in o)
    if primal == 'composite':
        assert a in FACTOR
        b, c = FACTOR[a]
        assert matmul(b, c) == a and b not in UNITS and c not in UNITS
    data.append((sum(a), len(o), abs(det(a)), primal, a))
assert seen == nonsing
assert len(data) == 8
assert sorted((w, sz, ad, status) for w, sz, ad, status, _ in data) == sorted([
    (3, 6, 1, 'unit'), (4, 36, 1, 'prime'),
    (5, 18, 1, 'composite'), (5, 18, 1, 'composite'),
    (5, 36, 1, 'composite'), (6, 6, 2, 'prime'),
    (6, 36, 1, 'composite'), (7, 18, 1, 'composite')])
assert {a for a in nonsing if abs(det(a)) == 2} == orbit(TRIANGLE)
print('VERIFY_OK: 512 binary matrices, 6 units, 42 prime nonunits, 464 composites.')
print('Singular=338, nonsingular=174, nonsingular orbits=8.')
for row in sorted(data, key=lambda x: (x[0], x[1], x[2], x[3])):
    print('ones=%d orbit=%d |det|=%d %s'%row[:4])
    if row[3] == 'composite':
        a = row[4]
        b, c = FACTOR[a]
        print('  representative:', [a[3*i:3*i+3] for i in range(3)])
        print('  left factor:   ', [b[3*i:3*i+3] for i in range(3)])
        print('  right factor:  ', [c[3*i:3*i+3] for i in range(3)])
