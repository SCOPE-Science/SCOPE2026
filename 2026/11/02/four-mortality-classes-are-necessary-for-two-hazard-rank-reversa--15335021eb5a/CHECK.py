"""Exact arithmetic checks for four-class mixture survival and hazard claims.

Run with Python 3: python CHECK.py
The analytic proof of the general three-class bound is in RESULT.md.
"""
from fractions import Fraction as F


def add(x, y):
    r = [F(0)] * max(len(x), len(y))
    for i, z in enumerate(x):
        r[i] += F(z)
    for i, z in enumerate(y):
        r[i] += F(z)
    return r


def neg(x):
    return [-F(z) for z in x]


def mul(x, y):
    r = [F(0)] * (len(x) + len(y) - 1)
    for i, u in enumerate(x):
        for j, v in enumerate(y):
            r[i+j] += F(u)*F(v)
    return r


def derivative(x):
    return [F(i)*F(x[i]) for i in range(1, len(x))]


def val(p, q):
    s=F(0)
    for c in reversed(p):
        s=s*q+c
    return s

A = [4,2,1,4]  # unnormalized cohort A class masses
B = [3,1,3,1]  # unnormalized cohort B class masses
P = add(mul(derivative(A),B),neg(mul(A,derivative(B))))
while P and P[-1] == 0:
    P.pop()
D = add([sum(B)*z for z in A],[-sum(A)*z for z in B])
assert P == [F(2),F(-18),F(19),F(4),F(11)], P
assert D == [F(-1),F(5),F(-25),F(21)], D
assert D == mul([-1,1],[1,-4,21]), D

for q in (F(0), F(1,10), F(1,5), F(1,2), F(4,5), F(1)):
    expected=11*q**4+4*q**3+19*q**2-18*q+2
    assert val(P,q)==expected
assert val(P,F(0))>0 and val(P,F(1,5))<0 and val(P,F(1))>0
assert val(P,F(1,10))>0 and val(P,F(1,2))<0 and val(P,F(4,5))>0
assert val(D,F(1,3))<0 and val(D,F(2,3))<0

# For every q in (0,1), D(q)=(q-1)*[21(q-2/21)^2+17/21] < 0.
# P(q) has two sign changes of coefficients, hence Descartes' rule gives
# at most two positive zeros. Two disjoint sign-change intervals establish
# exactly two, both simple, in (0,1).
# These are analytic statements, not inferred from sampling.
print('PASS: exact survival ordering polynomial and exact double-crossing certificate')
