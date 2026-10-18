#!/usr/bin/env python3
"""Independent exhaustive bounded-morphism versus combinatorial normal-form checks."""
from itertools import product
from math import factorial
from collections import Counter


def parts(n):
    if n == 0:
        yield ()
    else:
        for x in range(1, n + 1):
            for rest in parts(n-x):
                yield (x,) + rest


def relation(sizes):
    n = sum(sizes)
    levels = sum(([j] * a for j, a in enumerate(sizes)), [])
    return levels, tuple(frozenset(y for y in range(n) if levels[x] <= levels[y]) for x in range(n))


def profile(morphism, source_levels, target_levels, target_size):
    result = []
    for j in range(max(target_levels) + 1):
        cols = []
        for v in range(target_size):
            if target_levels[v] == j:
                cols.append(tuple(sum(morphism[x] == v for x, lev in enumerate(source_levels) if lev == i)
                                  for i in range(max(source_levels) + 1)))
        result.append(tuple(sorted(cols)))
    return tuple(result)


def direct_counts(a, b):
    sa, ups_a = relation(a)
    sb, ups_b = relation(b)
    n, m = sum(a), sum(b)
    count = 0
    orbits = set()
    for f in product(range(m), repeat=n):
        if len(set(f)) < m:
            continue
        if any(frozenset(f[y] for y in ups_a[x]) != ups_b[f[x]] for x in range(n)):
            continue
        count += 1
        orbits.add(profile(f, sa, sb, m))
    return count, len(orbits)


def onto_count(n, k):
    return sum((-1)**i * __import__('math').comb(k, i) * (k-i)**n for i in range(k+1))


def predicted_labeled(a, b):
    h, k = len(a), len(b)
    if k > h:
        return 0
    result = 0
    from itertools import combinations
    for cuts in combinations(range(1, h), k-1):
        ends = (0,) + cuts + (h,)
        summand = 1
        for j in range(k):
            t, u = ends[j], ends[j+1]
            summand *= (b[j] ** sum(a[t:u-1])) * onto_count(a[u-1], b[j])
        result += summand
    return result


def compositions_row(total, slots, positive=False):
    if slots == 1:
        if total >= int(positive):
            yield (total,)
        return
    for x in range(int(positive), total + 1):
        for xs in compositions_row(total-x, slots-1, positive):
            yield (x,) + xs


def predicted_orbits_block(rows, b):
    # Every column has a positive final coordinate.  Enumerate all multisets
    # of column vectors by assigning sorted columns to b target points.
    if rows[-1] < b:
        return 0
    signatures = set()
    for allrows in product(*(compositions_row(a, b, j == len(rows)-1)
                             for j, a in enumerate(rows))):
        cols = tuple(sorted(zip(*allrows)))
        signatures.add(cols)
    return len(signatures)


def predicted_orbits(a, b):
    h, k = len(a), len(b)
    if k > h:
        return 0
    from itertools import combinations
    total = 0
    for cuts in combinations(range(1, h), k-1):
        ends = (0,) + cuts + (h,)
        prod_count = 1
        for j in range(k):
            prod_count *= predicted_orbits_block(a[ends[j]:ends[j+1]], b[j])
        total += prod_count
    return total


def main():
    checked = 0
    pms = 0
    orbits = 0
    for n in range(1, 6):
        for a in parts(n):
            for m in range(1, min(4, n)+1):
                for b in parts(m):
                    observed = direct_counts(a, b)
                    expected = (predicted_labeled(a,b), predicted_orbits(a,b))
                    if observed != expected:
                        raise AssertionError((a,b,observed,expected))
                    checked += 1
                    pms += observed[0]
                    orbits += observed[1]
    print(f'PASS exhaustive comparisons={checked} total_bounded_morphisms={pms} total_orbits={orbits}')
    examples=[((1,2,1),(2,1)),((3,2,3),(2,2)),((2,3,2),(2,1)),((3,3),(2,2))]
    for a,b in examples:
        print('CASE',a,b,'maps',predicted_labeled(a,b),'orbits',predicted_orbits(a,b))

if __name__ == '__main__':
    main()
