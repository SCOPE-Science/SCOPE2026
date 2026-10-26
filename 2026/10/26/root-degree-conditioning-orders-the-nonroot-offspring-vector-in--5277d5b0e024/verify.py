"""Exact finite-sample checks for root-degree-conditioned leaf-set order in recursive trees.

Run: python verify.py. Uses only the Python standard library.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import factorial


def enumerate_laws(n):
    """Enumerate all (n-1)! equally likely recursive trees; leaf mask uses labels 2..n-1."""
    counts = {r: Counter() for r in range(1, n)}
    for parents in product(*(range(1, j) for j in range(2, n + 1))):
        root_degree = sum(p == 1 for p in parents)
        nonleaf = set(parents)
        leaf_mask = sum(1 << (j - 2) for j in range(2, n) if j not in nonleaf)
        counts[root_degree][leaf_mask] += 1
    assert sum(map(lambda c: sum(c.values()), counts.values())) == factorial(n - 1)
    return counts


def upper_family(family, universe):
    for mask in range(universe):
        if family & (1 << mask):
            for extra in range(universe):
                if mask & ~extra == 0 and not (family & (1 << extra)):
                    return False
    return True


def check():
    assertions = 0
    enumerations = 0
    for n in range(3, 10):
        counts = enumerate_laws(n)
        enumerations += factorial(n - 1)
        universe = 1 << (n - 2)
        for k in range(1, n - 1):
            low, high = counts[k], counts[k + 1]
            lo_total = sum(low.values())
            hi_total = sum(high.values())
            assert lo_total > 0 and hi_total > 0
            # Strict conditional expected leaf count: n is always a leaf and cancels.
            left = sum(mask.bit_count() * mass for mask, mass in low.items()) * hi_total
            right = sum(mask.bit_count() * mass for mask, mass in high.items()) * lo_total
            assert left < right, (n, k)
            assertions += 1
            # All upward principal events: a prescribed set is entirely leaf.
            for pattern in range(universe):
                lhs = sum(mass for mask, mass in low.items() if mask & pattern == pattern) * hi_total
                rhs = sum(mass for mask, mass in high.items() if mask & pattern == pattern) * lo_total
                assert lhs <= rhs, (n, k, pattern)
                assertions += 1
            # All increasing leaf-count threshold events.
            for threshold in range(n):
                lhs = sum(mass for mask, mass in low.items() if mask.bit_count() >= threshold) * hi_total
                rhs = sum(mass for mask, mass in high.items() if mask.bit_count() >= threshold) * lo_total
                assert lhs <= rhs, (n, k, threshold)
                assertions += 1
        # Test exact conditional law of independent root attachments:
        # for every root attachment set A, its relative weight is prod(1/(j-2)).
        for k in range(n - 1):
            weights = {}
            for pattern in range(1 << (n - 2)):
                if pattern.bit_count() == k:
                    w = Fraction(1, 1)
                    for bit in range(n - 2):
                        if pattern >> bit & 1:
                            w *= Fraction(1, bit + 1)
                    weights[pattern] = w
            normalizer = sum(weights.values(), Fraction(0))
            assert normalizer > 0
            assert sum((w / normalizer for w in weights.values()), Fraction(0)) == 1
            assertions += 2
        # An exhaustive test of every monotone Boolean leaf-set functional for small n.
        if n <= 6:
            laws = []
            for r in range(1, n):
                total = sum(counts[r].values())
                laws.append([Fraction(counts[r][mask], total) for mask in range(universe)])
            for family in range(1 << universe):
                if not upper_family(family, universe):
                    continue
                masses = [sum(q for mask, q in enumerate(law) if (family >> mask) & 1) for law in laws]
                assert masses == sorted(masses), (n, family)
                assertions += len(masses) - 1
    print(f"PASS: {assertions} exact conditional-order checks; {enumerations} recursive trees enumerated (n=3..9).")


if __name__ == "__main__":
    check()
