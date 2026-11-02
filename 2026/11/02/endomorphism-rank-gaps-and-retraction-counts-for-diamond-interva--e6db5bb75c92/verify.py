#!/usr/bin/env python3
"""Exhaustive small-case checks for endomorphisms of diamond interval semirings."""
from itertools import product
from collections import Counter
from math import comb, factorial, perm


def expected(n):
    counts = Counter()
    for m in range(n + 2):
        c = (comb(n, m) * 2**m if m <= n else 0)
        if 0 <= m-1 <= n:
            c += comb(n, m-1) * 2**(m-1)
        counts[m+1] += c * perm(2*n, m)
    counts[2*n+2] += factorial(n)
    return counts


def tabulate(n):
    size = 2*n + 2
    # 0 is absorbing; 1 is the long interval; 2+i and 2+n+i are short intervals.
    mul = [[0]*size for _ in range(size)]
    for i in range(n):
        mul[2+i][2+n+i] = 1
    add = [[a if a == b else 0 for b in range(size)] for a in range(size)]
    return size, add, mul


def exhaustive(n):
    size, add, mul = tabulate(n)
    counts = Counter()
    idempotents = 0
    automorphisms = 0
    for tail in product(range(size), repeat=size-1):
        f = (0,) + tail
        # Check all additive and multiplicative pairs using the actual tables.
        ok = True
        for a in range(size):
            for b in range(size):
                if f[add[a][b]] != add[f[a]][f[b]] or f[mul[a][b]] != mul[f[a]][f[b]]:
                    ok = False
                    break
            if not ok:
                break
        if not ok:
            continue
        counts[len(set(f))] += 1
        if all(f[f[a]] == f[a] for a in range(size)):
            idempotents += 1
        if len(set(f)) == size:
            automorphisms += 1
    assert counts == expected(n), (n, counts, expected(n))
    assert idempotents == 3**n + 1, (n, idempotents)
    assert automorphisms == factorial(n), (n, automorphisms)
    print(f"n={n} ranks={dict(sorted(counts.items()))} endomorphisms={sum(counts.values())} idempotents={idempotents} automorphisms={automorphisms}")


def independent_assignment_check(n):
    # A separate image-condition enumeration for n=3, above brute n<=2.
    size, add, mul = tabulate(n)
    counts = Counter()
    for tail in product(range(size), repeat=2*n):
        f = (0, 0) + tail
        # Addition constraints checked on each unordered pair, independently.
        if any(f[i] and f[i] == f[j] for i in range(2, size) for j in range(i+1, size)):
            continue
        if any(mul[f[i]][f[j]] != 0 for i in range(2,size) for j in range(2,size)):
            continue
        counts[len(set(f))] += 1
    for m,v in expected(n).items():
        if m != 2*n+2:
            assert counts[m] == v, (n,m,counts[m],v)
    assert sum(counts.values()) == sum(expected(n).values())-factorial(n)
    print(f"n={n} collapsed-long-interval rank profile={dict(sorted(counts.items()))}")


if __name__ == '__main__':
    for n in (1, 2):
        exhaustive(n)
    independent_assignment_check(3)
    print('VERIFY_OK')
