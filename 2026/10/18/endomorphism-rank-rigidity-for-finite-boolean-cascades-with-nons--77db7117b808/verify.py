#!/usr/bin/env python3
"""Independent finite tests for bounded morphisms of layered antichain posets.
Usage: python3 verify.py. No third-party dependencies.
"""
from itertools import product, permutations
from collections import Counter
from math import comb, factorial, prod


def setup(sizes):
    levels = tuple(i for i, m in enumerate(sizes) for _ in range(m))
    blocks = tuple(tuple(j for j, ell in enumerate(levels) if ell == i)
                   for i in range(len(sizes)))
    up = tuple(frozenset(j for j in range(len(levels))
                         if j == i or levels[j] > levels[i])
               for i in range(len(levels)))
    return levels, blocks, up


def is_bounded(f, up):
    return all({f[j] for j in upper} == set(up[f[i]])
               for i, upper in enumerate(up))


def normal_maps(sizes):
    levels, blocks, _ = setup(sizes)
    n = len(levels)
    # Type I: arbitrary map on bottom; permutations on all higher levels.
    for args in product(*([tuple(product(blocks[0], repeat=sizes[0]))]
                          + [tuple(permutations(block)) for block in blocks[1:]])):
        f = [None] * n
        for block, outputs in zip(blocks, args):
            for x, y in zip(block, outputs):
                f[x] = y
        yield tuple(f)
    # Type j: collapse the first j levels, permute all higher levels.
    for j in range(1, len(sizes)):
        tail_perms = [tuple(permutations(b)) for b in blocks[j+1:]]
        for c in blocks[j]:
            for perm_tuple in product(*tail_perms):
                f = [c if levels[x] <= j else None for x in range(n)]
                for block, outputs in zip(blocks[j+1:], perm_tuple):
                    for x, y in zip(block, outputs):
                        f[x] = y
                yield tuple(f)


def stirling(n, k):
    if n == k == 0: return 1
    if k == 0 or k > n: return 0
    return stirling(n-1, k-1) + k*stirling(n-1, k)


def hist_expected(sizes):
    result = Counter()
    n0 = sizes[0]
    upper = prod(factorial(m) for m in sizes[1:])
    for r in range(1, n0 + 1):
        rank = 1 + (2**r - 1) + sum(2**m - 1 for m in sizes[1:])
        result[rank] += comb(n0, r)*factorial(r)*stirling(n0, r)*upper
    for j in range(1, len(sizes)):
        rank = 2 + sum(2**m - 1 for m in sizes[j+1:])
        result[rank] += sizes[j]*prod(factorial(m) for m in sizes[j+1:])
    return result


def idem_expected(sizes):
    n0 = sizes[0]
    return sum(comb(n0, r)*r**(n0-r) for r in range(1, n0+1)) + sum(sizes[1:])


def upsets(up):
    n = len(up)
    return tuple(frozenset(i for i in range(n) if bit >> i & 1)
                 for bit in range(1 << n)
                 if all(up[i].issubset({j for j in range(n) if bit >> j & 1})
                        for i in range(n) if bit >> i & 1))


def check(sizes, full_algebra=False):
    levels, blocks, up = setup(sizes)
    n = len(levels)
    actual = {tuple(f) for f in product(range(n), repeat=n) if is_bounded(f, up)}
    predicted = set(normal_maps(sizes))
    assert actual == predicted, (sizes, len(actual), len(predicted), list(actual-predicted)[:3])
    all_u = upsets(up)
    hist = Counter()
    idem = 0
    for f in actual:
        # Full endomorphism-image cardinality from a direct computation on all upsets.
        rank = len({frozenset(i for i, y in enumerate(f) if y in U) for U in all_u})
        hist[rank] += 1
        idem += all(f[f[i]] == f[i] for i in range(n))
        if full_algebra:
            for U in all_u:
                pre_U = frozenset(i for i, y in enumerate(f) if y in U)
                for V in all_u:
                    implication = frozenset(i for i in range(n)
                                             if up[i].intersection(U).issubset(V))
                    lhs = frozenset(i for i, y in enumerate(f) if y in implication)
                    pre_V = frozenset(i for i, y in enumerate(f) if y in V)
                    rhs = frozenset(i for i in range(n)
                                    if up[i].intersection(pre_U).issubset(pre_V))
                    assert lhs == rhs, (sizes, f, U, V)
    assert hist == hist_expected(sizes), (sizes, hist, hist_expected(sizes))
    assert idem == idem_expected(sizes), (sizes, idem, idem_expected(sizes))
    print('CASE', sizes, 'bounded_maps', len(actual), 'idempotents', idem,
          'Heyting_image_ranks', sorted(hist.items()))
    return n**n


def main():
    cases = [(2,), (3,), (2, 2), (2, 3), (3, 2),
             (2, 2, 2), (2, 3, 2), (2, 2, 3), (3, 2, 2)]
    checks = 0
    for sizes in cases:
        checks += check(sizes, full_algebra=sum(sizes) <= 6)
    print('VERIFY_OK cases=', len(cases), 'brute_force_candidate_maps=', checks)


if __name__ == '__main__':
    main()
