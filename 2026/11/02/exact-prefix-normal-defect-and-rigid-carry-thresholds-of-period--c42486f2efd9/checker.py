#!/usr/bin/env python3
"""Independent finite checks for prefix-normal excess in period-doubling prefixes.

Uses both the substitution definition and an arithmetic definition, and
exhaustive enumeration of factor intervals.  These finite checks support but
do not replace the unrestricted carry proof in RESULT.md.
"""

def substitution_word(cap):
    s = '0'
    while len(s) < cap:
        s = ''.join('01' if b == '0' else '00' for b in s)
    return s[:cap]


def arithmetic_bit(i):
    n = i + 1
    return int(((n & -n).bit_length() - 1) % 2 == 1)


def floor_count(n):
    total = 0
    j = 1
    while 2**j <= n:
        total += (1 if j % 2 else -1) * (n >> j)
        j += 1
    return total


def threshold(N):
    t, s = 0, 0
    while s * 4 + 2 <= N:
        s = 4 * s + 2
        t += 1
    return t


def main():
    MAX = 4096
    w = substitution_word(MAX)
    prefix = [0]
    for i, b in enumerate(w):
        assert int(b) == arithmetic_bit(i), ('substitution', i)
        prefix.append(prefix[-1] + int(b))
        assert prefix[-1] == floor_count(i + 1), ('floor', i)

    max_so_far = 0
    first = {}
    for x in range(1, MAX+1):
        best_at_x = -10**9
        for a in range(x):
            length = x-a
            excess = prefix[x] - prefix[a] - prefix[length]
            if excess > best_at_x:
                best_at_x = excess
            odd_bit_popcount = ((x & 0xAAAAAAAAAAAAAAAA) >> 1).bit_count()
            # x is at most 4096, so a 64-bit mask suffices here.
            assert excess <= odd_bit_popcount, ('carry-bound', x, a)
        max_so_far = max(max_so_far, best_at_x)
        assert max_so_far == threshold(x), ('threshold', x, max_so_far, threshold(x))
        if max_so_far not in first:
            first[max_so_far] = x
    for t in range(1, threshold(MAX)+1):
        a = (4**t - 1) // 3
        x = 2*a
        assert first[t] == x, ('sharp cutoff', t)
        assert prefix[x] - prefix[a] - prefix[a] == t, ('witness', t)
    print('PASS: substitution/arithmetic symbols and counts for 4096 positions')
    print('PASS: exhaustive interval, carry bound, and sharp-threshold tests over all 4096 prefix lengths')
    print('PASS: exact cutoff witnesses', [first[t] for t in range(1, threshold(MAX)+1)])

if __name__ == '__main__':
    main()
