#!/usr/bin/env python3
"""Exact integer certificate for finite-support period-six counts of RESOCA 115.

Run: python3 rule115_period_six_verifier.py
No third-party modules required. The finite transfer identities imply
recurrences for ALL lengths by the Cayley--Hamilton theorem.
"""
from collections import defaultdict
from itertools import product


def local(left, center, right):
    return (115 >> ((left << 2) | (center << 1) | right)) & 1


def transfer(p):
    columns = range(1 << p)
    bit = lambda word, time: (word >> (time % p)) & 1
    background = sum(1 << t for t in range(2, p, 3))
    origin = (background, background)
    outgoing = defaultdict(list)
    incoming = defaultdict(list)
    for a in columns:
        for b in columns:
            for c in columns:
                if all(bit(b, t + 1) ^ bit(b, t - 1) ==
                       local(bit(a, t), bit(b, t), bit(c, t))
                       for t in range(p)):
                    source, target = (a, b), (b, c)
                    outgoing[source].append(target)
                    incoming[target].append(source)

    def reach(graph):
        seen = {origin}
        pending = [origin]
        for state in pending:
            for neighbor in graph[state]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    pending.append(neighbor)
        return seen

    states = sorted(reach(outgoing) & reach(incoming))
    assert origin in states
    index = {state: i for i, state in enumerate(states)}
    adjacency = [[] for _ in states]
    for state in states:
        adjacency[index[state]] = [index[target] for target in outgoing[state]
                                   if target in index]

    # An initial configuration is zero outside positions 0,...,n-1.
    # The unique left halo column, at -1, has initial two digits 00.
    start = [0] * len(states)
    for target in outgoing[origin]:
        if target in index and target[1] & 3 == 0:
            start[index[target]] += 1

    # Two right-boundary columns are the background column.
    finish = [0] * len(states)
    for state in states:
        for target in outgoing[state]:
            if target[1] != background:
                continue
            for final in outgoing[target]:
                if final == origin:
                    finish[index[state]] += 1
    return states, adjacency, start, finish


def step(row, adjacency):
    nxt = [0] * len(row)
    for i, amount in enumerate(row):
        if amount:
            for j in adjacency[i]:
                nxt[j] += amount
    return nxt


def pair(row, column):
    return sum(x * y for x, y in zip(row, column))


def spectral_sequence(p, terms):
    states, adjacency, row, finish = transfer(p)
    values = []
    for _ in range(terms):
        values.append(pair(row, finish))
        row = step(row, adjacency)
    return states, values


def certified_recurrence(p, coeff):
    """Check first dim(A) scalar differences; Cayley-Hamilton gives all."""
    states, adjacency, row, finish = transfer(p)
    degree = len(coeff) - 1
    values = []
    for _ in range(len(states) + degree):
        values.append(pair(row, finish))
        row = step(row, adjacency)
    for n in range(len(states)):
        difference = sum(coeff[j] * values[n + j]
                         for j in range(degree + 1))
        assert difference == 0, (p, n, difference)
    return states, values


def observed_returns(initial):
    """Independent direct space-time evolution relative to 001 background."""
    memory = {i for i, letter in enumerate(initial) if letter & 1}
    current = {i for i, letter in enumerate(initial) if letter & 2}
    initial_memory = memory.copy()
    initial_current = current.copy()
    found = set()
    base = (0, 0, 1)
    for t in range(1, 7):
        before, now, after = base[(t - 1) % 3], base[t % 3], base[(t + 1) % 3]
        cells = memory | current | {i - 1 for i in current} | {i + 1 for i in current}
        following = set()
        for i in cells:
            value = (before ^ (i in memory)) ^ local(
                now ^ (i - 1 in current), now ^ (i in current),
                now ^ (i + 1 in current)) ^ after
            if value:
                following.add(i)
        memory, current = current, following
        if t in (3, 6) and memory == initial_memory and current == initial_current:
            found.add(t)
    return found


def main():
    s3, a3 = spectral_sequence(3, 40)
    s6, a6 = spectral_sequence(6, 40)
    assert len(s3) == 3 and len(s6) == 27
    assert a3[:12] == [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]
    assert a6[:12] == [1, 2, 7, 21, 60, 165, 461, 1282, 3587, 10001,
                       27940, 77945]

    # b(n+2)-b(n+1)-b(n)=0 and
    # a(n+4)-2a(n+3)-3a(n+2)+4a(n+1)-5a(n)=0.
    st3, b = certified_recurrence(3, [-1, -1, 1])
    st6, a = certified_recurrence(6, [-5, 4, -3, -2, 1])
    assert len(st3) == 3 and len(st6) == 27
    assert b[:4] == [1, 2, 3, 5] and a[:4] == [1, 2, 7, 21]

    # Distinct direct algorithm: enumerate all 4**n initial memory/current
    # configurations without constructing temporal-column graphs.
    expected3 = [1, 2, 3, 5, 8, 13, 21, 34]
    expected6 = [1, 2, 7, 21, 60, 165, 461, 1282]
    for n in range(8):
        tally3 = tally6 = 0
        for initial in product(range(4), repeat=n):
            periods = observed_returns(initial)
            tally3 += 3 in periods
            tally6 += 6 in periods
        assert tally3 == expected3[n] == a3[n], (n, tally3)
        assert tally6 == expected6[n] == a6[n], (n, tally6)
    print('PASS: p=3 and p=6 complete-column automata have 3 and 27 states.')
    print('PASS: exact rational-function recurrences for all lengths (Cayley-Hamilton).')
    print('PASS: independent direct evolution for all 4^n states, 0 <= n <= 7.')
    print('period-three:', a3[:12])
    print('period-six:', a6[:12])


if __name__ == '__main__':
    main()
