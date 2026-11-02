#!/usr/bin/env python3
"""Exhaustive check of 2-switch cycle-type rates for small labelled bipartite 2-factors.
Uses row-pair edge replacement and component searches. Pure Python 3.10+.
"""
from collections import Counter
from itertools import combinations
from math import factorial


def enumerate_states(n):
    options = list(combinations(range(n), 2))
    degrees = [0] * n
    rows = []
    def dfs():
        if len(rows) == n:
            if all(x == 2 for x in degrees):
                yield tuple(rows)
            return
        remaining = n - len(rows) - 1
        for option in options:
            for col in option:
                degrees[col] += 1
            if all(x <= 2 and x + remaining >= 2 for x in degrees):
                rows.append(option)
                yield from dfs()
                rows.pop()
            for col in option:
                degrees[col] -= 1
    yield from dfs()


def cycle_type(rows):
    n = len(rows)
    unseen = set(range(n))
    result = []
    while unseen:
        first = next(iter(unseen))
        stack = [first]
        seen_rows = {first}
        seen_cols = set()
        while stack:
            r = stack.pop()
            for c in rows[r]:
                if c not in seen_cols:
                    seen_cols.add(c)
                    for t in range(n):
                        if t in unseen and t not in seen_rows and c in rows[t]:
                            seen_rows.add(t)
                            stack.append(t)
        unseen -= seen_rows
        result.append(len(seen_rows))
    assert all(k >= 2 for k in result)
    return tuple(sorted(result))


def theoretical_type_changes(part):
    transitions = Counter()
    for i, a in enumerate(part):
        transitions[part] += a * (a - 2)
        for j in range(i + 1, len(part)):
            b = part[j]
            after = tuple(sorted(part[:i] + part[i+1:j] + part[j+1:] + (a + b,)))
            transitions[after] += 4 * a * b
        for u in range(2, a//2 + 1):
            v = a-u
            if v >= 2:
                after = tuple(sorted(part[:i] + part[i+1:] + (u, v)))
                transitions[after] += a if u == v else 2*a
    return transitions


def expected_count(n, part):
    counts = Counter(part)
    denominator = 1
    for k, mult in counts.items():
        denominator *= (2*k)**mult * factorial(mult)
    return factorial(n)**2 // denominator


def switches(rows):
    n = len(rows)
    for a,b in combinations(range(n),2):
        aset, bset = set(rows[a]),set(rows[b])
        for x in aset-bset:
            for y in bset-aset:
                nxt = list(rows)
                nxt[a] = tuple(sorted((aset-{x})|{y}))
                nxt[b] = tuple(sorted((bset-{y})|{x}))
                yield tuple(nxt)


def main():
    for n in range(2,6):
        states = list(enumerate_states(n))
        lookup = set(states)
        hist = Counter(map(cycle_type, states))
        partitions = sorted(hist)
        for part in partitions:
            assert hist[part] == expected_count(n,part), (n,part,hist[part])
        for st in states:
            part = cycle_type(st)
            moves = list(switches(st))
            assert len(moves)==len(set(moves))
            assert all(t in lookup for t in moves)
            got = Counter(cycle_type(t) for t in moves)
            pred = theoretical_type_changes(part)
            assert got == pred, (n,part,got,pred)
            assert sum(got.values()) == n*(2*n-5)+2*part.count(2)
        assert sum(hist.values())==len(states)
        print(f'n={n} states={len(states)} partitions={len(partitions)} distinct_cycle_type_rates=PASS')
        print('  stratum_counts:',dict(sorted(hist.items())))
    print('PYTHON_EXHAUSTIVE_SWITCH_LUMPING_PASS')

if __name__ == '__main__':
    main()
