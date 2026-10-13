#!/usr/bin/env python3
"""Finite computational checks for cycle-convexity on specified cactus graphs.

Python standard library only. All graph vertex sets are 0,1,...,n-1.
The verifier compares iterative cycle completion with binary-span closure
and exhaustively enumerates the three independence parameters.
"""
from functools import reduce
from operator import and_


def rank2(vectors):
    basis = {}
    for z in vectors:
        while z:
            k = z.bit_length() - 1
            if k in basis:
                z ^= basis[k]
            else:
                basis[k] = z
                break
    return len(basis)


def profile(cycles, n):
    masks = [sum(1 << v for v in cyc) for cyc in cycles]
    assert all(len(cyc) >= 3 and len(cyc) == len(set(cyc)) for cyc in cycles)
    assert all((a & b).bit_count() <= 1 for i, a in enumerate(masks) for b in masks[i+1:])
    full = (1 << n) - 1
    hull = []
    for s in range(1 << n):
        z = s
        while True:
            y = z
            for c in masks:
                if (c & ~z).bit_count() == 1:
                    y |= c
            if y == z:
                break
            z = y
        hull.append(z)
    for s in range(1 << n):
        V = masks + [1 << j for j in range(n) if (s >> j) & 1]
        r = rank2(V)
        linear = s
        for j in range(n):
            if rank2(V + [1 << j]) == r:
                linear |= 1 << j
        assert linear == hull[s], (cycles, n, s, linear, hull[s])
    vals = [0, 0, 0]
    for s in range(1 << n):
        size = s.bit_count()
        if size < min(vals):
            continue
        unit = [1 << i for i in range(n) if (s >> i) & 1]
        c = all(not (hull[s ^ e] & e) for e in unit)
        if c: vals[2] = max(vals[2], size)
        if size <= 1: h = True
        else: h = reduce(and_, (hull[s ^ e] for e in unit), full) == 0
        if h: vals[0] = max(vals[0], size)
        # One representative of each unordered bipartition suffices.
        t = (s & -s)
        rd = True
        while t < (1 << n):
            if t & s == t and (hull[t] & hull[s ^ t]):
                rd = False
                break
            t += 1
        if rd: vals[1] = max(vals[1], size)
    assert vals == [n - len(cycles)] * 3, (cycles, vals)
    return len(hull), vals


def bouquet(lengths):
    cycles = []
    k = 1
    for m in lengths:
        c = [0] + list(range(k, k + m - 1))
        k += m - 1
        cycles.append(c)
    return cycles, k


def chain(lengths):
    cycles = []
    cur = 0
    nxt = 1
    for m in lengths:
        c = [cur] + list(range(nxt, nxt + m - 1))
        nxt += m - 1
        cur = c[-1]
        cycles.append(c)
    return cycles, nxt


def center_branch():
    cycles = [[0, 1, 2], [0, 3, 4], [1, 5, 6], [2, 7, 8]]
    return cycles, 9


def bridge_pair():
    # These two triangles may be joined by an edge 2--3, with pendant edge 5--6.
    # Bridges are omitted from the cycle list because they cannot infect vertices.
    return [[0, 1, 2], [3, 4, 5]], 7


def main():
    tests = [("forest", ([], 5))]
    tests += [("bouquet-" + str(a), bouquet(a)) for a in (
        (3,), (4,), (3,3), (3,3,3), (3,3,3,3), (3,4,3), (4,4,3))]
    tests += [("chain-" + str(a), chain(a)) for a in (
        (3,3), (3,3,3), (3,3,3,3), (3,4,3), (4,4,3))]
    tests += [("branch", center_branch()), ("bridge", bridge_pair())]
    checked = 0
    for name, (cycles, n) in tests:
        num, params = profile(cycles, n)
        checked += num
        print(f"{name}: n={n}; cycles={len(cycles)}; subsets={num}; H/R/rank={params}; OK")
    print(f"PASS profiles={len(tests)} tested_subsets={checked}")

if __name__ == '__main__':
    main()
