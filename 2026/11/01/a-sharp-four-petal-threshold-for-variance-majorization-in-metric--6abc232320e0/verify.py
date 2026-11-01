#!/usr/bin/env python3
"""Exact arithmetic checks for the metric-flower two-moment and variance theorem.

Only Python's standard library is required. Analytical inequalities and
Schur-majorization implications are proved in RESULT.md; finite assertions
below are independent algebraic and concrete-instance checks, not proofs by
sampling.
"""
from fractions import Fraction as F
from itertools import product


def direct_moments(lengths):
    """Compute moments from independently derived conditional edge-pair laws."""
    T = sum(lengths)
    p = [F(x, T) if isinstance(x, int) else x/T for x in lengths]
    mu = F(0)
    m2 = F(0)
    for i,a in enumerate(p):
        for j,b in enumerate(p):
            weight = a*b
            if i == j:
                mean = a/4
                square = a*a/12
            else:
                mean = (a+b)/4
                square = (a*a+b*b)/12 + a*b/8
            mu += weight*mean
            m2 += weight*square
    return mu, m2


def closed_moments(lengths):
    T = sum(lengths)
    p = [F(x, T) if isinstance(x, int) else x/T for x in lengths]
    s2 = sum((x*x for x in p), F(0))
    s3 = sum((x**3 for x in p), F(0))
    s4 = sum((x**4 for x in p), F(0))
    return (2*s2-s3)/4, s3/6+s2*s2/8-F(5,24)*s4


def variance(lengths):
    a,b=closed_moments(lengths)
    return b-a*a


def q_variance(a,b,c):
    s2=a*a+b*b+c*c
    s3=a**3+b**3+c**3
    mean=(2*s2-s3)/4
    return (-F(5,6)*(a*a+a*b+b*b)
            +(F(1,2)+F(3,2)*mean)*(a+b)
            +s2/2-2*mean)


def q_three(s,t):
    return (9*s**3+27*s*s*t-17*s*s-72*s*t+9*s+44*t)/24


count=0
for m in range(1,8):
    for lengths in product(range(1,5), repeat=m):
        assert direct_moments(lengths)==closed_moments(lengths)
        count += 1

# The identity q_variance=q_three is polynomial of degree <=4 in each
# of a,b after setting c=1-a-b. Matching on five distinct rational values
# for a and five for b establishes the identity globally by interpolation.
# This verifies the compressed three-petal gradient identity independently.
identity_count=0
for ai in range(-2,3):
    for bi in range(-2,3):
        a,b=F(ai,3),F(bi,5)
        c=1-a-b
        assert q_variance(a,b,c)==q_three(a+b,a*b)
        identity_count += 1

p=[F(49,100),F(49,100),F(1,100),F(1,100)]
q=[F(49,100),F(49,100),F(3,200),F(1,200)]
assert sum(p)==sum(q)==1
assert [sum(sorted(q,reverse=True)[:i])-sum(sorted(p,reverse=True)[:i])
        for i in range(1,5)]==[0,0,F(1,200),0]
mu_p,m2_p=closed_moments(p)
mu_q,m2_q=closed_moments(q)
assert mu_q-mu_p==F(197,8000000)
assert m2_q-m2_p==F(119977,19200000000)
assert variance(q)-variance(p)==F(-515428427,192000000000000)

# Critical coefficient as the two small petals shrink to zero.
A=F(1,2); B=F(1,4); M=(2*A-B)/4
assert A/2-2*M == -F(1,8)

# Exact coefficient at the equilateral point, positive for every m>=2:
# (2m^2-2m-3)/(4m^3) > 0.
for m in range(2,51):
    p=[F(1,m)]*m
    A=sum(x*x for x in p);B=sum(x**3 for x in p)
    mu=(2*A-B)/4
    a=b=F(1,m)
    Q=(-F(5,6)*(a*a+a*b+b*b)
       +(F(1,2)+F(3,2)*mu)*(a+b)+A/2-2*mu)
    assert Q==F(2*m*m-2*m-3,4*m**3)>0

# An exact polynomial identity proving strict decrease of h(s) on [0,1]:
# -h'(s) = 8(1-s)^2 + 40s(1-s) + 5s^2.
for s in [F(k,49) for k in range(50)]:
    assert 8+24*s-27*s*s == 8*(1-s)**2+40*s*(1-s)+5*s*s
    assert 9*s*s-17*s+9 == 9*(s-F(17,18))**2+F(35,36)
    assert 9*s**3-12*s*s-8*s+12 >= 1

print('PASS: %d exact independent edge-pair moment checks;' % count)
print('PASS: %d exact polynomial-interpolation identity nodes;' % identity_count)
print('PASS: exact majorization witness, raw-moment signs, variance sign;')
print('PASS: equilateral and four-petal differential signs, rational algebra checks.')
