"""Exhaustive finite checks of temporal transit reachability on Hasse trees.

Run: python3 checker.py
"""
from itertools import product


def closure(relation):
    n = len(relation)
    out = [[bool(i == j or relation[i][j]) for j in range(n)] for i in range(n)]
    for k in range(n):
        for i in range(n):
            if out[i][k]:
                for j in range(n):
                    out[i][j] |= out[k][j]
    return out


def hasse_edges(leq):
    n = len(leq)
    return [(a, b) for a in range(n) for b in range(n)
            if a != b and leq[a][b] and not any(
                c != a and c != b and leq[a][c] and leq[c][b]
                for c in range(n))]


def reachability(leq, looped):
    n = len(leq)
    edges = hasse_edges(leq)
    oriented = [[False] * n for _ in range(n)]
    for lower, upper in edges:
        oriented[lower][upper] = True
        if upper not in looped:
            oriented[upper][lower] = True
    via_hasse = closure(oriented)
    # Alvarez's B-step: x B w iff w<=x and (w,x] contains no looped vertex.
    step = [[any(leq[w][x] and not any(
                z in looped and z != w and leq[w][z] and leq[z][x]
                for z in range(n)) and leq[w][y]
                for w in range(n)) for y in range(n)] for x in range(n)]
    via_B = closure(step)
    assert via_B == via_hasse, (leq, looped, via_B, via_hasse)
    return via_hasse, edges


def enumerated_posets(n):
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    for orientations in product((0, 1, 2), repeat=len(pairs)):
        leq = [[i == j for j in range(n)] for i in range(n)]
        for (a, b), orientation in zip(pairs, orientations):
            if orientation == 1:
                leq[a][b] = True
            elif orientation == 2:
                leq[b][a] = True
        if any(leq[a][b] and leq[b][c] and not leq[a][c]
               for a in range(n) for b in range(n) for c in range(n)):
            continue
        yield leq


def tree_forced_vertices(n, edges):
    if len(edges) != n - 1:
        return None
    adjacent = [[] for _ in range(n)]
    for a, b in edges:
        adjacent[a].append(b)
        adjacent[b].append(a)
    seen, work = {0}, [0]
    while work:
        for v in adjacent[work.pop()]:
            if v not in seen:
                seen.add(v)
                work.append(v)
    if len(seen) != n:
        return None
    minima = [i for i in range(n) if not any(b == i for a, b in edges)]
    forbidden_by_minimal = []
    for root in minima:
        dist = {root: 0}
        todo = [root]
        for vertex in todo:
            for neighbour in adjacent[vertex]:
                if neighbour not in dist:
                    dist[neighbour] = dist[vertex] + 1
                    todo.append(neighbour)
        forbidden_by_minimal.append({upper for lower, upper in edges
                                     if dist[upper] < dist[lower]})
    return len(minima), forbidden_by_minimal



def check():
    for n in range(1, 6):
        nposets = ntree = 0
        for leq in enumerated_posets(n):
            nposets += 1
            edges = hasse_edges(leq)
            tree_data = tree_forced_vertices(n, edges)
            simple_count = root_count = 0
            for mask in range(1 << n):
                looped = {i for i in range(n) if (mask >> i) & 1}
                reachable, _ = reachability(leq, looped)
                simple_count += all(all(row) for row in reachable)
                root_count += any(all(row) for row in reachable)
            if tree_data is not None:
                ntree += 1
                nminimal, forbidden = tree_data
                assert simple_count == 2 ** nminimal, (n, leq, 'simple')
                si_exact = 0
                for mask in range(1, 1 << nminimal):
                    forced = set().union(*(forbidden[j] for j in range(nminimal)
                                           if (mask >> j) & 1))
                    sign = 1 if mask.bit_count() % 2 else -1
                    si_exact += sign * 2 ** (n - len(forced))
                assert root_count == si_exact, (
                    n, leq, 'subdirectly irreducible', root_count, si_exact)
        print('n =', n, 'labelled posets =', nposets,
              'Hasse trees =', ntree, 'all loop sets verified')
    print('ALL_CHECKS_OK')


if __name__ == '__main__':
    check()
