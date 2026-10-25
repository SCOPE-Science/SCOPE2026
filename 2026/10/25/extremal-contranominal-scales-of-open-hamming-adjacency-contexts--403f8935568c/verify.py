"""Independent finite enumerator for maximum contranominal scales of open Hamming adjacency.

Usage: python3 verify.py. Requires only Python's standard library.
"""
from itertools import combinations, product
from math import comb
import random


def predicted_dimension(q, d):
    return q if d <= 2 else max(q, 4)


def predicted_count(q, d):
    if q >= 5:
        return d * q ** (d - 1)
    if q == 4:
        return (d * 4 ** (d - 1)
                + (36 * d * (d - 1) * 4 ** (d - 2) if d >= 2 else 0)
                + (432 * comb(d, 3) * 4 ** (d - 3) if d >= 3 else 0))
    if q in (2, 3) and d >= 3:
        return 2 * comb(d, 3) * q ** (d - 3) * comb(q, 2) ** 3
    return None


def distance(x, y):
    return sum(a != b for a, b in zip(x, y))


def family(q, d, w, words):
    distances = sorted(distance(words[i], words[j]) for i, j in combinations(w, 2))
    if len(w) >= 5:
        assert len(w) == q and distances == [1] * comb(q, 2)
        return 'full_coordinate_line'
    if len(w) == 4:
        if distances == [1] * 6:
            assert q == 4
            return 'full_coordinate_line'
        if distances == [1, 1, 2, 2, 2, 2]:
            assert q == 4
            return 'two_parallel_pairs'
        if distances == [2] * 6:
            return 'parity_tetrahedron'
        raise AssertionError('Unexpected four-scale type ' + str(distances))
    return 'small_dimension'


def check(q, d):
    words = list(product(range(q), repeat=d))
    n = len(words)
    neis = [sum(1 << j for j, y in enumerate(words) if distance(x, y) == 1)
            for x in words]
    full_mask = (1 << n) - 1
    k = predicted_dimension(q, d)
    found = 0
    bytype = {}
    tested = 0
    for support in combinations(range(n), k):
        tested += 1
        witnesses = []
        for i in support:
            can = full_mask
            for j in support:
                if j != i:
                    can &= neis[j]
            can &= full_mask ^ neis[i]
            if not can:
                break
            witnesses.append(can)
        else:
            found += 1
            if k >= 4:
                assert all(w.bit_count() == 1 for w in witnesses), (q, d, support)
                indices = [w.bit_length() - 1 for w in witnesses]
                assert len(set(indices)) == k
                for i, yi in zip(support, indices):
                    for j, yj in zip(support, indices):
                        assert (distance(words[i], words[yj]) == 1) == (i != j)
                t = family(q, d, support, words)
                bytype[t] = bytype.get(t, 0) + 1
    expected = predicted_count(q, d)
    if expected is not None:
        assert found == expected, (q, d, found, expected)
        if q == 4:
            assert bytype.get('full_coordinate_line', 0) == d * q ** (d - 1)
            assert bytype.get('two_parallel_pairs', 0) == (36 * d * (d - 1) * q ** (d - 2) if d >= 2 else 0)
            assert bytype.get('parity_tetrahedron', 0) == (432 * comb(d, 3) * q ** (d - 3) if d >= 3 else 0)
        if q <= 3 and d >= 3:
            assert bytype == {'parity_tetrahedron': expected}
        if q >= 5:
            assert bytype == {'full_coordinate_line': expected}
    # Exhaustively rule out the first forbidden dimension when feasible.
    if comb(n, k + 1) <= 3_000_000:
        for support in combinations(range(n), k + 1):
            for i in support:
                can = full_mask
                for j in support:
                    if j != i:
                        can &= neis[j]
                if not (can & (full_mask ^ neis[i])):
                    break
            else:
                raise AssertionError('Found scale above predicted dimension: ' + repr((q,d,support)))
    print('CASE', q, d, 'max_dim', k, 'support_sets', found, 'tested_max', tested, 'types', bytype)
    return tested


def sampling():
    q, d, k = 5, 3, 5
    words = list(product(range(q), repeat=d))
    n = len(words)
    nm = [sum(1 << j for j, y in enumerate(words) if distance(x, y) == 1)
          for x in words]
    full = (1 << n) - 1
    rng = random.Random(20261018)
    for _ in range(25000):
        ss = tuple(sorted(rng.sample(range(n), k)))
        ok = True
        for i in ss:
            mask = full
            for j in ss:
                if i != j:
                    mask &= nm[j]
            if not mask & (full ^ nm[i]):
                ok = False
                break
        if ok:
            assert family(q, d, ss, words) == 'full_coordinate_line'
    print('SAMPLED', q, d, 'supports', 25000, 'PASS')

if __name__ == '__main__':
    total = 0
    for params in [(2,1),(2,2),(2,3),(2,4),(3,1),(3,2),(3,3),(3,4),
                   (4,1),(4,2),(4,3),(5,1),(5,2),(6,2)]:
        total += check(*params)
    sampling()
    print('VERIFY_OK candidates', total, 'upper_bounds=PASS witness_uniqueness=PASS extremal_counts=PASS geometric_classes=PASS')
