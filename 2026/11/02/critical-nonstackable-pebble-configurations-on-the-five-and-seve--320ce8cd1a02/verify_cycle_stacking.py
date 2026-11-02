#!/usr/bin/env python3
"""Exact finite reachability and symmetry checks for pebbling on C5 and C7.

No external libraries or previously computed output required. Run with Python 3:
    python verify_cycle_stacking.py
"""
from functools import lru_cache
from math import comb


def compositions(total, vertices):
    """Enumerate each nonnegative vertex-labelled configuration exactly once."""
    if vertices == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for rest in compositions(total - first, vertices - 1):
            yield (first,) + rest


def symmetric_orbit(word):
    n = len(word)
    return {
        tuple(word[(shift + sign * i) % n] for i in range(n))
        for shift in range(n) for sign in (-1, 1)
    }


def direct_criterion(n):
    """Independent forward reachability recursion (pebbling strictly loses size)."""
    @lru_cache(maxsize=None)
    def good(c):
        if sum(a > 0 for a in c) == 1:
            return True
        if sum(c) <= 1:
            return False
        for u in range(n):
            if c[u] < 2:
                continue
            for v in ((u - 1) % n, (u + 1) % n):
                child = list(c)
                child[u] -= 2
                child[v] += 1
                if good(tuple(child)):
                    return True
        return False
    return good


def reverse_criterion(n, highest):
    """Build all stackable configurations by reversing individual moves.

    For c of size t-1, every precursor d of size t has
    d[u]=c[u]+2, d[v]=c[v]-1 for an oriented cycle edge u->v
    with c[v]>=1. Since every move loses one pebble, this is exact.
    """
    old = set()
    hist = {}
    for t in range(1, highest + 1):
        current = {tuple(t if i == v else 0 for i in range(n))
                   for v in range(n)}
        for child in old:
            for u in range(n):
                for v in ((u - 1) % n, (u + 1) % n):
                    if child[v] == 0:
                        continue
                    p = list(child)
                    p[u] += 2
                    p[v] -= 1
                    current.add(tuple(p))
        hist[t] = current
        old = current
    return hist


def check(n, highest, targets, expected_bad):
    recursive = direct_criterion(n)
    backwards = reverse_criterion(n, highest)
    histogram = []
    for t in range(1, highest + 1):
        all_states = set(compositions(t, n))
        assert len(all_states) == comb(t + n - 1, n - 1)
        reverse_good = backwards[t]
        assert reverse_good <= all_states
        forward_good = {s for s in all_states if recursive(s)}
        assert forward_good == reverse_good, (n, t)
        histogram.append((t, len(all_states), len(all_states - reverse_good)))

    for t, representatives in targets.items():
        all_states = set(compositions(t, n))
        bad = all_states - backwards[t]
        expected = set()
        for rep in representatives:
            orb = symmetric_orbit(rep)
            assert len(orb) in (5, 14)
            assert not expected.intersection(orb)
            expected.update(orb)
        assert bad == expected, (n, t, len(bad), len(expected))
        assert len(bad) == expected_bad[t]
    print('C', n, 'profile (pebbles,total,bad):', histogram)
    return histogram


def main():
    a = check(5, 8,
              {7: [(5, 0, 1, 1, 0), (3, 3, 0, 1, 0)], 8: []},
              {7: 10, 8: 0})
    b = check(7, 17,
              {16: [(14, 0, 1, 0, 1, 0, 0)], 17: []},
              {16: 14, 17: 0})
    assert a[-2][-1] == 10 and b[-2][-1] == 14
    print('VERIFY_OK C5 7-pebble obstructions: 2 orbits (5,5); '
          'C7 16-pebble obstructions: 1 orbit (14); '
          'all 8/17-pebble configurations stackable; '
          'independent forward and reverse reachability agree')


if __name__ == '__main__':
    main()
