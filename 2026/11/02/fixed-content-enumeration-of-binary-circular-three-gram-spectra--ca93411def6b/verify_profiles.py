#!/usr/bin/env python3
"""Independent finite checks for the circular binary three-gram spectrum formula.

No external packages or downloaded data are needed.
"""
from collections import defaultdict
from itertools import product


def histogram(bits):
    n = len(bits)
    assert n >= 1
    out = [0] * 8
    for i in range(n):
        out[(bits[i] << 2) | (bits[(i + 1) % n] << 1) | bits[(i + 2) % n]] += 1
    return tuple(out)


def predicted(p, q):
    """Coefficient of X^p Y^q from the five disjoint flow regimes."""
    if p + q == 0:
        return 0
    count = int(p == 0) + int(q == 0) + int(p == q and p > 0)
    # The 00--01--10 component with t>0 and s=0.
    for t in range(1, min(q, p // 2) + 1):
        f = q - t
        a = p - 2 * t - f
        if a >= 0:
            count += 1
    # Its bit-complemented 01--11--10 component.
    for s in range(1, min(p, q // 2) + 1):
        c = p - s
        h = q - 2 * s - c
        if h >= 0:
            count += 1
    # The entire strongly connected four-vertex component.
    for t in range(1, p // 2 + 1):
        for s in range(1, q + 1):
            for f in range(max(0, s - t), min(p - 2 * t, q - t - s) + 1):
                count += 1
    return count


def possible_histograms(n):
    for t in range(n + 1):
        for s in range(n + 1):
            for f in range(n + 1):
                c = t + f - s
                if c < 0:
                    continue
                base = 3 * t + s + 2 * f
                if base > n:
                    continue
                for a in range(n - base + 1):
                    h = n - base - a
                    if t and s:
                        pass
                    elif t:
                        if h:
                            continue
                    elif s:
                        if a:
                            continue
                    elif c:
                        if a or h:
                            continue
                    elif a and h:
                        continue
                    yield (a, t, c, s, t, f, s, h)


def reconstruct(hist):
    """Build an Eulerian circuit independently from a histogram."""
    outgoing = [[] for _ in range(4)]
    for triple, amount in enumerate(hist):
        outgoing[triple >> 1].extend([triple] * amount)
    n = sum(hist)
    start = next(v for v in range(4) if outgoing[v])
    todo = [start]
    finished = []
    while todo:
        v = todo[-1]
        if outgoing[v]:
            triple = outgoing[v].pop()
            todo.append(triple & 3)
        else:
            finished.append(todo.pop())
    finished.reverse()
    assert len(finished) == n + 1
    assert finished[0] == finished[-1]
    bits = tuple(v >> 1 for v in finished[:-1])
    assert histogram(bits) == hist
    return bits


def min_rotation(word):
    return min(word[i:] + word[:i] for i in range(len(word)))


def main():
    expected = [2, 3, 4, 6, 8, 13, 18, 27, 38, 53, 72, 98, 128, 167, 214, 271, 338, 419]
    total_words = 0
    for n, reference in enumerate(expected, 1):
        observed = defaultdict(set)
        for bits in product((0, 1), repeat=n):
            observed[sum(b == 0 for b in bits)].add(histogram(bits))
            total_words += 1
        assert sum(map(len, observed.values())) == reference
        for p in range(n + 1):
            assert len(observed[p]) == predicted(p, n - p), (n, p)
        if n <= 6:
            sizes = defaultdict(set)
            for bits in product((0, 1), repeat=n):
                sizes[histogram(bits)].add(min_rotation(bits))
            if n <= 5:
                assert all(len(s) == 1 for s in sizes.values())
            else:
                assert sorted(len(s) for s in sizes.values()) == [1] * 12 + [2]

    constructed = 0
    for n in range(1, 23):
        histograms = set(possible_histograms(n))
        assert len(histograms) == sum(predicted(p, n - p) for p in range(n + 1)), n
        for hist in histograms:
            reconstruct(hist)
            constructed += 1

    for n in range(6, 27):
        w = tuple(map(int, '0' * (n - 4) + '1011'))
        v = tuple(map(int, '0' * (n - 4) + '1101'))
        assert histogram(w) == histogram(v)
        assert min_rotation(w) != min_rotation(v)
    print('VERIFY_OK; direct_words=%d; constructed_profiles=%d; n<=18; constructions<=22; padded_pairs<=26' % (total_words, constructed))


if __name__ == '__main__':
    main()
