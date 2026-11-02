#!/usr/bin/env python3
"""Exact reproducibility checks for pairwise-quota ranking subsampling.

Requires only Python 3's standard library. This finite verification supplements,
but does not replace, the total-unimodularity proof for arbitrary electorates.
"""
from itertools import permutations, combinations, combinations_with_replacement, product
from collections import Counter
from math import comb


def rankings(m):
    return list(permutations(range(m)))


def pair_mask(p, pairs):
    pos = {a: i for i, a in enumerate(p)}
    return sum(int(pos[a] < pos[b]) << j for j, (a, b) in enumerate(pairs))


def matrix3():
    ps = rankings(3)
    pairs = ((0, 1), (1, 2), (0, 2))
    return [[1] * 6] + [[int(p.index(a) < p.index(b)) for p in ps]
                            for a, b in pairs]


def determinant(a):
    n = len(a)
    if n == 1:
        return a[0][0]
    if n == 2:
        return a[0][0] * a[1][1] - a[0][1] * a[1][0]
    return sum((-1) ** j * a[0][j] * determinant(
        [row[:j] + row[j+1:] for row in a[1:]]) for j in range(n))


def check_total_unimodularity():
    a = matrix3()
    tested = 0
    for s in range(1, 5):
        for rr in combinations(range(4), s):
            for cc in combinations(range(6), s):
                d = determinant([[a[i][j] for j in cc] for i in rr])
                assert d in (-1, 0, 1), (rr, cc, d)
                tested += 1
    # Independent Ghouila-Houri signing characterization.
    for subset in range(1, 16):
        rr = [i for i in range(4) if subset >> i & 1]
        assert any(all(abs(sum(sign * a[i][j] for i, sign in zip(rr, signs))) <= 1
                       for j in range(6))
                   for signs in product((-1, 1), repeat=len(rr))), subset
    return tested


