#!/usr/bin/env python3
"""Exact finite cross-checks for Mersenne-index Domb valuations."""
from math import comb


def v2(n):
    assert n > 0
    return (n & -n).bit_length() - 1


def bits(n):
    assert n >= 0
    return n.bit_count()


def domb_direct(n):
    return sum(comb(n, k)**2 * comb(2*k, k) * comb(2*(n-k), n-k)
               for k in range(n+1))


def rogers_term(n, k):
    return (4**(n-2*k) * comb(2*k, k)**2 * comb(3*k, k)
            * comb(n+k, 3*k))


def domb_rogers(n):
    return sum(rogers_term(n,k) for k in range(n//2+1))


if __name__ == "__main__":
    coefficients = 80
    for n in range(coefficients):
        assert domb_direct(n) == domb_rogers(n), ("coefficient", n)
    for r in range(1, 10):
        n = (1 << r) - 1
        d = domb_direct(n)
        assert v2(d) == ({1: 2, 2: 8}.get(r, 3*r)), ("Domb index", r)
    summands = 0
    for r in range(3, 12):
        n = (1 << r) - 1
        minimizers = []
        for k in range(n//2+1):
            t = rogers_term(n, k)
            actual = v2(t)
            predicted = (2*(n-2*k) + 4*bits(k) + bits(n-2*k) - bits(n+k))
            assert actual == predicted, ("digit formula", r, k)
            j = (1 << (r-1))-1-k
            if k:
                predicted2 = 3*r + 4*j - 1 - 3*bits(j) + bits(j+1)
                assert actual == predicted2, ("complement formula", r, k)
            if actual == 3*r:
                minimizers.append(k)
            else:
                assert actual > 3*r
            summands += 1
        assert minimizers == [(1 << (r-1))-1], ("unique minimum", r, minimizers)
    print("VERIFY_OK", "identities", coefficients,
          "Domb Mersenne indices", 9, "summand comparisons", summands)
