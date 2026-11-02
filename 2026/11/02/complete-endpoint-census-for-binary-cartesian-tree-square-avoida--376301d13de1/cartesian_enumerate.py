#!/usr/bin/env python3
"""Exact finite enumeration of binary 3+-Cartesian-tree-square-free words.

The root of the Cartesian tree is the *leftmost* minimum in a nonempty
substring. The tree shape, not node labels, defines equivalence.
All arithmetic and all branching are exact.
"""
from functools import lru_cache
import hashlib

@lru_cache(maxsize=None)
def ct(word):
    if not word:
        return None
    k = word.find('0')
    if k == -1:
        k = 0
    return (k, ct(word[:k]), ct(word[k + 1:]))


def admissible_extension(word):
    """Assumes all proper prefixes are valid; check new ending only."""
    for half in range(3, len(word) // 2 + 1):
        if ct(word[-2 * half:-half]) == ct(word[-half:]):
            return False
    return True


def run():
    current = ['']
    sizes = []
    for length in range(1, 31):
        current = [u + letter for u in current for letter in '01'
                   if admissible_extension(u + letter)]
        sizes.append(len(current))
        if length == 29:
            extremal = current[:]
    assert sizes[-2:] == [20, 0], sizes[-2:]
    assert extremal == sorted(extremal)
    mask = ''.join(next(iter(q)) if len(q := {w[i] for w in extremal}) == 1
                   else '-' for i in range(29))
    assert mask == '110--11010--1101010--110101--', mask
    unknown = [i for i, c in enumerate(mask) if c == '-']
    patterns = [''.join(w[i] for i in unknown) for w in extremal]
    assert len(patterns) == len(set(patterns)) == 20
    digest = hashlib.sha256(('\n'.join(extremal) + '\n').encode()).hexdigest()
    print('COUNTS=' + ','.join(map(str, sizes)))
    print('MASK=' + mask)
    print('VARIABLE_POSITIONS_1BASED=' + ','.join(str(i + 1) for i in unknown))
    print('PATTERNS=' + ','.join(patterns))
    print('WORDS_SHA256=' + digest)
    print('CARTESIAN_ENUMERATION_OK')
    return extremal

if __name__ == '__main__':
    run()
