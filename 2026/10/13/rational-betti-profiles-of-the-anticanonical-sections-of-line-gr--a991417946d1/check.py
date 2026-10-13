#!/usr/bin/env python3
"""Exact cohomology-rank checks for anticanonical Plucker sections of Gr(2,N)."""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb


def multiply(f, g, limit):
    out = defaultdict(int)
    for (i, j), a in f.items():
        for (k, l), b in g.items():
            if i + j + k + l <= limit:
                out[(i+k, j+l)] += a*b
    return {key: v for key, v in out.items() if v}


def binomial_product_axis(n, axis, limit):
    return {(r, 0) if axis == 0 else (0, r): comb(n, r)
            for r in range(min(n, limit)+1)}


def inverse_hyperplane(n, d):
    out = {}
    for r in range(d+1):
        for i in range(r+1):
            out[(i, r-i)] = (-1)**r*comb(n+r-1, r)*comb(r, i)
    return out


def inverse_difference(d):
    out = defaultdict(int)
    for j in range(d//2+1):
        for i in range(2*j+1):
            out[(i, 2*j-i)] += comb(2*j, i)*(-1)**(2*j-i)
    return dict(out)


def hyperplane_power(n):
    return {(i, n-i): comb(n, i) for i in range(n+1)}


def chern_top(n):
    d = n-4
    c = multiply(binomial_product_axis(n, 0, d),
                 binomial_product_axis(n, 1, d), d)
    c = multiply(c, inverse_hyperplane(n, d), d)
    c = multiply(c, inverse_difference(d), d)
    return {key: val for key, val in c.items() if sum(key) == d}


def euler_by_alternant(n, c):
    f = multiply(hyperplane_power(n), c, 2*n-4)
    return f.get((n-2, n-2), 0)-f.get((n-1, n-3), 0)


def euler_by_localization(n, f, hyper_exponent):
    total = Fraction(0)
    for i, j in combinations(range(n), 2):
        numerator = (i+j)**hyper_exponent * sum(
            a*i**p*j**q for (p, q), a in f.items())
        denominator = 1
        for k in range(n):
            if k != i and k != j:
                denominator *= (i-k)*(j-k)
        total += Fraction(numerator, denominator)
    return total


def betti_profile(n, e):
    d = n-4
    betti = [0]*(2*d+1)
    low = []
    for s in range((d-1)//2+1):
        a = s//2+1
        betti[2*s] = a
        betti[2*d-2*s] = a
        low.append(a)
    betti[d] = e-2*sum(low)
    primitive = betti[d]-(d//4+1)
    assert sum(betti) == e
    return betti, primitive


def main():
    expectations = {
        6: (24, 21),
        8: (636, 630),
        10: (24920, 24910),
        12: (1082256, 1082241),
    }
    for n, (expected_e, expected_primitive) in expectations.items():
        c = chern_top(n)
        e = euler_by_alternant(n, c)
        assert e == expected_e
        assert euler_by_localization(n, c, n) == e
        assert euler_by_localization(n, {(n-2, n-2): 1}, 0) == 1
        betti, primitive = betti_profile(n, e)
        assert primitive == expected_primitive
        if n == 10:
            assert betti == [1,0,1,0,2,0,24912,0,2,0,1,0,1]
            assert c == {(0,6):1,(1,5):24,(2,4):195,(3,3):380,
                         (4,2):195,(5,1):24,(6,0):1}
        print('N=%d; Euler=%d; primitive_middle=%d; betti=%s' %
              (n, e, primitive, betti))
    print('GRASSMANNIAN_CY_BETTI_EXACT_OK')


if __name__ == '__main__':
    main()
