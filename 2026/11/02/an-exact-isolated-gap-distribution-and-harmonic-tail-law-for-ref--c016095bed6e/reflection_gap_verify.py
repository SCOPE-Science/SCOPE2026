#!/usr/bin/env python3
"""Independent finite tests for isolated-gap statistics of reflective semigroups.

Run: python3 reflection_gap_verify.py
Uses only the Python standard library. No finite check proves the asymptotic theorem.
"""
from collections import Counter
from math import isqrt


def dsieve(limit):
    divs = [[] for _ in range(limit + 1)]
    for d in range(1, limit + 1):
        for n in range(d, limit + 1, d):
            divs[n].append(d)
    return divs


def constructed_semigroup(g, a):
    r = g % a
    generators = sorted(set([a, 2 * g + a - r, *range(g + 1, g + a)]))
    bound = 2 * g + 2 * a + 5
    present = [False] * (bound + 1)
    present[0] = True
    for n in range(1, bound + 1):
        present[n] = any(n >= t and present[n - t] for t in generators)
    gaps = [n for n in range(1, bound) if not present[n]]
    isolated = [n for n in gaps if present[n - 1] and present[n + 1]]
    return gaps, isolated


def asserted_gap_lists(g, a):
    q, r = divmod(g, a)
    gaps = [n for n in range(1, g) if n % a]
    gaps += [g + a * j for j in range(q + 1)]
    isolated = gaps[:] if a == 2 else [g + a * j for j in range(1, q + 1)] + ([g] if r == 1 else [])
    return sorted(gaps), sorted(isolated)


def direct_count(g, a):
    q, r = divmod(g, a)
    return q + int(r == 1) + (g - 1) // 2 * int(a == 2 and g % 2 == 1)


def tail_formula(g, k, divs):
    b = g // k
    base = max(b - 1, 0) - sum(2 <= a <= b for a in divs[g])
    extra = int(k >= 2 and (g - 1) % (k - 1) == 0 and (g - 1) // (k - 1) >= 2)
    outlier = int(g % 2 == 1 and (g + 1) // 2 < k <= g)
    return base + extra + outlier


def divisor_sum(n, divs):
    return sum(divs[n])


def test():
    divs = dsieve(1200)
    semigroups = 0
    for g in range(1, 101):
        for a in range(2, g + 2):
            if g % a == 0:
                continue
            true_gaps, true_isolated = constructed_semigroup(g, a)
            pred_gaps, pred_isolated = asserted_gap_lists(g, a)
            assert true_gaps == pred_gaps, (g, a, 'gap_set')
            assert true_isolated == pred_isolated, (g, a, 'isolated_set')
            assert len(pred_isolated) == direct_count(g, a), (g, a, 'count')
            assert len(true_gaps) == g
            semigroups += 1
    print('PASS: independently generated numerical semigroups and isolated gaps:', semigroups)

    profiles = 0
    tails = 0
    for g in range(2, 1201):
        count = Counter(direct_count(g, a) for a in range(2, g + 2) if g % a)
        N = sum(count.values())
        assert N == g + 1 - len(divs[g])
        total = sum(j * number for j, number in count.items())
        D = sum(g // i for i in range(1, g + 1))
        sigma = divisor_sum(g, divs)
        predicted_total = D - sigma + len(divs[g - 1]) - 1 + (g - 1) // 2 * (g % 2)
        assert total == predicted_total, (g, total, predicted_total)
        assert count[0] == 1, (g, 'unique_perfect')
        if g >= 3:
            tail2 = sum(number for isolated, number in count.items() if isolated >= 2)
            numerator = (3 if g % 2 == 0 else 2) - len(divs[g])
            assert 2 * tail2 - N == numerator, (g, 'sharpness_at_k2')
        accum = N
        for k in range(1, max(count) + 2):
            accum -= count[k - 1]
            expected = tail_formula(g, k, divs)
            assert accum == expected, (g, k, accum, expected)
            assert abs(accum / N - 1 / k) <= (2 * len(divs[g]) + 4) / N + 1e-14
            tails += 1
        profiles += 1
    print('PASS: exact tail distribution, mean, uniqueness and uniform bound:', profiles, 'genera,', tails, 'tail checks')

    for g in (101, 211, 509, 997, 1193):
        count = Counter(direct_count(g, a) for a in range(2, g + 2) if g % a)
        N = sum(count.values())
        for k in (1, 2, 3, 4, 5, 10):
            proportion = sum(n for j, n in count.items() if j >= k) / N
            print(f'genus={g}, tail-k={k}, empirical={proportion:.6f}, limit={1/k:.6f}')
    print('ALL VERIFICATIONS PASSED')


if __name__ == '__main__':
    test()
