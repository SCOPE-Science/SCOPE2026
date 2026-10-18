"""Exact checks for joint rarefaction dominance under integer abundance transfers.

Run with standard Python 3: python verify_rarefaction.py
All comparisons use nonnegative integer counts, never simulations.
"""
from functools import lru_cache
from math import comb
from itertools import combinations


def C(n, r):
    """Zero for indices outside the combinatorial range."""
    return comb(n, r) if 0 <= r <= n else 0


@lru_cache(None)
def partitions(n, minimum=1):
    if n == 0:
        return ((),)
    return tuple((i,) + p for i in range(minimum, n + 1)
                 for p in partitions(n - i, i))


@lru_cache(None)
def richness_counts(profile, sample_size):
    """Number of individual subsets by sample size and represented species."""
    dp = {(0, 0): 1}
    for abundance in profile:
        next_dp = {}
        for (size, richness), weight in dp.items():
            for taken in range(min(abundance, sample_size - size) + 1):
                state = (size + taken, richness + (taken > 0))
                next_dp[state] = (next_dp.get(state, 0)
                                  + weight * C(abundance, taken))
        dp = next_dp
    return tuple(dp.get((sample_size, k), 0) for k in range(len(profile) + 1))


def gain_formula(profile, donor, recipient, sample_size, threshold):
    """Exact numerator for change in P(K >= threshold)."""
    a, b = profile[donor], profile[recipient]
    outside = tuple(x for i, x in enumerate(profile)
                    if i not in (donor, recipient))
    numerator = 0
    for j in range(2, a + 1):
        t = sample_size - j
        if not 0 <= t <= sum(outside):
            continue
        outside_counts = richness_counts(outside, t)
        q = threshold - 2
        coefficient = outside_counts[q] if 0 <= q < len(outside_counts) else 0
        numerator += (C(a - 1, j - 1) - C(b, j - 1)) * coefficient
    return numerator


def check_second_color_time():
    """Directly enumerate two-color words to verify coupling marginals."""
    checks = 0
    for a in range(2, 10):
        for b in range(1, a-1):
            total = a + b
            time_counts = {}
            for pos_a in combinations(range(total), a):
                included = set(pos_a)
                first_type = int(0 in included)
                t = next(j+1 for j in range(1,total)
                         if int(j in included) != first_type)
                time_counts[t] = time_counts.get(t,0) + 1
            for j in range(1,total+1):
                empirical_survival = sum(w for t,w in time_counts.items() if t>j)
                predicted = C(a,j)+C(b,j)
                assert empirical_survival * C(total,j) == predicted * C(total,a)
                assert C(a-1,j-1)-C(b,j-1) >= 0
                checks += 1
    return checks


def check():
    profiles = transfers = comparisons = tail_checks = 0
    for n in range(2, 15):
        for p in partitions(n):
            profiles += 1
            for donor in range(len(p)):
                for recipient in range(len(p)):
                    if donor == recipient or p[donor] < p[recipient] + 2:
                        continue
                    q = list(p)
                    q[donor] -= 1
                    q[recipient] += 1
                    q = tuple(q)
                    a, b = p[donor], p[recipient]
                    transfers += 1
                    for j in range(1, a + 2):
                        # Later discovery of both donor/recipient species cannot
                        # be more likely after an abundance-balancing transfer.
                        assert C(a-1, j-1) - C(b, j-1) >= 0
                    for m in range(n + 1):
                        old = richness_counts(p, m)
                        new = richness_counts(q, m)
                        comparisons += 1
                        assert sum(old) == sum(new) == C(n, m)
                        for k in range(1, len(p) + 1):
                            observed = sum(new[k:]) - sum(old[k:])
                            predicted = gain_formula(p, donor, recipient, m, k)
                            assert observed == predicted >= 0, (p, q, m, k)
                            tail_checks += 1
                        observed_mean = sum(k * (new[k] - old[k])
                                            for k in range(len(p) + 1))
                        expected_mean = C(n-b-1, m-1) - C(n-a, m-1)
                        if m == 0:
                            expected_mean = 0
                        assert observed_mean == expected_mean
                        assert (observed_mean > 0) == (2 <= m <= n-b)

    p = (4, 3, 1)
    q = (4, 2, 2)
    assert [sum(richness_counts(q,3)[k:]) -
            sum(richness_counts(p,3)[k:]) for k in (2,3)] == [1,4]
    assert [sum(richness_counts(q,4)[k:]) -
            sum(richness_counts(p,4)[k:]) for k in (2,3)] == [0,10]
    second_color_checks = check_second_color_time()
    print('PASS: second-color time enumeration checks:', second_color_checks)
    print('PASS: abundance profiles:', profiles)
    print('PASS: directed integer transfers:', transfers)
    print('PASS: transfer/sample-size pairs:', comparisons)
    print('PASS: exact nonnegative probability-tail kernels:', tail_checks)
    print('PASS: mean improvement formula and strictness ranges')
    print('PASS: (4,3,1) to (4,2,2) example')


if __name__ == '__main__':
    check()
