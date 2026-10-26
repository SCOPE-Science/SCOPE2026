"""Exact certificate for single-taxon phylogenetic conservation on binary trees.
Uses only the Python standard library. All checks are finite exact arithmetic.
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import accumulate
import json

LEAF = ()

@lru_cache(None)
def leaf_count(tree):
    return 1 if tree == LEAF else leaf_count(tree[0]) + leaf_count(tree[1])

@lru_cache(None)
def binary_shapes(n):
    """All unordered rooted full-binary tree shapes with n leaves.
    Recursive child-pair partition is exhaustive, and sorting removes swaps.
    """
    if n == 1:
        return (LEAF,)
    found = set()
    for left_n in range(1, n // 2 + 1):
        right_n = n - left_n
        for left in binary_shapes(left_n):
            for right in binary_shapes(right_n):
                if left_n == right_n and left > right:
                    continue
                found.add((left, right))
    return tuple(sorted(found))

def labeled_paths(tree, prefix=""):
    """Leaf name and sizes of descendant leaf clades along each root-to-leaf edge."""
    if tree == LEAF:
        return [(prefix or "root", ())]
    result = []
    for label, child in (("L", tree[0]), ("R", tree[1])):
        for name, profile in labeled_paths(child, prefix + label):
            result.append((name, (leaf_count(child),) + profile))
    return result

def coefficient_vector(path, n):
    counts = Counter(path)
    return tuple(counts[k] for k in range(1, n))

def partial_sums(profile):
    return tuple(accumulate(profile))

def cumulative_dominates(first, second):
    return all(a >= b for a, b in zip(partial_sums(first), partial_sums(second)))

def universally_certified_profiles(tree):
    n = leaf_count(tree)
    profiles = sorted({coefficient_vector(path, n) for _, path in labeled_paths(tree)})
    return [u for u in profiles if all(cumulative_dominates(u, v) for v in profiles)]

def expected_marginal_direct(tree, name, q):
    """Independent subset enumeration, separate from clade-profile identity."""
    p = 1 - q
    paths = dict(labeled_paths(tree))
    names = list(paths)
    assert name in paths
    others = [v for v in names if v != name]
    edges_by_leaf = {}
    # An edge of the rooted tree is uniquely identified by its child prefix.
    for v in names:
        edges_by_leaf[v] = {v[:k] for k in range(1, len(v) + 1)}
    target_edges = edges_by_leaf[name]
    result = Fraction(0)
    for mask in range(1 << len(others)):
        kept = {others[i] for i in range(len(others)) if mask & (1 << i)}
        probability = p ** len(kept) * q ** (len(others) - len(kept))
        all_edges = set().union(*(edges_by_leaf[v] for v in kept)) if kept else set()
        additional = len(target_edges - all_edges)
        result += q * probability * additional
    return result

def expected_marginal_profile(tree, name, q):
    path = dict(labeled_paths(tree))[name]
    return sum((q ** count for count in path), Fraction(0))

def verify():
    census = []
    exceptional = None
    for n in range(2, 9):
        trees = binary_shapes(n)
        no_common_cumulative = []
        for tree in trees:
            if not universally_certified_profiles(tree):
                no_common_cumulative.append(tree)
        census.append({"leaves": n,
                       "nonisomorphic_rooted_full_binary_shapes": len(trees),
                       "without_cumulative_dominating_leaf": len(no_common_cumulative)})
        if n < 8:
            assert not no_common_cumulative
        else:
            assert len(no_common_cumulative) == 1
            exceptional = no_common_cumulative[0]
    assert exceptional is not None
    assert str(exceptional) == '(((), ((), ())), ((), (((), ()), ((), ()))))'
    paths = dict(labeled_paths(exceptional))
    by_profile = {}
    for name, path in paths.items():
        by_profile.setdefault(path, []).append(name)
    profiles = set(by_profile)
    assert profiles == {(5, 1), (3, 1), (3, 2, 1), (5, 4, 2, 1)} or \
           profiles == {(1, 5), (1, 3), (1, 2, 3), (1, 2, 4, 5)}
    # Root-to-leaf order is descending clade size; all profiles include a pendant 1.
    assert profiles == {(3, 1), (3, 2, 1), (5, 1), (5, 4, 2, 1)}
    left = (3, 2, 1)
    right = (5, 4, 2, 1)
    assert any(left == z for z in profiles)
    assert any(right == z for z in profiles)
    # On (0,1), left dominates the short leaf in its own 3-clade;
    # right dominates the short leaf in the 5-clade.
    assert set(profiles) - {left, right} == {(3, 1), (5, 1)}
    assert set(left) > set((3, 1)) and set(right) > set((5, 1))
    # Right - left = q^4 + q^5 - q^3 = q^3(q^2+q-1).
    assert Counter(right) - Counter(left) == Counter({4: 1, 5: 1})
    assert Counter(left) - Counter(right) == Counter({3: 1})
    direct_tests = []
    for q in (Fraction(1, 4), Fraction(1, 2), Fraction(3, 4)):
        for name, path in paths.items():
            by_clades = expected_marginal_profile(exceptional, name, q)
            by_subsets = expected_marginal_direct(exceptional, name, q)
            assert by_clades == by_subsets
        left_gain = sum((q ** k for k in left), Fraction(0))
        right_gain = sum((q ** k for k in right), Fraction(0))
        assert (right_gain > left_gain) == (q == Fraction(3, 4))
        direct_tests.append({"extinction_probability": str(q),
                             "right_minus_left": str(right_gain - left_gain),
                             "all_eight_leaves_checked_by_subset_enumeration": True})
    return {"census": census,
            "exceptional_shape": str(exceptional),
            "distinct_leaf_profiles_clade_sizes_root_to_tip": sorted([list(v) for v in profiles]),
            "competing_profiles": {"high_survival": list(left), "low_survival": list(right)},
            "difference_low_minus_high": "q^3*(q^2+q-1)",
            "unique_extinction_threshold": "(sqrt(5)-1)/2",
            "independent_checks": direct_tests,
            "status": "VERIFY_OK"}

if __name__ == '__main__':
    print(json.dumps(verify(), sort_keys=True, ensure_ascii=False, separators=(',', ':')))
