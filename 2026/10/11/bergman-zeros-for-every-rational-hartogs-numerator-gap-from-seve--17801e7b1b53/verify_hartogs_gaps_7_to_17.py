#!/usr/bin/env python3
"""Exact rational positivity certificate for diagonal Bergman numerators.

Python 3 standard library only; no numerical approximation is used in assertions.
The mathematical proof of polynomial interpolation degree <= 3 is supplied
separately, not inferred from finite evaluations.
"""
from fractions import Fraction as F
from math import comb, gcd

LEVELS = {7: 4, 8: 6, 9: 6, 10: 6, 11: 7, 12: 8,
          13: 8, 14: 8, 15: 8, 16: 9, 17: 9}


def add(a, b):
    return [x + y for x, y in zip(a, b)]


def scale(a, z):
    return [z*x for x in a]


def mul(a, b):
    degree = len(a) - 1
    c = [F(0)] * (degree+1)
    for i in range(degree+1):
        for j in range(degree+1-i):
            c[i+j] += a[i]*b[j]
    return c


def chebyshev(degree):
    one = [F(1)] + [F(0)]*degree
    arg = [F(-1), F(2)] + [F(0)]*(degree-1)
    p = [one, arg]
    for j in range(2, degree+1):
        p.append(add(scale(mul(arg, p[-1]), 2), scale(p[-2], -1)))
    return p


def qcoeff(k, m):
    """Edholm--Mathew (3.21), reindexed using j=1,...,m-1."""
    assert 7 <= k <= 17 and m > k and gcd(k, m) == 1
    c = [0]*(2*k+1)
    c[k] = m*m
    for j in range(1, m):
        e = (k*j-1)//m
        tau = k*j-e*m
        assert 0 <= e < k and 1 <= tau < m
        c[e] += j*(m-tau)
        c[e+1] += j*tau
        c[e+k] += (m-j)*(m-tau)
        c[e+k+1] += (m-j)*tau
    assert all(c[i] == c[2*k-i] for i in range(2*k+1))
    return c


def angular_polynomial(k, m, cheb):
    c = qcoeff(k, m)
    p = [F(c[k])] + [F(0)]*k
    for j in range(1, k+1):
        p = add(p, scale(cheb[j], 2*c[k-j]))
    return p


def interpolate_in_q(k, residue, cheb):
    """Return q^0,...,q^3 coefficients; cubic degree is a proved lemma."""
    f = [angular_polynomial(k, k*(a+1)+residue, cheb) for a in range(4)]
    d1 = add(f[1], scale(f[0], -1))
    d2 = add(add(f[2], scale(f[1], -2)), f[0])
    d3 = add(add(f[3], scale(f[2], -3)),
             add(scale(f[1], 3), scale(f[0], -1)))
    return (f[0], add(add(d1, scale(d2, F(-1,2))), scale(d3, F(1,3))),
            add(scale(d2, F(1,2)), scale(d3, F(-1,2))), scale(d3, F(1,6)))


def bernstein_coefficients(poly):
    d = len(poly)-1
    return [sum(poly[j]*F(comb(i,j),comb(d,j)) for j in range(i+1))
            for i in range(d+1)]


def bisect_bernstein(b):
    """Exact de Casteljau subdivision at x=1/2."""
    left, right = [b[0]], [b[-1]]
    prev = b
    for _ in range(len(b)-1):
        prev = [(prev[i]+prev[i+1])/2 for i in range(len(prev)-1)]
        left.append(prev[0])
        right.append(prev[-1])
    return left, right[::-1]


def min_bernstein(poly, levels):
    chunks = [bernstein_coefficients(poly)]
    for _ in range(levels):
        chunks = [half for b in chunks for half in bisect_bernstein(b)]
    return min(min(b) for b in chunks)


def fejer_polynomial(k, cheb):
    # |1+exp(i theta)+...+exp(i(k-1)theta)|^2.
    p = [F(k)] + [F(0)]*k
    for j in range(1,k):
        p = add(p, scale(cheb[j], 2*(k-j)))
    return mul(p, [F(1),F(2)]+[F(0)]*(k-1))


def run():
    cases = 0
    for k, level in LEVELS.items():
        cc = chebyshev(k)
        f = fejer_polynomial(k, cc)
        smallest = None
        for r in range(1,k):
            if gcd(r,k)!=1:
                continue
            a0,a1,a2,a3 = interpolate_in_q(k,r,cc)
            assert a3 == scale(f, F(k,3))
            assert a2 == scale(f, k+r)
            for p in (a0,a1):
                low = min_bernstein(p, level)
                assert low > F(1,200), (k,r,low)
                if smallest is None or low < smallest:
                    smallest = low
            # Independent finite consistency tests, not substitutes for degree proof.
            for q in (4,13):
                calc = add(add(a0, scale(a1, q)),
                           add(scale(a2, q*q), scale(a3, q*q*q)))
                assert calc == angular_polynomial(k, k*(q+1)+r, cc)
            cases+=1
        print(f'k={k}: level={level}, residues={sum(gcd(r,k)==1 for r in range(1,k))}, '
              f'least Bernstein coefficient > 1/200: {smallest > F(1,200)}',flush=True)
    print(f'PASS: exact certificate, {cases} reduced-residue families, all positive.')

if __name__ == '__main__':
    run()
