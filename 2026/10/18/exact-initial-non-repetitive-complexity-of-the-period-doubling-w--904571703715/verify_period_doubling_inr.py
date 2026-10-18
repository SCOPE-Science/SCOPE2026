#!/usr/bin/env python3
"""Exact finite cross-checks for a formula concerning period-doubling factors.

This finite test is complementary to, not a substitute for, the mathematical
proof of the all-length formula.
"""


def substitution_prefix(length):
    word = bytes((0,))
    while len(word) < length:
        block = bytearray(2 * len(word))
        block[::2] = bytes(len(word))
        block[1::2] = bytes(1 - a for a in word)
        word = bytes(block)
    return word[:length]


def valuation_prefix(length):
    def v2(n):
        return (n & -n).bit_length() - 1
    return bytes(v2(j + 1) % 2 for j in range(length))


def predicted(n):
    if n == 1:
        return 2, 0
    k = n.bit_length() - 1
    threshold = 3 * (1 << (k - 1))
    if n < threshold:
        return threshold, (1 << k)
    return 1 << (k + 1), 0


def first_collision(word, n, safety):
    seen = {}
    for start in range(safety + 1):
        factor = word[start:start+n]
        earlier = seen.get(factor)
        if earlier is not None:
            return start, earlier
        seen[factor] = start
    raise AssertionError('No repetition within expected bound')


def run():
    nmax = 8192
    large = [512, 513, 767, 768, 1023, 1024, 1535, 1536,
             2047, 2048, 3071, 3072, 4095, 4096, 6143, 6144, 8191, 8192]
    lengths = sorted(set(range(1, 257)) | set(large))
    L = max(n + predicted(n)[0] + 1 for n in lengths)
    word = substitution_prefix(L)
    independently = valuation_prefix(L)
    assert word == independently, 'Independent word constructions disagree'
    assert all(word[2*j] == 0 and word[2*j+1] == 1-word[j] for j in range((L-1)//2))
    for n in lengths:
        exp_start, exp_match = predicted(n)
        start, earlier = first_collision(word, n, exp_start)
        assert (start, earlier) == (exp_start, exp_match), (n, start, earlier, exp_start, exp_match)
        assert 0 <= earlier < start
    for n in range(4, 257):
        assert predicted(n)[0] == 2 * predicted(n//2)[0]
        assert predicted(n)[1] == 2 * predicted(n//2)[1]
    print('VERIFY_OK; independent_generators=2; exhaustive_lengths=1..256; extra_lengths=%d; maximum_length=%d' %
          (len(large), max(lengths)))


if __name__ == '__main__':
    run()
