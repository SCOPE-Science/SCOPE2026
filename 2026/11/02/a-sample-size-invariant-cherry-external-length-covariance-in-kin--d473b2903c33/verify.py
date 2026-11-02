#!/usr/bin/env python3
"""Exact independent checks of cherry/external-length coalescent identities.

Run with Python 3: python verify.py
Uses only Python's standard library. Waiting times have rate binom(k,2).
"""
from fractions import Fraction as F
from math import comb


def formula(n, k):
    if n == 3:
        return F(0)
    return -F(k * (k - 1) * (n - k) * (n - k - 1),
              3 * (n - 1) * (n - 2) * (n - 3))


def recurrence(n):
    """Compute mixed moments using state mass and cherry-weighted state mass."""
    state = {n: (F(1), F(0))}
    states = {n: state}
    for k in range(n, 2, -1):
        nxt = {}
        for s, (p, m) in state.items():
            t = k - s
            for loss, inc, ways in ((2, 1, comb(s, 2)),
                                    (1, 0, s * t),
                                    (0, 0, comb(t, 2))):
                if ways == 0:
                    continue
                weight = F(ways, comb(k, 2))
                q, r = nxt.get(s - loss, (F(0), F(0)))
                nxt[s - loss] = (q + weight * p,
                                 r + weight * (m + inc * p))
        state = nxt
        states[k - 1] = state
    ec = sum(m for p, m in state.values())
    assert ec == F(n, 3)
    covariance = F(0)
    for k in range(n, 1, -1):
        state = states[k]
        es = sum(s * p for s, (p, m) in state.items())
        # For reachable states with n >= 3, S_2 <= 1.
        ecs = sum(s * (m + p * F(s * (s - 1), 3 * (k - 1)))
                  for s, (p, m) in state.items())
        mixed = ecs - ec * es
        assert mixed == formula(n, k), (n, k, mixed, formula(n, k))
        covariance += F(2, k * (k - 1)) * mixed
    assert covariance == (F(0) if n == 3 else F(-2, 9))
    return covariance


def enumerate_histories(n):
    """Exhaustively enumerate equiprobable *ranked* merger histories."""
    raw = {k: [0, 0, 0] for k in range(2, n + 1)}
    nc, total = 0, 0

    def go(clusters, cherries, visible):
        nonlocal nc, total
        k = len(clusters)
        if k == 1:
            total += 1
            nc += cherries
            for stage, s in visible.items():
                raw[stage][0] += s
                raw[stage][1] += cherries * s
                raw[stage][2] += 1
            return
        singleton_count = sum(len(c) == 1 for c in clusters)
        visible[k] = singleton_count
        for i in range(k):
            for j in range(i + 1, k):
                new_cherries = cherries + (len(clusters[i]) == len(clusters[j]) == 1)
                new_clusters = [clusters[t] for t in range(k) if t not in (i, j)]
                new_clusters.append(clusters[i] | clusters[j])
                go(new_clusters, new_cherries, visible)
        del visible[k]

    go([frozenset((i,)) for i in range(n)], 0, {})
    ways = 1
    for k in range(2, n + 1):
        ways *= comb(k, 2)
    assert total == ways, (n, total, ways)
    assert F(nc, total) == F(n, 3)
    got = F(0)
    for k, (ss, cs, count) in raw.items():
        assert count == total
        cov = F(cs, total) - F(nc * ss, total * total)
        assert cov == formula(n, k), (n, k, cov)
        got += F(2, k * (k - 1)) * cov
    assert got == (F(0) if n == 3 else F(-2, 9))
    return total


def main():
    checks = 0
    for n in range(3, 101):
        recurrence(n)
        checks += n - 1
    histories = 0
    for n in range(3, 8):
        count = enumerate_histories(n)
        histories += count
        print('n=%d histories=%d validated' % (n, count))
    # Deterministic all-n rational sum of the claimed covariance profile.
    for n in range(4, 101):
        x = sum(F(2, k * (k - 1)) * formula(n, k)
                for k in range(2, n + 1))
        assert x == F(-2, 9)
        checks += 1
    print('PASS: %d recurrence/sum checks; %d enumerated ranked histories'
          % (checks, histories))


if __name__ == '__main__':
    main()
