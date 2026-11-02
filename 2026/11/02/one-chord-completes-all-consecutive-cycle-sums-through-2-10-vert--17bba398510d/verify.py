#!/usr/bin/env python3
"""Replays an exact finite one-chord completion certificate, using Python 3 stdlib."""
from array import array
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LIMIT = 1024


def bits_to_integer(words):
    return int.from_bytes(words.tobytes(), 'little')


def cycle_sums(n):
    total = n * (n + 1) // 2
    words = array('Q', [0]) * ((total + 64) // 64)
    # All n cyclic starting vertices at each arc length k.
    for k in range(1, n + 1):
        first = k * (k + 1) // 2
        for i in range(n - k + 1):
            s = first + k * i
            words[s >> 6] |= 1 << (s & 63)
        for i in range(n - k + 1, n):
            s = first + k * i - n * (i + k - n)
            words[s >> 6] |= 1 << (s & 63)
    return bits_to_integer(words)


def prefix_suffix_sums(lo, hi):
    seq = list(range(lo, hi + 1))
    L = len(seq)
    left = [0]
    right = [0]
    for x in seq:
        left.append(left[-1] + x)
    for x in reversed(seq):
        right.append(right[-1] + x)
    return {left[a] + right[b]
            for a in range(L + 1) for b in range(L - a + 1)}


def chord_sums(n, q):
    # The two arcs between 1 and q have interior vertex sets [2,q-1] and
    # [q+1,n]. Prefixes and suffixes from these interiors, plus {1,q},
    # are connected via the new chord. No wrapping of vertex weights.
    total = n * (n + 1) // 2
    words = array('Q', [0]) * ((total + 64) // 64)
    L = n - q
    # Prefix a of [q+1,n] and suffix b, with a+b<=L.
    for a in range(L + 1):
        start_sum = a * (2 * q + a + 1) // 2
        for b in range(L - a + 1):
            s = start_sum + b * (2 * n - b + 1) // 2
            words[s >> 6] |= 1 << (s & 63)
    second_arc = bits_to_integer(words)
    first_arc = prefix_suffix_sums(2, q-1)
    out = 0
    for first in first_arc:
        out |= second_arc << (q + 1 + first)
    return out


def brute_connected_sums(n, q):
    # An unrelated direct connectivity test for small n, not used by the
    # main verification. It enumerates every vertex subset.
    neighborhood = [0] * n
    for i in range(n):
        neighborhood[i] |= 1 << ((i + 1) % n)
        neighborhood[i] |= 1 << ((i - 1) % n)
    neighborhood[0] |= 1 << (q-1)
    neighborhood[q-1] |= 1
    sums = {0}
    for subset in range(1, 1 << n):
        seen = subset & -subset
        fringe = seen
        while fringe:
            vbit = fringe & -fringe
            fringe -= vbit
            v = vbit.bit_length() - 1
            more = neighborhood[v] & subset & ~seen
            seen |= more
            fringe |= more
        if seen == subset:
            value = sum(i+1 for i in range(n) if subset & (1 << i))
            sums.add(value)
    return sums


def main():
    path = ROOT / 'chords.txt'
    lines = [z for z in path.read_text(encoding='ascii').splitlines()
             if z and not z.startswith('#')]
    records = [tuple(map(int, z.split())) for z in lines]
    assert len(records) == 1017
    assert [n for n, q in records] == list(range(8, LIMIT + 1))
    for n, q in records:
        assert 3 <= q <= n - 2, (n, q)  # an actual non-cycle edge
        total = n * (n + 1) // 2
        required = (1 << (total + 1)) - 2  # bits 1..total, nothing else
        achieved = cycle_sums(n) | chord_sums(n, q)
        missing = required & ~achieved
        assert missing == 0, (n, q, missing.bit_length())
    witnesses = dict(records)
    for n in (8, 12, 16):
        assert brute_connected_sums(n, witnesses[n]) == set(range(n*(n+1)//2 + 1))
    print('VERIFY_OK n=8..1024 count=1017 max_target=524800'
          ' one_chord_witnesses=PASS bitset_complete=PASS'
          ' brute_subset_check=8,12,16 finite_only=YES')


if __name__ == '__main__':
    main()
