"""Exact small-market verification of a common-first-choice RSD law.

This finite check supports, but does not replace, the general analytical proof.
Python 3.9+; no external dependencies.
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, permutations, product
from math import comb, factorial

@lru_cache(None)
def coupon_pmf(m):
    # Independent exact rational occupancy-chain calculation.
    @lru_cache(None)
    def solve(unseen, single):
        if unseen == 0:
            return {single: Fraction(1)}
        law = Counter()
        for k, p in solve(unseen - 1, single + 1).items():
            law[k] += Fraction(unseen, unseen + single) * p
        if single:
            for k, p in solve(unseen, single - 1).items():
                law[k] += Fraction(single, unseen + single) * p
        return dict(law)
    return solve(m, 0)

def direct(n, r):
    all_preferences = list(permutations(range(n)))
    force_first = [p for p in all_preferences if p[0] == 0]
    hist = Counter()
    profiles = 0
    for flagged in combinations(range(n), r):
        domains = [force_first if i in flagged else all_preferences for i in range(n)]
        for pref in product(*domains):
            remaining = set(range(n))
            assigned = []
            for order in pref:
                good = next(g for g in order if g in remaining)
                assigned.append(good)
                remaining.remove(good)
            ranks = [{g: k for k, g in enumerate(p)} for p in pref]
            unenvied = sum(all(ranks[j][assigned[j]] < ranks[j][assigned[i]]
                                for j in range(i + 1, n)) for i in range(n))
            hist[unenvied] += 1
            profiles += 1
    expected_profiles = comb(n, r) * factorial(n - 1) ** r * factorial(n) ** (n - r)
    assert profiles == expected_profiles, (n, r, profiles, expected_profiles)
    return {k: Fraction(v, profiles) for k, v in sorted(hist.items())}, profiles

def main():
    total = 0
    for n in (2, 3, 4):
        for r in range(n + 1):
            actual, profiles = direct(n, r)
            target = coupon_pmf(n if r < 2 else n - 1)
            assert actual == target, (n, r, actual, target)
            assert sum(actual.values(), Fraction()) == 1
            total += profiles
            print(f'n={n}, r={r}, profiles={profiles}, distribution={actual}')
    print(f'PASS: {total} full-profile/flag-placement cases, n=2,3,4; exact-rational independent coupon-chain comparison')

if __name__ == '__main__':
    main()
