#!/usr/bin/env python3
"""Exact rank-three two-marker coloured-order classification certificate.

The finite loops are exhaustive because every blue interval may be capped at 7
by the standard 3-move finite-linear-order equivalence and concatenation lemma.
No third-party dependencies.
"""
from functools import lru_cache
from itertools import product
from collections import Counter

@lru_cache(maxsize=None)
def type_key(word, depth):
    """A canonical immutable representation of an EF type, no hash collisions."""
    if depth == 0:
        return ()
    return frozenset((letter, type_key(word[:i], depth - 1),
                      type_key(word[i + 1:], depth - 1))
                     for i, letter in enumerate(word))

def word(t):
    a, b, c = t
    return 'B' * a + 'R' + 'B' * b + 'R' + 'B' * c

def normal(t):
    nonzero = sum(v != 0 for v in t)
    if nonzero == 3:
        caps = (6, 5, 6)
    elif nonzero == 2:
        caps = (6, 6, 6)
    elif nonzero == 1:
        caps = (7, 7, 7)
    else:
        caps = (0, 0, 0)
    return tuple(min(v, lim) for v, lim in zip(t, caps))

@lru_cache(maxsize=None)
def game_equal(u, v, rounds):
    """Independent EF game recurrence, quantifying Spoiler's first move."""
    if rounds == 0:
        return True
    for source, target in ((u, v), (v, u)):
        for i, letter in enumerate(source):
            if not any(letter == target[j]
                       and game_equal(source[:i], target[:j], rounds-1)
                       and game_equal(source[i+1:], target[j+1:], rounds-1)
                       for j in range(len(target))):
                return False
    return True

def main():
    triples = list(product(range(8), repeat=3))
    by_type = {}
    by_norm = {}
    for t in triples:
        ty = type_key(word(t), 3)
        no = normal(t)
        # Biconditional: the signature class and normal-form class must coincide.
        assert ty not in by_type or by_type[ty] == no, (t, 'different key')
        assert no not in by_norm or by_norm[no] == ty, (t, 'different type')
        by_type[ty] = no
        by_norm[no] = ty
    assert len(by_type) == len(by_norm) == 310
    assert max(sum(v)+2 for v in by_norm) == 19
    assert sum(sum(v)+2 == 19 for v in by_norm) == 1
    assert normal((7, 7, 7)) == (6, 5, 6)
    assert len({type_key(word(t), 2) for t in triples}) == 26
    # At and across the finite truncation boundary, check game recurrence
    # (independent of the nested-set implementation above).
    probes = [
        ((6,5,6),(7,7,7),True),
        ((6,5,6),(6,4,6),False),
        ((6,5,6),(5,5,6),False),
        ((6,5,6),(6,5,5),False),
        ((7,0,0),(6,0,0),False),
        ((7,0,0),(8,0,0),True),
        ((0,7,0),(0,6,0),False),
        ((0,7,0),(0,8,0),True),
        ((0,6,1),(0,7,1),True),
        ((0,5,1),(0,6,1),False),
        ((1,5,1),(1,6,1),True),
        ((1,4,1),(1,5,1),False),
        ((3,3,3),(3,3,3),True),
        ((0,0,0),(0,1,0),False),
    ]
    for s, t, expected in probes:
        assert game_equal(word(s), word(t), 3) == expected, (s,t)
    sizes = Counter(sum(v)+2 for v in by_norm)
    assert sizes == {2:1,3:3,4:6,5:10,6:15,7:21,8:28,9:36,
                     10:35,11:35,12:33,13:29,14:23,15:15,16:10,
                     17:6,18:3,19:1}
    print('CANONICAL_KEYS=310')
    print('RANK_TWO_KEYS=26')
    print('WORST_SHORTEST_LENGTH=19')
    print('UNIQUE_WORST_KEY=(6,5,6)')
    print('PROBES_EF_GAME=', len(probes))
    print('LENGTH_DISTRIBUTION=', sorted(sizes.items()))
    print('VERIFY_OK')
if __name__ == '__main__':
    main()
