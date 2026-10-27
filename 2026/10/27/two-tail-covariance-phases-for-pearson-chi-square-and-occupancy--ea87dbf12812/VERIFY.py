#!/usr/bin/env python3
"""Exact-rational verification for the Pearson/occupancy-frequency covariance law.

Usage: python3 VERIFY.py
Requires only Python 3 standard library. All finite comparisons are exact.
"""
from fractions import Fraction
from math import comb, factorial


def compositions(total, boxes):
    if boxes == 1:
        yield (total,)
    else:
        for first in range(total + 1):
            for tail in compositions(total - first, boxes - 1):
                yield (first,) + tail


def binomial_mass(k, N, p):
    if k < 0 or k > N:
        return Fraction(0)
    return Fraction(comb(N, k)) * p**k * (1 - p)**(N-k)


def test():
    coordinate_checks = 0
    curvature_checks = 0
    configurations = 0
    for m in range(2, 8):
        p = Fraction(1, m)
        q = 1-p
        for n in range(2, 11):
            if comb(n+m-1, m-1) > 25000:
                continue
            EX = Fraction(0)
            ER = [Fraction(0)] * (n+1)
            EXR = [Fraction(0)] * (n+1)
            fs = [lambda k: (k+1)**3, lambda k: (-1)**k*(k+1)]
            EF = [Fraction(0)] * len(fs)
            EXF = [Fraction(0)] * len(fs)
            for occ in compositions(n, m):
                weight = Fraction(factorial(n), m**n)
                for k in occ:
                    weight /= factorial(k)
                chisq = Fraction(m, n) * sum(k*k for k in occ) - n
                counts = [occ.count(r) for r in range(n+1)]
                EX += weight*chisq
                for r in range(n+1):
                    ER[r] += weight*counts[r]
                    EXR[r] += weight*chisq*counts[r]
                for j, f in enumerate(fs):
                    ff = sum(f(k) for k in occ)
                    EF[j] += weight*ff
                    EXF[j] += weight*chisq*ff
                configurations += 1
            assert EX == m-1, (m, n, EX)
            for r in range(n+1):
                raw = EXR[r]-EX*ER[r]
                b = lambda z: binomial_mass(z, n-2, p)
                curvature = (n-1)*q*(b(r-2)-2*b(r-1)+b(r))
                poly = r*(r-1)-2*r*(n-1)*p+n*(n-1)*p*p
                closed = binomial_mass(r, n, p)*poly/(n*p*p*q)
                assert raw == curvature == closed, (m, n, r, raw, closed)
                if r == 1:
                    assert (raw > 0)-(raw < 0) == (n > 2*m)-(n < 2*m)
                coordinate_checks += 1
            for j, f in enumerate(fs):
                curvature = (n-1)*q*sum(
                    binomial_mass(k, n-2, p) *
                    (f(k+2)-2*f(k+1)+f(k))
                    for k in range(n-1)
                )
                assert EXF[j]-EX*EF[j] == curvature, (m,n,j)
                curvature_checks += 1
    Pell_cases=[(3,3),(3,10),(15,10),(15,51),(85,51),(85,290)]
    for m, n in Pell_cases:
        assert n*n-(4*m+1)*n+2*m*m+4*m == 0, (m, n)
        k=abs(2*n-(4*m+1))
        assert k*k-2*(2*m-1)**2 == -1
    print('PASS: exact coordinate covariance checks:',coordinate_checks)
    print('PASS: exact nonlinear curvature checks:',curvature_checks)
    print('PASS: complete occupancy configurations:',configurations)
    print('PASS: Pell-zero integer examples:',len(Pell_cases))


if __name__ == '__main__':
    test()
