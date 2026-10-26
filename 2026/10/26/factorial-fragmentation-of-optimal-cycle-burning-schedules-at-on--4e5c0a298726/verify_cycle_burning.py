#!/usr/bin/env python3
"""Reproducible finite checks for near-square cycle burning schedules.

Run: python3 verify_cycle_burning.py
The direct brute enumerator uses vertex-wise distance coverings and the
strictly-unburned-before-ignition convention. The constructive enumerator uses
cyclic arc lengths and a one-cell overlap. Only Python's standard library is used.
"""
from itertools import permutations, product
from collections import defaultdict, Counter
from math import factorial


def dist(a, b, n):
    d = abs(a - b)
    return min(d, n - d)


def valid(t, n):
    k = len(t)
    if len(set(t)) != k:
        return False
    if any(dist(t[i], t[j], n) < j - i
           for i in range(k) for j in range(i + 1, k)):
        return False
    return all(any(dist(v, t[i], n) <= k - 1 - i for i in range(k))
               for v in range(n))


def direct_schedules(k, n):
    return {x for x in product(range(n), repeat=k) if valid(x, n)}


def arc_schedules(k, n):
    if n not in (k*k, k*k-1):
        raise ValueError('Only the square and one-below-square cases are encoded')
    radii = [k-1-i for i in range(k)]
    out = set()
    for perm_tail in permutations(range(1, k)):
        order = (0,) + perm_tail
        for overlapped_gap in (range(k) if n == k*k-1 else (None,)):
            step = [radii[order[j]] + radii[order[(j+1)%k]] + 1
                    - (int(j == overlapped_gap) if overlapped_gap is not None else 0)
                    for j in range(k)]
            assert sum(step) == n
            for start in range(n):
                x = [None] * k
                pos = start
                for j, source_index in enumerate(order):
                    x[source_index] = pos
                    pos = (pos + step[j]) % n
                out.add(tuple(x))
    target = n * factorial(k) if n == k*k-1 else n*factorial(k-1)
    assert len(out) == target, (k, n, len(out), target)
    return out


def components(schedules, k):
    seq = sorted(schedules)
    parent = list(range(len(seq)))
    weight = [1]*len(seq)
    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
    def join(i, j):
        i, j = find(i), find(j)
        if i != j:
            if weight[i] < weight[j]:
                i, j = j, i
            parent[j] = i
            weight[i] += weight[j]
    degree = [0]*len(seq)
    edges = 0
    for coordinate in range(k):
        fibers = defaultdict(list)
        for i,t in enumerate(seq):
            fibers[t[:coordinate]+t[coordinate+1:]].append(i)
        for fiber in fibers.values():
            for ix in range(len(fiber)):
                i = fiber[ix]
                for jy in range(ix):
                    j = fiber[jy]
                    degree[i] += 1
                    degree[j] += 1
                    edges += 1
                    join(i, j)
    sizes = Counter(find(i) for i in range(len(seq)))
    return edges, sorted(sizes.values()), dict(Counter(degree))


def main():
    for k in range(2,8):
        n = k*k-1
        schedules = arc_schedules(k,n)
        if k <= 4:
            brute = direct_schedules(k,n)
            assert brute == schedules, (k, n, len(brute), len(schedules))
        if k <= 5:
            assert all(valid(s,n) for s in schedules)
        edges, sizes, degrees = components(schedules,k)
        expected_c = factorial(k-2)
        expected_v = n*k*(k-1)
        expected_e = n*(3*k-4)*factorial(k-1)
        assert len(sizes) == expected_c
        assert sizes == [expected_v]*expected_c
        assert edges == expected_e
        if k == 2:
            assert degrees == {2:len(schedules)}
        else:
            low = n*factorial(k-1)*(k-2)
            high = 2*n*factorial(k-1)
            assert degrees == {2:low, 2*k-2:high}, (k,degrees)
        print(f'NEAR_SQUARE k={k} n={n} vertices={len(schedules)} '
              f'edges={edges} components={len(sizes)} each_size={expected_v} '
              f'degree_hist={sorted(degrees.items())} CHECK_OK')
        if k <= 4:
            n2=k*k
            direct = direct_schedules(k,n2)
            constructed = arc_schedules(k,n2)
            assert direct == constructed
            e2, sizes2, deg2 = components(constructed,k)
            assert e2 == 0 and len(sizes2)==n2*factorial(k-1)
            print(f'SQUARE k={k} n={n2} isolated={len(constructed)} CHECK_OK')
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
