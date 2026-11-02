"""Exact finite checks for record-conditioned convex rank displacement.

Run: python3 verify.py (standard library only).
These finite checks complement, but do not replace, the general proof.
"""
from collections import Counter
from fractions import Fraction
from itertools import permutations
from math import factorial


def bubble_prefix_max(perm, i):
    """Move the largest of the first i values to position i (1-based)."""
    pos = perm.index(max(perm[:i]))
    return perm[:pos] + perm[pos + 1:i] + perm[pos:pos + 1] + perm[i:]


def score(perm, fun):
    return sum(fun(abs(value - j)) for j, value in enumerate(perm, 1))


def main():
    assertions = 0
    losses = [lambda t: t, lambda t: t*t, lambda t: t*t*t,
              lambda t: max(0, t-1), lambda t: max(0, t-3)]
    for n in range(2, 9):
        family = list(permutations(range(1, n+1)))
        base_sum = sum(score(p, losses[0]) for p in family)
        base_sq_sum = sum(score(p, losses[1]) for p in family)
        for i in range(2, n+1):
            image_counts = Counter()
            conditional_sum = 0
            for p in family:
                q = bubble_prefix_max(p, i)
                image_counts[q] += 1
                assert q[i-1] == max(q[:i]); assertions += 1
                for phi in losses:
                    assert score(q, phi) <= score(p, phi); assertions += 1
            conditionals = [p for p in family if p[i-1] == max(p[:i])]
            assert len(conditionals) == len(family)//i; assertions += 1
            assert set(image_counts) == set(conditionals); assertions += 1
            assert set(image_counts.values()) == {i}; assertions += 1
            conditional_sum = sum(score(p, losses[0]) for p in conditionals)
            delta = Fraction(conditional_sum, len(conditionals)) - Fraction(base_sum, len(family))
            assert delta == Fraction(-i*(2*i-1), 3*n); assertions += 1
            cond_sq_sum = sum(score(p, losses[1]) for p in conditionals)
            delta_sq = Fraction(cond_sq_sum, len(conditionals)) - Fraction(base_sq_sum, len(family))
            assert delta_sq == Fraction(-i*(i-1)*(n+1), 2*(i+1)); assertions += 1
            dist_all = Counter(score(p, losses[0]) for p in family)
            dist_cond = Counter(score(p, losses[0]) for p in conditionals)
            for threshold in range(0, n*n+1):
                total_tail = Fraction(sum(count for value, count in dist_all.items() if value >= threshold), len(family))
                cond_tail = Fraction(sum(count for value, count in dist_cond.items() if value >= threshold), len(conditionals))
                assert cond_tail <= total_tail; assertions += 1
        summed_cov = sum((Fraction(-2*i+1, 3*n) for i in range(2, n+1)), Fraction(0))
        assert summed_cov == Fraction(-(n*n-1), 3*n); assertions += 1
        record_weighted = sum(score(p, losses[0]) * sum(p[k-1] == max(p[:k]) for k in range(1,n+1)) for p in family)
        mean_records = Fraction(sum(sum(p[k-1] == max(p[:k]) for k in range(1,n+1)) for p in family), len(family))
        direct_cov = Fraction(record_weighted, len(family)) - Fraction(base_sum, len(family))*mean_records
        assert direct_cov == summed_cov; assertions += 1
        print('n=', n, 'checks complete')
    print('PASSED:', assertions, 'exact assertions')


if __name__ == '__main__':
    main()
