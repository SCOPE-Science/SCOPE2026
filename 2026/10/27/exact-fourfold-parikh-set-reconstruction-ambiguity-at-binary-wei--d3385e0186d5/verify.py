"""Exhaustive direct check of fixed-weight-three Parikh-set reconstruction.

This verifier uses actual substring compositions, without using the proof's
maximum/minimum window formulas. Run: python3 verify.py
"""
from collections import Counter, defaultdict
from itertools import combinations
from math import comb


def bits_from_gaps(g):
    a, b, c, d = g
    return '0' * a + '1' + '0' * b + '1' + '0' * c + '1' + '0' * d


def parikh_set(w):
    spectrum = set()
    for i in range(len(w) + 1):
        count_ones = 0
        for j in range(i, len(w)):
            count_ones += w[j] == '1'
            spectrum.add((j - i + 1, count_ones))
    return frozenset(spectrum)


def predicted_class(g):
    a, b, c, d = g
    members = {(a, b, c, d), (d, c, b, a)}
    if min(b, c) >= max(a, d):
        members |= {(a, c, b, d), (d, b, c, a)}
    return frozenset(bits_from_gaps(t) for t in members)


def four_class_count_formula(n):
    if n < 7:
        return 0
    ways = 0
    target = n - 7
    for x in range(target // 4 + 1):
        for y in range((target - 4 * x) // 3 + 1):
            for z in range((target - 4 * x - 3 * y) // 2 + 1):
                t = target - 4 * x - 3 * y - 2 * z
                if t >= 0:
                    ways += 1
    return ways


def main():
    total_words = 0
    total_classes = 0
    for n in range(3, 25):
        groups = defaultdict(set)
        for p, q, r in combinations(range(n), 3):
            g = (p, q - p - 1, r - q - 1, n - r - 1)
            w = bits_from_gaps(g)
            groups[parikh_set(w)].add(w)
            total_words += 1
        spectrum = Counter(map(len, groups.values()))
        assert set(spectrum).issubset({1, 2, 4}), (n, spectrum)
        singleton = ((n - 1) // 2) if n % 2 else 0
        four = four_class_count_formula(n)
        two = (comb(n, 3) - singleton - 4 * four) // 2
        assert spectrum == Counter({1: singleton, 2: two, 4: four}) - Counter(), (n, spectrum, singleton, two, four)
        for members in groups.values():
            for w in members:
                ones = [i for i, v in enumerate(w) if v == '1']
                g = (ones[0], ones[1] - ones[0] - 1, ones[2] - ones[1] - 1, n - ones[2] - 1)
                assert predicted_class(g) == frozenset(members), (n, g, members)
        total_classes += len(groups)
    print(f'PASS: all {total_words} three-one words at lengths 3..24, all {total_classes} Parikh-set classes; every fiber and three class-size counts match.')


if __name__ == '__main__':
    main()
