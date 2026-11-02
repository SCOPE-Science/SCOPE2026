#!/usr/bin/env python3
"""Finite checks of the labelled inquisitive-epistemic frame census.

Uses independent enumeration of downsets and full frame maps for n <= 3.
All statements for unbounded n are proved mathematically, not by this checker.
"""
from itertools import product
from math import comb


def downsets(n):
    """All downsets of the n-dimensional Boolean lattice, as state-bitmasks."""
    states = 1 << n
    beneath = []
    for s in range(states):
        t = s
        lower = 0
        while True:
            lower |= 1 << t
            if t == 0:
                break
            t = (t - 1) & s
        beneath.append(lower)
    result = []
    for family in range(1 << states):
        if all(not ((family >> s) & 1) or (family & beneath[s]) == beneath[s]
               for s in range(states)):
            result.append(family)
    return result


def union_states(family, n):
    u = 0
    for s in range(1 << n):
        if (family >> s) & 1:
            u |= s
    return u


def direct_frame_count(n, families):
    admissible_by_world = [tuple(f for f in families
                                 if union_states(f, n) & (1 << w))
                           for w in range(n)]
    total = 0
    for profile in product(*admissible_by_world):
        supports = [union_states(d, n) for d in profile]
        if all(profile[v] == profile[w]
               for w in range(n)
               for v in range(n) if supports[w] & (1 << v)):
            total += 1
    return total


def check():
    ds = [downsets(n) for n in range(5)]
    dedekind = [len(x) for x in ds]
    assert dedekind == [2, 3, 6, 20, 168], dedekind
    # Independent slice decomposition for n=5: each downset of B_5
    # is a pair of B_4 downsets with the 1-slice included in the 0-slice.
    m5 = sum((b & ~a) == 0 for a in ds[4] for b in ds[4])
    assert m5 == 7581, m5
    dedekind.append(m5)

    c = [0] + [sum((-1)**j * comb(n, j) * dedekind[n-j]
                  for j in range(n+1)) for n in range(1, 6)]
    assert c == [0, 1, 2, 9, 114, 6894], c
    # Directly count downsets with union equal to the full carrier.
    for n in range(1, 5):
        direct = sum(union_states(d, n) == ((1 << n) - 1) for d in ds[n])
        assert direct == c[n], (n, direct, c[n])

    f = [1]
    for n in range(1, 6):
        # Distinguished block containing label 0.
        f.append(sum(comb(n-1, k-1) * c[k] * f[n-k]
                     for k in range(1, n+1)))
    assert f == [1, 1, 3, 16, 175, 7815], f
    for n in range(1, 4):
        explicit = direct_frame_count(n, ds[n][1:])
        assert explicit == f[n], (n, explicit, f[n])
    print('ALL_CHECKS_OK')
    print('Dedekind n=0..5:', dedekind)
    print('Full-support inquisitive states n=1..5:', c[1:])
    print('Labelled epistemic frames n=1..5:', f[1:])
    print('Full frame maps checked independently through n=3')


if __name__ == '__main__':
    check()
