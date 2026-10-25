#!/usr/bin/env python3
"""Exact full census for seven-column binary three-dimensional coverage depth.

This uses only the Python standard library. A code is represented by a
seven-column multiset of vectors 0,...,7 in F_2^3. All comparisons use
fractions, and two distinct expectation formulas are checked on every code.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, combinations_with_replacement, product
from math import comb, factorial
from pathlib import Path

N = 7
POINTS = tuple(range(1, 8))
LINES = tuple(
    tuple(v for v in POINTS if ((v & normal).bit_count() & 1) == 0)
    for normal in POINTS
)


def span_size(vectors):
    span = {0}
    for v in vectors:
        span |= {u ^ v for u in tuple(span)}
    return len(span)


def expectation_subspaces(multiplicities):
    """Subspace-lattice Moebius inclusion-exclusion plus geometric series."""
    a0 = multiplicities[0]
    result = sum(
        (Fraction(N, N - a0 - sum(multiplicities[v] for v in line))
         for line in LINES), Fraction(0)
    )
    result -= 2 * sum(
        (Fraction(N, N - a0 - multiplicities[v]) for v in POINTS),
        Fraction(0)
    )
    result += 8 * Fraction(N, N - a0)
    return result


def expectation_information_sets(columns):
    """Independent coupon-order/subset-rank calculation."""
    harmonic = sum((Fraction(1, j) for j in range(1, N + 1)), Fraction(0))
    result = N * harmonic
    for size in range(3, N):
        spanning = sum(
            span_size(columns[i] for i in indices) == 8
            for indices in combinations(range(N), size)
        )
        result -= Fraction(spanning, comb(N - 1, size))
    return result


def normalized_counts(columns):
    return tuple(columns.count(v) for v in range(8))


def main():
    assert len(LINES) == 7 and all(len(line) == 3 for line in LINES)
    assert len(set(LINES)) == 7
    all_profiles = 0
    full_rank = 0
    scores = Counter()
    labeled_scores = Counter()
    by_class = defaultdict(list)
    values_by_profile = {}
    for cols in combinations_with_replacement(range(8), N):
        all_profiles += 1
        if span_size(cols) != 8:
            continue
        full_rank += 1
        counts = normalized_counts(cols)
        exact_a = expectation_subspaces(counts)
        exact_b = expectation_information_sets(cols)
        assert exact_a == exact_b, (cols, exact_a, exact_b)
        values_by_profile[cols] = exact_a
        scores[exact_a] += 1
        labeled_count = factorial(N)
        for c in counts:
            labeled_count = labeled_count // factorial(c)
        labeled_scores[exact_a] += labeled_count
        zeros = counts[0]
        support = sum(bool(counts[i]) for i in POINTS)
        by_class[(zeros, support)].append((exact_a, cols))
    assert all_profiles == comb(14, 7) == 3432
    assert full_rank == 2696
    assert sum(scores.values()) == full_rank
    assert sum(labeled_scores.values()) == (128-1)*(128-2)*(128-4) == 1984248
    direct_labeled = Counter()
    for ordered in product(range(8), repeat=N):
        canonical = tuple(sorted(ordered))
        if canonical in values_by_profile:
            direct_labeled[values_by_profile[canonical]] += 1
    assert direct_labeled == labeled_scores
    # Left multiplication by GL(3,2) acts freely on full-rank matrices;
    # each row space (linear code) has exactly 168 generator bases.
    assert all(count % 168 == 0 for count in labeled_scores.values())
    assert sum(labeled_scores.values()) // 168 == 11811

    simplex = tuple(range(1, 8))
    min_score = min(scores)
    assert min_score == Fraction(47, 12)
    assert scores[min_score] == 1
    assert values_by_profile[simplex] == min_score

    next_score = min(x for x in scores if x > min_score)
    assert next_score == Fraction(17, 4)
    assert scores[next_score] == 42
    minimizers = [cols for cols, score in values_by_profile.items() if score == next_score]
    expected_minimizers = {
        tuple(sorted(tuple(v for v in POINTS if v != missing) + (duplicate,)))
        for missing in POINTS for duplicate in POINTS if duplicate != missing
    }
    assert len(expected_minimizers) == 42
    assert set(minimizers) == expected_minimizers

    assert by_class[(0, 5)] and min(v for v, _ in by_class[(0, 5)]) == Fraction(67, 15)
    assert by_class[(1, 6)] and min(v for v, _ in by_class[(1, 6)]) == Fraction(287, 60)
    assert next_score - min_score == Fraction(1, 3)

    # Explicitly enumerate all invertible binary linear maps, checking a
    # single orbit of the 42 ordered (missing, duplicate) pairs.
    def mat_action(rows, vector):
        return sum(((vector & rows[i]).bit_count() & 1) << i for i in range(3))
    invertible = [
        rows for rows in __import__('itertools').product(range(8), repeat=3)
        if len({mat_action(rows, v) for v in range(8)}) == 8
    ]
    assert len(invertible) == 168
    orbit = {(mat_action(rows, 1), mat_action(rows, 2)) for rows in invertible}
    assert len(orbit) == 42
    assert orbit == {(a, b) for a in POINTS for b in POINTS if a != b}

    csv_lines = ["expectation,profile_count,ordered_full_rank_matrices,binary_linear_codes"]
    for value in sorted(scores):
        csv_lines.append(f"{value},{scores[value]},{labeled_scores[value]},{labeled_scores[value] // 168}")
    csv_bytes = ("\n".join(csv_lines) + "\n").encode("ascii")
    csv_path = Path(__file__).with_name("coverage_depth_spectrum.csv")
    csv_path.write_bytes(csv_bytes)
    mean = sum((v * count for v, count in labeled_scores.items()), Fraction(0)) / sum(labeled_scores.values())
    second_moment = sum((v * v * count for v, count in labeled_scores.items()), Fraction(0)) / sum(labeled_scores.values())
    variance = second_moment - mean * mean
    assert variance > 0
    print(f"TOTAL_MULTISETS {all_profiles}")
    print(f"FULL_RANK {full_rank}")
    print(f"ORDERED_FULL_RANK_MATRICES {sum(labeled_scores.values())}")
    print(f"DISTINCT_BINARY_LINEAR_CODES {sum(labeled_scores.values()) // 168}")
    print(f"DISTINCT_EXPECTATIONS {len(scores)}")
    print(f"ENSEMBLE_MEAN {mean}")
    print(f"ENSEMBLE_VARIANCE {variance}")
    print(f"SIMPLEX_ORDERED {labeled_scores[min_score]}")
    print(f"SECOND_ORDERED {labeled_scores[next_score]}")
    print(f"SIMPLEX_BINARY_LINEAR_CODES {labeled_scores[min_score] // 168}")
    print(f"SECOND_BINARY_LINEAR_CODES {labeled_scores[next_score] // 168}")
    print(f"SIMPLEX_EXPECTATION {min_score} COUNT {scores[min_score]}")
    print(f"SECOND_EXPECTATION {next_score} COUNT {scores[next_score]}")
    print(f"SHARP_GAP {next_score - min_score}")
    print("SECOND_EQUALITY_ALL_42_MISSING_DUPLICATE_PROFILES VERIFIED")
    print("GL3_F2_ORDER 168 TRANSITIVE_ON_ORDERED_DISTINCT_NONZERO_PAIRS 42")
    for (zeros, support) in sorted(by_class):
        vals = by_class[(zeros, support)]
        best = min(v for v, _ in vals)
        print(f"CLASS zero={zeros} support={support} profiles={len(vals)} min={best} min_count={sum(v == best for v, _ in vals)}")
    print(f"SPECTRUM_CSV_BYTES {len(csv_bytes)}")
    print("DIRECT_ENUMERATION_AGREES_FOR_ALL_2097152_ORDERED_MATRICES")
    print("TWO_INDEPENDENT_FORMULAS_AGREE_FOR_ALL_2696_PROFILES")
    print("VERIFY_OK")

if __name__ == '__main__':
    main()
