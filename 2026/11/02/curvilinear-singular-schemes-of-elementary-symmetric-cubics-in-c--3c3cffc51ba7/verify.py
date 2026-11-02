#!/usr/bin/env python3
"""Finite characteristic-two checks for an elementary-symmetric cubic gradient scheme.

The infinite-family theorem follows from the accompanying proof, not these examples.
No third-party libraries are required.
"""
from itertools import combinations, combinations_with_replacement
from math import comb


def gradient_binary(point):
    n = len(point)
    return [sum(point[j] * point[k] for j, k in combinations((j for j in range(n) if j != i), 2)) % 2 for i in range(n)]


def rank_gf2(rows):
    pivots = {}
    for row in rows:
        while row:
            j = row.bit_length() - 1
            if j in pivots:
                row ^= pivots[j]
            else:
                pivots[j] = row
                break
    return len(pivots)


def hilbert_quotient(n, degree):
    monomials = list(combinations_with_replacement(range(n), degree))
    if degree < 2:
        return len(monomials)
    index = {m: j for j, m in enumerate(monomials)}
    generators = [list(combinations((j for j in range(n) if j != i), 2)) for i in range(n-1)]
    rows = []
    for multiplier in combinations_with_replacement(range(n), degree-2):
        for terms in generators:
            row = 0
            for i, j in terms:
                monomial = tuple(sorted(multiplier+(i, j)))
                row ^= 1 << index[monomial]
            rows.append(row)
    return len(monomials) - rank_gf2(rows)


def check_double_point(n, subset):
    # Coordinates equal u on S and t outside S, in F_2[u,t]/(t^2).
    # Return coefficients of u^2 and ut in each partial derivative.
    s = len(subset)
    for i in range(n):
        if i in subset:
            uu = comb(s - 1, 2) if s-1 >= 2 else 0
            ut = (s-1) * (n-s)
        else:
            uu = comb(s, 2)
            ut = s * (n-s-1)
        assert uu % 2 == 0 and ut % 2 == 0, (n, subset, i, uu, ut)


def main():
    for n in (4, 8, 12, 16):
        size = sum(comb(n, s) for s in range(1, n+1) if s%4 == 1)
        assert size == 2**(n-2)
        assert 2*size == 2**(n-1)
        for s in range(1, n+1, 4):
            check_double_point(n, set(range(s)))
        print('length and local double-point checks', n, size, 2*size)

    for n in (4, 8):
        count = 0
        for mask in range(1,1 << n):
            point = [(mask >> i)&1 for i in range(n)]
            actual = all(z == 0 for z in gradient_binary(point))
            expected = (mask.bit_count()%4 == 1)
            assert actual == expected, (n, mask, actual, expected)
            if actual:count += 1
        assert count == 2**(n-2)
        for d in range(n+1):
            actual = hilbert_quotient(n, d)
            expected = sum(comb(n-1,j) for j in range(min(d,n-1)+1))
            assert actual == expected, (n,d,actual,expected)
        print('binary support and all initial Hilbert checks',n,'OK')
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
