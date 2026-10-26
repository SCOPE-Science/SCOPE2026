#!/usr/bin/env python3
"""Independent exact finite-window checks for cyclic classes of the period-doubling word."""
from collections import defaultdict


def image(word):
    return ''.join('01' if letter == '0' else '00' for letter in word)


def arithmetic_symbol(index):
    n = index + 1
    exponent = 0
    while n % 2 == 0:
        exponent += 1
        n //= 2
    return str(exponent % 2)


def necklace(word):
    """Lexicographically least rotation (Booth's linear-time algorithm)."""
    length = len(word)
    doubled = word + word
    first, second, offset = 0, 1, 0
    while first < length and second < length and offset < length:
        a = doubled[first + offset]
        b = doubled[second + offset]
        if a == b:
            offset += 1
        elif a > b:
            first = first + offset + 1
            if first <= second:
                first = second + 1
            offset = 0
        else:
            second = second + offset + 1
            if second <= first:
                second = first + 1
            offset = 0
    position = min(first, second)
    return doubled[position:position + length]


def complete_factors(length, blocks):
    """All factors of given length, via a complete aligned two-block cover."""
    return {
        block[start:start + length]
        for block in blocks
        for start in range(len(block) - length + 1)
    }


def main():
    prefix = '0'
    for _ in range(16):
        prefix = image(prefix)
    assert len(prefix) == 65536
    assert prefix == ''.join(arithmetic_symbol(i) for i in range(len(prefix)))
    print('VERIFY_OK two_independent_generators=65536_symbols')

    assert {prefix[i:i + 2] for i in range(len(prefix) - 1)} == {'00', '01', '10'}
    unit = '0'
    for _ in range(8):
        unit = image(unit)
    # The two blocks are images of all three adjacent source pairs; the
    # fixed point is a concatenation of length-256 substitution images.
    level = {letter: image('0') for letter in '01'}
    block0, block1 = '0', '1'
    for _ in range(8):
        block0, block1 = image(block0), image(block1)
    templates = [left + right for left in (block0, block1)
                 for right in (block0, block1)
                 if ('0' if left == block0 else '1') +
                    ('0' if right == block0 else '1') in {'00', '01', '10'}]
    assert len(templates) == 3 and all(len(t) == 512 for t in templates)
    print('VERIFY_OK complete_source_pairs=00,01,10 aligned_templates=3 block_size=256')

    complexity = {}
    spread = {0: 0}
    for n in range(1, 129):
        factors = complete_factors(n, templates)
        complexity[n] = len({necklace(x) for x in factors})
        counts = [x.count('1') for x in factors]
        spread[n] = max(counts) - min(counts)
        # Direct factor inclusion in independently generated prefix.
        assert factors == {prefix[i:i+n] for i in range(2048-n+1)}
        assert complexity[n] >= spread[n] + 1
        if n % 2 and n >= 3:
            assert spread[n] >= 2
        assert (complexity[n] == 2) == (n & (n - 1) == 0)
    print('VERIFY_OK exhaustive_cyclic_classes_all_lengths=1..128')
    for n in range(1, 65):
        assert complexity[2*n] == complexity[n]
    print('VERIFY_OK cyclic_complexity_doubling=1..64')
    for n in range(2, 129):
        power = 1 << (n.bit_length() - 1)
        rem = n - power
        if rem <= power // 2:
            predicted = spread[rem] + 1
        else:
            predicted = spread[2 * power - rem]
        assert spread[n] == predicted, (n, spread[n], predicted)
    print('VERIFY_OK published_abelian_spread_recurrence=2..128')
    for n in range(1, 129):
        if n % 2 == 1 and n >= 3:
            assert complexity[n] >= 3
    print('VERIFY_OK minimum_two_cyclic_classes_iff_power_of_two=1..128')

    # A separate exhaustive cyclic-image injection test on all binary words.
    for n in range(1, 8):
        words = [f'{x:0{n}b}' for x in range(1 << n)]
        for i, a in enumerate(words):
            for b in words[i:]:
                assert (necklace(image(a)) == necklace(image(b))) == (necklace(a) == necklace(b))
    print('VERIFY_OK morphism_reflects_cyclic_conjugacy_all_binary_words_length=1..7')


if __name__ == '__main__':
    main()
