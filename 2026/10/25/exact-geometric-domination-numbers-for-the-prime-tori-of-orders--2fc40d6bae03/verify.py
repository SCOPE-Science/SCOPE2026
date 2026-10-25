#!/usr/bin/env python3
"""Exact finite checks for two prime-order discrete-torus domination values.

A line in F_p^2 is the set {a + t(b-a): t in F_p} for distinct a,b.
The mathematical lower bounds are proved in RESULT.md. This program checks
the explicit upper-bound witnesses and exhaustively cross-checks that no
five-point set dominates F_7^2.
Only the Python standard library is required.
"""
from itertools import combinations
from math import comb


def point_index(p, point):
    x, y = point
    return x * p + y


def pair_line_mask(p, i, j):
    ax, ay = divmod(i, p)
    bx, by = divmod(j, p)
    dx = (bx - ax) % p
    dy = (by - ay) % p
    if dx == 0 and dy == 0:
        raise ValueError("a line requires two distinct points")
    mask = 0
    for t in range(p):
        x = (ax + t * dx) % p
        y = (ay + t * dy) % p
        mask |= 1 << point_index(p, (x, y))
    return mask


def pair_masks(p):
    return {
        (i, j): pair_line_mask(p, i, j)
        for i in range(p * p)
        for j in range(i + 1, p * p)
    }


def covers_torus(p, witness, masks=None):
    if len(set(witness)) != len(witness):
        return False
    if masks is None:
        masks = pair_masks(p)
    union = 0
    for i, j in combinations(sorted(point_index(p, q) for q in witness), 2):
        union |= masks[(i, j)]
    return union == (1 << (p * p)) - 1


def no_five_point_dominator_for_seven(masks):
    p = 7
    full = (1 << (p * p)) - 1
    tested = 0
    for candidate in combinations(range(p * p), 5):
        tested += 1
        union = 0
        for i, j in combinations(candidate, 2):
            union |= masks[(i, j)]
            if union == full:
                raise AssertionError(
                    f"unexpected five-point dominating set: {candidate}"
                )
    assert tested == comb(49, 5) == 1_906_884
    return tested


def main():
    witness5 = [(0, 0), (0, 1), (1, 0), (1, 2), (3, 2)]
    witness7 = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (5, 2)]

    masks5 = pair_masks(5)
    masks7 = pair_masks(7)
    assert covers_torus(5, witness5, masks5)
    assert covers_torus(7, witness7, masks7)

    # Counting upper bound for sets of at most four points:
    # s + binom(s,2)(p-2), maximized at s=4 for these p.
    assert 4 + comb(4, 2) * (5 - 2) < 5 * 5
    assert 4 + comb(4, 2) * (7 - 2) < 7 * 7

    tested = no_five_point_dominator_for_seven(masks7)
    print("CHECKS_PASSED")
    print("T5_witness_size=5; all_25_points_covered=True")
    print("T7_witness_size=6; all_49_points_covered=True")
    print(f"T7_five_subsets_exhausted={tested}; dominating_five_sets=0")
    print("small-set_counting_bounds=True")


if __name__ == "__main__":
    main()
