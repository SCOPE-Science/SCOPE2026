#!/usr/bin/env python3
"""Exact-rational consistency checks for two-coordinate TV homogenization.

All universal assertions are proved analytically in RESULT.md; this script checks
independently constructed finite examples and the exact sharpness family.
"""
from fractions import Fraction as F
from itertools import product


def tv(p, q):
    assert len(p) == len(q)
    return sum((abs(a-b) for a, b in zip(p, q)), F(0)) / 2


def tensor(p, q):
    return tuple(a*b for a in p for b in q)


def avg(p, q):
    return tuple((a+b)/2 for a, b in zip(p, q))


def labelled(p1, p2):
    return tuple(x/2 for x in p1) + tuple(x/2 for x in p2)


count = 0
for k in range(2, 400):
    e = F(1, k)
    p1 = (1-e, e, F(0))
    p2 = (F(0), F(1), F(0))
    q1 = (F(1), F(0), F(0))
    q2 = (F(0), 1-e, e)
    heterogeneous = tv(tensor(p1,p2), tensor(q1,q2))
    homogeneous = tv(tensor(avg(p1,p2),avg(p1,p2)), tensor(avg(q1,q2),avg(q1,q2)))
    assert heterogeneous == e
    assert homogeneous == e*(3-e)/2
    assert heterogeneous/homogeneous == F(2)/(3-e)
    assert heterogeneous >= F(2,3)*homogeneous
    count += 4

# Rational trinary simplex with denominator three: 10 probability vectors,
# and 10**4 ordered configurations. Each assertion is exact, but a finite grid
# cannot prove the universal inequality.
prob = [tuple(F(a, 3) for a in (i,j,3-i-j))
        for i in range(4) for j in range(4-i)]
assert len(prob) == 10
for p1,p2,q1,q2 in product(prob, repeat=4):
    direct = tv(tensor(p1,p2),tensor(q1,q2))
    hom = tv(tensor(avg(p1,p2),avg(p1,p2)),tensor(avg(q1,q2),avg(q1,q2)))
    assert direct >= F(2,3)*hom
    lift = tv(tensor(labelled(p1,p2), labelled(p1,p2)),
              tensor(labelled(q1,q2), labelled(q1,q2)))
    formula = (tv(tensor(p1,p1),tensor(q1,q1)) +
               tv(tensor(p2,p2),tensor(q2,q2)))/4 + direct/2
    assert lift == formula
    assert hom <= lift
    count += 3

print(f'VERIFY_OK: {count} exact-rational assertions')
