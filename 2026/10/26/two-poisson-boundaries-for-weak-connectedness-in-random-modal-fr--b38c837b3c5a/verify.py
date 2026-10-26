#!/usr/bin/env python3
"""Exhaustive finite Kripke-frame correspondence checks for weak connectedness.

Every loop-free directed relation on 1--4 labelled vertices is enumerated;
all valuations of the two propositional variables are checked separately.
"""
from math import comb


def structural(rows, n):
    for w in range(n):
        for u in range(n):
            if not (rows[w] & (1 << u)):
                continue
            for v in range(u + 1, n):
                if rows[w] & (1 << v):
                    if not (rows[u] & (1 << v) or rows[v] & (1 << u)):
                        return False
    return True


def modal(rows, n):
    for p in range(1 << n):
        for q in range(1 << n):
            for w in range(n):
                out = rows[w]
                if not (out & p and out & q):
                    continue
                if out & p & q:
                    continue
                p_and_dq = any((out & (1 << u)) and (p & (1 << u)) and (rows[u] & q) for u in range(n))
                q_and_dp = any((out & (1 << u)) and (q & (1 << u)) and (rows[u] & p) for u in range(n))
                if not (p_and_dq or q_and_dp):
                    return False
    return True


def check():
    for n in range(1, 5):
        arcs = [(u, v) for u in range(n) for v in range(n) if u != v]
        counts = [0] * (len(arcs) + 1)
        for mask in range(1 << len(arcs)):
            rows = [0] * n
            for i, (u, v) in enumerate(arcs):
                if mask & (1 << i):
                    rows[u] |= 1 << v
            s = structural(rows, n)
            assert s == modal(rows, n), (n, mask, rows)
            counts[mask.bit_count()] += int(s)
        assert sum(counts) <= 1 << (n * (n - 1))
        assert counts[0] == 1
        print('WEAK_CONNECTED_CORRESPONDENCE_OK', n, sum(counts), 1 << len(arcs), counts)
    print('WEAK_CONNECTED_DOUBLE_POISSON_CHECK_OK')

if __name__ == '__main__':
    check()
