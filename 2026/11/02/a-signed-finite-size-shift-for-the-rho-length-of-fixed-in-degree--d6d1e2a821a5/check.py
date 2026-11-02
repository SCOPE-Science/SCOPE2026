#!/usr/bin/env python3
"""Exact checks for finite restricted-in-degree random mapping orbit lengths."""
from fractions import Fraction
from itertools import permutations
from math import comb, factorial, pi, sqrt


def exact_survival(n, d):
    assert n % d == 0 and d >= 2
    m = n // d
    values = [Fraction(1)]
    p = Fraction(1)
    for k in range(1, m + 2):
        if k <= m:
            p *= Fraction(n - d * (k - 1), n - (k - 1))
            values.append(Fraction(n - k, n) * p)
        else:
            values.append(Fraction(0))
    return values


def independent_elementary_survival(n, d):
    m = n // d
    return [Fraction(n-k, n) * Fraction(d**k * comb(m, k), comb(n, k))
            for k in range(m + 1)] + [Fraction(0)]


def enumerate_survival(n,d):
    # Exactly n/d positive indegree vertices, each with indegree d.
    multi = tuple(i for i in range(n//d) for _ in range(d))
    tails = [0] * (n//d + 2)
    maps = 0
    for f in set(permutations(multi)):
        maps += 1
        for root in range(n):
            seen = set()
            v = root
            while v not in seen:
                seen.add(v)
                v = f[v]
            rho = len(seen)
            for k in range(rho):
                tails[k] += 1
    return [Fraction(x, maps*n) for x in tails], maps


def float_mean(n,d):
    m=n//d
    q=1.0
    ans=1.0
    for k in range(1,m+1):
        q *= (n-d*(k-1))/(n-k+1)
        ans += (n-k)/n*q
        if q < 1e-18 and k> 3*sqrt(n):
            break
    return ans


def main():
    count=0
    for n,d in [(4,2),(6,2),(6,3),(8,2),(8,4),(9,3)]:
        a=exact_survival(n,d)
        b=independent_elementary_survival(n,d)
        brute,num=enumerate_survival(n,d)
        assert a==b==brute,(n,d,a,b,brute)
        count+=3*len(a)
        assert sum(a) == sum(brute)
        count+=1
        print('EXACT',n,d,'maps',num,'E[R]',sum(a),'assertions',count)
    for d,n in [(2,10000),(3,12000),(4,12000),(5,15000),(10,30000)]:
        value=float_mean(n,d)
        c=(2*d-7)/(3*(d-1))
        delta=value-sqrt(pi*n/(2*(d-1)))
        assert abs(delta-c)<0.04, (n,d,delta,c)
        count += 1
        print('NUMERIC',n,d,'offset',round(delta,9),'limit',round(c,9))
    print('CHECK_OK',count)

if __name__=='__main__':
    main()
