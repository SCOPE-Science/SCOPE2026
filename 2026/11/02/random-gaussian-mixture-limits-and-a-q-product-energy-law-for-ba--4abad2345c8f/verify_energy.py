#!/usr/bin/env python3
"""Finite arithmetic diagnostics for a batch-reset Brownian gas.

The infinite-particle limit and tail are proved analytically in the accompanying
result. These bounded diagnostics do not certify those limiting statements.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import comb, factorial
from decimal import Decimal, localcontext

checks = 0

def equal(a, b):
    global checks
    assert a == b, (a, b)
    checks += 1

def hit_probability(n, m, k):
    choices = list(combinations(range(n), m))
    return F(sum(any(i in c for i in range(k)) for c in choices), len(choices))

# Directly enumerate marked reset events. Re-derive joint age moment
# recurrences via the age-process generator, without using a Fourier density.
for n in range(2, 13):
    for m in range(1, n + 1):
        q = [F(0)]
        for k in range(1, min(n, 5) + 1):
            brute = hit_probability(n, m, k)
            formula = 1 - F(comb(n-k, m) if n-k >= m else 0, comb(n, m))
            equal(brute, formula)
            q.append(brute)
        mom = F(1)
        for k in range(1, len(q)):
            # L(prod_i age_i) = sum_i prod_(j!=i) age_j - r q_k prod_i age_i.
            mom = F(k) * mom / q[k]  # r = 1
            exact = F(factorial(k))
            for j in range(1, k + 1):
                exact /= q[j]
            equal(mom, exact)

# Verify the exact finite-population conditional-variance computation and
# its O(1/N) bound, using rational arithmetic only.
for n in range(2, 100):
    for m in range(1, n + 1):
        theta = F(m, n)
        q2 = hit_probability(n, m, 2) if n <= 12 else 1 - F(comb(n-2, m) if n-2 >= m else 0, comb(n, m))
        equal(q2, theta*(2-theta)+theta*(1-theta)/F(n-1))
        total_second = F(6, n*theta*theta) + F(2*(n-1), n*theta*q2)
        clock_second = F(2, theta*theta*(2-theta))
        err = total_second - clock_second
        assert F(0) <= err <= F(6, n*theta*theta)
        checks += 1

# The finite fraction of reset labels has an explicit conditional geometric
# latest-reset index. Enumerate its finite-horizon expectation without invoking
# an infinite-particle limit.
for n, m, gaps in [(3, 1, [2,1,3]), (4,2,[1,3,2]), (5,4,[3,2,1])]:
    cs = list(combinations(range(n), m))
    tot = F(0)
    for marks in product(cs, repeat=len(gaps)):
        ages = []
        for i in range(n):
            age = 0
            for j, gap in enumerate(gaps):
                age += gap
                if i in marks[j]:
                    break
            ages.append(age)
        tot += F(sum(ages), n)
    tot /= len(cs)**len(gaps)
    ans = sum(F(gap)*(F(n-m,n)**j) for j,gap in enumerate(gaps))
    equal(tot, ans)

# Separately check the product transform against cumulants of truncated
# weighted exponential sums for a nondegenerate set of batch fractions.
with localcontext() as c:
    c.prec = 70
    for q in (Decimal('0'), Decimal('0.25'), Decimal('0.5'), Decimal('0.75')):
        s = Decimal('0.31')
        prod_s = Decimal(1)
        prod_qs = Decimal(1)
        for j in range(400):
            prod_s /= (1+s*(Decimal(1) if j == 0 else q**j))
            prod_qs /= (1+s*q**(j+1))
        assert abs((1+s)*prod_s-prod_qs)<Decimal('1e-38')
        checks+=1
        for k in range(1, 6):
            cumulant_inf = Decimal(factorial(k-1))/(1-q**k)
            cumulant_partial = Decimal(factorial(k-1))*sum(((Decimal(1) if j == 0 else q**(j*k)) for j in range(400)),Decimal(0))
            assert abs(cumulant_inf-cumulant_partial)<Decimal('1e-35')
            checks+=1
    # Exact finite hypoexponential survival, compared with its leading pole.
    q = Decimal('0.5')
    k = 7
    t = Decimal('28')
    rates = [Decimal(2)**j for j in range(k)]
    coeffs = []
    for j in range(k):
        a = Decimal(1)
        for h in range(k):
            if j != h:
                a *= rates[h]/(rates[h]-rates[j])
        coeffs.append(a)
    survival = sum((coeffs[j]*(-rates[j]*t).exp() for j in range(k)),Decimal(0))
    prefactor = Decimal(1)
    for j in range(1,k):
        prefactor /= 1-q**j
    assert abs(survival/t.copy_negate().exp()-prefactor) < Decimal('1e-9')
    checks += 1

print('PASS:', checks, 'bounded arithmetic checks')
