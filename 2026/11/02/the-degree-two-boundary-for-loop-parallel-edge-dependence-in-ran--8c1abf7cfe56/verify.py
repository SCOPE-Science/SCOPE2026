#!/usr/bin/env python3
"""Finite checks for an exact configuration-model loop/parallel-pair theorem.

This program checks finite instances only. The all-size theorem uses the
separate symbolic counting and inequality proof.
"""
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, combinations_with_replacement
from math import comb


@lru_cache(None)
def pairings(stubs):
    if not stubs:
        return ((),)
    first = stubs[0]
    return tuple(((first, stubs[k]),) + rem
                 for k in range(1, len(stubs))
                 for rem in pairings(stubs[1:k] + stubs[k+1:]))


def covariance_from_all_matchings(degrees):
    labels = tuple(i for i, d in enumerate(degrees) for _ in range(d))
    total = loops = doubles = mixed = 0
    for pairing in pairings(tuple(range(len(labels)))):
        total += 1
        L = 0
        edges = {}
        for p, q in pairing:
            i, j = labels[p], labels[q]
            if i == j:
                L += 1
            else:
                edge = (min(i, j), max(i, j))
                edges[edge] = edges.get(edge, 0) + 1
        P = sum(x * (x - 1) // 2 for x in edges.values())
        loops += L
        doubles += P
        mixed += L * P
    return Fraction(mixed, total) - Fraction(loops * doubles, total * total)


def algebra(degrees):
    m = sum(degrees)
    assert m >= 6 and m % 2 == 0
    a = [comb(d, 2) for d in degrees]
    A = sum(a)
    B = sum(a[i] * a[j] for i in range(len(a)) for j in range(i+1, len(a)))
    F = sum(a[i] * (2*d - 3) * (A - a[i]) for i, d in enumerate(degrees))
    D = (m - 1)*F - 4*A*B
    covariance = Fraction(-2*D, (m-1)**2*(m-3)*(m-5))
    return A, B, F, D, covariance


def certificate(degrees):
    A, B, F, D, covariance = algebra(degrees)
    active = [i for i, d in enumerate(degrees) if d >= 2]
    leaves = sum(d == 1 for d in degrees)
    a = [comb(d,2) for d in degrees]
    q = lambda x,y: 2*x*y - 3*(x+y) + 3
    rhs = sum(a[i]*a[j]*q(degrees[i], degrees[j]) for i,j in combinations(active,2))
    for i,j,k in combinations(active,3):
        x,y,z = degrees[i],degrees[j],degrees[k]
        T = (a[i]*a[j]*z*(x+y-z-2) +
             a[i]*a[k]*y*(x+z-y-2) +
             a[j]*a[k]*x*(y+z-x-2))
        assert T >= 0
        assert (T == 0) == (x == y == z == 2)
        rhs += T
    rhs += leaves*sum(a[i]*a[j]*(degrees[i]+degrees[j]-3)
                      for i,j in combinations(active,2))
    assert 2*rhs == D
    if B:
        only_twos = all(d in (0,2) for d in degrees)
        assert (covariance > 0) == only_twos
        assert covariance != 0
    else:
        assert covariance == 0
    return 1


def regular_closed_form(d, n):
    m = d*n
    numerator = n*(n-1)*d*d*(d-1)**2*(m*(2-d)+2*d-3)
    return Fraction(numerator,2*(m-1)**2*(m-3)*(m-5))


def check():
    exact_cases = 0
    for m in (6, 8, 10):
        for v in range(2, 7):
            for ds in combinations_with_replacement(range(1,m+1),v):
                if sum(ds) != m:
                    continue
                direct = covariance_from_all_matchings(ds)
                assert direct == algebra(ds)[-1], (ds, direct, algebra(ds)[-1])
                certificate(ds)
                exact_cases += 1
    inequality_cases = 0
    for m in range(6, 25, 2):
        for v in range(2, 7):
            for ds in combinations_with_replacement(range(0, m+1), v):
                if sum(ds) == m:
                    certificate(ds)
                    inequality_cases += 1
    regular_cases = 0
    for d in range(2, 11):
        for n in range(2, 51):
            if n*d >= 6 and n*d % 2 == 0:
                assert algebra((d,)*n)[-1] == regular_closed_form(d,n)
                regular_cases += 1
    print(f"OK: {exact_cases} independently enumerated degree profiles; "
          f"{inequality_cases} finite sign/decomposition profiles; "
          f"{regular_cases} regular-degree identities")


if __name__ == "__main__":
    check()
