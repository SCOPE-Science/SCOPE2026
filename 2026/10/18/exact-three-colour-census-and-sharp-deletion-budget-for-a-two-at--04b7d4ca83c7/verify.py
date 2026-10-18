#!/usr/bin/env python3
"""Independent finite checks for quantitative three-colour dependence splitting.

No external packages required. The tests distinguish a semantic split enumeration
from the closed-form row--column calculation and verify the finite 9-template
inclusion--exclusion identity for all column lengths.
"""
from collections import Counter, defaultdict
from itertools import product

COLORS = (0, 1, 2)
PAIRS = tuple(product(COLORS, repeat=2))


def semantic_satisfies(edges):
    """Enumerate actual split partitions, without using row--column normal form."""
    k = len(edges)
    for mask in range(1 << k):
        x_to_z, y_to_z = {}, {}
        valid = True
        for i, (x, y, z) in enumerate(edges):
            d, key = (x_to_z, x) if mask & (1 << i) else (y_to_z, y)
            if key in d and d[key] != z:
                valid = False
                break
            d[key] = z
        if valid:
            return True
    return False


def semantic_distance(edges):
    """Search all deletion subsets, applying the defining split semantics."""
    k = len(edges)
    for count in range(k + 1):
        for mask in range(1 << k):
            if mask.bit_count() != count:
                continue
            if semantic_satisfies([e for i, e in enumerate(edges) if not (mask & (1 << i))]):
                return count
    raise AssertionError("An empty retained team must satisfy the formula")


def row_column_distance(columns):
    return min(sum(a != b and a != r and b != s for a, b in columns)
               for r in COLORS for s in COLORS)


def predicted_count(n):
    return 3 * 7**n + 6 * 6**n - 21 * 5**n + 18 * 4**n - 5 * 3**n


def verify_inclusion_exclusion():
    universe = set(PAIRS)
    covers = [{(a, b) for a, b in universe if a == b or a == r or b == s}
              for r, s in product(COLORS, repeat=2)]
    assert sorted(Counter(map(len, covers)).items()) == [(6, 6), (7, 3)]
    parity_counts = defaultdict(lambda: [0, 0])
    for mask in range(1, 1 << len(covers)):
        intersection = set.intersection(*(covers[i] for i in range(9) if mask & (1 << i)))
        parity_counts[len(intersection)][0 if mask.bit_count() % 2 else 1] += 1
    assert dict(parity_counts) == {
        3: [187, 192], 4: [54, 36], 5: [6, 27], 6: [6, 0], 7: [3, 0]
    }, parity_counts
    print("NINE_TEMPLATE_INCLUSION_EXCLUSION_OK 511")


def verify_direct_semantics():
    for n in range(5):
        satisfied = 0
        maximum_distance = 0
        examined = 0
        for columns in product(PAIRS, repeat=n):
            edges = [(side, j, columns[j][side]) for j in range(n) for side in (0, 1)]
            formula_distance = row_column_distance(columns)
            direct_truth = semantic_satisfies(edges)
            assert direct_truth == (formula_distance == 0), (n, columns)
            if n <= 3 or not direct_truth:
                assert semantic_distance(edges) == formula_distance, (n, columns)
            satisfied += direct_truth
            maximum_distance = max(maximum_distance, formula_distance)
            examined += 1
        assert satisfied == predicted_count(n), (n, satisfied)
        assert maximum_distance == n // 3, (n, maximum_distance)
        assert examined == 9**n
        print(f"SEMANTIC_SPLITTING_OK n={n} colorings={examined} satisfied={satisfied} max_deletions={maximum_distance}")


def verify_extended_census():
    n = 5
    exact = sum(row_column_distance(c) == 0 for c in product(PAIRS, repeat=n))
    assert exact == predicted_count(n) == 48669
    for n in range(1, 20):
        balanced = [i % 3 for i in range(n)]
        columns = [(a, (a + 1) % 3) for a in balanced]
        assert row_column_distance(columns) == n // 3
    print("EXTENDED_COUNT_AND_SHARPNESS_OK n=5 n_up_to=19")


if __name__ == "__main__":
    verify_inclusion_exclusion()
    verify_direct_semantics()
    verify_extended_census()
    print("THREE_COLOR_DEPENDENCE_QUANTITATIVE_THEOREM_OK")
