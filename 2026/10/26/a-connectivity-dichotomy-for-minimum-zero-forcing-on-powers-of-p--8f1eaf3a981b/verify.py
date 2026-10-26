#!/usr/bin/env python3
"""Finite checks for minimum zero forcing reconfiguration of path and cycle powers.

Usage: python3 verify.py
Requires only the Python standard library.  The all-parameter result has a
mathematical proof; these finite tests independently check small instances.
"""

from collections import Counter, deque
from itertools import combinations


def adjacency(n, k, cycle):
    out = []
    for i in range(n):
        nbr = 0
        for j in range(n):
            d = abs(i - j)
            if cycle:
                d = min(d, n - d)
            if 0 < d <= k:
                nbr |= 1 << j
        out.append(nbr)
    return out


def forcing_parallel(blue, adj):
    full = (1 << len(adj)) - 1
    while True:
        newly = 0
        for i, neighbors in enumerate(adj):
            if blue & (1 << i):
                white = neighbors & ~blue
                if white and not (white & (white - 1)):
                    newly |= white
        if not newly:
            return blue == full
        blue |= newly


def forcing_sequential(blue, adj):
    full = (1 << len(adj)) - 1
    while blue != full:
        for i, neighbors in enumerate(adj):
            if blue & (1 << i):
                white = neighbors & ~blue
                if white and not (white & (white - 1)):
                    blue |= white
                    break
        else:
            return False
    return True


def theoretical(n, k, cycle):
    if cycle:
        out = set()
        for center in range(n):
            window = {((center + d) % n) for d in range(-k, k + 1)}
            for hole in window - {center}:
                out.add(sum(1 << v for v in window - {hole}))
        return out
    left = set(range(k + 1))
    right = set(range(n - 1 - k, n))
    out = set()
    for j in range(1, k + 1):
        out.add(sum(1 << v for v in left - {j}))
        out.add(sum(1 << v for v in right - {n - 1 - j}))
    return out


def exchange_graph(states, n):
    states = sorted(states)
    ids = {s: t for t, s in enumerate(states)}
    neighbors = [set() for _ in states]
    for v, s in enumerate(states):
        for i in range(n):
            if not s & (1 << i):
                continue
            for j in range(n):
                if s & (1 << j):
                    continue
                other = s ^ (1 << i) ^ (1 << j)
                if other in ids:
                    neighbors[v].add(ids[other])
    assert all(v in neighbors[w] for w, A in enumerate(neighbors) for v in A)
    return states, neighbors


def component_sizes(neighbors):
    unseen = set(range(len(neighbors)))
    sizes = []
    while unseen:
        start = unseen.pop()
        q = [start]
        count = 0
        while q:
            u = q.pop()
            count += 1
            for v in neighbors[u] & unseen:
                unseen.remove(v)
                q.append(v)
        sizes.append(count)
    return sorted(sizes, reverse=True)


def check_predicted(n, k, cycle, exhaustive):
    adj = adjacency(n, k, cycle)
    expected = theoretical(n, k, cycle)
    assert all(forcing_parallel(x, adj) for x in expected)
    if exhaustive:
        actual = set()
        for c in combinations(range(n), 2*k if cycle else k):
            state = sum(1 << j for j in c)
            a = forcing_parallel(state, adj)
            b = forcing_sequential(state, adj)
            assert a == b, (n, k, cycle, c)
            if a:
                actual.add(state)
        assert actual == expected, (n, k, cycle, len(actual), len(expected))
    states, neighbors = exchange_graph(expected, n)
    if cycle:
        assert len(states) == n * (2*k - 1), (n, k, len(states))
        assert component_sizes(neighbors) == [len(states)], (n, k)
        if n >= 2*k + 4:
            assert sum(map(len, neighbors)) // 2 == n*(k+1)*(2*k-1), (n,k)
    else:
        assert len(states) == 2*k
        if n == k + 2:
            assert component_sizes(neighbors) == [2*k]
            assert Counter(map(len, neighbors)) == {k:2*k}
        elif n == k + 3:
            assert component_sizes(neighbors) == [2*k]
            assert sum(map(len, neighbors)) // 2 == k*(k-1)+1
        else:
            assert component_sizes(neighbors) == [k, k]
            assert sum(map(len, neighbors)) // 2 == k*(k-1)
    return len(states), sum(map(len,neighbors)) // 2, component_sizes(neighbors)


def main():
    small = 0
    for k in range(2, 7):
        for n in range(k+2, k+9):
            result = check_predicted(n,k,False,True)
            small += 1
    print('PATH_EXHAUSTIVE_OK', small, 'parameter pairs, two independent forcing simulations')
    small=0
    for k in range(2,5):
        for n in range(2*k+3, min(2*k+8,16)):
            result=check_predicted(n,k,True,True)
            small+=1
    print('CYCLE_EXHAUSTIVE_OK',small,'parameter pairs, two independent forcing simulations')
    for k,n in [(2,20),(3,25),(4,30),(5,35),(6,40),(7,45)]:
        p=check_predicted(n,k,False,False)
        c=check_predicted(n,k,True,False)
        print(f'k={k} n={n}: path={p[0]} states, components={p[2]}; cycle={c[0]} states, edges={c[1]}, components={len(c[2])} STRUCTURAL_OK')
    print('ALL_VERIFY_OK')

if __name__ == '__main__':
    main()
