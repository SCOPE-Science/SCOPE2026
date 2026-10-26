#!/usr/bin/env python3
"""Exact cyclic binary window-composition reconstruction certificate.

No external packages or probabilistic hashing are used. The two independent
representations provide a cross-check of the exact finite classification.
"""
import csv
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def canonical_string(w):
    n = len(w)
    rev = w[::-1]
    return min(w[j:] + w[:j] for j in range(n)) if n == 1 else min(
        [w[j:] + w[:j] for j in range(n)]
        + [rev[j:] + rev[:j] for j in range(n)]
    )


def spectrum_string(w):
    """All window histograms, through floor(n/2), using running sums."""
    n = len(w)
    a = [int(v) for v in w]
    hist = []
    for k in range(1, n // 2 + 1):
        v = sum(a[j] for j in range(k))
        counts = [0] * (k + 1)
        counts[v] += 1
        for start in range(1, n):
            v += a[(start + k - 1) % n] - a[start - 1]
            counts[v] += 1
        hist.extend(counts)
    return (sum(a),) + tuple(hist)


def canonical_integer(x, n):
    mask = (1 << n) - 1
    flipped = sum(((x >> i) & 1) << (n - 1 - i) for i in range(n))
    candidates = []
    for z in (x, flipped):
        for j in range(n):
            candidates.append(((z << j) | (z >> (n - j))) & mask)
    return min(candidates)


def spectrum_integer(x, n):
    """All window histograms from independent modular bit access."""
    hist = []
    for k in range(1, n // 2 + 1):
        count = [0] * (k + 1)
        for start in range(n):
            ones = 0
            for offset in range(k):
                ones += (x >> ((start + offset) % n)) & 1
            count[ones] += 1
        hist.extend(count)
    return (x.bit_count(),) + tuple(hist)


def autocorrelation(x, n):
    return (x.bit_count(),) + tuple(
        sum(((x >> i) & 1) * ((x >> ((i + d) % n)) & 1) for i in range(n))
        for d in range(1, n // 2 + 1)
    )


def moment_identity(x, n):
    bits = [(x >> j) & 1 for j in range(n)]
    row = [0]
    for k in range(1, n + 1):
        row.append(sum(sum(bits[(start + t) % n] for t in range(k)) ** 2
                       for start in range(n)))
    for k in range(1, n):
        correlation = sum(bits[i] * bits[(i + k) % n] for i in range(n))
        assert row[k + 1] - 2 * row[k] + row[k - 1] == 2 * correlation


def compute():
    target_counts = [2, 3, 4, 6, 8, 13, 18, 30, 46, 78, 126, 224]
    result = []
    pairs = []
    for n in range(1, 13):
        reps = set()
        for x in range(1 << n):
            w = format(x, '0%db' % n)
            # An integer mask is little-endian, but its reversal is a dihedral
            # transform of its displayed big-endian binary expansion.
            ci = canonical_integer(x, n)
            cs = canonical_string(w)
            assert format(ci, '0%db' % n) == cs
            assert spectrum_integer(x, n) == spectrum_string(w)
            reps.add(ci)
        assert len(reps) == target_counts[n - 1]
        groups = defaultdict(list)
        homometry = defaultdict(list)
        for x in sorted(reps):
            groups[spectrum_integer(x, n)].append(x)
            homometry[autocorrelation(x, n)].append(x)
            moment_identity(x, n)
        collision_sizes = Counter(len(group) for group in groups.values())
        homometry_sizes = Counter(len(group) for group in homometry.values())
        assert max(collision_sizes) <= 2
        assert max(homometry_sizes) <= 2
        result.append((n, len(reps), len(groups), sum(len(g) - 1 for g in homometry.values()),
                       sum(len(g) - 1 for g in groups.values())))
        if n == 12:
            for collision in groups.values():
                if len(collision) == 2:
                    assert [format(z, '012b') for z in collision] == [
                        '001011001101', '001011010011']
            assert len(groups) == 223
            assert collision_sizes == {1: 222, 2: 1}
            assert homometry_sizes == {1: 178, 2: 23}
            for group in homometry.values():
                if len(group) == 2:
                    s, t = [format(z, '012b') for z in group]
                    first_differing = next((k for k in range(1, 7)
                        if Counter(sum(int(s[(i + j) % 12]) for j in range(k))
                                   for i in range(12)) !=
                           Counter(sum(int(t[(i + j) % 12]) for j in range(k))
                                   for i in range(12))), 0)
                    pairs.append((s, t, first_differing))
    assert [r[4] for r in result] == [0] * 11 + [1]
    assert [r[3] for r in result] == [0, 0, 0, 0, 0, 0, 0, 1, 0, 3, 0, 23]
    assert Counter(x[2] for x in pairs) == {0: 1, 3: 17, 4: 3, 5: 2}
    return result, sorted(pairs)


def verify_repetition():
    u, v = '001011001101', '001011010011'
    for r in range(1, 6):
        x, y = u * r, v * r
        assert canonical_string(x) != canonical_string(y)
        assert spectrum_string(x) == spectrum_string(y)


def main():
    result, pairs = compute()
    verify_repetition()
    expected = ROOT / 'homometric_pairs_n12.csv'
    with expected.open(encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f)
        observed = [(r['first_bracelet'], r['second_bracelet'], int(r['first_distinguishing_window_length']))
                    for r in reader]
    assert observed == pairs
    for line in result:
        print('length=%2d bracelets=%3d observations=%3d homometric_extra=%2d spectrum_extra=%d' % line)
    print('HOMOMETRIC_PAIRS_12', len(pairs))
    print('AMBIGUITY', next(p for p in pairs if p[2] == 0)[:2])
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
