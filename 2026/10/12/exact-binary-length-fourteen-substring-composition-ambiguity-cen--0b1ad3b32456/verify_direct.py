#!/usr/bin/env python3
"""Exact census of binary length-14 all-substring-composition fibers."""
from collections import defaultdict, Counter
from itertools import product
import json

N = 14

def signature(bits):
    # For each length and number of ones, retain the exact multiplicity.
    out = []
    for width in range(1, N + 1):
        counts = [0] * (width + 1)
        for left in range(N - width + 1):
            ones = sum(bits[left:left + width])
            counts[ones] += 1
        out.extend(counts)
    return tuple(out)

def run():
    fibers = defaultdict(list)
    for bits in product((0, 1), repeat=N):
        fibers[signature(bits)].append(''.join(map(str, bits)))
    histogram = Counter(map(len, fibers.values()))
    assert histogram == {1: 128, 2: 8104, 4: 12}, histogram
    assert sum(k*v for k, v in histogram.items()) == 2**N
    fours = sorted(sorted(c) for c in fibers.values() if len(c) == 4)
    assert len(fours) == 12
    assert all(''.join(reversed(w)) in c for c in fours for w in c)
    print(json.dumps({'n': N, 'number_of_words': 2**N,
        'number_of_profiles': len(fibers), 'size_histogram': {str(k): histogram[k] for k in sorted(histogram)},
        'maximum_fiber': max(histogram), 'four_word_classes': fours},
        sort_keys=True, separators=(',', ':')))

if __name__ == '__main__':
    run()
