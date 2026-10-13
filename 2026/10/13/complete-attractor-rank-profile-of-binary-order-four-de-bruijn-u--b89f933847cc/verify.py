#!/usr/bin/env python3
"""Exact binary order-four de Bruijn attractor census (standard library only)."""
from itertools import combinations, product
from collections import Counter
from pathlib import Path
import csv

N = 16
K = 4
MANDATORY_FOUR = (3, 7, 11, 15)  # zero-based positions in length-19 linearization
UNIVERSAL_FIVE = (3, 6, 9, 12, 15)


def rotate(word, offset):
    return word[offset:] + word[:offset]


def circular_factors(word):
    extended = word + word[:K-1]
    return tuple(extended[j:j+K] for j in range(N))


def is_de_bruijn(word):
    return len(word) == N and len(set(circular_factors(word))) == N


def distinct_factors(word, ell):
    return {word[j:j+ell] for j in range(len(word)-ell+1)}


def covered_factors(word, positions, ell):
    return {word[j:j+ell]
            for j in range(len(word)-ell+1)
            if any(j <= x < j+ell for x in positions)}


def attracts(word, positions, largest_length=None):
    if largest_length is None:
        largest_length = len(word)
    return all(distinct_factors(word, ell) == covered_factors(word, positions, ell)
               for ell in range(1, largest_length+1))


def covers_all_order_four_windows(positions):
    return all(any(j <= x < j+K for x in positions) for j in range(N))


def census():
    all_words = [''.join(bits) for bits in product('01', repeat=N)]
    rooted = [w for w in all_words if is_de_bruijn(w)]
    assert len(rooted) == 256
    necklaces = sorted({min(rotate(w,j) for j in range(N)) for w in rooted})
    assert len(necklaces) == 16
    assert all(len({rotate(w,j) for j in range(N)}) == N for w in necklaces)

    feasible_fours = [s for s in combinations(range(N+K-1), 4)
                      if covers_all_order_four_windows(s)]
    assert feasible_fours == [MANDATORY_FOUR], feasible_fours

    distribution = Counter()
    root_sizes = Counter()
    rows = []
    for cyclic in necklaces:
        success = []
        for cut in range(N):
            linear = rotate(cyclic, cut) + rotate(cyclic, cut)[:K-1]
            assert len(distinct_factors(linear, K)) == 16
            short_check = attracts(linear, MANDATORY_FOUR, K)
            full_check = attracts(linear, MANDATORY_FOUR)
            assert short_check == full_check
            assert attracts(linear, UNIVERSAL_FIVE, K)
            assert attracts(linear, UNIVERSAL_FIVE)
            if short_check:
                success.append(cut)
                root_sizes[4] += 1
            else:
                root_sizes[5] += 1
        distribution[len(success)] += 1
        rows.append((cyclic, len(success), ' '.join(map(str, success))))
    assert dict(distribution) == {8:4, 12:8, 16:4}, distribution
    assert dict(root_sizes) == {4:192, 5:64}, root_sizes
    return rows, distribution, root_sizes


def main():
    rows, counts, roots = census()
    table_path = Path(__file__).with_name('CENSUS.csv')
    with open(table_path, encoding='utf-8', newline='') as handle:
        reader = csv.reader(handle)
        observed = list(reader)
    assert observed == [['cycle', 'optimal_cut_count', 'zero_based_cuts']] + [list(map(str, r)) for r in rows]
    print('VERIFY_OK all_binary_16_words=65536 rooted_debruijn=256 cycles=16 '
          'unique_four_window_hittings=1 four_roots=192 five_roots=64 '
          'orbit_classes_8_12_16=4_8_4 universal_five=verified')


if __name__ == '__main__':
    main()
