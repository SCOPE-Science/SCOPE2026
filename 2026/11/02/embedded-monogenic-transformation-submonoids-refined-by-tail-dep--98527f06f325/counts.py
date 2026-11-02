"""Compute counts of embedded monogenic submonoids by cycle-type summation.
Standalone, using exact integer/rational arithmetic only.
"""
from collections import Counter
from fractions import Fraction
from math import factorial, gcd, comb


def integer_partitions(n, cap=None):
    if n==0:
        yield ()
    else:
        for x in range(min(n, cap or n), 0, -1):
            for rest in integer_partitions(n-x, x):
                yield (x,)+rest


def phi(n):
    return sum(gcd(k,n)==1 for k in range(1,n+1))


def permutation_counts(m):
    for typ in integer_partitions(m):
        mult=Counter(typ)
        z=1
        for j,r in mult.items():
            z *= j**r*factorial(r)
        cnt=factorial(m)//z
        period=1
        for j in typ:
            period=period*j//gcd(period,j)
        yield cnt,period


def submonoids(n):
    total=Fraction(n**n)
    loss=Fraction(0)
    for m in range(1,n+1):
        weight=comb(n,m)*m**(n-m)
        for cnt,p in permutation_counts(m):
            loss += weight*cnt*(1-Fraction(1,phi(p)))
    assert (total-loss).denominator==1
    return int(total-loss)


if __name__=='__main__':
    expect=[1,4,26,237,2842,42488]
    for n in range(1,13):
        value=submonoids(n)
        if n<=len(expect): assert value==expect[n-1]
        print(n,value)
    print('FORMULA_OK')
