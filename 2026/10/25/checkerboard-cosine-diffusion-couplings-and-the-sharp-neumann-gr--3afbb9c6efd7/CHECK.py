#!/usr/bin/env python3
"""Numerical and exact-arithmetic cross-checks for the DCT-II heat semigroup.

The universal mathematical statements require the analytic proof in RESULT.md;
these finite tests do not certify all dimensions or all continuous times.
"""
from fractions import Fraction as F
import math

checks = 0


def check(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)


def dct(k, p, n):
    return (1.0 / math.sqrt(n)) if p == 0 else math.sqrt(2.0 / n) * math.cos(math.pi * p * (k + .5) / n)


def generator(i, j, n):
    return -sum((p * p) * dct(i, p, n) * dct(j, p, n) for p in range(1, n))


def generator_formula(i, j, n):
    assert i != j
    d = abs(j - i)
    s = i + j + 1
    return (-1.0)**(d+1) * .5 * (
        (1.0 / math.tan(math.pi * d / (2 * n)))**2 -
        (1.0 / math.tan(math.pi * s / (2 * n)))**2)


def semigroup(i, j, n, t):
    return sum(math.exp(-p * p * t) * dct(i, p, n) * dct(j, p, n) for p in range(n))


for n in range(2, 37):
    for i in range(n):
        check(abs(sum(generator(i, j, n) for j in range(n))) < 3e-10,
              ('row sum', n, i))
        for j in range(i+1, n):
            value = generator(i, j, n)
            closed = generator_formula(i, j, n)
            check(abs(value - closed) < 8e-10 * max(1.0, abs(value)),
                  ('entry', n, i, j, value, closed))
            check(value * (-1)**(j-i+1) > 0,
                  ('sign', n, i, j, value))
    negative = sum((j-i) % 2 == 0 for i in range(n) for j in range(i+1,n))
    check(negative == ((n-1)*(n-1))//4, ('count', n, negative))

p0 = [[F(1, 3) for _ in range(3)] for _ in range(3)]
p1 = [[F(k,2) for k in row] for row in ((1,0,-1),(0,0,0),(-1,0,1))]
p2 = [[F(k,6) for k in row] for row in ((1,-2,1),(-2,4,-2),(1,-2,1))]
projections = [p0,p1,p2]
for k, p in enumerate(projections):
    for l, q in enumerate(projections):
        for i in range(3):
            for j in range(3):
                product = sum(p[i][h]*q[h][j] for h in range(3))
                check(product == (p[i][j] if k == l else 0), ('projector', k,l,i,j))
q = [[-p1[i][j]-4*p2[i][j] for j in range(3)] for i in range(3)]
expected = [[F(-7,6),F(4,3),F(-1,6)],
            [F(4,3),F(-8,3),F(4,3)],
            [F(-1,6),F(4,3),F(-7,6)]]
check(q == expected, '3-node matrix')
for i in range(3):
    for j in range(3):
        check(sum(p[i][j] for p in projections) == (1 if i==j else 0), ('sum',i,j))

lo,hi = F(810535713765,10**12), F(810535713768,10**12)
f = lambda x:x*x*x+x*x+x-2
check(f(lo)<0<f(hi),'unique cubic root rational bracket')
check(3*lo*lo+2*lo+1>0,'strictly increasing cubic')

for n in range(3,22):
    t=math.log(n-1)+0.1
    for i in range(n):
        for j in range(n):
            check(semigroup(i,j,n,t)>0, ('late positivity',n,i,j))

for t in (0.0001, .02, .1, .2100598749078, .4, 1.0):
    y=math.exp(-t)
    h13= (2 - 3*y + y**4) / 6
    check(abs(semigroup(0,2,3,t)-h13)<4e-15, ('N3 entry', t))

print('PASS:',checks,'deterministic checks; finite checks are not the analytic proof')
