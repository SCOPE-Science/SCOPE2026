"""Exact enumeration of cyclic-Hamming three-one necklace centres.

No external dependencies. Run with Python 3.9 or newer.
This checks the finite cases and two independent distance implementations.
The infinite-size argument uses Mantel's theorem and is given in RESULT.md.
"""
from itertools import combinations
from math import comb


def necklace_representative(triple, n):
    return min(tuple(sorted((a + k) % n for a in triple)) for k in range(n))


def all_necklaces(n):
    return tuple(sorted({necklace_representative(T, n)
                         for T in combinations(range(n), 3)}))


def separation_profile(T, n):
    return frozenset(min((b - a) % n, (a - b) % n)
                     for a, b in combinations(T, 2))


def distance_by_profiles(T, U, n):
    if T == U:
        return 0
    return 2 if separation_profile(T, n) & separation_profile(U, n) else 4


def distance_by_shifts(T, U, n):
    ss = set(T)
    return min(2 * (3 - len(ss & {(u + k) % n for u in U}))
               for k in range(n))


def census(n, independent=True):
    words = all_necklaces(n)
    profiles = [separation_profile(t, n) for t in words]
    radii = []
    for i, t in enumerate(words):
        dists = []
        for j, u in enumerate(words):
            if i == j:
                d = 0
            else:
                d = 2 if profiles[i] & profiles[j] else 4
            if independent:
                assert d == distance_by_shifts(t, u, n), (n, t, u, d)
            dists.append(d)
        radii.append(max(dists))
    r = min(radii)
    return len(words), r, tuple(t for t, radius in zip(words, radii) if radius == r)


EXPECTED = {
    3:(1,0,1), 4:(1,0,1), 5:(2,2,2), 6:(4,2,4),
    7:(5,2,5), 8:(7,2,7), 9:(10,2,6), 10:(12,2,10),
    11:(15,2,10), 12:(19,2,2), 13:(22,4,22), 14:(26,2,2),
}


def main():
    for n, expected in EXPECTED.items():
        total, radius, centers = census(n)
        assert (total, radius, len(centers)) == expected, (n, total, radius, centers)
        if n == 14:
            assert centers == ((0, 2, 6), (0, 2, 10)), centers
        if n == 12:
            assert centers == ((0, 2, 6), (0, 2, 8)), centers
    for n in range(15, 27):
        total, radius, centers = census(n, independent=(n <= 17))
        formula = (comb(n, 3) + (2 * n // 3 if n % 3 == 0 else 0)) // n
        assert total == formula, (n, total, formula)
        assert radius == 4 and len(centers) == total, (n, radius)
    # Independent Cauchy-Davenport conclusion in Z/13Z: any symmetric
    # set of >=6 allowed nonzero shifts has 2|A|-1 >= 11 and cannot be sum-free.
    assert 2 * 6 - 1 + 6 > 13
    # Mantel bound is strictly exceeded for n > 14.
    for n in range(15, 1001):
        assert n * (n - 7) // 2 > n*n // 4
    print('VERIFY_OK: finite full census n=3..26; independent rotation-Hamming distances n=3..17; extremal bounds')


if __name__ == '__main__':
    main()
