#!/usr/bin/env python3
"""Self-contained exhaustive certificate for the smallest ternary dihedral-shuffle obstructions.

Requires Python 3 standard library only. No unverified extrapolation to longer words.
"""
from itertools import combinations, permutations, product
from collections import Counter

ALPHABET = "012"
WITNESS = "00011022"


def is_even(w):
    return all(w.count(c) % 2 == 0 for c in ALPHABET)


def dihedral_equivalent(a, b):
    """All rotations and reflected rotations of a, independently of embeddings."""
    return b in (a + a) or b in (a[::-1] + a[::-1])


def balanced_pairs(w):
    n = len(w) // 2
    for indices in combinations(range(len(w)), n):
        indexset = set(indices)
        a = ''.join(w[i] for i in indices)
        b = ''.join(w[i] for i in range(len(w)) if i not in indexset)
        if sorted(a) == sorted(b):
            yield a, b


def direct_dihedral_shuffle(w):
    if len(w) % 2:
        return False
    return any(dihedral_equivalent(a, b) for a, b in balanced_pairs(w))


def zero_orbit_type(s, repeated):
    """For a four-letter string of type (2,1,1): cyclic-zero adjacency."""
    assert len(s) == 4 and s.count(repeated) == 2
    i, j = (k for k, a in enumerate(s) if a == repeated)
    return 'opposite' if (j-i) == 2 else 'adjacent'


def structural_dihedral_shuffle(w):
    """Independent exact D4 criterion on words with multiplicities (4,2,2)."""
    assert len(w) == 8 and sorted(Counter(w).values()) == [2, 2, 4]
    repeated = next(c for c in ALPHABET if w.count(c) == 4)
    return any(zero_orbit_type(a, repeated) == zero_orbit_type(b, repeated)
               for a, b in balanced_pairs(w))


def orbit(w):
    """Letter relabeling, reversal, and cyclic rotation of the full word."""
    result = set()
    for p in permutations(ALPHABET):
        v = ''.join(p[int(x)] for x in w)
        for u in (v, v[::-1]):
            for k in range(len(u)):
                result.add(u[k:] + u[:k])
    return result


def run():
    counts = {}
    exceptional = set()
    for length in (2, 4, 6, 8):
        total_even = 0
        failures = set()
        for letters in product(ALPHABET, repeat=length):
            w = ''.join(letters)
            if not is_even(w):
                continue
            total_even += 1
            dihedral = direct_dihedral_shuffle(w)
            if length == 8 and sorted(Counter(w).values()) == [2, 2, 4]:
                assert dihedral == structural_dihedral_shuffle(w), w
            if not dihedral:
                failures.add(w)
        counts[length] = (total_even, len(failures))
        assert len(failures) == (48 if length == 8 else 0), (length, len(failures))
        if length == 8:
            exceptional = failures
    assert counts == {2: (3, 0), 4: (21, 0), 6: (183, 0), 8: (1641, 48)}
    assert len(orbit(WITNESS)) == 48
    assert exceptional == orbit(WITNESS)
    assert not direct_dihedral_shuffle(WITNESS)
    pairs = list(balanced_pairs(WITNESS))
    assert len(pairs) == 24
    assert set(pairs) == {('0012', '0102'), ('0102', '0012')}
    assert Counter(pairs) == {('0012', '0102'): 12, ('0102', '0012'): 12}
    parikh = Counter(tuple(w.count(c) for c in ALPHABET) for w in exceptional)
    assert parikh == {(4, 2, 2): 16, (2, 4, 2): 16, (2, 2, 4): 16}
    print('DIHEDRAL_SHUFFLE_COUNTEREXAMPLE_PASS')
    print('even_and_failure_counts', counts)
    print('minimal_exception_orbit_size', len(exceptional))
    print('witness_balanced_partitions', len(pairs), 'different_pairs', sorted(set(pairs)))


if __name__ == '__main__':
    run()
