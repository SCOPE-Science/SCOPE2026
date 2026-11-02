#!/usr/bin/env python3
"""Exact finite certificate for translated boxes in SL_2(Z).

For width w, the proof reduces all integer coordinate intervals to starting
points in range(-2*(w-1), w). This program evaluates those finite cases.
"""
from itertools import product
from math import gcd
from random import Random

EXPECTED = {
    2: (6, 4),
    3: (20, 1),
    4: (36, 16),
    5: (60, 8),
}


def count_direct(starts, w):
    a, b, c, d = starts
    return sum(x * t - y * z == 1
               for x in range(a, a + w)
               for y in range(b, b + w)
               for z in range(c, c + w)
               for t in range(d, d + w))


def count_by_columns(starts, w):
    a, b, c, d = starts
    out = 0
    for x in range(a, a + w):
        for z in range(c, c + w):
            if gcd(x, z) != 1:
                continue
            for y in range(b, b + w):
                if x == 0:
                    if -y*z == 1:
                        out += w
                else:
                    q = 1+y*z
                    if q % x == 0 and d <= q // x < d+w:
                        out += 1
    return out


def main():
    maxima = {}
    for w, (expected_peak, expected_number) in EXPECTED.items():
        best = -1
        attainers = []
        tested = 0
        starts_range = range(-2 * (w-1), w)
        for s in product(starts_range, repeat=4):
            count = count_direct(s, w)
            tested += 1
            if count > best:
                best = count
                attainers = [s]
            elif count == best:
                attainers.append(s)
        assert (best, len(attainers)) == (expected_peak, expected_number)
        for s in attainers:
            assert count_by_columns(s, w) == best
        maxima[w] = (best, attainers)
        print(f'width={w} starts_tested={tested} maximum={best} attainers={len(attainers)}')
        print('attainers:', attainers)
    for w in range(2,6):
        assert count_direct(tuple([-w//2]*4), w) == count_by_columns(tuple([-w//2]*4), w)
    rng = Random(137)
    for w in range(2,6):
        for _ in range(300):
            s = tuple(rng.randrange(-2*(w-1),w) for _ in range(4))
            assert count_direct(s,w)==count_by_columns(s,w)
    # Every boundary coordinate value occurs in a determinant-one matrix at
    # each maximizing width-five block. Consequently no smaller integer
    # coordinate interval can attain the same maximum.
    expected_centers = {
        (u,0,0,v) for u in (-1,1) for v in (-1,1)
    } | {
        (0,u,v,0) for u in (-1,1) for v in (-1,1)
    }
    attained_centers = {
        tuple(s_i+2 for s_i in s) for s in maxima[5][1]
    }
    assert attained_centers == expected_centers
    for s in maxima[5][1]:
        solutions = [point for point in product(*(range(v, v+5) for v in s))
                     if point[0]*point[3] - point[1]*point[2] == 1]
        assert len(solutions) == 60
        for coordinate in range(4):
            assert set(m[coordinate] for m in solutions) == set(range(s[coordinate], s[coordinate]+5))
    origin = count_direct((-2,-2,-2,-2),5)
    shifted = count_direct((-2,-1,-1,-2),5)
    assert origin == 52 and shifted == 60
    assert count_by_columns((-2,-1,-1,-2),5)==60
    print(f'origin_T2={origin} shifted_T2={shifted} crosscheck_random=1200')
    print('radius2_exact_real_centers=8 all_boundary_values_essential=PASS')
    print('VERIFY_OK width=2..5, all reduced starts, exact integer determinant, finite certificate')


if __name__ == '__main__':
    main()
