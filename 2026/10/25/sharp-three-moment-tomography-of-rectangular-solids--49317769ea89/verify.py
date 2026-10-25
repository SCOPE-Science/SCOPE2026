#!/usr/bin/env python3
"""Exact checks for the stated random-distance moment identities in rectangular solids."""
from fractions import Fraction as F
from itertools import product
from math import factorial, sqrt
from random import Random

mu = [F(1), F(1, 6), F(1, 15), F(1, 28)]
kappa = [F(0), F(1, 6), F(7, 180), F(11, 945)]

def moments_squared_distance(s):
    """Independent multinomial derivation: s = squared edge lengths."""
    out = []
    for n in (1, 2, 3):
        z = F(0)
        for k in product(range(n + 1), repeat=3):
            if sum(k) != n:
                continue
            multinomial = F(factorial(n), factorial(k[0])*factorial(k[1])*factorial(k[2]))
            term = multinomial
            for j in range(3):
                term *= s[j] ** k[j] * mu[k[j]]
            z += term
        out.append(z)
    return tuple(out)

def recover_s(s):
    m1, m2, m3 = moments_squared_distance(s)
    p1 = 6 * m1
    p2 = F(180, 7) * (m2 - m1*m1)
    p3 = F(945, 11) * (m3 - 3*m2*m1 + 2*m1**3)
    e1 = p1
    e2 = (p1*p1 - p2) / 2
    e3 = (p1**3 - 3*p1*p2 + 2*p3) / 6
    return e1, e2, e3

def norm_uv(s):
    m1, m2, m3 = moments_squared_distance(s)
    x = m2/m1**2
    y = m3/m1**3
    u = F(5, 7) * (x - 1)
    v = F(35, 88) * (y - 3*x + 2)
    return u, v

def product_discriminant(s):
    return (s[0]-s[1])**2*(s[0]-s[2])**2*(s[1]-s[2])**2

count = 0
for a,b,c in product(range(1, 14), repeat=3):
    s = (F(a, 5), F(b, 7), F(c, 9))
    e1,e2,e3 = recover_s(s)
    assert e1 == sum(s)
    assert e2 == s[0]*s[1]+s[0]*s[2]+s[1]*s[2]
    assert e3 == s[0]*s[1]*s[2]
    u,v = norm_uv(s)
    norm = tuple(t/e1 for t in s)
    assert u == sum(t*t for t in norm)
    assert v == sum(t*t*t for t in norm)
    assert F(1,3) <= u < 1
    assert 1-3*u+2*v > 0
    # The normalized cubic discriminant and the positive-volume condition.
    disc_num = (3*u-1)**3 - 2*(9*u-9*v-2)**2
    assert disc_num >= 0
    if u >= F(1,2):
        assert v > (3*u-1)/2
    # The squared box volume follows directly from all three moments.
    m1,_,_ = moments_squared_distance(s)
    assert e3 == 36*m1**3*(1-3*u+2*v)
    count += 1

# Normalized unit cube agrees with independently tabulated cube line-picking moments.
assert moments_squared_distance((F(1),)*3) == (F(1,2), F(11,30), F(211,630))

# Exact two-moment ambiguity, with nonzero third-moment separation.
for t in [F(1,100), F(1,10), F(1,4), F(2,5)]:
    plus = (1+2*t,1-t,1-t)
    minus = (1-2*t,1+t,1+t)
    P= moments_squared_distance(plus)
    N= moments_squared_distance(minus)
    assert P[:2] == N[:2]
    assert P[2]-N[2] == F(44,315)*t**3
    assert plus != minus

# Direct point sampling is a secondary diagnostic, never a proof.
rng=Random(20261024)
s = (F(1,1), F(9,4), F(25,16))
analytic=[float(v) for v in moments_squared_distance(s)]
N=260000
emp=[0.0, 0.0, 0.0]
for _ in range(N):
    q=0.0
    for sj in s:
        q+=float(sj)*(rng.random()-rng.random())**2
    emp[0]+=q;emp[1]+=q*q;emp[2]+=q*q*q
emp=[v/N for v in emp]
errors=[abs(a-b)/a for a,b in zip(analytic,emp)]
assert max(errors)<0.019, errors
print('EXACT_TESTS',count,'cube',moments_squared_distance((F(1),)*3))
print('AMBIGUITY_EXACT',True,'STOCHASTIC_ERRORS',errors)
