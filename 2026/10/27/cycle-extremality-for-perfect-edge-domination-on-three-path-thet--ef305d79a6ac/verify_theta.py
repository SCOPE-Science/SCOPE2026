#!/usr/bin/env python3
"""Exact checks for perfect edge domination in three-path theta graphs.

Requires only Python 3's standard library. Run: python3 verify_theta.py
"""
from itertools import combinations_with_replacement, product
from functools import lru_cache

STATES = ((0, 0), (0, 1), (1, 0), (1, 1))
T = tuple(tuple(int(v == w and (v == 1 or u + z == 1))
                for w, z in STATES) for u, v in STATES)
I = tuple(tuple(int(i == j) for j in range(4)) for i in range(4))

def multiply(X, Y):
    return tuple(tuple(sum(X[i][h] * Y[h][j] for h in range(4))
                       for j in range(4)) for i in range(4))

@lru_cache(None)
def power(k):
    assert k >= 0
    return I if k == 0 else multiply(power(k - 1), T)

def path_count(length, a, b, first, last):
    """Count one path given endpoint incidence totals and edge bits."""
    assert length >= 2
    ans = 0
    Q = power(length - 2)
    for i, (u, v) in enumerate(STATES):
        if u != first or (first == 0 and a + v != 1):
            continue
        for j, (w, z) in enumerate(STATES):
            if z != last or (last == 0 and b + w != 1):
                continue
            ans += Q[i][j]
    return ans

@lru_cache(None)
def theta_count(a, b, c):
    assert min(a, b, c) >= 2
    total = 0
    for start in product((0, 1), repeat=3):
        left_degree = sum(start)
        for end in product((0, 1), repeat=3):
            right_degree = sum(end)
            z = 1
            for length, first, last in zip((a, b, c), start, end):
                z *= path_count(length, left_degree, right_degree, first, last)
            total += z
    return total

def cycle_count(n):
    assert n >= 3
    Q = power(n)
    return sum(Q[i][i] for i in range(4))

def graph_edges(lengths):
    """Construct three internally vertex-disjoint paths between 0 and 1."""
    edges = []
    new_vertex = 2
    for length in lengths:
        previous = 0
        for step in range(length):
            current = 1 if step == length - 1 else new_vertex
            if step < length - 1:
                new_vertex += 1
            edges.append((previous, current))
            previous = current
    assert new_vertex == sum(lengths) - 1
    return edges

def independent_bruteforce(lengths):
    """Exhaust all edge subsets without using transfer states."""
    edges = graph_edges(lengths)
    adj = []
    for i, (u, v) in enumerate(edges):
        adj.append([j for j, (p, q) in enumerate(edges)
                    if i != j and (u in (p, q) or v in (p, q))])
    count = 0
    for mask in range(1 << len(edges)):
        good = True
        for i, nbrs in enumerate(adj):
            if mask & (1 << i):
                continue
            if sum(bool(mask & (1 << j)) for j in nbrs) != 1:
                good = False
                break
        if good:
            count += 1
    return count

# The 20 unordered three-parameter base cases: (a,b,c) -> PED count.
BASE = {
    (2, 2, 2): 6, (2, 2, 3): 4, (2, 2, 4): 6, (2, 2, 5): 12,
    (2, 3, 3): 7, (2, 3, 4): 8, (2, 3, 5): 12,
    (2, 4, 4): 12, (2, 4, 5): 18, (2, 5, 5): 30,
    (3, 3, 3): 10, (3, 3, 4): 13, (3, 3, 5): 20,
    (3, 4, 4): 19, (3, 4, 5): 27, (3, 5, 5): 39,
    (4, 4, 4): 29, (4, 4, 5): 41, (4, 5, 5): 59,
    (5, 5, 5): 89,
}

def main():
    assert T == ((0, 1, 0, 0), (0, 0, 1, 1),
                 (1, 0, 0, 0), (0, 0, 1, 1))
    four, three, one = power(4), power(3), power(1)
    assert all(four[i][j] == three[i][j] + one[i][j]
               for i in range(4) for j in range(4))
    assert [cycle_count(n) for n in range(3, 6)] == [4, 5, 6]
    for n in range(6, 42):
        assert cycle_count(n) == cycle_count(n - 1) + cycle_count(n - 3)

    assert set(BASE) == set(combinations_with_replacement(range(2, 6), 3))
    for lengths, expected in BASE.items():
        assert theta_count(*lengths) == expected
        assert independent_bruteforce(lengths) == expected
        N = sum(lengths) - 1
        difference = cycle_count(N) - expected
        assert difference >= 0
        assert (difference == 0) == (lengths == (2, 2, 2))

    # Independent exact subset checks outside the base cube.
    for lengths in product(range(2, 9), repeat=3):
        if sum(lengths) > 17:
            continue
        assert theta_count(*lengths) == independent_bruteforce(lengths)

    for a in range(2, 23):
        for b in range(2, 15):
            for c in range(2, 15):
                value = theta_count(a, b, c)
                assert value <= cycle_count(a + b + c - 1)
                if (a, b, c) != (2, 2, 2):
                    assert value < cycle_count(a + b + c - 1)
                if a >= 6:
                    assert value == theta_count(a - 1, b, c) + theta_count(a - 3, b, c)
    print('VERIFY_OK: transfer identity, 20 independently enumerated base cases,')
    print('independent small-graph enumeration, cycle and theta recurrences,')
    print('and additional parameter checks passed.')

if __name__ == '__main__':
    main()
