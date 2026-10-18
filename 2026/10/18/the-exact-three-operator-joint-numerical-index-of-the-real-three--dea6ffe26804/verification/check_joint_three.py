#!/usr/bin/env python3
"""Exact finite sanity checks for a sharp 3-by-3 real matrix norm inequality."""
from itertools import product
from random import Random

SIGNS = tuple(product((-1, 1), repeat=3))
WITNESS = ((-1, -2, 2), (2, -2, -1), (2, 1, 2))

def invariant(rows):
    columns = tuple(tuple(rows[r][c] for r in range(3)) for c in range(3))
    D2 = sum(sum(abs(a) for a in col)**2 for col in columns)
    W2 = max(sum(sum(s[r]*rows[r][c] for r in range(3))**2
                for c in range(3)) for s in SIGNS)
    return D2, W2

def check(rows):
    d2, w2 = invariant(rows)
    assert 9*d2 <= 25*w2, (rows, d2, w2)

assert invariant(WITNESS) == (75,27), invariant(WITNESS)
assert all(sum(WITNESS[i][k]*WITNESS[j][k] for k in range(3)) ==
           (9 if i==j else 0) for i in range(3) for j in range(3))
REPS = ((1, 1, 1), (1, 1, -1), (1, -1, 1), (-1, 1, 1))
for omitted in REPS:
    chosen = [s for s in REPS if s != omitted]
    assert any(tuple(sum(c[j]*chosen[j][i] for j in range(3)) for i in range(3))
               in (omitted, tuple(-v for v in omitted))
               for c in product((-1,1),repeat=3))
for a in product((-1,0,1),repeat=9):
    check((a[:3],a[3:6],a[6:]))
rng=Random(231011)
for k in range(50000):
    a=tuple(rng.randint(-20,20) for _ in range(9))
    check((a[:3],a[3:6],a[6:]))
print('VERIFY_OK exhaustive_ternary_matrices=19683 random_integer_matrices=50000 witness_D2=75 witness_W2=27 sign_class_relations=4')
