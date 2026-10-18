#!/usr/bin/env python3
"""Independent finite tests for two lower approximation operators.

Run with Python 3 (standard library only).  No external input files are needed.
"""
from itertools import product

def set_partitions(n):
    # Restricted-growth strings encode each set partition exactly once.
    def rec(prefix, highest):
        if len(prefix) == n:
            yield tuple(tuple(i for i, a in enumerate(prefix) if a == j)
                        for j in range(highest + 1))
            return
        for j in range(highest + 2):
            yield from rec(prefix + [j], max(highest, j))
    if n == 0:
        yield ()
    else:
        yield from rec([0], 0)

def lower(partition, mask):
    ans = 0
    for block in partition:
        bm = sum(1 << a for a in block)
        if mask & bm == bm:
            ans |= bm
    return ans

def component_masks(part1, part2, n):
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x
    for P in (part1, part2):
        for block in P:
            for x in block[1:]:
                parent[find(x)] = find(block[0])
    comps = {}
    for x in range(n):
        comps[find(x)] = comps.get(find(x), 0) | (1 << x)
    return list(comps.values())

def two_step_granules(part1, part2):
    out = []
    for outer, inner in ((part1, part2), (part2, part1)):
        for block in outer:
            neighborhood = set(block)
            for other in inner:
                if not neighborhood.isdisjoint(other):
                    neighborhood.update(other)
            out.append(sum(1 << a for a in neighborhood))
    return out

def hit_criterion(part1, part2, n, mask):
    granules = two_step_granules(part1, part2)
    for component in component_masks(part1, part2, n):
        if mask & component == component:
            continue
        if any((g & component) == g and (mask & g) == g for g in granules):
            return False
    return True

def transfer_trace(length):
    T = [[0] * 4 for _ in range(4)]
    for state in range(4):
        T[state][0] = 1
        if state < 3:
            T[state][state + 1] = 1
    P = [[int(i == j) for j in range(4)] for i in range(4)]
    for _ in range(length):
        P = [[sum(P[i][k] * T[k][j] for k in range(4))
              for j in range(4)] for i in range(4)]
    return sum(P[i][i] for i in range(4))

def no_four(length, mask):
    return all(any((mask >> ((start + delta) % length)) & 1 == 0
                   for delta in range(4)) for start in range(length))

def check():
    general_cases = 0
    for n in range(1, 6):
        parts = list(set_partitions(n))
        for E in parts:
            for F in parts:
                for mask in range(1 << n):
                    a = lower(E, lower(F, mask))
                    b = lower(F, lower(E, mask))
                    assert (a == b) == hit_criterion(E, F, n, mask), (n, E, F, mask)
                    general_cases += 1
    cycle_cases = 0
    counts = []
    for n in range(2, 9):
        N = 2 * n
        E = tuple((2 * j, 2 * j + 1) for j in range(n))
        F = tuple(((2 * j + 1) % N, (2 * j + 2) % N) for j in range(n))
        counted = 0
        for mask in range(1 << N):
            a = lower(E, lower(F, mask))
            b = lower(F, lower(E, mask))
            agree = a == b
            expected = no_four(N, mask) or mask == (1 << N) - 1
            assert agree == expected, (n, mask)
            counted += agree
            cycle_cases += 1
        assert counted == transfer_trace(N) + 1, (n, counted)
        counts.append((n, counted))
    # Test the transfer's length-4 linear recurrence, distinct from brute-force cycles.
    traces = [transfer_trace(N) for N in range(2, 45)]
    for j in range(4, len(traces)):
        assert traces[j] == sum(traces[j - k] for k in range(1, 5))
    print('VERIFY_OK general_partition_subset_cases=%d cycle_subsets=%d '
          'cycle_counts=%s recurrence=YES' % (general_cases, cycle_cases, counts))

if __name__ == '__main__':
    check()
