#!/usr/bin/env python3
"""Exact reproducibility checks for the fixed-composition run-count fourth cumulant.

Requires Python 3.10+ for ordinary checks; optional `--symbolic` requires sympy.
All numbers are exact integers or fractions. This file contains no external data.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb
import sys


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def count_runs_by_composition(a, b):
    out = {}
    for k in range(0, min(a, b) + 2):
        even = 2 * choose(a - 1, k - 1) * choose(b - 1, k - 1)
        odd = (choose(a - 1, k) * choose(b - 1, k - 1)
               + choose(a - 1, k - 1) * choose(b - 1, k))
        if even:
            out[2*k] = even
        if odd:
            out[2*k + 1] = odd
    return out


def fourth_cumulant(counts):
    z = sum(counts.values())
    mom = [Fraction(1)] + [sum(Fraction(v * r**j, z) for r, v in counts.items())
                                   for j in range(1, 5)]
    m1, m2, m3, m4 = mom[1:]
    return m4 - 4*m1*m3 - 3*m2*m2 + 12*m1*m1*m2 - 6*m1**4


def polynomial(n, t):
    return ((240*n-288)*t**3 + (-96*n**3-144*n**2+288*n)*t**2
            + (8*n**5+90*n**4-74*n**3-36*n**2)*t
            - 7*n**6-6*n**5+19*n**4-6*n**3)


def conjectured_formula(a, b):
    n = a + b
    if n == 2:
        return Fraction(0)
    if n == 3:
        return Fraction(-2, 27)
    t = a*b
    return Fraction(2*t*polynomial(n, t), n**4*(n-3)*(n-2)*(n-1)**2)


def run_count_of_word(word):
    return 1 + sum(x != y for x, y in zip(word, word[1:]))


def ordinary_checks():
    count = 0
    # Reconstruct the count law completely independently by enumerating label positions.
    for n in range(2, 14):
        for a in range(1, n):
            tally = Counter()
            for ones in combinations(range(n), a):
                word = [0] * n
                for i in ones:
                    word[i] = 1
                tally[run_count_of_word(word)] += 1
            expected = count_runs_by_composition(a, n-a)
            assert tally == expected, (n, a, tally, expected)
            count += 1
            assert fourth_cumulant(tally) == conjectured_formula(a, n-a)
            count += 1
    # Higher-order independent distribution checks without enumerating each word.
    for n in range(14, 101):
        for a in range(1, n):
            pmf = count_runs_by_composition(a, n-a)
            assert sum(pmf.values()) == comb(n, a)
            assert fourth_cumulant(pmf) == conjectured_formula(a, n-a)
            count += 2
    # The precise finite cutoff and signs in every feasible row through 1000.
    for n in range(4, 1001):
        signs = [polynomial(n, a*(n-a)) for a in range(1, n//2+1)]
        if n <= 9:
            assert all(s < 0 for s in signs)
        else:
            assert signs[0] > 0 and signs[-1] < 0
            # No switch back from a negative sign to a positive sign is possible.
            assert all(not (x < 0 and y > 0) for x, y in zip(signs, signs[1:]))
        count += 1
    # Endpoint signs and exact transformed-cubic coefficients.
    for n in range(10, 500):
        c0=(n-3)*(n-2)**2*(n-1)*(n*n-12*n+24)
        c1=n*(n-4)*(n-3)*(n-2)**2*(4*n*n-17*n+12)
        c2=-n*n*(n-2)**2*(2*n**3-12*n*n+22*n-9)
        c3=-n**3*(n-2)**2*(n*n-4*n+6)
        assert c0>0 and c1>0 and c2<0 and c3<0
        # c1 is twice the true coefficient and c3 four times the true coefficient.
        assert polynomial(n,n-1) == c0
        assert 4*polynomial(n, Fraction(n*n,4))==c3
        count+=4
    print('EXACT TESTS PASSED:',count)


def symbolic_certificate():
    import sympy as s
    from functools import lru_cache
    from sympy.functions.combinatorial.numbers import stirling
    n,a,b=s.symbols('n a b',integer=True,positive=True)
    t,y=s.symbols('t y')
    def compositions(q):
        if q==0:
            yield ()
        else:
            for i in range(1,q+1):
                for rest in compositions(q-i):
                    yield (i,)+rest
    def fall(x,j):
        return s.prod(x-i for i in range(j))
    @lru_cache(None)
    def cluster_probability(lengths):
        tally={(0,0):1}
        for ell in lengths:
            q=ell//2
            options=(((q+1,q),(q,q+1)) if ell%2==0
                     else (((ell+1)//2,(ell+1)//2),)*2)
            nxt={}
            for (u,v),multiplicity in tally.items():
                for du,dv in options:
                    k=(u+du,v+dv)
                    nxt[k]=nxt.get(k,0)+multiplicity
            tally=nxt
        return sum(mult*fall(a,u)*fall(b,v) for (u,v),mult in tally.items())/fall(n,sum(lengths)+len(lengths))
    factorial_moments={0:s.Integer(1)}
    for j in range(1,5):
        total=sum(fall(n-j,len(lengths))/s.factorial(len(lengths)) * cluster_probability(lengths)
                  for lengths in compositions(j))
        factorial_moments[j]=s.cancel(s.factorial(j)*total)
    moments=[s.Integer(1)]
    for j in range(1,5):
        moments.append(s.cancel(sum(stirling(j,k,kind=2)*factorial_moments[k]
                                   for k in range(j+1))))
    m1,m2,m3,m4=moments[1:]
    cumulant=s.cancel(m4-4*m1*m3-3*m2**2+12*m1*m1*m2-6*m1**4)
    Q=((240*n-288)*t**3+(-96*n**3-144*n**2+288*n)*t**2
       +(8*n**5+90*n**4-74*n**3-36*n**2)*t-7*n**6-6*n**5+19*n**4-6*n**3)
    formula=2*a*b*Q.subs(t,a*b)/(n**4*(n-3)*(n-2)*(n-1)**2)
    assert s.cancel((cumulant-formula).subs(b,n-a))==0
    p=s.Poly(s.cancel((1+y)**3*Q.subs(t,(n-1+n**2*y/4)/(1+y))),y)
    target=[(n-3)*(n-2)**2*(n-1)*(n*n-12*n+24),
            n*(n-4)*(n-3)*(n-2)**2*(4*n*n-17*n+12)/2,
            -n*n*(n-2)**2*(2*n**3-12*n*n+22*n-9),
            -n**3*(n-2)**2*(n*n-4*n+6)/4]
    for j in range(4):
        assert s.factor(p.coeff_monomial(y**j)-target[j])==0
    print('SYMBOLIC IDENTITIES PASSED: cumulant polynomial and four cubic coefficients')

if __name__ == '__main__':
    ordinary_checks()
    if '--symbolic' in sys.argv:
        symbolic_certificate()
