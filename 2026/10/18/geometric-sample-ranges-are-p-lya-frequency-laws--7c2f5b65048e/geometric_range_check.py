"""Exact checks for the geometric sample-range Eulerian identity.

Finite tests corroborate rather than replace the general proof, which uses
Savage--Visontai real-rootedness for the major-index Eulerian polynomial.
"""
from fractions import Fraction
from itertools import permutations
from math import comb


def polynomial_mul(a, b):
    c = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return c


def eulerian(q, n):
    a = [Fraction(0)] * n
    for p in permutations(range(1, n+1)):
        positions = [i + 1 for i in range(n-1) if p[i] > p[i+1]]
        a[len(positions)] += q**sum(n-i for i in positions)
    return a


def range_cdf(q, n, r):
    if r < 0:
        return Fraction(0)
    return ((1-q**(r+1))**n-q**n*(1-q**r)**n)/(1-q**n)


def fraction_pgf_coefficients(q, n, bound):
    coeff = [Fraction(1)]
    for k in range(1, n):
        g = [q**(k*j) for j in range(bound+1)]
        coeff = polynomial_mul(coeff, g)[:bound+1]
    coeff = polynomial_mul(coeff, eulerian(q,n))[:bound+1]
    norm = (1-q)**n/(1-q**n)
    return [norm*c for c in coeff]


def check():
    checks=0
    for n in range(2, 8):
        for q in [Fraction(1, 2), Fraction(1, 3), Fraction(2, 5), Fraction(4, 5)]:
            a = eulerian(q, n)
            assert all(c>0 for c in a)
            # Normalization of rational Eulerian formula at z=1.
            identity=(1-q)**n * sum(a)/(1-q**n)
            for k in range(1,n): identity/=1-q**k
            assert identity==1
            got=fraction_pgf_coefficients(q,n,10)
            expected=[range_cdf(q,n,r)-range_cdf(q,n,r-1) for r in range(11)]
            assert got == expected,(n,q,got,expected)
            checks+=len(got)+1
    # Binomial(3,1/2) parent and two draws: exact non-PF-infinity boundary.
    p=[Fraction(comb(3,k),8) for k in range(4)]
    direct=[sum((p[j]*p[j+r]*(2 if r else 1) for j in range(4-r)),Fraction(0)) for r in range(4)]
    assert direct==[Fraction(10,32),Fraction(15,32),Fraction(6,32),Fraction(1,32)]
    # Numerator factors (z+1)(z^2+5z+10); the quadratic discriminant is -15.
    assert polynomial_mul([Fraction(1),Fraction(1)], [Fraction(10),Fraction(5),Fraction(1)])==[Fraction(10),Fraction(15),Fraction(6),Fraction(1)]
    assert 5**2-4*10 == -15
    print('PASS',checks,'exact coefficient/normalization checks; counterexample discriminant -15')


if __name__=='__main__': check()
