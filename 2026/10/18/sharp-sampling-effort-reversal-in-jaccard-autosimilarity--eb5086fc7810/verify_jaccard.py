#!/usr/bin/env python3
"""Exact finite-census check for replicate Jaccard autosimilarity.

Only Python's standard library is needed. The theorem for arbitrary census size
is analytical; the exhaustive check covers the stated sharp finite boundary.
"""
import csv
from fractions import Fraction
from itertools import combinations
from math import comb
from pathlib import Path


def integer_partitions(n, minimum=1):
    """All nondecreasing tuples of positive integers summing to n."""
    if n == 0:
        yield ()
    for a in range(minimum, n + 1):
        for rest in integer_partitions(n - a, a):
            yield (a,) + rest


def support_counts_by_inclusion_exclusion(abundances, m):
    s = len(abundances)
    sizes = [sum(a for i, a in enumerate(abundances) if mask & (1 << i))
             for mask in range(1 << s)]
    weights = {}
    for mask in range(1, 1 << s):
        count = 0
        sub = mask
        while True:
            if sizes[sub] >= m:
                count += (-1 if (mask ^ sub).bit_count() % 2 else 1) * comb(sizes[sub], m)
            if sub == 0:
                break
            sub = (sub - 1) & mask
        if count:
            assert count > 0
            weights[mask] = count
    assert sum(weights.values()) == comb(sum(abundances), m)
    return weights


def expected_jaccard_inclusion_exclusion(abundances, m):
    weights = support_counts_by_inclusion_exclusion(abundances, m)
    den = comb(sum(abundances), m) ** 2
    numerator = sum(Fraction(x * y * (a & b).bit_count(), (a | b).bit_count())
                    for a, x in weights.items() for b, y in weights.items())
    return numerator / den


def expected_jaccard_direct(abundances, m):
    labels = []
    for species, count in enumerate(abundances):
        labels.extend([species] * count)
    weights = {}
    for selected in combinations(range(len(labels)), m):
        mask = 0
        for ix in selected:
            mask |= 1 << labels[ix]
        weights[mask] = weights.get(mask, 0) + 1
    den = comb(len(labels), m) ** 2
    numerator = sum(Fraction(x * y * (a & b).bit_count(), (a | b).bit_count())
                    for a, x in weights.items() for b, y in weights.items())
    return numerator / den


def run():
    rows = []
    violations = []
    profiles = 0
    pairs_checked = 0
    for n in range(1, 7):
        for profile in integer_partitions(n):
            profiles += 1
            seq = []
            for m in range(1, n + 1):
                x = expected_jaccard_inclusion_exclusion(profile, m)
                y = expected_jaccard_direct(profile, m)
                assert x == y, (profile, m, x, y)
                pairs_checked += 1
                seq.append(x)
            drops = [m for m in range(1, n) if seq[m] < seq[m - 1]]
            if drops:
                violations.append((profile, drops))
            rows.append((n, profile, seq, drops))
    assert profiles == 29, profiles
    assert violations == [((1, 5), [2])], violations

    for n in range(3, 121):
        p = (1, n - 1)
        assert expected_jaccard_inclusion_exclusion(p, 1) == Fraction(1 + (n-1)**2, n*n)
        for m in range(2, n+1):
            exact = 1 - Fraction(m, n) + Fraction(m*m, n*n)
            assert expected_jaccard_inclusion_exclusion(p, m) == exact
            if m < n:
                nxt = 1 - Fraction(m+1, n) + Fraction((m+1)**2, n*n)
                assert nxt - exact == Fraction(2*m+1-n, n*n)
    for n in range(6, 120):
        assert (1 - Fraction(3, n) + Fraction(9, n*n)) < (1-Fraction(2,n)+Fraction(4,n*n))
    # Disjoint designs are verified independently through exhaustive labeled draws.
    for n in range(4, 12):
        species = [0] * (n-1) + [1]
        for m in range(1, n//2+1):
            total = hits = 0
            for left in combinations(range(n), m):
                rem = set(range(n)) - set(left)
                lmask = 0
                for i in left: lmask |= 1 << species[i]
                for right in combinations(sorted(rem), m):
                    rmask = 0
                    for i in right: rmask |= 1 << species[i]
                    total += 1
                    hits += Fraction((lmask & rmask).bit_count(), (lmask | rmask).bit_count())
            expected = Fraction(hits, total)
            theoretical = (1 - Fraction(m,n)) if m >= 2 else (1 - Fraction(2,n))
            assert expected == theoretical, (n,m,expected,theoretical)

    path = Path(__file__).resolve().parent / 'census_n_le_6.csv'
    with path.open('w', encoding='utf-8', newline='') as handle:
        writer=csv.writer(handle)
        writer.writerow(['total_individuals','abundances','expected_autosimilarity_by_sample_size','strict_drop_after_size'])
        for n,profile,seq,drops in rows:
            writer.writerow([n,';'.join(map(str,profile)),';'.join(map(str,seq)),';'.join(map(str,drops))])
    print('PROFILES',profiles)
    print('EXACT_PAIRWISE_EQUIVALENCES',pairs_checked)
    print('VIOLATIONS',violations)
    print('SIX_INDIVIDUAL_WITNESS', [str(expected_jaccard_inclusion_exclusion((1,5),m)) for m in range(1,7)])
    print('CERTIFICATE',path.name)

if __name__ == '__main__': run()
