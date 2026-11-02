#!/usr/bin/env python3
"""Exact checks for order-density generating functions of a rational map.

Requires Python 3 and SymPy. The infinite theorem rests on the written proof.
"""
from fractions import Fraction
from math import comb, gcd
from sympy import Symbol, Rational, cancel, fraction, divisors, factorint, totient

z=Symbol('z')
F={1:0}

def generating(M):
    if M in F:
        return F[M]
    ds=divisors(M)
    for d in ds:
        if 1<d<M:
            generating(d)
    F[M]=cancel((Rational(1,M) + z*sum(totient(d)*F[d] for d in ds if 1<d<M)/M)/(1-z*Rational(totient(M),M)))
    return F[M]

# Dominant-prime pole cancellation is checked algebraically over Q(z).
checks=[6,10,12,14,15,18,20,21,24,30,36,42,45,50,54,60,66,70,72,75,84,90,96,100,120,126,144,150,180]
for M in checks:
    factorization=factorint(M)
    p=max(factorization)
    a=factorization[p]
    diff=cancel(generating(M)-generating(p**a))
    numerator,denominator=fraction(diff)
    assert denominator.subs(z,Rational(p,p-1))!=0, (M,'uncanceled dominant pole')
    assert cancel(diff).subs(z,0)==Rational(1,M)-Rational(1,p**a)

# The exact recurrence yields the closed prime-power profile.
for M in [2,3,4,5,6,8,9,10,12,18,25,30,36,45,75,90,150]:
    ds=[int(d) for d in divisors(M) if d>1]
    dist={d:Fraction(1,d) for d in ds}
    for n in range(1,31):
        for d in ds:
            if len(factorint(d))==1:
                p=next(iter(factorint(d)))
                a=factorint(d)[p]
                expected=Fraction(comb(n+a-2,a-1),p**a)*Fraction(p-1,p)**(n-1)
                assert dist[d]==expected, (d,n,dist[d],expected)
        dist={d:sum(Fraction(int(totient(e)),d)*dist[e] for e in ds if d%e==0) for d in ds}

# Direct iteration, independent of the divisor recurrence and rational-function calculations.
def exact_order_at_most(a,M,n):
    x=a
    den=M
    for j in range(1,n+1):
        whole,rem=divmod(x,den)
        x=whole*(den+rem)
        g=gcd(x,den)
        x//=g; den//=g
        if den==1:
            return j
    return None

brute_cases=0
for M in [3,4,6,10,12]:
    ds=[int(d) for d in divisors(M) if d>1]
    old={d:Fraction(1,d) for d in ds}
    for n in range(1,4):
        expected=old[M]*int(totient(M))*M**n
        count=0
        period=M**(n+1)
        for k in range(period):
            aa=2*M+k
            if gcd(aa,M)!=1:
                continue
            if exact_order_at_most(aa,M,n)==n:
                count+=1
        assert count==expected, (M,n,count,expected)
        brute_cases+=1
        old={d:sum(Fraction(int(totient(e)),d)*old[e] for e in ds if d%e==0) for d in ds}

print(f'VERIFY_OK symbolic_pole_cancellations={len(checks)} divisor_recurrence_primepower_cases={17*30} direct_orbit_cases={brute_cases} exact_arithmetic=yes')
