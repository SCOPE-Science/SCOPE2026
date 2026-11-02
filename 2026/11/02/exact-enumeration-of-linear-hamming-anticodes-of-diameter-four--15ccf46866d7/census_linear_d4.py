#!/usr/bin/env python3
"""Exact finite certificate for the diameter-four linear Hamming-anticode counts.

Every subspace of F_q^s has exactly one reduced-row-echelon generator.
We enumerate all legal echelon matrices over F_2, F_3, and F_4 on the
small supports allowed by a strict mean-weight inequality.
Run: python3 census_linear_d4.py
"""
from collections import Counter
from itertools import combinations, product
from math import comb

EXPECTED = {
    2: [1, 1, 2, 6, 26, 91, 100, 30],
    3: [1, 1, 3, 15, 129, 200],
    4: [1, 1, 4, 28, 388, 162],
}
EXPECTED_LAST_BY_DIM = {
    2: {3: 30},
    3: {2: 160, 3: 40},
    4: {2: 162},
}


def plus(a, b, q):
    return a ^ b if q == 4 else (a + b) % q


def times(a, b, q):
    if q != 4:
        return (a * b) % q
    # GF(4)=F_2[z]/(z^2+z+1): 0,1,z,z+1 represented by 0..3.
    raw = ((a & 1) * (b & 1)) ^ (
        ((((a & 1) * (b >> 1)) ^ ((a >> 1) * (b & 1))) & 1) << 1
    ) ^ (((a >> 1) * (b >> 1)) << 2)
    return raw ^ (7 if raw & 4 else 0)


def check_field(q):
    vals = range(q)
    for x, y, z in product(vals, repeat=3):
        assert times(times(x, y, q), z, q) == times(x, times(y, z, q), q)
        assert times(x, plus(y, z, q), q) == plus(times(x, y, q), times(x, z, q), q)
    for x in range(1, q):
        assert any(times(x, y, q) == 1 for y in range(1, q))


def rref_generators(s, q):
    """Yield every row space once: unique reduced row echelon representatives."""
    for rank in range(s + 1):
        for pivots in combinations(range(s), rank):
            free = [(i, j) for i, p in enumerate(pivots)
                    for j in range(p + 1, s) if j not in pivots]
            for choices in product(range(q), repeat=len(free)):
                rows = [[0] * s for _ in range(rank)]
                for i, p in enumerate(pivots):
                    rows[i][p] = 1
                for (i, j), a in zip(free, choices):
                    rows[i][j] = a
                yield rows


def number_of_all_subspaces(s, q):
    def gauss(k):
        num, den = 1, 1
        for i in range(k):
            num *= q ** (s - i) - 1
            den *= q ** (k - i) - 1
        assert num % den == 0
        return num // den
    return sum(gauss(k) for k in range(s + 1))


def diameter_le_four(rows, q, s):
    # Generate the whole code, not sampled messages or a truncated search.
    code = [tuple([0] * s)]
    for row in rows:
        extended = []
        for a in range(1, q):
            for old in code:
                z = tuple(plus(old[i], times(a, row[i], q), q)
                          for i in range(s))
                if sum(x != 0 for x in z) > 4:
                    return False
                extended.append(z)
        code += extended
    assert len(code) == q ** len(rows)
    return True


def profile(s, q):
    seen = 0
    good_full = Counter()
    good_all = 0
    for rows in rref_generators(s, q):
        seen += 1
        full = all(any(row[j] != 0 for row in rows) for j in range(s))
        valid = diameter_le_four(rows, q, s)
        if valid:
            good_all += 1
            if full:
                good_full[len(rows)] += 1
    assert seen == number_of_all_subspaces(s, q), (q, s, seen)
    return sum(good_full.values()), dict(good_full), good_all, seen


def main():
    for q in (2, 3, 4):
        check_field(q)
        arr = []
        for s, expected in enumerate(EXPECTED[q]):
            total, dimensions, good_all, all_sub = profile(s, q)
            assert total == expected, (q, s, total, expected)
            if s == len(EXPECTED[q]) - 1:
                assert dimensions == EXPECTED_LAST_BY_DIM[q]
            arr.append(total)
            print(f'q={q} s={s} full={total} by_dimension={dimensions} '
                  f'valid_subspaces={good_all} all_subspaces={all_sub}')
        # A distinct check of the support-decomposition formula for the small
        # full ambient dimensions: all valid subspaces are counted directly.
        n = len(arr) - 1
        direct_all = profile(n, q)[2]
        by_support = sum(comb(n, j) * arr[j] for j in range(n + 1))
        assert direct_all == by_support
        print(f'PASS q={q} support_profile={arr}; ambient_n={n}; '
              f'all_valid={direct_all}')
    # On supports s<=4 there is no diameter restriction. The number of
    # full-support subspaces follows by coordinate inclusion-exclusion:
    # a_q(0..4)=[1,1,q,q(2q-1),q^4+3q^3-4q^2+q].
    for q in (2, 3, 4, 5, 7, 8, 9):
        def g(s):
            return number_of_all_subspaces(s, q)
        for s in range(5):
            incl = sum((-1)**(s-j) * comb(s,j) * g(j)
                       for j in range(s+1))
            explicit = [1,1,q,q*(2*q-1),q**4+3*q**3-4*q*q+q][s]
            assert incl == explicit
    print('PASS short-support symbolic coefficients and field arithmetic')

if __name__ == '__main__':
    main()
