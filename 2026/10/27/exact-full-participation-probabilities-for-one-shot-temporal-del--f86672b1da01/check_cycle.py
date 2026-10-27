#!/usr/bin/env python3
"""Exact, self-contained direct audit of temporal cycle delegation counts."""
from collections import Counter
from itertools import permutations
from math import factorial


def direct_count(times):
    """Build every possible cycle-rooted delegation tree and trace every vote."""
    n = len(times)
    successful = 0
    for removed in range(n):
        # Vertex 0 is the guru. Edge i joins vertex i to (i+1) modulo n.
        # Deleting one edge leaves a path, with every edge directed to guru 0.
        out = {}
        for v in range(1, n):
            # Both neighbor choices: the retained-edge branch must reach 0.
            left = (v - 1) % n
            right = (v + 1) % n
            # The branch to the root cannot cross the removed edge.
            if v <= removed:
                out[v] = (left, times[v - 1])
            else:
                out[v] = (right, times[v])
        valid = True
        for v in range(1, n):
            node = v
            prev_time = n + 1
            visited = set()
            while node != 0:
                if node in visited or node not in out:
                    valid = False
                    break
                visited.add(node)
                node, current_time = out[node]
                if current_time >= prev_time:
                    valid = False
                    break
                prev_time = current_time
            if not valid:
                break
        successful += int(valid)
    return successful


def formula(n):
    return {
        0: factorial(n) - (n - 2) * (1 << (n - 1)) - 2,
        1: (n - 3) * (1 << (n - 1)) + 2,
        2: 2,
        3: (1 << (n - 1)) - 2,
    }


def run():
    for n in range(3, 9):
        tally = Counter(direct_count(p) for p in permutations(range(1, n + 1)))
        expected = formula(n)
        assert dict(tally) == {k: v for k, v in expected.items() if v != 0}, (n, tally, expected)
        assert sum(k * tally[k] for k in tally) == n * 2 ** (n - 1)
        print('n=', n, 'direct_tally=', dict(sorted(tally.items())), 'expected=', expected)
    print('PASS: every labeled edge order, three through eight vertices')


if __name__ == '__main__':
    run()
