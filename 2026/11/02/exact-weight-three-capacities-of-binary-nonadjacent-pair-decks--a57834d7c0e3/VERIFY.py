#!/usr/bin/env python3
"""Independent finite checks of a fixed-weight gapped-pair spectrum theorem.

Only Python's standard library is required. Run: python3 VERIFY.py
Finite checks illustrate, but do not replace, the symbolic proof in RESULT.md.
"""
from itertools import combinations


def gapped_profile(word):
    """Composition and all ordered nonadjacent pair multiplicities."""
    z = o = 0
    c00 = c01 = c10 = c11 = 0
    last = None
    for t in word:
        pz = z - (last == 0)
        po = o - (last == 1)
        if t == 0:
            c00 += pz
            c10 += po
            z += 1
        else:
            c01 += pz
            c11 += po
            o += 1
        last = t
    return (o, c00, c01, c10, c11)


def profile_classes(n):
    result = set()
    state_sets = {}
    for ones in combinations(range(n), 3):
        s = [0] * n
        for i in ones:
            s[i] = 1
        p = gapped_profile(s)
        result.add(p)
        r1 = sum(s[i] == 1 and (i == 0 or s[i-1] == 0) for i in range(n))
        r0 = sum(s[i] == 0 and (i == 0 or s[i-1] == 1) for i in range(n))
        state_sets.setdefault((r1, r0), set()).add(p[2])
        assert p[3] == (n - 2) * (n - 1) // 2 - p[1] - p[2] - p[4]
    return result, state_sets


def predicted_run_classes(z):
    assert z >= 5
    k22 = set(range(0, 3 * z - 2))
    if z % 2:
        k22 -= set(range(z - 1, 2 * z - 1, 2))
    return {
        (1, 1): {0, 3 * z - 1},
        (1, 2): set(range(2, 3 * z - 3, 3)),
        (2, 1): {z - 1, 2 * z - 1},
        (2, 2): k22,
        (2, 3): set(range(2, 3 * z - 5)),
        (3, 2): set(range(z - 1, 2 * z - 2)),
        (3, 3): set(range(1, 3 * z - 5)),
        (3, 4): set(range(3, 3 * z - 8)),
    }


def capacity(n):
    if n == 3:
        return 1
    if n == 4:
        return 4
    if n == 5:
        return 10
    if n == 6:
        return 17
    if n == 7:
        return 31
    return 14 * n - 66 if n % 2 else (27 * n - 130) // 2


def main():
    all_words_tested = 0
    for n in range(3, 81):
        profiles, states = profile_classes(n)
        all_words_tested += n * (n - 1) * (n - 2) // 6
        assert len(profiles) == capacity(n), (n, len(profiles), capacity(n))
        if n >= 8:
            wanted = predicted_run_classes(n - 3)
            assert states == wanted, (n, states, wanted)
            assert sum(map(len, wanted.values())) == len(profiles)
    for n in range(3, 15):
        brute = set()
        for mask in range(1 << n):
            if mask.bit_count() != 3:
                continue
            bits = [(mask >> i) & 1 for i in range(n)]
            direct = tuple(sum(bits[i] == a and bits[j] == b
                               for i in range(n) for j in range(i + 2, n))
                           for a, b in ((0, 0), (0, 1), (1, 0), (1, 1)))
            assert gapped_profile(bits)[1:] == direct
            brute.add((3,) + direct)
        assert len(brute) == capacity(n)
    print('PASS: weight-three profiles, run-state sets and formulas for n=3..80')
    print(f'PASS: {all_words_tested:,} source words checked with a prefix-count algorithm')
    print('PASS: independent literal-pair verification for n=3..14')
    for n in (6, 7, 8, 9, 10, 11, 12, 20, 30, 80):
        print(f'n={n}: {capacity(n)} distinct profiles')


if __name__ == '__main__':
    main()
