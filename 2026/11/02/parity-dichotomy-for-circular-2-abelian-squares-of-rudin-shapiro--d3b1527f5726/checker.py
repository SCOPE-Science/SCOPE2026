#!/usr/bin/env python3
"""Independent finite-rank checks for the stated cyclic 2-Abelian-square theorem."""
from collections import Counter


def bits_direct(rank):
    return [(i & (i >> 1)).bit_count() % 2 for i in range(1 << rank)]


def predicted_starts(rank):
    width = 1 << (rank - 2)
    if rank % 2 == 0:
        return set()
    return set(range(1, width)) | set(range(2 * width + 1, 3 * width))


def signatures_for_all_cuts(word):
    size = len(word)
    half = size // 2
    doubled = word + word
    pref_one = [0]
    pref_pair = [[0] for _ in range(4)]
    for i, bit in enumerate(doubled):
        pref_one.append(pref_one[-1] + bit)
        if i + 1 < len(doubled):
            pair = (bit << 1) | doubled[i+1]
            for t in range(4):
                pref_pair[t].append(pref_pair[t][-1] + (pair == t))
    def sig(start):
        counts = (pref_one[start+half] - pref_one[start],)
        counts += tuple(pref_pair[t][start+half-1] - pref_pair[t][start] for t in range(4))
        return counts
    return {i for i in range(size) if sig(i) == sig(i+half)}


def signs_recursive(rank):
    p = q = [1]
    for _ in range(rank):
        p, q = p+q, p+[-x for x in q]
    return p, q


def run_checks():
    for k in range(2, 15):
        p, q = signs_recursive(k)
        direct = bits_direct(k)
        assert p == [1 - 2*b for b in direct], ('Rudin-Shapiro sign mismatch', k)
        actual = signatures_for_all_cuts(direct)
        expected = predicted_starts(k)
        assert actual == expected, ('position mismatch', k, sorted(actual ^ expected)[:10])
        m = k - 2
        ap, bq = signs_recursive(m)
        assert sum(bq) == (0 if m % 2 else 1 << (m//2)), ('B total mismatch', k)
        if m >= 1:
            assert ap[0] == bq[0] == 1
            assert ap[-1] == -bq[-1]
        print('rank', k, 'length', 1<<k, 'matching rotations', len(actual), 'OK')
    print('ALL CHECKS PASSED; finite ranks are not an infinite proof.')


if __name__ == '__main__':
    run_checks()
