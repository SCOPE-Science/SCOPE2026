#!/usr/bin/env python3
"""Exact affine-stratified support classification of five-point Walsh transforms."""
from collections import Counter
P = 101

def canonical_basis(rows):
    """Reduced span over F_101; same ranks as over Q by |minor| < 101."""
    pivots = {}
    for row in rows:
        a = [x % P for x in row]
        for j, v in sorted(pivots.items()):
            if a[j]:
                t = a[j]
                a = [(x - t*y) % P for x, y in zip(a, v)]
        k = next((j for j, x in enumerate(a) if x), None)
        if k is None:
            continue
        a = [(x*pow(a[k], -1, P)) % P for x in a]
        for j, v in list(pivots.items()):
            if v[k]:
                t = v[k]
                pivots[j] = [(x-t*y) % P for x, y in zip(v, a)]
        pivots[k] = a
    return tuple(tuple(pivots[j]) for j in sorted(pivots))

def run_case(rank, points, expected, expected_flats, witnesses):
    rows = [tuple(-1 if (x & k).bit_count() % 2 else 1 for x in points)
            for k in range(1 << rank)]
    flats = {()}
    for row in rows:
        extra = set()
        for b in flats:
            joined = canonical_basis(b + (row,))
            if len(joined) < 5:
                extra.add(joined)
        flats.update(extra)
    assert len(flats) == expected_flats, ('closure count', rank, len(flats))
    histogram = Counter()
    for b in flats:
        if any(len(canonical_basis(b + (tuple(int(j == i) for j in range(5)),))) == len(b)
               for i in range(5)):
            continue
        forced = sum(len(canonical_basis(b + (row,))) == len(b) for row in rows)
        histogram[len(rows) - forced] += 1
    assert dict(histogram) == expected, ('spectrum count', rank, histogram)
    for support, c in witnesses.items():
        assert len(c) == 5 and all(c)
        nonzeros = sum(sum(x*y for x, y in zip(row, c)) != 0 for row in rows)
        assert nonzeros == support, ('witness', rank, support, nonzeros)
    return sorted(histogram.items())

def main():
    rank3 = run_case(3, (0,1,2,4,3), {4:8,5:32,6:24,7:8,8:1}, 95,
                     {4:(-2,-2,-2,-4,2), 5:(-4,-4,-4,-3,-1),
                      6:(-4,-4,-3,-4,1), 7:(-4,-4,-3,-4,-1),
                      8:(-4,-4,-4,-4,-4)})
    rank4 = run_case(4, (0,1,2,4,8), {12:80,13:160,14:80,15:16,16:1}, 537,
                     {12:(-4,-2,-2,-2,-2), 13:(-4,-4,-4,-3,-1),
                      14:(-4,-4,-3,-2,-1), 15:(-4,-4,-3,-3,-2),
                      16:(-4,-4,-4,-4,-4)})
    print('rank3', rank3)
    print('rank4', rank4)
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
