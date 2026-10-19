"""Finite cross-checks for exact string-attractor classification of Zimin words.

Run: python3 check.py
The theorem for arbitrary order uses a separate structural proof.
"""
from collections import defaultdict
from itertools import product


def zimin(n):
    assert n >= 1
    w = (1,)
    for j in range(2, n + 1):
        w = w + (j,) + w
    return w


def factor_coverages(w):
    result = defaultdict(int)
    N = len(w)
    for left in range(N):
        for right in range(left + 1, N + 1):
            mask = ((1 << (right - left)) - 1) << left
            result[w[left:right]] |= mask
    return result


def minimal_coverages(masks):
    ordered = sorted(set(masks), key=lambda m: (m.bit_count(), m))
    return {m for m in ordered if not any(a & m == a for a in ordered if a != m)}


def verify(n):
    w = zimin(n)
    N = len(w)
    groups = [tuple(i for i, letter in enumerate(w) if letter == k) for k in range(1, n + 1)]
    letter_masks = {sum(1 << p for p in group) for group in groups}
    cov = factor_coverages(w)
    assert minimal_coverages(cov.values()) == letter_masks
    assert all(any((c & group_mask) == group_mask for group_mask in letter_masks) for c in cov.values())

    # Check every minimum-cardinality set using the actual distinct-factor coverage masks.
    count = 0
    min_span = N
    min_span_count = 0
    for chosen in product(*groups):
        mask = sum(1 << p for p in chosen)
        assert all(mask & c for c in cov.values())
        count += 1
        spread = max(chosen) - min(chosen)
        if spread < min_span:
            min_span, min_span_count = spread, 1
        elif spread == min_span:
            min_span_count += 1
    predicted = 1 << (n * (n - 1) // 2)
    assert count == predicted
    expected_span = 0 if n == 1 else 1 << (n - 2)
    expected_span_count = 1 if n == 1 else 1 << (1 + (n - 2) * (n - 3) // 2)
    assert (min_span, min_span_count) == (expected_span, expected_span_count)
    return (n, N, len(cov), len(letter_masks), count, min_span, min_span_count)


if __name__ == '__main__':
    print('order | length | distinct factors | minimal coverages | optimum attractors | min span | min-span optimum attractors')
    for n in range(1, 7):
        print(' | '.join(map(str, verify(n))))
    print('All independent finite coverage, counting, and span checks passed.')
