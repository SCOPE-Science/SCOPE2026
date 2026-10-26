#!/usr/bin/env python3
"""Reproduce distinct scattered-subsequence counts for complement-doubling words.

No packages beyond the Python standard library are required.
"""
from itertools import product


def complement(word):
    return word.translate(str.maketrans('01', '10'))


def counts_from_last_occurrence(word):
    # T[i] counts distinct subsequences, including the empty subsequence,
    # of the first i symbols. This is independent of the trace recurrence.
    totals = [1]
    last = {}
    for position, symbol in enumerate(word):
        nxt = 2 * totals[-1]
        if symbol in last:
            nxt -= totals[last[symbol]]
        last[symbol] = position
        totals.append(nxt)
    return totals[-1] - 1


def brute_subsequences(word):
    pool = {''}
    for symbol in word:
        pool |= {prefix + symbol for prefix in pool}
    return len(pool) - 1


def trace_pair(word):
    # Multiply 2x2 letter-shear matrices on the LEFT, starting at identity.
    a, b, c, d = 1, 0, 0, 1
    for x in word:
        if x == '0':
            a, b, c, d = a + c, b + d, c, d
        else:
            a, b, c, d = a, b, a + c, b + d
    return a + d, b + c


def check(seed, rounds):
    word = seed
    s, t = trace_pair(seed)
    for m in range(rounds):
        assert trace_pair(word) == (s, t), (seed, m, 'matrix')
        expected = s + t - 2
        assert counts_from_last_occurrence(word) == expected, (seed, m, 'last-occurrence')
        if len(word) <= 16:
            assert brute_subsequences(word) == expected, (seed, m, 'exhaustive set')
        s, t = t * t + 2, s * t
        word += complement(word)


def run():
    tested = 0
    for size in range(1, 7):
        for bits in product('01', repeat=size):
            seed = ''.join(bits)
            check(seed, 5 if size <= 2 else 4 if size <= 4 else 3)
            tested += 1
    check('0', 13)  # Includes a length-4096 block.
    check('01001', 8)  # Nontrivial non-singleton seed.
    s, t = 2, 1
    observed = []
    for _ in range(7):
        observed.append(s + t - 2)
        s, t = t * t + 2, s * t
    assert observed == [1, 3, 10, 72, 2664, 3647088, 6476006417760]
    print(f'VERIFY_OK exhaustive_seeds={tested} Thue_Morse_prefix_length=4096')


if __name__ == '__main__':
    run()
