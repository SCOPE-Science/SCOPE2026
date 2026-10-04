#!/usr/bin/env python3
from itertools import product
from math import comb
from fractions import Fraction


def iota_arch(w):
    k = 0
    seen = set()
    for c in w:
        seen.add(c)
        if len(seen) == 2:
            k += 1
            seen.clear()
    return k


def is_subsequence(v, w):
    it = iter(w)
    return all(any(c == d for d in it) for c in v)


def iota_direct(w):
    # Independent definition-based implementation, used only at small n.
    k = 0
    while True:
        nxt = k + 1
        if all(is_subsequence(v, w) for v in product('01', repeat=nxt)):
            k = nxt
        else:
            return k


def exact_formula(n, j):
    if n == 0:
        return 1 if j == 0 else 0
    if j == 0:
        return 2
    if j < 0 or 2*j > n:
        return 0
    a = comb(n-j-1, j-1)
    b = comb(n-j-1, j) if n-j-1 >= j else 0
    return (2**j) * (a + 2*b)


def universal_formula(n, k):
    if k == 0:
        return 2**n
    if n < 2*k:
        return 0
    return (2**k) * sum(
        (2**(n-2*k-r)) * comb(k+r-1, k-1)
        for r in range(n-2*k+1)
    )


def mean_formula(n):
    r = Fraction((-1)**n, 2**n)
    return Fraction(n,3) - Fraction(2,9) + Fraction(2,9)*r


def var_formula(n):
    r = Fraction((-1)**n, 2**n)
    return Fraction(2,81) * (1 + 2*r) * (3*n + 1 - r)


def check_small_definition(max_n=10):
    for n in range(max_n+1):
        for bits in product('01', repeat=n):
            w = ''.join(bits)
            a = iota_arch(w)
            d = iota_direct(w)
            if a != d:
                raise AssertionError(('definition mismatch', n, w, a, d))


def check_counts(max_n=18):
    for n in range(max_n+1):
        hist = [0]*(n//2+1)
        for bits in product('01', repeat=n):
            hist[iota_arch(bits)] += 1
        if sum(hist) != 2**n:
            raise AssertionError(('mass', n, sum(hist), 2**n))
        for j,c in enumerate(hist):
            f = exact_formula(n,j)
            if c != f:
                raise AssertionError(('exact count', n,j,c,f))
        # cumulative k-universal counts
        for k in range(n//2+2):
            c = sum(hist[k:]) if k < len(hist) else 0
            f = universal_formula(n,k)
            if c != f:
                raise AssertionError(('universal count', n,k,c,f))
        # exact first two moments
        den = 2**n
        mean = sum(Fraction(j*c, den) for j,c in enumerate(hist))
        second = sum(Fraction(j*j*c, den) for j,c in enumerate(hist))
        var = second - mean*mean
        if mean != mean_formula(n):
            raise AssertionError(('mean',n,mean,mean_formula(n)))
        if var != var_formula(n):
            raise AssertionError(('variance',n,var,var_formula(n)))


def check_recurrence(max_n=80):
    # Coefficient recurrence from (1-z-2u z^2)F=1+z.
    N = {(0,0):1}
    for n in range(1,max_n+1):
        for j in range(n//2+1):
            rec = N.get((n-1,j),0) + 2*N.get((n-2,j-1),0)
            if n == 1 and j == 0:
                rec += 1
            N[n,j] = rec
            if rec != exact_formula(n,j):
                raise AssertionError(('recurrence',n,j,rec,exact_formula(n,j)))


def main():
    check_small_definition()
    check_counts()
    check_recurrence()
    print('VERIFY_OK definition_n<=10 exhaustive_n<=18 recurrence_n<=80')

if __name__ == '__main__':
    main()
