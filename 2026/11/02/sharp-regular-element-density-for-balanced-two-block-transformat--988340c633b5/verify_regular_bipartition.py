"""Finite checks for regular maps preserving a balanced two-block partition.

This script uses explicit compositions for its small cases, independent of the
image-containment counting formula. It also evaluates the formula by Stirling
recursion and compares its larger-degree trend with the stated saddle constant.
"""
from functools import lru_cache
from itertools import product
from math import comb, factorial, exp, sqrt


def all_maps(n):
    for ch in product((0, 1), repeat=2):
        for a in product(range(n), repeat=n):
            for b in product(range(n), repeat=n):
                yield tuple(ch[0]*n+v for v in a) + tuple(ch[1]*n+v for v in b)


def compose(f, g):
    return tuple(g[v] for v in f)


def direct_count(n):
    maps = list(all_maps(n))
    reg = 0
    for f in maps:
        for g in maps:
            if compose(compose(f, g), f) == f:
                reg += 1
                break
    return reg


@lru_cache(None)
def stirling(n, k):
    if n == 0:
        return int(k == 0)
    if k == 0 or k > n:
        return 0
    return stirling(n-1, k-1) + k*stirling(n-1, k)


def predicted_count(n):
    a = sum(comb(n, s)*factorial(s)*stirling(n, s)*s**n for s in range(1, n+1))
    b = sum(comb(n, s)*(factorial(s)*stirling(n, s))**2 for s in range(1, n+1))
    return 2*n**(2*n) + 4*a-2*b


def saddle():
    def f(x):
        y = x/(1-exp(-x))
        return exp(-y) - (1+(x-1)*exp(x))
    l,r=0.1,1.0
    for _ in range(90):
        c=(l+r)/2
        if f(c)>0: l=c
        else:r=c
    x=(l+r)/2
    y=x/(1-exp(-x))
    F=1+(exp(x)-1)*exp(y)
    rho=F/(exp(2)*x*y)
    C=2/sqrt(x*y-(y-1)**2)
    return rho,C


def main():
    for n in range(1,4):
        actual = direct_count(n)
        expected = predicted_count(n)
        print('direct',n,actual,expected)
        assert actual == expected
    for n in range(4,13):
        val = predicted_count(n)
        assert 0 < val < 4*n**(2*n)
        print('formula',n,val)
    rho,C=saddle()
    print('rho',rho,'prefactor',C)
    assert 0.6967 < rho < 0.6968
    for n in (40,80):
        ratio = (predicted_count(n)/(4*n**(2*n))-.5)/(.5*C*rho**n)
        print('asymptotic_ratio',n,ratio)
        assert abs(ratio-1) < .01
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
