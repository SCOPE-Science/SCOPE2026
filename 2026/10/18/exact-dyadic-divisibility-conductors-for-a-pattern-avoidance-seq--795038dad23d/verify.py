#!/usr/bin/env python3
"""Finite cross-checks for an exact 2-adic conductor theorem.

The supplied mathematical proof establishes the infinite statement.
This script provides independently organized finite consistency checks.
"""
from math import comb


def coefficients_from_quadratic(nmax):
    """Solve A(x)=(1-x)(1+2*x*A(x)^2) coefficientwise over Z."""
    a = []
    for n in range(nmax + 1):
        def q(t):
            return 0 if t < 0 else sum(a[i] * a[t-i] for i in range(t+1))
        a.append((1 if n == 0 else -1 if n == 1 else 0) + 2*q(n-1) - 2*q(n-2))
    return a


def coefficients_from_catalan(nmax):
    """Independently expand (1-x)*C(2*x*(1-x)**2)."""
    a = []
    for n in range(nmax + 1):
        z = 0
        for k in range((n-1)//3 if n else 0, n+1):
            h = n-k
            if 0 <= h <= 2*k+1:
                cat = comb(2*k,k)//(k+1)
                z += (2**k)*cat*(-1)**h*comb(2*k+1,h)
        a.append(z)
    return a


def conductor(r):
    assert r >= 1
    k = max(k for k in range(1,r+1) if k + k.bit_count() <= r+1)
    return 3*k-1


def main():
    nmax = 155
    a = coefficients_from_quadratic(nmax)
    b = coefficients_from_catalan(nmax)
    assert a == b
    assert a[:11] == [1,1,2,6,22,88,368,1584,6968,31192,141656]
    assert all(x > 0 for x in a)
    for k in range(140):
        c = comb(2*k,k)//(k+1)
        v = (c & -c).bit_length()-1
        assert v == (k+1).bit_count()-1
    for r in range(1,50):
        L = conductor(r)
        assert L <= nmax
        assert a[L-1] % (2**r) != 0
        assert all(x % (2**r) == 0 for x in a[L:])
        assert (L == 3*r-1) == (r & (r-1) == 0)
    # Published four-residue question, checked for a finite range of precisions.
    for alpha in range(6,40):
        mod = 2**alpha
        bad = {2**(alpha-1)+c for c in (1,2,6,22)}
        assert all(x % mod not in bad for x in a)
    assert [conductor(r) for r in range(1,17)] == [2,5,5,11,11,14,17,23,23,26,29,29,35,35,38,47]
    print('VERIFY_OK')
    print('coefficients_checked=', nmax+1)
    print('conductor_exponents_checked=49')
    print('valuation_indices_checked=140')
    print('open_question_precisions_checked=34')

if __name__ == '__main__':
    main()
