#!/usr/bin/env python3
"""Exact self-inverse partial-automorphism enumeration for alternating finite fences.

The formula engine uses run types and integer polynomial products.  The
independent engine enumerates all candidate involutions of every domain.
"""
from collections import Counter
from itertools import permutations
from math import factorial


def run_types(selected, n):
    selected = set(selected)
    counter = Counter()
    i = 1
    while i <= n:
        if i not in selected:
            i += 1
            continue
        j = i
        while j + 1 in selected:
            j += 1
        length = j - i + 1
        key = (length, i % 2 if length >= 3 and length % 2 else 0)
        counter[key] += 1
        i = j + 1
    return counter


def pmul(a, b):
    out = Counter()
    for (f, t), x in a.items():
        for (g, s), y in b.items():
            out[(f + g, t + s)] += x * y
    return out


def ppow(a, exponent):
    out = {(0, 0): 1}
    for _ in range(exponent):
        out = pmul(out, a)
    return out


def formula(n):
    out = Counter()
    for mask in range(1 << n):
        selected = [i + 1 for i in range(n) if (mask >> i) & 1]
        summand = {(0, 0): 1}
        for (length, parity), multiplicity in run_types(selected, n).items():
            group_size = 2 if length >= 3 and length % 2 else 1
            local = {(length, 0): 1}
            if group_size == 2:
                local[(1, (length - 1) // 2)] = 1
            part = Counter()
            for pairs in range(multiplicity // 2 + 1):
                ways = (factorial(multiplicity) //
                        (2 ** pairs * factorial(pairs) *
                         factorial(multiplicity - 2 * pairs)))
                ways *= group_size ** pairs
                for (fixed, trans), count in ppow(local, multiplicity - 2 * pairs).items():
                    part[(fixed, trans + length * pairs)] += ways * count
            summand = pmul(summand, part)
        out.update(summand)
    return out


def independent_direct_count(n):
    out = Counter()
    for mask in range(1 << n):
        selected = [i + 1 for i in range(n) if (mask >> i) & 1]
        less_pairs = {(x, y) for x in selected for y in selected
                      if x % 2 == 1 and abs(x - y) == 1}
        for images in permutations(selected):
            image = dict(zip(selected, images))
            if any(image[image[x]] != x for x in selected):
                continue
            if any((image[x], image[y]) not in less_pairs
                   for x, y in less_pairs):
                continue
            fixed = sum(image[x] == x for x in selected)
            out[(fixed, (len(selected) - fixed) // 2)] += 1
    return out


def rank_vector(poly, n):
    return [sum(coefficient for (fixed, swaps), coefficient in poly.items()
                if fixed + 2 * swaps == rank)
            for rank in range(n + 1)]


def near_top(n):
    if n % 2 == 0:
        return 2 * n - 2
    if n % 4 == 1:
        return (5 * n - 9) // 2
    return (5 * n - 7) // 2


def main():
    totals = []
    for n in range(1, 13):
        p = formula(n)
        if n <= 8:
            brute = independent_direct_count(n)
            assert p == brute, (n, "cycle-type mismatch", p - brute, brute - p)
        row = rank_vector(p, n)
        assert row[0] == 1
        if n >= 2:
            assert row[2] == (n - 1) ** 2
            assert row[n - 1] == near_top(n)
        assert row[n] == (2 if n >= 3 and n % 2 else 1)
        totals.append(sum(row))
        if n in (7, 8, 9):
            print("n=", n, "rank counts", row)
    assert totals == [2, 4, 10, 21, 48, 106, 246, 561, 1312, 3060, 7266, 17265]
    print("VERIFY_OK")


if __name__ == '__main__':
    main()
