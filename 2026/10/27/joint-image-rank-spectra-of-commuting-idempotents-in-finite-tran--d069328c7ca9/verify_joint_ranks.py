#!/usr/bin/env python3
"""Exact checks of the joint rank polynomial for commuting retractions.

Pure Python 3. No external mathematical software or downloaded data required.
The first method constructs each map and composes maps pointwise; the second
builds labeled root-block structures using binomial convolution.
"""
from collections import Counter
from itertools import product
from math import comb, factorial


def composition(f, g):
    return tuple(f[g[i]] for i in range(len(f)))


def brute_joint_ranks(n):
    if n == 0:
        return Counter({(0, 0, 0): 1}), 1
    maps = product(range(n), repeat=n)
    idem = [f for f in maps if composition(f, f) == f]
    spectrum = Counter()
    for e in idem:
        for f in idem:
            p = composition(e, f)
            if p == composition(f, e):
                spectrum[(len(set(e)), len(set(f)), len(set(p)))] += 1
    return spectrum, len(idem)


def block_spectrum(m):
    """Counts on fixed labeled m-set for one designated common-image point."""
    spectrum = Counter()
    for a in range(m):
        for c in range(m - a):
            d = m - 1 - a - c
            allocations = m * factorial(m-1) // (factorial(a) * factorial(c) * factorial(d))
            choices = (a+1)**d * (c+1)**d
            spectrum[(a+1, c+1, 1)] += allocations * choices
    return spectrum


def species_joint_ranks(upto):
    """Connected-root-block species; root block contains the smallest label."""
    spectra = [Counter() for _ in range(upto + 1)]
    spectra[0][(0, 0, 0)] = 1
    blocks = {m: block_spectrum(m) for m in range(1, upto + 1)}
    for n in range(1, upto + 1):
        for m in range(1, n + 1):
            placement = comb(n-1, m-1)
            for (a, b, c), ways in blocks[m].items():
                for (x, y, z), rest in spectra[n-m].items():
                    spectra[n][(a+x, b+y, c+z)] += placement * ways * rest
    return spectra


def feasible(n, r, s, k):
    return (r, s, k) == (0, 0, 0) if n == 0 else (
        1 <= k <= min(r, s) and r + s - k <= n
    )


def main():
    spectra = species_joint_ranks(8)
    assert spectra[0] == Counter({(0, 0, 0): 1})
    for n in range(0, 7):
        direct, num_idempotents = brute_joint_ranks(n)
        assert direct == spectra[n], (n, direct - spectra[n], spectra[n] - direct)
        print(f'n={n} idempotents={num_idempotents} commuting_pairs={sum(direct.values())} profiles={len(direct)}')
    for n in range(1, 9):
        for r in range(1, n + 1):
            for s in range(1, n + 1):
                for k in range(1, n + 1):
                    assert (spectra[n].get((r, s, k), 0) > 0) == feasible(n, r, s, k)
        assert all(spectra[n][(r, s, k)] == spectra[n][(s, r, k)]
                   for (r, s, k) in spectra[n])
    print('total_counts_n0_to_n8=' + repr([sum(s.values()) for s in spectra]))
    print('ALL_COMMUTING_IDEMPOTENT_JOINT_RANK_CHECKS_PASSED')


if __name__ == '__main__':
    main()
