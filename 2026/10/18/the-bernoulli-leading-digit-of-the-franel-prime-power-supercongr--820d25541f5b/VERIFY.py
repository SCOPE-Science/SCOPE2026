"""Exact finite checks for the Franel prime-power leading-digit theorem.

The accompanying proof establishes the infinite statement; finite tests are
independent diagnostics only. Runs with Python 3 and the standard library.
"""
from math import comb
from fractions import Fraction


def primes_to(n):
    return [p for p in range(5, n+1) if all(p % d for d in range(2, int(p**0.5)+1))]


def franel(n):
    return sum(comb(n,k)**3 for k in range(n+1))


def bernoulli(m):
    # Akiyama-Tanigawa; B1=+1/2, same even indices as B1=-1/2.
    a=[Fraction(0) for _ in range(m+1)]
    ans=Fraction(0)
    for i in range(m+1):
        a[i]=Fraction(1,i+1)
        for j in range(i,0,-1):
            a[j-1]=j*(a[j-1]-a[j])
        ans=a[0]
    return ans


def leading_digit(p):
    return sum((1 if k%2 else -1)*pow(k,-3,p) for k in range(1,p))%p


checks=0
for p in primes_to(79):
    h=leading_digit(p)
    b=bernoulli(p-3)
    assert b.denominator % p, (p,"denominator")
    assert h == (b.numerator * pow(2*b.denominator,-1,p))%p, (p,"Bernoulli")
    r=1
    while p**r <= 1000:
        n=p**r
        delta=franel(n)-franel(n//p)
        assert delta % p**(3*r) == 0, (p,r,"baseline")
        assert (delta//p**(3*r))%p == h, (p,r,"leading")
        checks += 1
        r += 1

# Directly check the non-multiple p summation decomposition and the
# valuation bound for the divisible block in several small cases.
for p,r in ((5,2),(5,3),(7,2),(7,3),(11,2)):
    n=p**r
    a=sum(comb(n,k)**3 for k in range(n+1) if k%p)
    b=sum(comb(n,k)**3 for k in range(0,n+1,p))-franel(n//p)
    assert a % p**(3*r+1) == p**(3*r)*leading_digit(p) % p**(3*r+1)
    assert b % p**(3*r+1) == 0

print(f"VERIFY_OK: {checks} exact prime-power comparisons; Bernoulli and residue-block checks")
