"""Exact exhaustive certificate for the smallest no-singleton three-run homometry.

Run: python3 CHECK.py. Uses only Python's standard library.
"""
from collections import defaultdict
from itertools import combinations

MIN_N, MAX_N = 8, 19
EXPECTED = {
    8: (1, 1), 9: (3, 3), 10: (9, 9), 11: (19, 19),
    12: (38, 38), 13: (66, 66), 14: (110, 110),
    15: (170, 170), 16: (255, 255), 17: (365, 365),
    18: (511, 511), 19: (693, 692),
}
PAIR = ((2, 1, 10, 3, 3), (2, 3, 5, 1, 8))
TARGET_CORRELATION = (15, 12, 10, 9, 9, 9, 9, 8, 7, 6,
                      5, 5, 4, 3, 2, 2, 2, 2, 1)


def admissible(n):
    """All normalized three-run patterns, modulo reversal, once each.

    The four boundaries among n cells are strictly increasing.  Subtracting
    the endpoints produces positive lengths; all three occupied runs must
    have length at least two.  Every such pattern occurs exactly once.
    """
    for e1, e2, e3, e4 in combinations(range(1, n), 4):
        a, g, b, h, c = e1, e2-e1, e3-e2, e4-e3, n-e4
        if min(a, b, c) < 2:
            continue
        v = (a, g, b, h, c)
        if v <= tuple(reversed(v)):
            yield v


def cells(runs):
    a, g, b, h, c = runs
    return [1]*a + [0]*g + [1]*b + [0]*h + [1]*c


def signature_dot(runs):
    v = cells(runs)
    return tuple(sum(v[j]*v[j+k] for j in range(len(v)-k))
                 for k in range(len(v)))


def signature_bits(runs):
    v = cells(runs)
    bitmap = sum(bit << i for i, bit in enumerate(v))
    return tuple((bitmap & (bitmap >> k)).bit_count()
                 for k in range(len(v)))


def direct_ambiguous_classes(n):
    groups = defaultdict(list)
    for runs in admissible(n):
        groups[signature_dot(runs)].append(runs)
        assert signature_dot(runs) == signature_bits(runs)
        assert len(cells(runs)) == n
        assert cells(runs)[0] == cells(runs)[-1] == 1
    return groups


def independent_enumeration(n):
    """A second loop over compositions (not the breakpoint construction)."""
    groups = defaultdict(list)
    for a in range(2, n-5):
        for g in range(1, n-5):
            for b in range(2, n-5):
                for h in range(1, n-5):
                    c = n-a-g-b-h
                    if c < 2:
                        continue
                    runs = (a, g, b, h, c)
                    if runs <= (c, h, b, g, a):
                        groups[signature_bits(runs)].append(runs)
    return groups


def main():
    total = 0
    for n in range(MIN_N, MAX_N+1):
        groups = direct_ambiguous_classes(n)
        groups2 = independent_enumeration(n)
        assert groups == groups2, ('independent enumeration mismatch', n)
        profiles = (sum(len(v) for v in groups.values()), len(groups))
        assert profiles == EXPECTED[n], (n, profiles)
        assert all(len(v) == 1 for v in groups.values()) if n < 19 else True
        if n == 19:
            ambiguous = [sorted(v) for v in groups.values() if len(v) > 1]
            assert ambiguous == [list(PAIR)], ambiguous
            assert signature_dot(PAIR[0]) == TARGET_CORRELATION
            assert signature_dot(PAIR[1]) == TARGET_CORRELATION
        total += profiles[0]
        print('length=%02d classes=%d autocorrelations=%d' %
              (n, profiles[0], profiles[1]))
    assert total == sum(c for c, _ in EXPECTED.values())
    print('CHECK_OK lengths=8..19 normalized_masks=%d ambiguity_classes_at_19=1' % total)

if __name__ == '__main__':
    main()
