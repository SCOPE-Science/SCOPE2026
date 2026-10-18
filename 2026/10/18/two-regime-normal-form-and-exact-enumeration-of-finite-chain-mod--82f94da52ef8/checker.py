#!/usr/bin/env python3
"""Exhaustive checker for the finite involutive-chain modal-operator theorem.
Run as: python3 checker.py.  Uses only the Python standard library."""
from itertools import combinations_with_replacement, product
from math import comb


def axioms(f):
    """Evaluate meet preservation, Pos, and Con exactly as quantified."""
    n = len(f)
    neg = lambda a: n - 1 - a
    for x in range(n):
        for y in range(n):
            if f[min(x, y)] != min(f[x], f[y]):
                return False
        for z in range(n):
            if neg(f[max(z, neg(z))]) > f[max(z, neg(z))]:
                return False
            v = f[max(x, min(z, neg(z)))]
            if v > max(f[x], neg(v)):
                return False
    return True


def classification(f):
    """The independent monotone/threshold/plateau characterization."""
    n = len(f)
    c = (n - 1) // 2
    p = n // 2
    if any(f[i] > f[i + 1] for i in range(n - 1)):
        return False
    if f[p] < p:
        return False
    return f[c] <= c or all(f[i] == f[c] for i in range(c + 1))


def total_formula(n):
    h = n // 2
    if n % 2:
        return comb(2*h, h)**2 + comb(2*h, h+1)
    return comb(2*h-1, h)**2 + comb(2*h, h+1)


def top_formula(n):
    if n == 1:
        return 1
    h = n // 2
    if n % 2:
        return comb(2*h, h)*comb(2*h-1, h-1) + comb(2*h-1, h)
    return comb(2*h-1, h)*comb(2*h-2, h-1) + comb(2*h-1, h)


def check(n, all_maps):
    maps = product(range(n), repeat=n) if all_maps else combinations_with_replacement(range(n), n)
    tot = top = examined = 0
    for f in maps:
        examined += 1
        actual = axioms(f)
        proposed = classification(f)
        assert actual == proposed, (n, f, actual, proposed)
        if actual:
            tot += 1
            if f[-1] == n - 1:
                top += 1
    assert tot == total_formula(n), (n, tot, total_formula(n))
    assert top == top_formula(n), (n, top, top_formula(n))
    print(f'n={n:2d} candidates={examined:7d} accepted={tot:6d} top-preserving={top:6d} mode={"all maps" if all_maps else "isotone maps"}')


if __name__ == '__main__':
    for n in range(1, 7):
        check(n, all_maps=True)
    for n in range(7, 11):
        check(n, all_maps=False)
    print('EXHAUSTIVE_CHECK_OK')
