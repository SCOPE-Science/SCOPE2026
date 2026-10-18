#!/usr/bin/env python3
"""Finite independent checks of the universal-palindrome enumerator.

This is corroboration only. General validity is supplied by the paper's
combinatorial derivation and renewal argument, not by these finite tests.
"""
from collections import defaultdict
from functools import lru_cache
from itertools import product
from math import comb, factorial


def is_subsequence(pattern, word):
    it = iter(word)
    return all(any(x == target for x in it) for target in pattern)


def universal_index_direct(word, alphabet_size):
    # No arch factorization is used in this direct specification.
    idx = 0
    for k in range(1, len(word) // alphabet_size + 1):
        if all(is_subsequence(p, word)
               for p in product(range(alphabet_size), repeat=k)):
            idx = k
        else:
            break
    return idx


def archived_half(word, alphabet_size):
    arches = 0
    seen = set()
    for x in word:
        seen.add(x)
        if len(seen) == alphabet_size:
            arches += 1
            seen.clear()
    return arches, seen


def add(a, b, bound):
    c = [0] * (bound + 1)
    for i in range(bound + 1):
        c[i] = a[i] + b[i]
    return c


def mul(a, b, bound):
    c = [0] * (bound + 1)
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b[:bound-i+1]):
                c[i+j] += ai * bj
    return c


def inverse_1_minus_ct(c, bound):
    return [c**k for k in range(bound + 1)]


def rational_polys(q, bound):
    # Explicit numerator/product expansion, independent of word enumeration.
    arches = [0] * (bound + 1)
    if q <= bound:
        arches[q] = factorial(q)
    for j in range(1, q):
        arches = mul(arches, inverse_1_minus_ct(j, bound), bound)
    rest_all = [0] * (bound + 1)
    rest_top = None
    for j in range(q):
        r = [0] * (bound + 1)
        if j <= bound:
            r[j] = factorial(q) // factorial(q-j)
        for ell in range(1, j + 1):
            r = mul(r, inverse_1_minus_ct(ell, bound), bound)
        rest_all = add(rest_all, r, bound)
        if j == q-1:
            rest_top = r
    assert rest_top is not None
    return arches, rest_all, rest_top


def expected_coeffs(q, half_bound):
    A, R, Rtop = rational_polys(q, half_bound)
    # Collect polynomial in u by length variable t, t marks HALF length.
    # Complete arch counts using convolution.
    coeffs_even = defaultdict(int)
    coeffs_odd = defaultdict(int)
    arch_power = [1] + [0] * half_bound
    h = 0
    while h*q <= half_bound:
        poly = mul(arch_power, R, half_bound)
        high = mul(arch_power, Rtop, half_bound)
        for m in range(half_bound + 1):
            if poly[m]:
                coeffs_even[(m, 2*h)] += poly[m]
                coeffs_odd[(m, 2*h)] += q*poly[m] - high[m]
            if high[m]:
                coeffs_odd[(m, 2*h+1)] += high[m]
        arch_power = mul(arch_power, A, half_bound)
        h += 1
    return coeffs_even, coeffs_odd


def run():
    configurations = ((2, 7), (3, 5), (4, 4), (5, 3))
    for q, bound in configurations:
        even, odd = expected_coeffs(q, bound)
        for m in range(bound + 1):
            got_even = defaultdict(int)
            got_odd = defaultdict(int)
            min_even = {}
            min_odd = {}
            for x in product(range(q), repeat=m):
                ind = universal_index_direct(x + x[::-1], q)
                got_even[ind] += 1
                min_even.setdefault(ind, []).append(x)
                for middle in range(q):
                    ind = universal_index_direct(x + (middle,) + x[::-1], q)
                    got_odd[ind] += 1
                    min_odd.setdefault(ind, []).append((x, middle))
            for k in set(got_even) | {k for (mm,k) in even if mm == m}:
                assert got_even[k] == even[(m,k)], (q, m, k, got_even[k], even[(m,k)])
            for k in set(got_odd) | {k for (mm,k) in odd if mm == m}:
                assert got_odd[k] == odd[(m,k)], (q, m, k, got_odd[k], odd[(m,k)])
            # Explicit independent palindrome parity (Barker, Proposition 15).
            for x in product(range(q), repeat=m):
                h, residual = archived_half(x, q)
                assert universal_index_direct(x+x[::-1], q) == 2*h
                for middle in range(q):
                    predicted = 2*h + (len(residual) == q-1 and middle not in residual)
                    assert universal_index_direct(x+(middle,)+x[::-1], q) == predicted
        print('q=', q, 'verified all palindrome lengths through', 2*bound+1)
    # Sharp minimal-length formulas checked separately for q=2,3,4.
    for q in (2,3,4):
        for k in range(1, 5 if q==2 else 3):
            r = k//2
            length = q*k if k%2 == 0 else q*(k+1)-1
            predicted = factorial(q)**(r if k%2==0 else r+1)
            m = length//2
            assert m <= 8
            count = 0
            for x in product(range(q), repeat=m):
                if length%2 == 0:
                    count += universal_index_direct(x+x[::-1],q) >= k
                else:
                    for middle in range(q):
                        count += universal_index_direct(x+(middle,)+x[::-1],q) >= k
            assert count == predicted, (q,k,length,count,predicted)
        print('q=',q,'minimum-length extremals verified')
    print('ALL CHECKS PASSED (finite verification only)')

if __name__ == '__main__':
    run()
