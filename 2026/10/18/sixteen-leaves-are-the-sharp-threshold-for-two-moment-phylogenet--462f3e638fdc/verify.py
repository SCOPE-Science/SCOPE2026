#!/usr/bin/env python3
"""Exact unit-edge rooted phylogenetic-diversity moment fingerprint census.

Run: python3 verify.py
No third-party dependencies. All arithmetic is integral except rational display.
"""
import collections
import functools
import itertools
import json
import math

@functools.lru_cache(None)
def shapes(n):
    """Canonical unordered full rooted binary shapes with n tip vertices."""
    if n == 1:
        return ((),)
    result = set()
    for a in range(1, n // 2 + 1):
        b = n - a
        for x in shapes(a):
            for y in shapes(b):
                result.add((x, y) if x <= y else (y, x))
    return tuple(sorted(result))

def all_clades(tree, first=0):
    """Return tip-mask and masks of descendant tip sets, INCLUDING root."""
    if not tree:
        mask = 1 << first
        return mask, (mask,), first + 1
    left, a, next_id = all_clades(tree[0], first)
    right, b, next_id = all_clades(tree[1], next_id)
    mask = left | right
    return mask, a + b + (mask,), next_id

def fingerprint(tree, n):
    root, clades, last = all_clades(tree)
    assert root == (1 << n) - 1 and last == n
    edges = clades[:-1]
    assert len(edges) == 2 * n - 2
    singles = [0] * (n + 1)
    unions = [0] * (n + 1)
    for e in edges:
        singles[e.bit_count()] += 1
    for a in range(len(edges)):
        for b in range(a + 1, len(edges)):
            unions[(edges[a] | edges[b]).bit_count()] += 1
    return tuple(singles), tuple(unions)

def distributions(tree, n):
    root, clades, _ = all_clades(tree)
    edges = clades[:-1]
    counts = collections.Counter()
    for drawn in range(1 << n):
        k = drawn.bit_count()
        pd = sum(bool(drawn & c) for c in edges)
        counts[k, pd] += 1
    return counts

if __name__ == '__main__':
    classes = []
    exceptional = []
    for n in range(1, 17):
        seen = {}
        ambiguous = []
        mean_counts = collections.Counter()
        for shape in shapes(n):
            signature = fingerprint(shape, n)
            mean_counts[signature[0]] += 1
            if signature in seen:
                ambiguous.append((seen[signature], shape))
            else:
                seen[signature] = shape
        classes.append({
            'tips': n, 'rooted_binary_shapes': len(shapes(n)),
            'different_mean_fingerprints': len(mean_counts),
            'different_mean_variance_fingerprints': len(seen),
            'moment_fingerprint_duplicate_excess': len(ambiguous),
        })
        if ambiguous:
            exceptional.extend(ambiguous)
    assert len(exceptional) == 1
    tree_a, tree_b = exceptional[0]
    cherry = ((), ())
    comb4 = ((), ((), ((), ())))
    balance4 = (cherry, cherry)
    assortative = ((comb4, comb4), (balance4, balance4))
    mixed = ((comb4, balance4), (comb4, balance4))
    assert set(map(repr, (tree_a, tree_b))) == set(map(repr, (assortative, mixed)))
    sig_a, sig_b = fingerprint(assortative, 16), fingerprint(mixed, 16)
    assert sig_a == sig_b
    D_a, D_b = distributions(assortative, 16), distributions(mixed, 16)
    assert all(sum(D[k, p] for p in range(31)) == math.comb(16, k)
               for D in (D_a, D_b) for k in range(17))
    for k in range(17):
        for exponent in (1, 2):
            lhs = sum(count * p ** exponent for (kk, p), count in D_a.items() if kk == k)
            rhs = sum(count * p ** exponent for (kk, p), count in D_b.items() if kk == k)
            assert lhs == rhs, (k, exponent, lhs, rhs)
    factorial3_a = sum(v * p * (p-1) * (p-2) // 6 for (k, p), v in D_a.items() if k == 2)
    factorial3_b = sum(v * p * (p-1) * (p-2) // 6 for (k, p), v in D_b.items() if k == 2)
    assert (factorial3_a, factorial3_b) == (5909, 5910)
    assert any(D_a[k, p] != D_b[k, p] for k in range(17) for p in range(31))
    certificate = {
        'arithmetic': 'exact integers; no floating point',
        'model': 'rooted full binary trees, every edge length one, uniform fixed-size leaf subsets',
        'class_counts': classes,
        'first_two_moment_collision_tips': 16,
        'total_collision_pairs_at_16': 1,
        'witness_assortative': repr(assortative),
        'witness_mixed': repr(mixed),
        'witness_single_clade_size_histogram': {str(i): c for i, c in enumerate(sig_a[0]) if c},
        'witness_clade_union_size_histogram': {str(i): c for i, c in enumerate(sig_a[1]) if c},
        'direct_65536_subset_check_per_tree': True,
        'identical_first_and_second_raw_moments_every_sampling_depth': True,
        'sample_two_third_binomial_moment_unnormalized_assortative': factorial3_a,
        'sample_two_third_binomial_moment_unnormalized_mixed': factorial3_b,
        'sample_two_third_binomial_moment_difference_mixed_minus_assortative': '1/120',
    }
    print(json.dumps(certificate, sort_keys=True, indent=2))
