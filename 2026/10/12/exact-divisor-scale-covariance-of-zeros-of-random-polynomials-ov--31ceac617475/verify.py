#!/usr/bin/env python3
"""Exact finite checks for finite-ring polynomial zero-count covariance."""
from fractions import Fraction
from itertools import product
from math import gcd, prod


def phi(d):
    return sum(gcd(j, d) == 1 for j in range(1, d + 1))


def divisors(m):
    return [d for d in range(1, m + 1) if m % d == 0]


def predicted_cov(m, a, b):
    g = gcd(m, *(x-y for x, y in zip(a, b)))
    return Fraction(g - 1, m*m)


def predicted_variance(m, n):
    return m**(2*n-2)*sum((Fraction(phi(d), d**n) for d in divisors(m) if d > 1), Fraction(0))


def subset_variance_from_classes(m, n, subset):
    total = Fraction(0)
    for d in divisors(m):
        if d == 1:
            continue
        counts = {}
        for a in subset:
            v = tuple(x % d for x in a)
            counts[v] = counts.get(v, 0) + 1
        total += Fraction(phi(d), m*m)*sum(v*v for v in counts.values())
    return total


def exhaustive(m, n, exponents):
    assert (0,)*n in exponents
    for i in range(n):
        assert tuple(1 if i == j else 0 for j in range(n)) in exponents
    pts = list(product(range(m), repeat=n))
    monomials = [[prod(pow(x, t, m) for x, t in zip(a, ex)) % m for a in pts] for ex in exponents]
    coefficients = product(range(m), repeat=len(exponents))
    num = m**len(exponents)
    total_roots = 0
    sum_sq = 0
    pair_sum = [[0]*len(pts) for _ in pts]
    marginal = [0]*len(pts)
    subset = [i for i, a in enumerate(pts) if (sum((i+1)*a[i] for i in range(n)) % 3) != 1]
    subset_s = 0
    subset_sq = 0
    for coeff in coefficients:
        vals = [sum(c*term[j] for c, term in zip(coeff, monomials)) % m for j in range(len(pts))]
        roots = [j for j, v in enumerate(vals) if v == 0]
        k = len(roots)
        total_roots += k
        sum_sq += k*k
        s = sum(j in roots for j in subset)
        subset_s += s
        subset_sq += s*s
        for i in roots:
            marginal[i] += 1
            for j in roots:
                pair_sum[i][j] += 1
    mean = Fraction(total_roots, num)
    variance = Fraction(sum_sq, num) - mean*mean
    assert mean == m**(n-1), (m, n, mean)
    assert variance == predicted_variance(m, n), (m, n, variance, predicted_variance(m, n))
    for i, a in enumerate(pts):
        assert Fraction(marginal[i], num) == Fraction(1,m), (m,n,a)
        for j, b in enumerate(pts):
            cov = Fraction(pair_sum[i][j], num) - Fraction(1, m*m)
            assert cov == predicted_cov(m, a, b), (m, n, a, b, cov, predicted_cov(m, a, b))
    partial_mean = Fraction(subset_s, num)
    partial_var = Fraction(subset_sq, num) - partial_mean*partial_mean
    assert partial_mean == Fraction(len(subset), m)
    assert partial_var == subset_variance_from_classes(m, n, [pts[i] for i in subset])
    return len(pts)**2, num


def main():
    cases = [
        (2,1,[(0,),(1,)]),
        (4,1,[(0,),(1,)]),
        (4,1,[(0,),(1,),(2,)]),
        (6,1,[(0,),(1,),(2,)]),
        (8,1,[(0,),(1,),(2,)]),
        (9,1,[(0,),(1,),(2,)]),
        (4,2,[(0,0),(1,0),(0,1)]),
        (4,2,[(0,0),(1,0),(0,1),(1,1),(2,0),(0,2)]),
        (6,2,[(0,0),(1,0),(0,1)]),
        (3,3,[(0,0,0),(1,0,0),(0,1,0),(0,0,1)]),
    ]
    cov_checks = 0
    polys = 0
    for m,n,ex in cases:
        p,num = exhaustive(m,n,ex)
        cov_checks += p
        polys += num
        print('OK', 'modulus',m,'variables',n,'monomials',len(ex),'polynomials',num,'pairs',p)
    identity_checks = 0
    for m in range(2,31):
        for n in range(1,5):
            lattice_sum = sum((gcd(m, *a)-1 for a in product(range(m), repeat=n))) if m**n<=100000 else None
            if lattice_sum is not None:
                assert Fraction(lattice_sum,m**2)*m**n == predicted_variance(m,n)
            assert sum((phi(d) for d in divisors(m))) == m
            if n == 1:
                fac = sum(Fraction(phi(d),d) for d in divisors(m) if d>1)
                assert predicted_variance(m,n)==fac
            identity_checks += 1
    print('PASS: exhaustive', len(cases),'ensembles,',polys,'polynomials,',cov_checks,'ordered pair tests;',identity_checks,'modulus-dimension divisor checks')

if __name__ == '__main__':
    main()
