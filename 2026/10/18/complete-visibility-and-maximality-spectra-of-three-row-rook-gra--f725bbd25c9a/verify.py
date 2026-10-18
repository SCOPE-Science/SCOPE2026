"""Standalone finite checks of maximal mutual-visibility sets in K_3 square K_n.
Python 3 standard library only.  Run: python3 verify.py
"""
from collections import Counter
from itertools import permutations, product
from math import comb, factorial


def direct_visible(cols):
    """Check shortest-path visibility directly in the Cartesian rook graph."""
    chosen = {(r, c) for c, b in enumerate(cols) for r in range(3) if b & (1 << r)}
    for (r, c) in chosen:
        for (s, d) in chosen:
            if c != d and r != s:
                # Precisely two graph-geodesics of length 2.
                if (r, d) in chosen and (s, c) in chosen:
                    return False
    return True


def c4_free(cols):
    used = set()
    for bits in cols:
        for a in range(3):
            for b in range(a + 1, 3):
                if bits & (1 << a) and bits & (1 << b):
                    if (a, b) in used:
                        return False
                    used.add((a, b))
    return True


def maximal(cols, predicate):
    if not predicate(cols):
        return False
    for c in range(len(cols)):
        for r in range(3):
            if not cols[c] & (1 << r):
                newer = cols[:c] + (cols[c] | (1 << r),) + cols[c + 1 :]
                if predicate(newer):
                    return False
    return True


def canonical(cols):
    variants = []
    for order in permutations(range(3)):
        mapped = [sum(1 << order[i] for i in range(3) if b & (1 << i)) for b in cols]
        variants.append(tuple(sorted(mapped)))
    return min(variants)


def p_le3(k):
    return sum(1 for a in range(k + 1) for b in range(a, k + 1) if k - a - b >= b)


def expected(n):
    return {n + 2: n * 3 ** (n - 1) + 3 * n * (n - 1),
            n + 3: n * (n - 1) * (n - 2) * 3 ** (n - 3)}


def polynomial_coefficients(n):
    """Independently form coefficients by expanding the four closed terms."""
    expected = Counter()
    for j in range(n + 1):
        expected[j] += comb(n, j) * 3**j
    for j in range(n):
        coefficient = comb(n - 1, j) * 3**j
        expected[j + 2] += 3 * n * coefficient
        expected[j + 3] += n * coefficient
    for j in range(n - 1):
        expected[j + 4] += 3 * n * (n - 1) * comb(n - 2, j) * 3**j
    for j in range(n - 2):
        expected[j + 6] += n * (n - 1) * (n - 2) * comb(n - 3, j) * 3**j
    return dict(expected)


def main():
    checked = 0
    shortest_path_checked = 0
    for n in range(3, 8):
        counts = Counter()
        all_valid_by_size = Counter()
        orbits = set()
        by_families = Counter()
        for cols in product(range(8), repeat=n):
            checked += 1
            valid = c4_free(cols)
            if n <= 5:
                assert direct_visible(cols) == valid
                shortest_path_checked += 1
            if valid:
                all_valid_by_size[sum(x.bit_count() for x in cols)] += 1
            if not maximal(cols, c4_free):
                continue
            assert valid
            assert all(x != 0 for x in cols)
            counts[sum(x.bit_count() for x in cols)] += 1
            occupancy = Counter(x.bit_count() for x in cols)
            if occupancy[3] == 1:
                by_families['one_triple'] += 1
            elif occupancy[2] == 2:
                by_families['two_double'] += 1
            elif occupancy[2] == 3:
                by_families['three_double'] += 1
            else:
                raise AssertionError(('unclassified maximal set', n, cols))
            if n <= 5:
                orbits.add(canonical(cols))
                assert maximal(cols, direct_visible)
        assert dict(all_valid_by_size) == polynomial_coefficients(n), (n, all_valid_by_size, polynomial_coefficients(n))
        assert dict(counts) == expected(n), (n, counts, expected(n))
        assert by_families == {
            'one_triple': n * 3 ** (n - 1),
            'two_double': 3 * n * (n - 1),
            'three_double': n * (n - 1) * (n - 2) * 3 ** (n - 3)
        }, (n,by_families)
        if n <= 5:
            assert len(orbits) == p_le3(n-1) + 1 + p_le3(n-3), (n,orbits)
        print('n', n, 'maximal_size_counts', sorted(counts.items()),
              'families', dict(sorted(by_families.items())),
              'orbits', len(orbits) if n <= 5 else 'not_computed')
    print('VERIFICATION_OK candidates=' + str(checked) +
          ' direct_geodesic_candidates=' + str(shortest_path_checked))


if __name__ == '__main__':
    main()
