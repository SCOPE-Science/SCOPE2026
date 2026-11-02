#!/usr/bin/env python3
"""Exact finite-field checks for characteristic-five Humbert-curve p-rank strata.

All operations are in F_25 = F_5[t]/(t^2-2).  The infinite-field
classification relies on the separate geometric argument in RESULT.md.
"""
from collections import Counter
from itertools import combinations

P = 5
F = [(a, b) for a in range(P) for b in range(P)]
ZERO, ONE = (0, 0), (1, 0)
def add(x, y): return ((x[0]+y[0])%P, (x[1]+y[1])%P)
def neg(x): return ((-x[0])%P, (-x[1])%P)
def sub(x, y): return add(x, neg(y))
def mul(x, y): return ((x[0]*y[0]+2*x[1]*y[1])%P, (x[0]*y[1]+x[1]*y[0])%P)
def sq(x): return mul(x, x)
def eqpoly(x, y): return add(sub(sq(x), mul(x, y)), sq(y))
def hasse(x): return eqpoly(x, ONE)
def frob(x): return (x[0], (-x[1])%P)

def divisors(a, b):
    a1, b1 = sub(a, ONE), sub(b, ONE)
    return (
        hasse(a) == ZERO,
        hasse(b) == ZERO,
        eqpoly(a, b) == ZERO,
        eqpoly(a1, b1) == ZERO,
        eqpoly(mul(a,b1), mul(b,a1)) == ZERO,
    )

roots = [r for r in F if hasse(r) == ZERO]
assert len(roots) == 2
assert roots[0] != roots[1] and frob(roots[0]) == roots[1]
assert add(roots[0],roots[1]) == ONE and mul(roots[0],roots[1]) == ONE
assert divisors(roots[0],roots[1]) == (True, True, False, False, False)
assert (ONE[0]-4)%P == 2  # discriminant of T^2-T+1 modulo 5

pairs = [(a,b) for a in F for b in F if a not in (ZERO,ONE) and b not in (ZERO,ONE) and a != b]
assert len(pairs) == 506
C = Counter(sum(divisors(a,b)) for a,b in pairs)
assert C == {0:306, 1:180, 2:20}, C
D = [set((a,b) for a,b in pairs if divisors(a,b)[i]) for i in range(5)]
assert all(len(t) == 44 for t in D)
assert all(len(D[i] & D[j]) == 2 for i,j in combinations(range(5),2))
assert all(not (D[i] & D[j] & D[k]) for i,j,k in combinations(range(5),3))
S = set((a,b) for a,b in pairs if sum(divisors(a,b)) == 2)
assert len(S) == 20 and all((frob(a),frob(b)) in S for a,b in S)
assert all((frob(a),frob(b)) != (a,b) for a,b in S)
FIVE = [(a,0) for a in range(P)]
B = [(a,b) for a in FIVE for b in FIVE if a not in (ZERO,ONE) and b not in (ZERO,ONE) and a != b]
assert len(B) == 6 and all(sum(divisors(a,b))==0 for a,b in B)
print('HASSE_POLYNOMIAL=T^2-T+1; TWO_F25_CONJUGATE_ROOTS_OK')
print('MODULI_M0_5_F25_POINTS=506')
print('EQUianharmonic_DIVISOR_F25_COUNTS=44,44,44,44,44')
print('PAIR_INTERSECTIONS=2_FOR_EACH_OF_10_PAIRS; TRIPLE_INTERSECTIONS=0')
print('P_RANK_5=306; P_RANK_4=180; P_RANK_3=20')
print('P_RANK_3_FROBENIUS_CYCLES=10_PAIRS; F5_MODULI_ALL_6_ORDINARY')
print('VERIFY_OK')
