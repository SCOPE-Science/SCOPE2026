#!/usr/bin/env python3
"""Independent finite checks of a cycle-square Italian-domination count formula.

Run with Python 3 (standard library only). This script verifies only finite
instances. The general formula requires the structural proof in RESULT.md.
"""
from itertools import combinations, product
from math import ceil


def predicted(n):
    if n % 3 == 0:
        return 3
    if n % 3 == 2:
        return n + (10 if n == 5 else 0)
    return n * (n + 5) // 6 + (10 if n == 10 else 0)


def brute(n):
    w = ceil(n / 3)
    nb = [((i - 2) % n, (i - 1) % n, (i + 1) % n, (i + 2) % n)
          for i in range(n)]
    count = 0
    by_twos = {}
    for t in range(w // 2 + 1):
        for twos in combinations(range(n), t):
            two = set(twos)
            rest = [i for i in range(n) if i not in two]
            for ones in combinations(rest, w - 2 * t):
                labels = [0] * n
                for i in twos:
                    labels[i] = 2
                for i in ones:
                    labels[i] = 1
                if all(labels[i] > 0 or sum(labels[j] for j in nb[i]) >= 2
                       for i in range(n)):
                    count += 1
                    by_twos[t] = by_twos.get(t, 0) + 1
    return count, by_twos


def transfer(n):
    """Minimum and multiplicity from a cyclic 4-memory transfer matrix."""
    sts = list(product(range(3), repeat=4))
    outgoing = {}
    for a, b, c, d in sts:
        out = []
        for e in (0, 1, 2):
            if c != 0 or a + b + d + e >= 2:
                out.append(((b, c, d, e), e))
        outgoing[(a, b, c, d)] = out
    best, multiplicity = float('inf'), 0
    for initial in sts:
        cur = {initial: (0, 1)}
        for _ in range(n):
            following = {}
            for s, (cost, ways) in cur.items():
                for nxt, added in outgoing[s]:
                    nc = cost + added
                    if nxt not in following or nc < following[nxt][0]:
                        following[nxt] = (nc, ways)
                    elif nc == following[nxt][0]:
                        old, times = following[nxt]
                        following[nxt] = (old, times + ways)
            cur = following
        if initial in cur:
            cost, times = cur[initial]
            if cost < best:
                best, multiplicity = cost, times
            elif cost == best:
                multiplicity += times
    return best, multiplicity


def main():
    brute_cases = 0
    for n in range(5, 19):
        count, by_twos = brute(n)
        assert count == predicted(n), (n, count, predicted(n))
        assert sum(v for k, v in by_twos.items() if k) == (
            5 if n == 5 else 5 if n == 10 else 0), (n, by_twos)
        brute_cases += 1
    print('INDEPENDENT_DIRECT_ENUMERATION_OK', brute_cases,
          'orders n=5..18 (all assignments of minimum weight)')
    dp_cases = 0
    for n in range(5, 61):
        weight, count = transfer(n)
        assert weight == ceil(n / 3), (n, weight)
        assert count == predicted(n), (n, count, predicted(n))
        dp_cases += 1
    print('INDEPENDENT_CYCLIC_TRANSFER_OK', dp_cases,
          'orders n=5..60; optimal weight and count')
    print('SPECIAL_TWO_LABEL_COUNTS_OK n=5:5 n=10:5 others:0 through n=18')
    print('FINITE_VERIFICATION_OK; proof of the infinite theorem is in RESULT.md')


if __name__ == '__main__':
    main()
