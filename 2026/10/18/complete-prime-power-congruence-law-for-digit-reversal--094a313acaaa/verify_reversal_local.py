#!/usr/bin/env python3
"""Exact finite modular checks for local digit-reversal gcd theorem."""
from fractions import Fraction
from collections import defaultdict
from math import gcd


def reverse_digits(n, b):
    r = 0
    while n:
        r = r*b + n%b
        n //= b
    return r


def valuation(n, p):
    z = 0
    while n and n % p == 0:
        n //= p
        z += 1
    return z


def predicted(b, p, a):
    q = p**a
    if b % p:
        tau = valuation(b*b-1, p)
        return Fraction(1, p**(2*a-min(a, tau)))
    e = valuation(b, p)
    t = min(e, a)
    return Fraction(b//p**t-1, b-1) / p**(2*a-t)


def direct_count(b, p, a, ell):
    q = p**a
    low, high = b**(ell-1), b**ell
    favorable = sum(n%q == 0 and reverse_digits(n,b)%q == 0
                    for n in range(low,high))
    return Fraction(favorable, high-low)


def group_index_check(b, p, a):
    q = p**a
    if b % p == 0:
        return
    tau = valuation(b*b-1,p)
    u = min(a,tau)
    v0 = (1,1)
    v1 = (b%q, pow(b,-1,q))
    image = {((r*v0[0]+s*v1[0])%q,
              (r*v0[1]+s*v1[1])%q)
             for r in range(q) for s in range(q)}
    expected = {(x,y) for x in range(q) for y in range(q)
                if (y-x)%p**u == 0}
    assert image == expected,(b,p,a,len(image),len(expected))
    assert len(image) == p**(2*a-u)


def exact_modular_pair(b,p,a,ell):
    """Exact DP for the normalized joint residue, with leading digit constraint."""
    q=p**a
    ib=pow(b,-1,q)
    states={(0,0):1}
    mult1=mult2=1
    for j in range(ell):
        next_states=defaultdict(int)
        choices=range(1,b) if j==ell-1 else range(b)
        for (x,y),count in states.items():
            for d in choices:
                key=((x+d*mult1)%q,(y+d*mult2)%q)
                next_states[key]+=count
        states=next_states
        mult1=(mult1*b)%q
        mult2=(mult2*ib)%q
    assert sum(states.values())==(b-1)*b**(ell-1)
    return states


if __name__ == '__main__':
    exact_tests=[(2,2,1,10),(4,2,1,6),(4,2,2,6),
                 (6,2,1,6),(6,3,1,6),
                 (10,2,1,5),(10,2,2,5),
                 (10,5,1,5),(10,5,2,5),(12,2,3,5)]
    for b,p,a,ell in exact_tests:
        assert ell>=2*((a+valuation(b,p)-1)//valuation(b,p))
        actual=direct_count(b,p,a,ell)
        goal=predicted(b,p,a)
        assert actual==goal,(b,p,a,ell,actual,goal)
    independent_test_count=len(exact_tests)

    group_tests=[(2,3,1),(2,3,2),(2,7,1),
                 (3,2,1),(3,2,2),(5,2,3),
                 (10,3,1),(10,3,2),(10,3,3),
                 (10,7,1),(10,11,1),(10,11,2)]
    for b,p,a in group_tests:
        group_index_check(b,p,a)

    convergence_tests=[(2,3,2,85,Fraction(1,150)),
                       (10,3,3,32,Fraction(1,500)),
                       (10,7,1,22,Fraction(1,500)),
                       (10,11,1,28,Fraction(1,500))]
    for b,p,a,ell,tolerance in convergence_tests:
        states=exact_modular_pair(b,p,a,ell)
        q=p**a
        u=min(a,valuation(b*b-1,p))
        assert all((x-y)%(p**u)==0 for x,y in states)
        total=sum(states.values())
        actual=Fraction(states.get((0,0),0),total)
        goal=predicted(b,p,a)
        assert abs(actual-goal) < tolerance,(b,p,a,ell,actual,goal)
    print('REVERSAL_LOCAL_EXACT_REGRESSION_OK',
          'exact_divisibility',independent_test_count,
          'group_images',len(group_tests),
          'modular_convergence',len(convergence_tests))
    print('Exact base-ten p=3,a=3 limit:',predicted(10,3,3))
    print('Exact base-ten p=11,a=2 limit:',predicted(10,11,2))
