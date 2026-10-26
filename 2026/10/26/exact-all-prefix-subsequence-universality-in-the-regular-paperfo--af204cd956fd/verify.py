"""Reproducibility checks for the paperfolding prefix subsequence-universality formula.

Run with Python 3, no external packages: python verify.py
"""
from itertools import product


def arithmetic_symbol(z):
    v = z + 1
    while v % 2 == 0:
        v //= 2
    return '1' if v % 4 == 1 else '0'


def folding_word(level):
    w = ''
    for _ in range(level):
        w += '1' + ''.join('0' if c == '1' else '1' for c in w[::-1])
    return w


def odd_part(k):
    assert k >= 1
    while k % 2 == 0:
        k //= 2
    return k


def proposed_index(n):
    if n == 0:
        return 0
    result = (3 * n + 1) // 8
    if n % 16 == 5:
        result -= 1
    if n % 8 == 0 and odd_part(n // 8) % 4 == 3:
        result -= 1
    return result


def scan(word, start=''):
    completed = 0
    memory = start
    for symbol in word:
        if not memory:
            memory = symbol
        elif memory != symbol:
            completed += 1
            memory = ''
    return completed, memory


def is_subsequence(needle, haystack):
    pos = 0
    for symbol in haystack:
        if pos < len(needle) and symbol == needle[pos]:
            pos += 1
    return pos == len(needle)


def independent_universality(prefix):
    k = 0
    while all(is_subsequence(''.join(w), prefix) for w in product('01', repeat=k + 1)):
        k += 1
    return k


def test():
    n = (1 << 18) - 1
    word = folding_word(18)
    assert len(word) == n
    assert all(word[i] == arithmetic_symbol(i) for i in range(n))
    print('VERIFY_OK independent_paperfolding_generators_length=262143')

    # Entire transition table of each possible eight-symbol aligned block.
    for a, b in product('01', repeat=2):
        block = '110' + a + '100' + b
        for state in ('', '0'):
            count, output = scan(block, state)
            assert (count, output) == (2 + int(b) + (state == '0'), '' if b == '1' else '0')
            for r in range(1, 8):
                extra, _ = scan(block[:r], state)
                expected = (state == '0') + [None, 0, 0, 1, 1, 2 - int(a), 2, 2][r]
                assert extra == expected
    print('VERIFY_OK all_four_aligned_block_types_both_reachable_states_all_prefix_offsets')

    current = ''
    number_of_arches = 0
    max_minus = (0, 0)
    max_plus = (0, 0)
    for j, symbol in enumerate(word, start=1):
        if current == '':
            current = symbol
        elif current != symbol:
            number_of_arches += 1
            current = ''
        expected = proposed_index(j)
        assert number_of_arches == expected, (j, number_of_arches, expected)
        discrepancy = 8 * number_of_arches - 3 * j
        if discrepancy < max_minus[0]:
            max_minus = (discrepancy, j)
        if discrepancy > max_plus[0]:
            max_plus = (discrepancy, j)
    assert max_minus[0] == -8 and max_plus[0] == 1
    print('VERIFY_OK exact_all_prefix_formula_lengths=1..262143; sharp_discrepancies=-1,+1/8')

    for length in range(0, 29):
        prefix = word[:length]
        actual = independent_universality(prefix)
        assert actual == proposed_index(length), (length, actual, proposed_index(length))
    print('VERIFY_OK direct_all_binary_subsequence_enumeration_prefix_lengths=0..28')

    for k in range(3, 18):
        assert proposed_index(1 << k) == 3 * (1 << (k - 3))
    print('VERIFY_OK dyadic_prefix_formula_k=3..17')
    print('VERIFY_OK')


if __name__ == '__main__':
    test()
