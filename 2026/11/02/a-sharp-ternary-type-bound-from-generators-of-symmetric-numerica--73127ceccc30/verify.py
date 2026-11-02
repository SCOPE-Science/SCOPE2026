#!/usr/bin/env python3
"""Exact finite checks for three-quotients of symmetric numerical semigroups.

This bounded enumeration is not the proof of the unrestricted result.
"""
from itertools import combinations, combinations_with_replacement
from math import gcd
from heapq import heappush, heappop


def apery(gens):
    m = min(gens)
    dist = [None] * m
    dist[0] = 0
    q = [(0, 0)]
    while q:
        x, r = heappop(q)
        if x != dist[r]:
            continue
        for v in gens:
            j = (r + v) % m
            y = x + v
            if dist[j] is None or y < dist[j]:
                dist[j] = y
                heappush(q, (y, j))
    assert all(v is not None for v in dist)
    return dist


def check(gens):
    m = min(gens)
    assert m >= 4 and gcd(*gens) == 1
    ap = apery(gens)
    F = max(ap) - m
    if F < 1 or F % 2 != 1:
        return None
    genus = sum(x < ap[x % m] for x in range(1, F + 1))
    if genus * 2 != F + 1:
        return None
    limit = max(4 * F + 100, max(gens) + 20)
    inS = [False] * (limit + 1)
    inS[0] = True
    for x in range(1, limit + 1):
        inS[x] = any(x >= g and inS[x - g] for g in gens)
    assert all(inS[x] == (x >= ap[x % m]) for x in range(limit + 1))
    minimal = tuple(g for g in gens if not any(
        h != g and g >= h and inS[g - h] for h in gens))
    inH = [inS[3 * x] for x in range(2 * (F // 3 + 2) + 25)]
    gaps = [x for x in range(1, F // 3 + 1) if not inH[x]]
    assert gaps, (gens, F)
    FH = max(gaps)
    pf = sorted(f for f in gaps if all(
        inH[f + s] for s in range(1, FH + 2) if inH[s]))
    r = F % 3
    if r == 0:
        predicted = [F // 3]
    else:
        same = [g for g in minimal if g % 3 == r]
        opposite = [g for g in minimal if g % 3 == (3 - r)]
        candidates = set(same)
        candidates.update(x + y for x, y in combinations_with_replacement(opposite, 2))
        candidates = {c for c in candidates if c < F}
        minima = {c for c in candidates if not any(
            c != b and c > b and (c - b) % 3 == 0 and inS[c - b]
            for b in candidates)}
        predicted = sorted((F - c) // 3 for c in minima)
        assert len(pf) <= len(same) + len(opposite) * (len(opposite) + 1) // 2
    assert pf == predicted, (gens, F, minimal, pf, predicted)
    return len(pf)


def main():
    checked = 0
    by_residue = {0: 0, 1: 0, 2: 0}
    for m in range(4, 10):
        for extra in (1, 2, 3):
            for rest in combinations(range(m + 1, m + 15), extra):
                gens = (m,) + rest
                if gcd(*gens) != 1:
                    continue
                t = check(gens)
                if t is not None:
                    F = max(apery(gens)) - m
                    checked += 1
                    by_residue[F % 3] += 1
    sharp = 0
    for m in (4, 5, 7, 8, 10, 11, 13):
        for d in (3, 6, 9, 12):
            if gcd(m, d) != 1:
                continue
            gens = tuple(m + j * d for j in range(m - 1))
            assert check(gens) == m - 1
            sharp += 1
    print('VERIFY_OK symmetric_inputs=%d residue_classes=%s sharp_families=%d independent_apery_dp=yes' %
          (checked, ','.join('%d:%d' % z for z in sorted(by_residue.items())), sharp))


if __name__ == '__main__':
    main()
