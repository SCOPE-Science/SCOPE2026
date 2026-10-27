from fractions import Fraction
from math import comb
from collections import Counter

LEAF = None


def shapes(n, cache=None):
    if cache is None:
        cache = {}
    if n in cache:
        return cache[n]
    if n == 1:
        cache[n] = [LEAF]
    else:
        cache[n] = [
            (left, right)
            for i in range(1, n)
            for left in shapes(i, cache)
            for right in shapes(n - i, cache)
        ]
    return cache[n]


def clade_masks(tree, start=0):
    """Return the node mask, all node masks in preorder, and next leaf index."""
    if tree is LEAF:
        mask = 1 << start
        return mask, [mask], start + 1
    left_mask, left_nodes, middle = clade_masks(tree[0], start)
    right_mask, right_nodes, end = clade_masks(tree[1], middle)
    mask = left_mask | right_mask
    return mask, [mask] + left_nodes + right_nodes, end


def variance_curve(tree, n):
    _, all_nodes, _ = clade_masks(tree)
    edge_clades = all_nodes[1:]  # the root itself has no incoming edge
    sums = [0] * (n + 1)
    sums_sq = [0] * (n + 1)
    counts = [0] * (n + 1)
    for sample in range(1 << n):
        k = sample.bit_count()
        pd = sum(bool(sample & clade) for clade in edge_clades)
        sums[k] += pd
        sums_sq[k] += pd * pd
        counts[k] += 1
    return [
        Fraction(sums_sq[k], counts[k]) - Fraction(sums[k], counts[k]) ** 2
        for k in range(n + 1)
    ]


def variance_by_clade_formula(tree, n, k):
    _, all_nodes, _ = clade_masks(tree)
    edge_clades = all_nodes[1:]
    denominator = comb(n, k)
    avoid = [
        Fraction(comb(n - clade.bit_count(), k) if k <= n - clade.bit_count() else 0, denominator)
        for clade in edge_clades
    ]
    variance = sum((q * (1 - q) for q in avoid), Fraction(0))
    for i, left in enumerate(edge_clades):
        for j in range(i + 1, len(edge_clades)):
            right = edge_clades[j]
            union_size = (left | right).bit_count()
            joint_avoid_count = comb(n - union_size, k) if k <= n - union_size else 0
            covariance = Fraction(joint_avoid_count, denominator) - avoid[i] * avoid[j]
            variance += 2 * covariance
    return variance


def is_unimodal(values):
    """A sequence is unimodal if it weakly rises to some peak, then falls."""
    return any(
        all(values[i] <= values[i + 1] for i in range(peak))
        and all(values[i] >= values[i + 1] for i in range(peak, len(values) - 1))
        for peak in range(len(values))
    )


def main():
    expected_counts = {1: 1, 2: 1, 3: 2, 4: 5, 5: 14, 6: 42, 7: 132, 8: 429, 9: 1430}
    for n, expected in expected_counts.items():
        all_shapes = shapes(n)
        assert len(all_shapes) == expected
        for tree in all_shapes:
            assert is_unimodal(variance_curve(tree, n)), f"non-unimodal tree below 10 leaves: n={n}, tree={tree}"

    leaf = LEAF
    cherry = (leaf, leaf)
    four = (cherry, cherry)
    eight = (four, four)
    witness = (eight, cherry)
    _, witness_nodes, _ = clade_masks(witness)
    edge_clades = witness_nodes[1:]
    assert len(edge_clades) == 18
    assert Counter(mask.bit_count() for mask in edge_clades) == {1: 10, 2: 5, 4: 2, 8: 1}
    curve = variance_curve(witness, 10)
    expected_curve = [
        Fraction(0), Fraction(16, 25), Fraction(136, 225), Fraction(28, 45),
        Fraction(1306, 2205), Fraction(1916, 3969), Fraction(3884, 11025),
        Fraction(2, 9), Fraction(8, 81), Fraction(0), Fraction(0),
    ]
    assert curve == expected_curve
    assert all(curve[k] == variance_by_clade_formula(witness, 10, k) for k in range(11))
    assert not is_unimodal(curve)
    assert curve[1] > curve[2] < curve[3] > curve[4]

    print("EXACT_CHECK_OK")
    print("rooted_plane_shapes_checked_by_leaf_count", expected_counts)
    print("all_shapes_through_9_leaves_unimodal", True)
    print("10_leaf_witness_edge_clade_size_counts", {1: 10, 2: 5, 4: 2, 8: 1})
    print("10_leaf_witness_variance_curve", [str(x) for x in curve])
    print("strict_valley_and_rebound", curve[1] > curve[2] < curve[3] > curve[4])


if __name__ == "__main__":
    main()
