"""Exact finite tests for binary dyadic Haar magnitude fibers. Python 3 stdlib."""
from collections import Counter, defaultdict
from fractions import Fraction


def signature(bits):
    """Root total and level-by-level absolute unnormalized Haar contrasts."""
    layer = tuple(bits)
    details = []
    while len(layer) > 1:
        details.extend(abs(layer[j] - layer[j + 1]) for j in range(0, len(layer), 2))
        layer = tuple(layer[j] + layer[j + 1] for j in range(0, len(layer), 2))
    return layer[0], *details


def balanced_splits(bits):
    length = len(bits)
    if length == 1:
        return 0
    half = length // 2
    left, right = bits[:half], bits[half:]
    lsum, rsum = sum(left), sum(right)
    return int(lsum + rsum == half and lsum != rsum) + balanced_splits(left) + balanced_splits(right)


def enumerate_length(length):
    groups = defaultdict(list)
    for integer in range(1 << length):
        bits = tuple((integer >> j) & 1 for j in range(length))
        groups[signature(bits)].append((integer, bits))
    histogram = Counter()
    weight_max = {k: 0 for k in range(length + 1)}
    singleton_signals = set()
    for sig, group in groups.items():
        size = len(group)
        assert size & (size - 1) == 0
        histogram[size] += 1
        for integer, bits in group:
            b = balanced_splits(bits)
            k = sum(bits)
            assert size == 1 << b, (length, bits, size, b)
            assert b <= min(k, length-k), (length,bits,b)
            weight_max[k] = max(weight_max[k], size)
            if size == 1:
                singleton_signals.add(integer)
    assert all(weight_max[k] == 1 << min(k,length-k) for k in weight_max)
    assert singleton_signals == {0, (1 << length) - 1}
    assert max(histogram) == 1 << (length // 2)
    assert histogram[1 << (length // 2)] == 1
    alternating = tuple(j % 2 for j in range(length))
    assert len(groups[signature(alternating)]) == (1 << (length // 2))
    print(length, 'signatures', len(groups), 'fiber_histogram', dict(sorted(histogram.items())))


def local_parseval(bits):
    """Prove the integer-scale Parseval identity at every dyadic subtree."""
    length = len(bits)
    s = sum(bits)
    if length == 1:
        assert s*length == s*s
        return 0
    half = length // 2
    a, b = bits[:half], bits[half:]
    details_num = (sum(a) - sum(b)) ** 2
    variance = Fraction(details_num, length) + local_parseval(a) + local_parseval(b)
    assert Fraction(s) - Fraction(s*s,length) == variance
    return variance


if __name__ == '__main__':
    for length in (2,4,8,16):
        enumerate_length(length)
    for length in (2,4,8):
        for mask in range(1 << length):
            local_parseval(tuple((mask >> j) & 1 for j in range(length)))
    print('PASS: exact full-length fiber census through length 16 and subtree Parseval tests')
