#!/usr/bin/env python3
"""Finite exact checks of the path law for rational ceiling iteration.
No finite check is claimed to establish the all-horizon theorem.
"""
from collections import Counter
from fractions import Fraction
from math import gcd


def phi(n):
    return sum(gcd(k,n)==1 for k in range(1,n+1))


def path(a, m, horizon):
    numerator, denominator = a, m
    output = [m]
    for _ in range(horizon):
        multiplier = (numerator + denominator - 1)//denominator
        numerator *= multiplier
        g = gcd(numerator,denominator)
        numerator //= g
        denominator //= g
        output.append(denominator)
    return tuple(output)


def audit(m, horizon):
    modulus = m**(horizon+1)
    observed = Counter(path(a,m,horizon)
                       for a in range(1,modulus+1) if gcd(a,m)==1)
    total = phi(modulus)
    assert sum(observed.values()) == total
    for pp,count in observed.items():
        probability = Fraction(1,1)
        for before,after in zip(pp,pp[1:]):
            assert before % after == 0
            probability *= Fraction(phi(after),before)
        assert Fraction(count,total) == probability, (m,horizon,pp,count,probability)
    # No positive-probability transition string may have been omitted.
    def allpaths(prefix):
        if len(prefix) == horizon+1:
            yield prefix
        else:
            value = prefix[-1]
            for d in range(1,value+1):
                if value % d == 0:
                    yield from allpaths(prefix+(d,))
    for pp in allpaths((m,)):
        if pp not in observed:
            raise AssertionError(('missing',m,horizon,pp))


def hensel_polynomial_check(m, exponent):
    # For every d|m and every unit r mod m, check unit-class
    # bijectivity of s -> (r-m)s + g*m*s*s modulo d**exponent.
    for d in range(2,m+1):
        if m%d: continue
        g=m//d
        modulus=d**exponent
        units={s for s in range(modulus) if gcd(s,d)==1}
        for r in range(1,m):
            if gcd(r,m)>1: continue
            images={((r-m)*s+g*m*s*s)%modulus for s in units}
            assert images == units, (m,d,exponent,r)


if __name__ == '__main__':
    for m in (2,3,4,6,8,9,10,12,15):
        for horizon in (1,2,3):
            audit(m,horizon)
    for m in range(2,17):
        for exponent in (1,2):
            hensel_polynomial_check(m,exponent)
    print('VERIFY_OK')
