#!/usr/bin/env python3
"""Finite independent tests for dyadic borders in generalized paperfolding words."""
from itertools import product


def paperfolding(n, instructions):
    out = []
    for i in range(n):
        z = i + 1
        v = (z & -z).bit_length() - 1
        odd = z >> v
        out.append(str(instructions[v] ^ (((odd - 1) // 2) & 1)))
    return ''.join(out)


def is_unbordered(word):
    return all(word[:j] != word[-j:] for j in range(1, len(word)))


def local_rule(word):
    return word[0] != word[-1] and word[:3] != word[-3:]


cases = 0
for choices in product(range(2), repeat=4):
    instructions = list(choices) + [0] * 12
    sequence = paperfolding(4096, instructions)
    for exponent in range(2, 8):
        n = 1 << exponent
        for word in set(sequence[i:i+n] for i in range(len(sequence)-n+1)):
            assert local_rule(word) == is_unbordered(word), (choices, n, word)
            cases += 1
regular = paperfolding(4096, [0]*16)
for exponent in range(3, 11):
    n = 1 << exponent
    w = regular[3:3+n]
    assert w[:3] == w[-3:] and w[0] != w[-1], n
print('VERIFY_OK', 'instruction_prefixes=16', 'dyadic_lengths=4..128',
      'factor_tests='+str(cases), 'sharpness_lengths=8..1024')
