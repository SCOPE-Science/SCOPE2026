#!/usr/bin/env python3
"""Exact checks for three-symbol symmetric peeling random access (stdlib only)."""
from fractions import Fraction as F
from functools import lru_cache
from collections import defaultdict

VECTORS = list(range(1, 8))   # nonzero supports on three source symbols
TARGET = 1
@lru_cache(None)
def decoded_support(observed):
    known = 0
    while True:
        previous = known
        for j, edge in enumerate(VECTORS):
            if observed & (1 << j):
                unknown = edge & ~known
                if unknown.bit_count() == 1:
                    known |= unknown
        if known == previous:
            return known

# Expand a monomial product (1-z)^present z^absent exactly.
def mul_poly(p, q):
    out = defaultdict(int)
    for i, a in p.items():
        for j, b in q.items():
            out[tuple(x+y for x,y in zip(i,j))] += a*b
    return dict(out)

survival = defaultdict(int)
fail_count = 0
for observed in range(128):
    if decoded_support(observed) & TARGET:
        continue
    fail_count += 1
    polynomial = {(0,0,0): 1}
    for j, edge in enumerate(VECTORS):
        deg = edge.bit_count() - 1
        if observed & (1 << j):
            factor = {(0,0,0):1, tuple(int(t == deg) for t in range(3)):-1}
        else:
            factor = {tuple(int(t == deg) for t in range(3)):1}
        polynomial = mul_poly(polynomial, factor)
    for powers, coef in polynomial.items():
        survival[powers] += coef
survival = {key:v for key,v in survival.items() if v}
expected_polynomial = {
    (3,3,1):2,(3,2,1):-1,(3,2,0):-2,(3,0,0):1,
    (2,3,1):-2,(2,2,0):2,(1,2,1):1,
}
assert fail_count == 28, fail_count
assert survival == expected_polynomial, (survival,expected_polynomial)

# Independent first-appearance dynamic programming for the exact number of draws.
def expectation_dp(p):
    rate = {v: p[v.bit_count()-1] / (3 if v.bit_count()<3 else 1) for v in VECTORS}
    e = [F(0) for _ in range(128)]
    for observed in range(127,-1,-1):
        if decoded_support(observed) & TARGET:
            continue
        unseen = [i for i in range(7) if not (observed & (1 << i))]
        den = sum((rate[VECTORS[j]] for j in unseen), F(0))
        assert den > 0
        e[observed] = (1 + sum((rate[VECTORS[j]] * e[observed | (1<<j)] for j in unseen), F(0))) / den
    return e[0]

def expectation_integral(p):
    a, b, c = p[0]/3, p[1]/3, p[2]
    assert a > 0 and b >= 0 and c >= 0 and sum(p) == 1
    return sum((F(coef, 1)/(i*a+j*b+k*c) for (i,j,k),coef in expected_polynomial.items()), F(0))

for p in [(F(1),F(0),F(0)), (F(1,2),F(1,2),F(0)),
          (F(4,5),F(1,10),F(1,10)), (F(18,25),F(27,100),F(1,100)),
          (F(7,10),F(3,10),F(0)), (F(1,3),F(1,3),F(1,3))]:
    assert expectation_dp(p) == expectation_integral(p), p

p = (F(18,25),F(27,100),F(1,100))
witness = expectation_integral(p)
assert witness == F(13700419, 4906902), witness
boundary = F(27921,10000)
assert witness < boundary
assert boundary - witness == F(710371,24534510000)

# The polynomial numerator of E_2(x) - 27921/10000.
def q(x):
    return 22079*x**4 - 116237*x**3 + 361684*x*x - 375052*x + 120000
def qp(x):
    return 88316*x**3 - 348711*x*x + 723368*x - 375052
# Q'''(x)=529896*x-697422<0 for 0<=x<=1.
# Hence Q'' is decreasing and its min on [0,1] is Q''(1)=290894.
x0=F(363,500)
strict_convexity_bound = q(x0) - qp(x0)**2/F(581788)
assert strict_convexity_bound == F(71305991069476208741,35509521484375000000)
assert strict_convexity_bound > 0
for x in [F(1,100), F(1,10), F(1,2), F(363,500), F(3,4), F(1)]:
    expected2 = expectation_integral((x,1-x,F(0)))
    D = x*(x-3)*(x-2)*(x+2)
    assert D>0
    assert expected2-boundary == q(x)/(10000*D)
    assert expected2>boundary
print('CHECK_OK')
print('failure_sets',fail_count, 'survival_monomials',len(survival))
print('finite_full_support_columns',{'singletons_each':24,'pairs_each':9,'triple':1,'total':100})
print('exact_expected_reads',witness,'decimal',float(witness))
print('degree_le_2_strict_lower_bound',boundary)
print('convexity_certificate',strict_convexity_bound)
