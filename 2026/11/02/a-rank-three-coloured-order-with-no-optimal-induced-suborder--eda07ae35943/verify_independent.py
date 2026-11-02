#!/usr/bin/env python3
"""Independent, exact rank-three checks for two-colour finite words."""
from functools import lru_cache
from itertools import product, combinations
import random

LEFT = "rrrrrrbbbbbbrbbbbbr"
RIGHT = "rbbbbbrbbbbbbrrrrrr"
BASE = LEFT + "rbrbrrbbbrbrbbrbbbbbrrrrrbrrrbbr" + RIGHT
TEST = LEFT + "rbrrrbbrbbbbbrbrrbrbrbbrrrrrbrrbbbr" + RIGHT

@lru_cache(maxsize=250000)
def two_type(word):
    # The rank-two type is the set of left-colour-set,
    # current-colour, right-colour-set triples.
    return frozenset((frozenset(word[:i]), letter,
                      frozenset(word[i + 1:]))
                     for i, letter in enumerate(word))

def three_type(word):
    return frozenset((two_type(word[:i]), letter,
                      two_type(word[i + 1:]))
                     for i, letter in enumerate(word))

@lru_cache(maxsize=None)
def game_equivalent(a, b, rounds):
    if rounds == 0:
        return True
    if rounds == 1:
        return set(a) == set(b)
    for source, target in [(a,b),(b,a)]:
        for i, letter in enumerate(source):
            if not any(c == letter
                       and game_equivalent(source[:i],target[:j],rounds-1)
                       and game_equivalent(source[i+1:],target[j+1:],rounds-1)
                       for j,c in enumerate(target)):
                return False
    return True

assert len(BASE) == 70 and len(TEST) == 73
sig0 = three_type(BASE)
assert len(sig0) == 70
assert three_type(TEST) == sig0
words = [''] + [''.join(x) for n in range(1,5)
                for x in product('rb', repeat=n)]
for a in words:
    for b in words:
        assert game_equivalent(a,b,3) == (three_type(a)==three_type(b))
print('INDEPENDENT_EF_GAME_VALIDATION_PASS pairs=',len(words)**2)

rng = random.Random(170504632)
choices = list(combinations(range(len(TEST)),3))
selected = {choices[0],choices[-1],choices[len(choices)//2]}
selected.update(rng.sample(choices, min(1200,len(choices))))
for deleted in sorted(selected):
    excluded = set(deleted)
    word=''.join(c for i,c in enumerate(TEST) if i not in excluded)
    assert three_type(word) != sig0
print('INDEPENDENT_SUBSEQUENCE_SAMPLE_PASS count=',len(selected))
print('INDEPENDENT_RANK3_ALL_CHECKS_PASS')
