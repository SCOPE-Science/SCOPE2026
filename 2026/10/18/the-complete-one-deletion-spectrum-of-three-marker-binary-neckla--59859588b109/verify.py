#!/usr/bin/env python3
"""Direct finite checks for a circular binary single-deletion theorem.

No scientific or review status is assigned by this script. The infinite
classification follows from a combinatorial proof in RESULT.md.
"""
from collections import Counter
from math import comb
from random import Random


def rotations(t):
    return [t[i:] + t[:i] for i in range(len(t))]


def canonical(t):
    return min(rotations(t))


def cyclic_descendants(gaps):
    word = ''.join('1' + '0' * x for x in gaps)
    return {canonical(word[:i] + word[i+1:]) for i in range(len(word))}


def gap_count(gaps):
    zero = set()
    for i in range(3):
        if gaps[i] > 0:
            modified = tuple(gaps[j] - (i == j) for j in range(3))
            zero.add(canonical(modified))
    total = sum(gaps)
    one = {min(x, total-x) for x in gaps}
    return len(zero) + len(one)


def classification(gaps):
    s = sum(gaps)
    if s == 0:
        return 1
    positives = [x for x in gaps if x > 0]
    if len(positives) == 1:
        return 2
    if len(positives) == 2:
        return 3 if sorted(gaps) == [0, 1, 1] else 4
    counts = Counter(gaps)
    if len(counts) == 1:
        return 2
    if len(counts) == 3:
        return 6
    repeated = next(x for x in counts if counts[x] == 2)
    singleton = next(x for x in counts if counts[x] == 1)
    return 4 if singleton == repeated-1 else 5


def expected_histogram(s):
    if s == 0:
        return Counter({1: 1})
    equal = int(s % 3 == 0)
    exceptional = int(s >= 5 and s % 3 == 2)
    small = int(s == 2)
    out = {
        2: 1 + equal,
        3: small,
        4: s - 1 - small + exceptional,
        5: (s-1)//2 - equal - exceptional,
        6: (comb(s-1, 2) if s >= 3 else 0)//3
    }
    # The last class counts all ordered positive distinct triples, /3.
    out[6] = ((comb(s-1, 2) if s >= 3 else 0)
              - 3*((s-1)//2) + 2*equal)//3
    assert all(v >= 0 for v in out.values()), (s, out)
    return Counter({key: count for key, count in out.items() if count})


def check(s):
    seen = Counter()
    objects = 0
    for a in range(s+1):
        for b in range(s-a+1):
            g = (a, b, s-a-b)
            if g != canonical(g):
                continue
            c1 = len(cyclic_descendants(g))
            c2 = gap_count(g)
            c3 = classification(g)
            assert c1 == c2 == c3, (s, g, c1, c2, c3)
            seen[c1] += 1
            objects += 1
    assert seen == expected_histogram(s), (s, seen, expected_histogram(s))
    necklace_count = (comb(s+2, 2)+2*int(s % 3 == 0)) // 3
    assert objects == necklace_count, (s, objects, necklace_count)
    return objects


def main():
    total = sum(check(s) for s in range(37))
    rng = Random(20261016)
    samples = 0
    for s in [45, 61, 90, 128, 256]:
        for _ in range(90):
            a = rng.randrange(s+1)
            b = rng.randrange(s-a+1)
            g = (a, b, s-a-b)
            assert len(cyclic_descendants(g)) == classification(g)
            samples += 1
    print('PASS circular one-deletion three-marker profile: '
          f'complete_zero_totals=0..36 necklaces={total} '
          f'random_larger_cases={samples}')


if __name__ == '__main__':
    main()
