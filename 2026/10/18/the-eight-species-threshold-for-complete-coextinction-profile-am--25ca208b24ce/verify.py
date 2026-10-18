"""Exact exhaustive census for the extinction-count inverse problem.

Run: python3 verify.py > certificate.json
Requires only Python 3 standard library.
"""
import itertools
import json
from collections import Counter, defaultdict


def neighborhood_columns(rows, n):
    return tuple(sum(((row >> j) & 1) << i for i, row in enumerate(rows)) for j in range(n))


def connected(rows, n):
    m = len(rows)
    seen_rows = {0}
    seen_cols = set()
    while True:
        new_cols = seen_cols | {j for i in seen_rows for j in range(n) if rows[i] & (1 << j)}
        new_rows = seen_rows | {i for j in new_cols for i, r in enumerate(rows) if r & (1 << j)}
        if new_cols == seen_cols and new_rows == seen_rows:
            return len(seen_rows) == m and len(seen_cols) == n
        seen_rows, seen_cols = new_rows, new_cols


def canonical(rows, n):
    # The two guilds have different ecological roles: permute within, never across.
    best = None
    for perm in itertools.permutations(range(n)):
        trial = tuple(sorted(sum(((row >> old) & 1) << new for new, old in enumerate(perm)) for row in rows))
        if best is None or trial < best:
            best = trial
    return best


def histogram(rows, n):
    # H[k,y] = number of k-pollinator survivor sets leaving y plants viable.
    counts = Counter()
    for subset in range(1 << n):
        y = sum(bool(row & subset) for row in rows)
        counts[(subset.bit_count(), y)] += 1
    return tuple(sorted((k, y, count) for (k, y), count in counts.items()))


def group_degree_profiles(rows, n):
    return (tuple(sorted(r.bit_count() for r in rows)),
            tuple(sorted(c.bit_count() for c in neighborhood_columns(rows, n))))


def valid(rows, n):
    if len(set(rows)) < len(rows):
        return False
    cols = neighborhood_columns(rows, n)
    if not all(cols) or len(set(cols)) < n:
        return False
    return connected(rows, n)


def classes(m, n):
    # Twin-free excludes m>2^n-1 and n>2^m-1 immediately.
    if m > (1 << n) - 1 or n > (1 << m) - 1:
        return []
    # Distinct nonempty plant neighborhoods, in row-sorted order.
    output = []
    for rows in itertools.combinations(range(1, 1 << n), m):
        if not valid(rows, n):
            continue
        if rows == canonical(rows, n):
            output.append(rows)
    return output


def four_cycles(rows):
    return sum(((a & b).bit_count() * ((a & b).bit_count()-1)) // 2
               for a, b in itertools.combinations(rows, 2))


def direct_histogram(rows, n):
    # Independent calculation by deleting pollinators and removing isolated plants.
    result = Counter()
    for deletion in itertools.product((0, 1), repeat=n):
        present = {j for j, is_lost in enumerate(deletion) if not is_lost}
        remaining = 0
        for row in rows:
            if any(row & (1 << j) for j in present):
                remaining += 1
        result[(len(present), remaining)] += 1
    return tuple(sorted((k, y, v) for (k, y), v in result.items()))


def explicitly_isomorphic(a, b, n):
    # Independent of the canonical-class enumeration used for minimality.
    for perm in itertools.permutations(range(n)):
        transformed = sorted(sum(((r >> j) & 1) << perm[j] for j in range(n)) for r in a)
        if tuple(transformed) == tuple(sorted(b)):
            return True
    return False


def main():
    data = {'census': [], 'first_collision_total': None}
    max_size = 8
    for total in range(2, max_size + 1):
        for m in range(1, total):
            n = total - m
            fs = classes(m, n)
            buckets = defaultdict(list)
            for rows in fs:
                buckets[histogram(rows, n)].append(rows)
            excess = sum(len(b) - 1 for b in buckets.values())
            collisions = [b for b in buckets.values() if len(b) > 1]
            # Full direct independent pairwise check at all smaller orders.
            if total < 8:
                for pair in collisions:
                    for a, b in itertools.combinations(pair, 2):
                        assert explicitly_isomorphic(a, b, n)
            data['census'].append({'plants': m, 'pollinators': n,
                                    'classes': len(fs), 'collision_excess': excess,
                                    'collision_classes': len(collisions)})
            if collisions and data['first_collision_total'] is None:
                data['first_collision_total'] = total
    A = (1, 3, 6, 13)
    B = (1, 3, 6, 14)
    assert valid(A, 4) and valid(B, 4)
    assert A != B and canonical(A, 4) != canonical(B, 4)
    assert not explicitly_isomorphic(A, B, 4)
    assert histogram(A, 4) == histogram(B, 4)
    assert histogram(A, 4) == direct_histogram(A, 4) == direct_histogram(B, 4)
    assert group_degree_profiles(A, 4) == group_degree_profiles(B, 4)
    assert four_cycles(A) == 0 and four_cycles(B) == 1
    assert data['first_collision_total'] == 8
    assert all(t['collision_excess'] == 0 for t in data['census'] if t['plants'] + t['pollinators'] < 8)
    data['witness'] = {'plants': 4, 'pollinators': 4,
                       'matrix_A_row_masks': list(A), 'matrix_B_row_masks': list(B),
                       'degree_multisets': [list(s) for s in group_degree_profiles(A, 4)],
                       'cycle4_count_A': four_cycles(A), 'cycle4_count_B': four_cycles(B),
                       'common_H_k_y_count': [list(s) for s in histogram(A, 4)],
                       'direct_exhaustive_subsets_per_network': 16,
                       'side_preserving_isomorphic': False}
    data['checks'] = 'exact integer census; all checks passed'
    print(json.dumps(data, ensure_ascii=False, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
