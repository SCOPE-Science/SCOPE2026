#!/usr/bin/env python3
"""Exact checks of four-digit Kaprekar stable-region entrance counts.

No external dependencies or network access. The argument for all bases is in RESULT.md.
"""
from collections import Counter
from itertools import product


def iterate_word(base, digits):
    ordered = sorted(digits)
    ascending = sum(v * base ** (3 - i) for i, v in enumerate(ordered))
    descending = sum(v * base ** (3 - i) for i, v in enumerate(reversed(ordered)))
    value = descending - ascending
    result = []
    for _ in range(4):
        result.append(value % base)
        value //= base
    assert value == 0
    return result


def differences(word):
    a, b, c, d = sorted(word, reverse=True)
    return a - d, b - c


def entrance_time(base, word):
    for time in range(4):
        d, e = differences(word)
        if d > e > 0 and d % 2 == 1 and e % 2 == 1:
            return time
        word = iterate_word(base, word)
    raise AssertionError(f"outside stable region after 3 steps: {base},{word}")


def predicted(base):
    m = (base - 1) // 2
    delta = int(m % 2 == 0)
    states0 = m * (m - 1) // 2
    states2 = 4 * m - delta
    states3 = 1
    states1 = m * (2 * m + 3) - states0 - states2 - states3
    words0 = 4 * m * (m - 1) * (m + 1) * (m + 2)
    words2 = 16*m**3 + 32*m**2 + 10*m - delta * (12*m**2 + 8*m)
    words3 = 4*m*(3*m+2)
    words1 = base**4 - base - words0 - words2 - words3
    return [states0, states1, states2, states3], [words0, words1, words2, words3]


def weight(base, d, e):
    if e == 0:
        return (base-d)*(12*d-4)
    if e == d:
        return 6*(base-d)
    return 24*(base-d)*(d-e)


def check():
    total_states = 0
    for base in range(5, 102, 2):
        states = Counter()
        weighted = Counter()
        exceptional = []
        for d in range(1, base):
            for e in range(d+1):
                t = entrance_time(base, [d, e, 0, 0])
                states[t] += 1
                weighted[t] += weight(base,d,e)
                if t == 3:
                    exceptional.append((d,e))
        expected_states, expected_words = predicted(base)
        assert [states[t] for t in range(4)] == expected_states, (base,states)
        assert [weighted[t] for t in range(4)] == expected_words, (base,weighted)
        assert exceptional == [((base+1)//2, 0)], (base,exceptional)
        assert sum(weighted.values()) == base**4-base
        total_states += sum(states.values())
    for base in (5, 7, 9, 11):
        brute = Counter()
        for word in product(range(base), repeat=4):
            if len(set(word)) == 1:
                continue
            brute[entrance_time(base, word)] += 1
        assert [brute[t] for t in range(4)] == predicted(base)[1], (base,brute)
        print('base',base,'word_counts',*[brute[t] for t in range(4)])
    print('VERIFY_OK bases_5_through_101_odd=49 state_pairs=',total_states,
          'direct_word_bases=5,7,9,11 all_counts_exact=yes')


if __name__ == '__main__':
    check()
