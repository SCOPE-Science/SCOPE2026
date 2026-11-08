#!/usr/bin/env python3
"""Exact small-cardinality checks for nested equivalence-modal obstruction counts."""
from math import comb, factorial
from fractions import Fraction
from itertools import combinations


def partitions(n):
    def rec(i, blocks):
        if i == n:
            yield tuple(tuple(b) for b in blocks)
            return
        for j in range(len(blocks)):
            blocks[j].append(i)
            yield from rec(i + 1, blocks)
            blocks[j].pop()
        blocks.append([i])
        yield from rec(i + 1, blocks)
        blocks.pop()
    yield from rec(0, [])


def bell_numbers(n):
    b = [1]
    for j in range(1, n + 1):
        b.append(sum(comb(j - 1, k) * b[k] for k in range(j)))
    return b


def stirling(n):
    s = [[0] * (n + 1) for _ in range(n + 1)]
    s[0][0] = 1
    for m in range(1, n + 1):
        for k in range(1, m + 1):
            s[m][k] = k * s[m-1][k] + s[m-1][k-1]
    return s


def falling(v, k):
    t = 1
    for i in range(k):
        t *= v - i
    return t


def check():
    checks = 0
    for n in range(1, 6):
        parts = list(partitions(n))
        bells = bell_numbers(n)
        assert len(parts) == bells[n]
        stir = stirling(n)
        # Exact conditional factorial moment identity, for every deterministic set F.
        for m in range(n + 1):
            F = set(range(m))
            direct = [Fraction(sum(falling(sum(set(C) <= F for C in P), k) for P in parts), bells[n]) for k in range(m + 1)]
            formula = [sum((Fraction(comb(m, s) * factorial(k) * stir[s][k] * bells[n-s], bells[n])
                            for s in range(k, m + 1)), Fraction(0)) for k in range(m + 1)]
            assert direct == formula, (n,m,direct,formula)
            checks += m + 1
        # Full two-agent modal semantics, averaging over all partitions and valuations.
        if n <= 4:
            for Q in parts:
                Qsets = [set(C) for C in Q]
                for mask in range(1 << n):
                    truths = {v for v in range(n) if mask & (1 << v)}
                    good = set().union(*(C for C in Qsets if C & truths)) if truths else set()
                    F = set(range(n)) - good
                    for P in parts:
                        z = sum(set(C) <= F for C in P)
                        world_successes = set().union(*(set(C) for C in P if set(C) & good)) if good else set()
                        assert (z == 0) == (len(world_successes) == n)
                        checks += 1
    print('NESTED_S5_EXACT_CHECKS_OK', checks)


if __name__ == '__main__':
    check()
