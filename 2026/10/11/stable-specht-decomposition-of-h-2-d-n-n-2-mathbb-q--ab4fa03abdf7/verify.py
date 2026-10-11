#!/usr/bin/env python3
"""Exact finite checks of symmetric-group characters for domination complexes.

Requires only Python >=3.9. This script independently enumerates graph
simplices, checks their signed permutation actions, and computes irreducible
characters by rim-hook recursion. The infinite-family proof is mathematical
and is not inferred from finitely many tests.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations
from math import comb, factorial


def partitions(n, top=None):
    if n == 0:
        yield ()
        return
    top = n if top is None else min(top, n)
    for i in range(top, 0, -1):
        for rest in partitions(n-i, i):
            yield (i,) + rest


def boxes(part):
    return {(r, c) for r, length in enumerate(part) for c in range(length)}


def rim_hook(larger, smaller):
    strip = boxes(larger) - boxes(smaller)
    if not strip:
        return None
    reachable = {next(iter(strip))}
    stack = list(reachable)
    while stack:
        r, c = stack.pop()
        for nxt in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
            if nxt in strip and nxt not in reachable:
                reachable.add(nxt)
                stack.append(nxt)
    if reachable != strip:
        return None
    if any((r+1, c) in strip and (r, c+1) in strip and (r+1, c+1) in strip
           for r, c in strip):
        return None
    return len({r for r, _ in strip})


@lru_cache(None)
def specht_character(lam, cyc):
    if not cyc:
        return 1 if not lam else 0
    k = cyc[0]
    total = 0
    for nu in partitions(sum(lam)-k):
        if len(nu) <= len(lam) and all(nu[i] <= lam[i] for i in range(len(nu))):
            height = rim_hook(lam, nu)
            if height is not None:
                total += (-1)**(height-1) * specht_character(nu, cyc[1:])
    return total


def cycle_rep(cyc):
    p = list(range(sum(cyc)))
    start = 0
    for length in cyc:
        for i in range(length):
            p[start+i] = start+(i+1) % length
        start += length
    return tuple(p)


def expected_parts(n):
    if n == 4:
        return {(2,1,1): 1}
    if n == 5:
        return {(3,1,1): 1, (2,2,1): 1, (2,1,1,1): 2}
    return {(n-2,1,1): 1, (n-3,2,1): 1,
            (n-3,1,1,1): 2, (n-4,2,1,1): 2}


def c(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def claimed_polynomial(cyc):
    ct = Counter(cyc)
    a, b, z, w = (ct[i] for i in (1, 2, 3, 4))
    F = c(a, 2) + b
    F2 = c(a+2*b, 2) + 2*w
    return (F - (F*F-F2)//2 + c(a,3) - a*b + z
            + 9*c(a,4) - 3*c(b,2) - b*c(a,2) + w-1)


def graph_facets(n):
    edges = list(combinations(range(n), 2))
    targets = [sum(1 << v for v in vs) for vs in combinations(range(n), n-3)]
    selected = [[] for _ in range(4)]
    # A dominating set of at most n-3 elements extends to exactly n-3.
    for k in range(1, 6):
        for indices in combinations(range(len(edges)), k):
            closed = [(1 << v) for v in range(n)]
            for idx in indices:
                a, b = edges[idx]
                closed[a] |= 1 << b
                closed[b] |= 1 << a
            allowed = True
            for target in targets:
                cover = 0
                for v in range(n):
                    if target & (1 << v):
                        cover |= closed[v]
                if cover == (1 << n)-1:
                    allowed = False
                    break
            if allowed:
                assert k <= 4, (n, k, indices)
                selected[k-1].append(indices)
    counts = tuple(len(x) for x in selected)
    expected = (c(n,2), c(c(n,2),2), c(n,3)+12*c(n,4), 3*c(n,4))
    assert counts == expected, (n, counts, expected)
    return edges, selected


def permutation_sign(arr):
    return -1 if sum(arr[i] > arr[j] for i in range(len(arr))
                     for j in range(i+1, len(arr))) % 2 else 1


def signed_trace(edges, faces, p):
    look = {tuple(e): i for i,e in enumerate(edges)}
    edge_image = [look[tuple(sorted((p[a],p[b])))] for a,b in edges]
    traces = []
    for level in faces:
        total = 0
        for face in level:
            moved = [edge_image[i] for i in face]
            if tuple(sorted(moved)) == face:
                total += permutation_sign(moved)
        traces.append(total)
    return tuple(traces)



def verify_orbit_characters():
    edges, faces = graph_facets(4)
    disjoint_pairs = [f for f in faces[1]
                      if len({v for idx in f for v in edges[idx]}) == 4]
    paths = [f for f in faces[2] if len({v for idx in f for v in edges[idx]}) == 4]
    squares = faces[3]
    assert (len(disjoint_pairs), len(paths), len(squares)) == (3, 12, 3)
    for cyc in partitions(4):
        p = cycle_rep(cyc)
        disjoint = signed_trace(edges, [disjoint_pairs], p)[0]
        path = signed_trace(edges, [paths], p)[0]
        square = signed_trace(edges, [squares], p)[0]
        assert disjoint == specht_character((3,1),cyc), (cyc, 'pairs')
        assert path == (2*specht_character((3,1),cyc) +
                        2*specht_character((2,1,1),cyc)), (cyc,'paths')
        assert square == specht_character((3,1),cyc), (cyc, 'squares')
    print('local_S4_orbit_characters=5_classes OK')

def hook_dim(lam):
    return factorial(sum(lam)) // __import__('math').prod(
        (lam[r]-j + sum(1 for t in range(r+1,len(lam)) if lam[t]>=j+1))
        for r in range(len(lam)) for j in range(lam[r]))


def main():
    verify_orbit_characters()
    for n in range(4, 13):
        expected = expected_parts(n)
        dim = sum(mult*hook_dim(lam) for lam, mult in expected.items())
        formula = (n-2)*(n-3)*(3*n*n-7*n-2)//12
        assert dim == formula, (n, dim, formula)
        for cyc in partitions(n):
            ch = sum(mul*specht_character(lam,cyc) for lam,mul in expected.items())
            assert ch == claimed_polynomial(cyc), (n,cyc,ch,claimed_polynomial(cyc))
        if n <= 7:
            edges, faces = graph_facets(n)
            for cyc in partitions(n):
                trace = signed_trace(edges, faces, cycle_rep(cyc))
                actual = trace[0]-trace[1]+trace[2]-trace[3]-1
                assert actual == claimed_polynomial(cyc), (n,cyc,actual,claimed_polynomial(cyc),trace)
            print('n=%s faces=%s character_classes=%s dimension=%s OK' %
                  (n, tuple(len(x) for x in faces), len(list(partitions(n))), dim))
        else:
            print('n=%s exact_character_classes=%s dimension=%s OK' %
                  (n,len(list(partitions(n))),dim))
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