def quotas_from_counts(profile, masks, pair_count, k):
    n = len(profile)
    counts = [sum((masks[i] >> j) & 1 for i in profile) for j in range(pair_count)]
    return [(k * c) // n for c in counts], [k - (k * (n - c)) // n for c in counts]


def satisfies(output, masks, pair_count, lows, highs):
    return all(lows[j] <= sum((masks[i] >> j) & 1 for i in output) <= highs[j]
               for j in range(pair_count))


def small_three_alternative_check(max_n=9):
    ps = rankings(3)
    pairs = list(combinations(range(3), 2))
    masks = [pair_mask(p, pairs) for p in ps]
    profiles = 0
    quota_instances = 0
    for n in range(1, max_n + 1):
        for profile in combinations_with_replacement(range(6), n):
            profiles += 1
            for k in range(1, n + 1):
                lows, highs = quotas_from_counts(profile, masks, 3, k)
                assert any(satisfies(subset, masks, 3, lows, highs)
                           for subset in combinations(profile, k)), (n, k, profile)
                quota_instances += 1
    return profiles, quota_instances


def direct_four_alternative_census():
    ps = rankings(4)
    pairs = list(combinations(range(4), 2))
    masks = [pair_mask(p, pairs) for p in ps]
    total, failures, distinct_failures = 0, 0, 0
    for profile in combinations_with_replacement(range(24), 4):
        total += 1
        lows, highs = quotas_from_counts(profile, masks, 6, 2)
        if not any(satisfies(subset, masks, 6, lows, highs)
                   for subset in combinations(profile, 2)):
            failures += 1
            distinct_failures += int(len(set(profile)) == 4)
    return total, failures, distinct_failures


def independent_tie_only_census():
    # With four distinct voters and k=2, comparisons split 3:1 or 4:0
    # impose no restriction on a two-voter subcommittee; 2:2 splits require
    # selecting voters with opposite orientations.
    ps = rankings(4)
    pairs = list(combinations(range(4), 2))
    masks = [pair_mask(p, pairs) for p in ps]
    count = 0
    for profile in combinations(range(24), 4):
        tied = [j for j in range(6)
                if sum((masks[i] >> j) & 1 for i in profile) == 2]
        if not any(all(((masks[x] >> j) & 1) != ((masks[y] >> j) & 1)
                       for j in tied) for x, y in combinations(profile, 2)):
            count += 1
    return count


def four_alternative_orbits():
    # Relabel candidates in each four-distinct-ranking failure profile.
    ps = rankings(4)
    pairs = list(combinations(range(4), 2))
    masks = [pair_mask(p, pairs) for p in ps]
    where = {p: i for i, p in enumerate(ps)}
    symmetries = ps
    classes = Counter()
    for profile in combinations(range(24), 4):
        tied = [j for j in range(6)
                if sum((masks[i] >> j) & 1 for i in profile) == 2]
        if any(all(((masks[x] >> j) & 1) != ((masks[y] >> j) & 1)
                   for j in tied) for x, y in combinations(profile, 2)):
            continue
        canonical = min(tuple(sorted(where[tuple(sym[a] for a in ps[i])]
                                     for i in profile)) for sym in symmetries)
        classes[canonical] += 1
    sizes = Counter(classes.values())
    assert len(classes) == 30 and sizes == {24:28, 12:1, 6:1}, sizes
    return len(classes), dict(sizes)


def witness_check():
    profile = [(0,1,2,3), (0,2,3,1), (2,0,1,3), (3,1,2,0)]
    pairs = list(combinations(range(4), 2))
    masks = [pair_mask(p,pairs) for p in profile]
    lows, highs = quotas_from_counts(range(4), masks, 6, 2)
    fail_by_pair = {}
    for x, y in combinations(range(4), 2):
        violated = [pairs[j] for j in range(6)
                    if not lows[j] <= ((masks[x] >> j) & 1) +
                                            ((masks[y] >> j) & 1) <= highs[j]]
        assert len(violated) == 1, (x,y,violated)
        fail_by_pair[f'{x+1}{y+1}'] = violated[0]
    # Even allowing repetitions of one input ranking cannot satisfy all quotas.
    assert not any(satisfies(t, masks, 6, lows, highs)
                   for t in combinations_with_replacement(range(4), 2))
    # Unrestricted synthetic output can meet them, distinguishing the scopes.
    pset = rankings(4)
    fullmasks = [pair_mask(p, pairs) for p in pset]
    assert any(satisfies(t, fullmasks, 6, lows, highs)
               for t in combinations_with_replacement(range(24), 2))
    return fail_by_pair


def check_prior_example_projections():
    # The six-alternative input-only example in Halpern et al., Proposition 1.
    profile = [(3,4,2,5,1,6), (3,4,5,2,6,1),
               (4,3,2,5,6,1), (4,3,5,2,1,6)]
    count = 0
    for subset in combinations(range(1, 7), 4):
        comparisons = list(combinations(subset, 2))
        masks = [pair_mask(tuple(x for x in p if x in subset), comparisons)
                 for p in profile]
        lows, highs = quotas_from_counts(range(4), masks, 6, 2)
        assert any(satisfies(chosen, masks, 6, lows, highs)
                   for chosen in combinations(range(4), 2)), subset
        count += 1
    assert count == 15
    return count


def main():
    tested = check_total_unimodularity()
    print(f'TU certificate: all {tested} nonempty square minors and 15 row subsets PASS')
    nprof, inst = small_three_alternative_check(9)
    print(f'Three alternatives: {nprof} anonymous profiles, {inst} (profile,k) cases PASS')
    total, fail, distinct_fail = direct_four_alternative_census()
    second = independent_tie_only_census()
    assert (total,fail,distinct_fail,second) == (17550,690,690,690)
    print(f'Four alternatives, n=4,k=2: {fail}/{total} multisets fail; independent method {second} PASS')
    count_orb, dist = four_alternative_orbits()
    print(f'Candidate-relabeling: {count_orb} orbits, size distribution {dist} PASS')
    print('Witness failures by selected voter pair:', witness_check())
    print(f'Earlier six-alternative example: {check_prior_example_projections()} four-alternative projections checked')
    print('ALL CHECKS PASSED')


if __name__ == '__main__':
    main()
