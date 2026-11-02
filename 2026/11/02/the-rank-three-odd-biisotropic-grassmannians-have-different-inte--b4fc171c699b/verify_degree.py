#!/usr/bin/env python3
"""Exact coefficient and localization checks for rank-three biisotropic degrees.

Only Python standard library; no precomputed finite-count tables are inputs.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from math import factorial


def mul3(a, b):
    out = defaultdict(int)
    for u, c in a.items():
        for v, d in b.items():
            out[tuple(u[i] + v[i] for i in range(3))] += c * d
    return {u: c for u, c in out.items() if c}


def linear3(i, j, sign):
    zero = (0, 0, 0)
    a = [0, 0, 0]
    b = [0, 0, 0]
    a[i] += 1
    b[j] += 1
    return {tuple(a): 1, tuple(b): sign}


def aux_polynomial():
    p = {(0, 0, 0): 1}
    for i, j in [(0, 1), (0, 2), (1, 2)]:
        p = mul3(p, linear3(i, j, -1))
        p = mul3(p, linear3(i, j, 1))
        p = mul3(p, linear3(i, j, 1))
    return p


def mul1(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def falling_2n(shift, length):
    p = [1]
    for j in range(length):
        p = mul1(p, [shift-j, 2])
    return p


def polynomial_identity():
    aux = aux_polynomial()
    accum = [0] * 10
    for (a, b, c), coeff in aux.items():
        term = mul1(mul1(falling_2n(0, a), falling_2n(-1, b)), falling_2n(-2, c))
        for j, tj in enumerate(term):
            accum[j] += coeff*tj
    expected = [32]
    for fac in ([-1,1],[-3,2],[-1,2],[-165,404,-288,64]):
        expected = mul1(expected, fac)
    assert accum[:len(expected)] == expected
    assert all(x == 0 for x in accum[len(expected):])
    assert len(aux) == 30
    return aux


def coeff_degree(n, aux):
    d = 6*n-12
    ans = 0
    for (a,b,c),t in aux.items():
        ia = 2*n-a
        ib = 2*n-1-b
        ic = 2*n-2-c
        if min(ia,ib,ic) >= 0 and ia+ib+ic == d:
            ans += t*factorial(d)//(factorial(ia)*factorial(ib)*factorial(ic)) if t >= 0 else -(-t)*factorial(d)//(factorial(ia)*factorial(ib)*factorial(ic))
    return ans


def degree_formula(n):
    d = 6*n-12
    q = 64*n**3-288*n**2+404*n-165
    top = factorial(d)*32*(n-1)*(2*n-3)*(2*n-1)*q
    bottom = factorial(2*n)*factorial(2*n-1)*factorial(2*n-2)
    assert top % bottom == 0
    return top//bottom


def degree_ordinary(n):
    d=6*n-12
    num=2*factorial(d)
    den=factorial(2*n-2)*factorial(2*n-3)*factorial(2*n-4)
    assert num%den==0
    return num//den


def localization(n):
    N=2*n+1
    d=6*n-12
    result=Fraction(0)
    for I in combinations(range(N),3):
        outside=[j for j in range(N) if j not in I]
        numerator=sum(I)**d
        for a,b in combinations(I,2):
            numerator*= (a+b)**2
        denominator=1
        for i in I:
            for j in outside:
                denominator *= j-i
        result += Fraction(numerator,denominator)
    assert result.denominator == 1
    return int(result)


if __name__ == '__main__':
    aux=polynomial_identity()
    for n in range(3,10):
        calculated=coeff_degree(n,aux)
        formula=degree_formula(n)
        ordinary=degree_ordinary(n)
        assert calculated == formula and formula>ordinary
        q=64*n**3-288*n**2+404*n-165
        assert formula*n*(n-1)*(2*n-1) == ordinary*2*q
        assert 2*q-n*(n-1)*(2*n-1) == 3*(n-2)*(6*n-11)*(7*n-5)
        if n<=6:
            assert localization(n)==calculated
        print(f'n={n} degree_biisotropic={formula} degree_ordinary={ordinary}')
    print('VERIFY_OK: exact polynomial identity, seven coefficient degrees, four independent localization sums, and ratio identities')
