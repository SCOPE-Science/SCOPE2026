"""Independent finite replay for exact ternary unordered-bigram singleton profiles.

Run with Python 3 standard library: python verify.py
Finite verification complements, but does not replace, the all-length proofs.
"""
from collections import defaultdict
from itertools import product
from math import comb

EDGE_INDEX = ((0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2))
WHERE = {e: i for i, e in enumerate(EDGE_INDEX)}


def read_profile(word):
    ans = [0] * 6
    for x, y in zip(word, word[1:]):
        ans[WHERE[(min(x, y), max(x, y))]] += 1
    return tuple(ans)


def singleton_characterization(profile):
    a = profile[:3]
    positives = [(i, j, profile[WHERE[(i, j)]]) for i, j in ((0, 1), (0, 2), (1, 2)) if profile[WHERE[(i, j)]] > 0]
    if len(positives) == 0:
        return sum(x > 0 for x in a) == 1
    if len(positives) == 1:
        i, j, t = positives[0]
        k = 3 - i - j
        if a[k]:
            return False
        return t == 1 or (t >= 3 and t % 2 == 1 and a[i] == a[j] == 0)
    if len(positives) == 3:
        return False
    # With exactly two non-loop edge types, their common vertex is the center.
    i, j, p = positives[0]
    h, k, q = positives[1]
    center = ({i, j} & {h, k}).pop()
    leaf_p = i if i != center else j
    leaf_q = h if h != center else k
    if p == q == 1:
        return True
    if p > 1 and q > 1:
        return False
    if max(p, q) == 2:
        return a[center] == 0
    long_leaf = leaf_p if p > q else leaf_q
    return a[center] == 0 and a[long_leaf] == 0


def expected_all(m):
    if m == 0:
        return 1
    choose = lambda n, k: comb(n, k) if n >= k else 0
    return 3 + 3 * choose(m + 1, 2) + 3 * choose(m + 2, 4) + choose(m + 2, 5)


def expected_singleton(m):
    if m == 0:
        return 0
    choose = lambda n, k: comb(n, k) if n >= k else 0
    return (3 + 3 * m + 3 * choose(m, 2)
            + 6 * max(m - 2, 0) + 6 * max(m - 3, 0)
            + 3 * (m >= 3 and m % 2 == 1))


def main():
    total_words = 0
    total_profiles = 0
    total_singletons = 0
    for n in range(1, 13):
        # Number of reversal orbits represented by each observed profile.
        by_profile = defaultdict(set)
        for word in product(range(3), repeat=n):
            reverse = word[::-1]
            by_profile[read_profile(word)].add(min(word, reverse))
            total_words += 1
        m = n - 1
        observed_all = len(by_profile)
        observed_singletons = sum(len(v) == 1 for v in by_profile.values())
        assert observed_all == expected_all(m), (n, observed_all, expected_all(m))
        assert observed_singletons == expected_singleton(m), (n, observed_singletons, expected_singleton(m))
        for p, family in by_profile.items():
            assert singleton_characterization(p) == (len(family) == 1), (n, p, family)
        total_profiles += observed_all
        total_singletons += observed_singletons
        print(f"n={n}: profiles={observed_all}, singleton_reversal_classes={observed_singletons}")
    # The leading terms of the two rational enumerators give this exact asymptotic ratio.
    assert total_words == (3 ** 13 - 3) // 2
    print(f"VERIFY_OK ternary_source_words={total_words} examined_profiles={total_profiles} "
          f"singleton_profiles={total_singletons} n_range=1..12")


if __name__ == '__main__':
    main()
