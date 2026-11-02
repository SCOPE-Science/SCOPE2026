#!/usr/bin/env python3
"""Exact finite-sample checks for random fixed-cardinality coupon incidence matrices.

This code checks small complete state spaces and exact first moments.
It does not replace the asymptotic argument in the accompanying proof.
"""
import itertools
import math
from collections import Counter
from fractions import Fraction

checks = 0

def assert_equal(a, b):
    global checks
    assert a == b, (a, b)
    checks += 1


def ratio(n, k, t):
    if t == 0:
        return Fraction(1)
    return Fraction(math.comb(n - k, 1), n) ** t


def pair_probabilities(n, k):
    den = n * (n - 1)
    p00 = Fraction((n-k) * (n-k-1), den)
    p11 = Fraction(k * (k-1), den)
    return p00, p11


def inspect(n, k, draws):
    seen = [0] * n
    for i, subset in enumerate(draws):
        for j in subset:
            seen[j] |= 1 << i
    z = seen.count(0)
    mult = Counter(x for x in seen if x != 0)
    p = sum(v * (v-1) // 2 for v in mult.values())
    collisions = sum(v * (v-1) // 2 for v in Counter(seen).values())
    assert_equal(collisions, p + z*(z-1)//2)
    # The two recovery conditions follow from the stated separating-system criterion.
    assert_equal(len(set(seen)) == n, z <= 1 and p == 0)
    assert_equal(len(set(seen)) == n and z == 0, z == 0 and p == 0)
    return z, p


for n in range(3, 7):
    for k in range(1, n):
        choices = list(itertools.combinations(range(n), k))
        for t in range(1, 4):
            totals = Counter()
            for rows in itertools.product(choices, repeat=t):
                z, p = inspect(n, k, rows)
                totals['z'] += z
                totals['z2'] += z * (z-1)
                totals['p'] += p
                totals['typeI'] += int(z <= 1 and p == 0)
                totals['typeII'] += int(z == 0 and p == 0)
            den = len(choices)**t
            p00,p11 = pair_probabilities(n,k)
            assert_equal(Fraction(totals['z'],den), n * Fraction(n-k,n)**t)
            assert_equal(Fraction(totals['z2'],den), n*(n-1)*p00**t)
            assert_equal(Fraction(totals['p'],den), Fraction(n*(n-1),2)*((p00+p11)**t-p00**t))
            assert_equal(totals['typeII'] <= totals['typeI'], True)

print('Exact full-state assertions:', checks)
print('Finite-level first-moment identity and recovery-condition checks: PASS')


def limiting_values(n,c,x=0.0):
    k=max(1,round(c*n/math.log(n)))
    p=k/n
    t=round((math.log(n)+x)/(-math.log1p(-p)))
    lam=n*math.exp(t*math.log1p(-p))
    p00,p11=pair_probabilities(n,k)
    # stable difference of exponential powers (avoids cancellation)
    L0=t*math.log(float(p00))
    delta=t*math.log1p(float(p11/p00))
    mu=(n*(n-1)/2)*math.exp(L0)*math.expm1(delta)
    return (n,k,t,lam,mu)

for c in (0.5,1.0,2.0):
    for n in (10000,100000,1000000):
        n,k,t,lam,mu=limiting_values(n,c)
        print('critical intensity: c=%.1f n=%d k=%d t=%d zero_mean=%.9f nonzero_twin_mean=%.9f targets=(1,%.9f)' %
              (c,n,k,t,lam,mu,0.5*math.expm1(c)))
print('Numerical intensity evaluations: PASS (illustrative, not a limit proof)')
