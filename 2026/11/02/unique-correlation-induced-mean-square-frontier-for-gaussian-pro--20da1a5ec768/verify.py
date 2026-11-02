#!/usr/bin/env python3
"""Exact-rational checks for the scalar Gaussian-probe transition."""
from fractions import Fraction as F
from functools import lru_cache
from math import factorial


def dfact_odd(k):
    if k < 1:
        return 1
    result = 1
    for j in range(k, 0, -2):
        result *= j
    return result


def gaussian_expect(poly):
    return sum(v * dfact_odd(power - 1) for power, v in poly.items() if power % 2 == 0)


def product(p, q):
    r = {}
    for i, a in p.items():
        for j, b in q.items():
            r[i+j] = r.get(i+j, F(0)) + a*b
    return {i: a for i, a in r.items() if a}


def binomial(n, k):
    return factorial(n)//(factorial(k)*factorial(n-k))


def ou_polynomial(p, rho):
    # Exact Gaussian conditional expectation given Z=z,
    # Z'=rho*z+sqrt(1-rho*rho)*N, N standard normal.
    r = {}
    for n, a in p.items():
        for k in range(0, n+1, 2):
            v = a*binomial(n, k)*rho**(n-k)*(1-rho*rho)**(k//2)*dfact_odd(k-1)
            j = n-k
            r[j] = r.get(j, F(0)) + v
    return {i: a for i, a in r.items() if a}


def moment_sequence(c, rho, max_m):
    f = {0:F(1), 2:-2*c, 4:c*c}
    q = {0:F(1)}
    out = [F(1)]
    for _ in range(max_m):
        q = product(f, ou_polynomial(q, rho))
        out.append(gaussian_expect(q))
    return out


def bivar_moment(a, b, rho):
    # Wick pairing enumeration, independent of the polynomial OU recursion.
    covariance = ((F(1),rho),(rho,F(1)))
    @lru_cache(None)
    def wick(indices):
        if not indices:
            return F(1)
        first = indices[0]
        return sum(covariance[first][indices[k]]*wick(indices[1:k]+indices[k+1:])
                   for k in range(1,len(indices)))
    return wick((0,)*a+(1,)*b)


def main():
    checks = 0
    for c in (F(1,10), F(1,3), F(1,2), F(1)):
        for rho in (F(0),F(1,5),F(1,2),F(3,4)):
            seq=moment_sequence(c,rho,6)
            expectation=1-2*c+3*c*c
            assert seq[1] == expectation
            checks+=1
            if rho==0:
                assert all(seq[m] == expectation**m for m in range(7))
                checks+=7
            # Independent bivariate Gaussian Wick computation of two weights.
            pol={0:F(1),2:-2*c,4:c*c}
            joint=sum(a*b*bivar_moment(i,j,rho) for i,a in pol.items() for j,b in pol.items())
            assert seq[2] == joint
            checks+=1
            assert all(s>0 for s in seq)
            checks+=1
    for J in (1,2,3,5,10,23):
        c=F(1,2)
        avg_square=(F(3*J+J*(J-1),J*J))
        assert avg_square==1+F(2,J)
        moment=1-2*c+c*c*avg_square
        assert moment==F(1,4)+F(1,2*J)
        checks+=2
    c=F(1,2); rho=F(1,2)
    seq=moment_sequence(c,rho,7)
    assert seq[1] == F(3,4)
    assert seq[2] == F(25,32)
    assert seq[2]/seq[1] == F(25,24) > 1
    checks+=3
    # Hermite spectral identity: f=3/4+(1/2)He_2+(1/4)He_4,
    # with E He_n(Z)He_n(Z')=n! rho^n.
    for rho in (F(0),F(1,5),F(1,2),F(3,4)):
        corr=F(3,4)**2+F(1,2)*rho*rho+F(3,2)*rho**4
        assert corr==moment_sequence(c,rho,2)[2]
        checks+=1
    print('VERIFY_OK',checks,'exact rational checks; witness',seq[2]/seq[1]);

if __name__=='__main__':
    main()
