#!/usr/bin/env python3
"""Exact finite checks for graph-adjacency/cycle covariance in uniform permutations."""
from fractions import Fraction
from itertools import permutations
from math import factorial
from random import Random


def cycle_count(perm):
    n = len(perm)
    visited = [False] * n
    count = 0
    for i in range(n):
        if visited[i]:
            continue
        count += 1
        j = i
        while not visited[j]:
            visited[j] = True
            j = perm[j]
    return count


def edge_index(n, a, b):
    if a > b:
        a, b = b, a
    assert 0 <= a < b < n
    return a * (2 * n - a - 1) // 2 + (b - a - 1)


def predicted(n, bits):
    e = 0
    d0 = dn = adjacent = 0
    for a in range(n):
        for b in range(a + 1, n):
            if bits >> edge_index(n, a, b) & 1:
                e += 1
                d0 += (a == 0)
                dn += (b == n-1)
                adjacent += (b == a + 1)
    return Fraction(Fraction(2 * e, n) + adjacent - d0 - dn, n * (n - 1))


def enumerate_pieces(n):
    data = []
    for perm in permutations(range(n)):
        mask = 0
        for j in range(n - 1):
            mask |= 1 << edge_index(n, perm[j], perm[j+1])
        data.append((mask, cycle_count(perm)))
    return data


def exact_cov(data, bits):
    N = len(data)
    sb = sc = sbc = 0
    for mask, c in data:
        b = (mask & bits).bit_count()
        sb += b
        sc += c
        sbc += b * c
    return Fraction(sbc, N) - Fraction(sb * sc, N * N)


def run():
    rng = Random(137)
    graph_cases = 0
    for n in range(2, 8):
        data = enumerate_pieces(n)
        total = n * (n - 1) // 2
        if n <= 5:
            masks = range(1 << total)
        else:
            masks = [0, (1 << total) - 1] + [rng.getrandbits(total) for _ in range(200 if n == 6 else 50)]
        for bits in masks:
            actual = exact_cov(data, bits)
            expected = predicted(n, bits)
            assert actual == expected, (n, bits, actual, expected)
            graph_cases += 1

    # Independently test the conditional cycle completion identity.
    conditional_checks = 0
    for n in range(2, 7):
        perms = list(permutations(range(n)))
        hn2 = sum((Fraction(1,k) for k in range(1, n-1)), Fraction())
        for i in range(n-1):
            j=i+1
            for a in range(n):
                for b in range(n):
                    if a==b:
                        continue
                    matched = [p for p in perms if p[i] == a and p[j] == b]
                    observed = Fraction(sum(cycle_count(p) for p in matched), len(matched))
                    expected = hn2 + (a == i) + (b == j) + (a == j and b == i)
                    assert observed == expected, (n,i,a,b,observed,expected)
                    conditional_checks += 1

    examples = 0
    for n in range(3, 24):
        path = sum(1 << edge_index(n,i,i+1) for i in range(n-1))
        first_star = sum(1 << edge_index(n,0,j) for j in range(1,n))
        interior_star = sum(1 << edge_index(n,1,j) for j in range(n) if j!=1)
        assert predicted(n,path) == Fraction((n-2)*(n+1), n*n*(n-1))
        assert predicted(n,first_star) == -Fraction(n-2, n*n)
        assert predicted(n,interior_star) == Fraction(2, n*n)
        examples += 3

    print(f'VERIFY_OK graph_cases={graph_cases} conditional_cases={conditional_checks} family_cases={examples}')


if __name__ == '__main__':
    run()
