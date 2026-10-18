#!/usr/bin/env python3
"""Direct finite checks for diagonal subsemigroups of meet-chains."""
from itertools import product
from math import factorial


def compatible(n, rel):
    return all((min(a, c), min(b, d)) in rel
               for a, b in rel for c, d in rel)


def transitive(rel):
    return all((a, c) in rel for a, b in rel for bb, c in rel if b == bb)


def enumerate_reflexive(n):
    off = [(i, j) for i in range(n) for j in range(n) if i != j]
    diagonal = {(i, i) for i in range(n)}
    for mask in range(1 << len(off)):
        yield diagonal | {pair for bit, pair in enumerate(off) if mask & (1 << bit)}


def from_codes(a, b):
    n = len(a) + 1
    rel = {(i, i) for i in range(n)}
    for i in range(n - 1):
        rel.update((i, i + d) for d in range(1, a[i] + 1))
        rel.update((i + d, i) for d in range(1, b[i] + 1))
    return rel


def code(rel, n):
    return (tuple(max([0] + [j - i for j in range(i + 1, n) if (i, j) in rel])
                  for i in range(n - 1)),
            tuple(max([0] + [j - i for j in range(i + 1, n) if (j, i) in rel])
                  for i in range(n - 1)))


def poly_mul(a, b):
    v = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            v[i + j] += x * y
    return v


def rank_polynomial(n):
    p = [1]
    for r in range(2, n + 1):
        p = poly_mul(p, [1] * r)
        p = poly_mul(p, [1] * r)
    return p


def test_bruteforce(n):
    ds = [r for r in enumerate_reflexive(n) if compatible(n, r)]
    codes = set(code(r, n) for r in ds)
    assert len(ds) == len(codes) == factorial(n) ** 2
    assert all(from_codes(*code(r, n)) == r for r in ds)
    congruences = [r for r in ds if all((b, a) in r for a, b in r) and transitive(r)]
    assert len(congruences) == 2 ** (n - 1)
    ranks = [0] * (n * (n - 1) + 1)
    for r in ds:
        ranks[len(r) - n] += 1
    assert ranks == rank_polynomial(n)
    print('BRUTE_N', n, 'DIAG', len(ds), 'CONG', len(congruences), 'RANK_POLY_OK')


def test_parameter_family(n):
    opts = [range(n-i) for i in range(n-1)]
    codes = list(product(*opts))
    seen = set()
    ranks = [0] * (n * (n-1)+1)
    for a in codes:
        for b in codes:
            r = from_codes(a, b)
            assert compatible(n, r)
            assert code(r, n) == (a, b)
            seen.add(frozenset(r))
            ranks[len(r)-n] += 1
    assert len(seen) == factorial(n)**2
    assert ranks == rank_polynomial(n)
    print('PARAMETER_N', n, 'DIAG', len(seen), 'RANK_POLY_OK')


def main():
    for n in (1, 2, 3, 4):
        test_bruteforce(n)
    for n in (2, 3, 4, 5):
        test_parameter_family(n)
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
