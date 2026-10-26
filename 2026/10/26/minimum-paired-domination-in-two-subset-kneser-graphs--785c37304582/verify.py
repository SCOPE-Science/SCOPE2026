#!/usr/bin/env python3
"""Exact checks for paired domination in two-subset Kneser graphs.
Pure Python 3 standard library, with independent domination and coverage tests.
"""
from collections import Counter
from itertools import combinations, permutations
from math import comb


def model(n):
    edges = list(combinations(range(n), 2))
    # A vertex of KG(n,2) is an edge of K_n.
    bit = [sum(1 << i for i, f in enumerate(edges)
               if not (set(e) & set(f))) for e in edges]
    return edges, bit


def perfect_matching(indices, bit):
    if not indices:
        return True
    x, rest = indices[0], indices[1:]
    return any((bit[x] >> y) & 1 and
               perfect_matching(tuple(z for z in rest if z != y), bit)
               for y in rest)


def paired_dominating(indices, bit):
    used = sum(1 << i for i in indices)
    # Every unselected vertex is adjacent to a selected one.
    if any(not (row & used) for i, row in enumerate(bit)
           if not (used >> i) & 1):
        return False
    return perfect_matching(indices, bit)


def comp_type(subedges):
    support = set(sum((list(e) for e in subedges), []))
    adjacency = {u: set() for u in support}
    for a, b in subedges:
        adjacency[a].add(b)
        adjacency[b].add(a)
    comps = []
    while support:
        x = support.pop()
        seen, stack = {x}, [x]
        while stack:
            z = stack.pop()
            for y in adjacency[z] - seen:
                seen.add(y)
                stack.append(y)
        support.difference_update(seen)
        degrees = tuple(sorted(len(adjacency[z]) for z in seen))
        comps.append((len(seen), sum(len(adjacency[z]) for z in seen)//2, degrees))
    return tuple(sorted(comps))


def classify_type(subedges):
    ct = comp_type(subedges)
    if sorted(c[1] for c in ct) == [1, 1, 1, 1]:
        return '4K2'
    if sorted(c[1] for c in ct) == [1, 1, 2]:
        return 'P3+2K2'
    if sorted(c[1] for c in ct) == [1, 3]:
        c = next(c for c in ct if c[1] == 3)
        if c[0] == 4 and c[2] == (1,1,2,2):
            return 'P4+K2'
    return 'OTHER'


def count_four(n):
    edges, bit = model(n)
    count = Counter()
    independent_count = 0
    for chosen in combinations(range(len(edges)), 4):
        direct = paired_dominating(chosen, bit)
        # Alternative characterization: no two vertices meet all chosen edges,
        # and the selected induced disjointness graph has a perfect matching.
        uncovered = [p for p in edges if all(set(p) & set(edges[i]) for i in chosen)]
        by_cover = not uncovered and perfect_matching(chosen, bit)
        if direct != by_cover:
            raise AssertionError((n, chosen, direct, by_cover))
        if direct:
            independent_count += 1
            count[classify_type([edges[i] for i in chosen])] += 1
    expected = {'P4+K2': 180*comb(n, 6) if n>=6 else 0,
                'P3+2K2': 315*comb(n, 7) if n>=7 else 0,
                '4K2': 105*comb(n, 8) if n>=8 else 0}
    assert count == Counter({k:v for k,v in expected.items() if v}), (n,count,expected)
    return independent_count


def small_cases():
    # Exhaust all even subset sizes, not only the predicted optimum.
    for n, expected_count in ((4, 1), (5, 125)):
        edges, bit = model(n)
        first, sets = None, []
        for k in range(2, len(edges)+1, 2):
            good = [s for s in combinations(range(len(edges)), k)
                    if paired_dominating(s, bit)]
            if good:
                first, sets = k, good
                break
        assert first == 6 and len(sets) == expected_count, (n, first, len(sets))
        if n == 5:
            index = {e: j for j, e in enumerate(edges)}
            family = set(sets)
            unprocessed = set(sets)
            sizes = []
            complements = []
            for s in sets:
                if s not in unprocessed:
                    continue
                orbit = set()
                for p in permutations(range(5)):
                    translated = tuple(sorted(index[tuple(sorted((p[a], p[b])))]
                                              for i in s for a,b in (edges[i],)))
                    orbit.add(translated)
                assert orbit <= family
                unprocessed -= orbit
                sizes.append(len(orbit))
                t = [i for i in range(10) if i not in s]
                complements.append((len(orbit),sum(1 for x,y in combinations(t,2)
                                          if (bit[x] >> y) & 1)))
            assert sorted(sizes) == [5,60,60], sizes
            assert sorted(complements) == [(5,0),(60,2),(60,3)], complements
        print('small', n, 'minimum', first, 'count', len(sets))


if __name__ == '__main__':
    small_cases()
    for n in range(4, 11):
        c=count_four(n)
        print('four', n, c)
    print('VERIFY_OK')
