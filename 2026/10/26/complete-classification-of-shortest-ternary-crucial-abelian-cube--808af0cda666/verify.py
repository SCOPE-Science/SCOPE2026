#!/usr/bin/env python3
"""Exact enumeration of shortest ternary crucial Abelian-cube-free words.
No third-party packages. Run: python3 verify.py
"""
from collections import Counter
from itertools import permutations, product

ALPHABET = (0, 1, 2)


def parikh(t):
    return (t.count(0), t.count(1), t.count(2))


def has_cube(t):
    n = len(t)
    for block in range(1, n // 3 + 1):
        for s in range(n - 3 * block + 1):
            a = t[s:s + block]
            b = t[s + block:s + 2 * block]
            c = t[s + 2 * block:s + 3 * block]
            if parikh(a) == parikh(b) == parikh(c):
                return True
    return False


def periods_after_append(w, letter):
    t = w + (letter,)
    n = len(t)
    return tuple(block for block in range(1, n // 3 + 1)
                 if parikh(t[n-3*block:n-2*block]) ==
                    parikh(t[n-2*block:n-block]) ==
                    parikh(t[n-block:n]))


def construct():
    blocks = sorted(set(permutations((0, 0, 1, 2))))
    possible_b = tuple(b for b in blocks if b[-2:] in ((0, 1), (1, 0)))
    forbidden = set()
    candidates = set()
    for a in blocks:
        for b in possible_b:
            w = a + b + (1, 0, 0)
            if has_cube(w):
                forbidden.add(w)
            else:
                candidates.add(w)
    assert len(blocks) == 12
    assert possible_b == ((0, 2, 0, 1), (0, 2, 1, 0),
                          (2, 0, 0, 1), (2, 0, 1, 0))
    assert forbidden == {
        a + b + (1, 0, 0)
        for a in ((1, 2, 0, 0), (2, 1, 0, 0))
        for b in ((0, 2, 0, 1), (0, 2, 1, 0))
    }
    assert len(candidates) == 44
    full = set()
    for perm in permutations(ALPHABET):
        for w in candidates:
            v = tuple(perm[x] for x in w)
            full.add(v)
            assert not has_cube(v)
            assert [periods_after_append(v, x) for x in perm] == [(1,), (2,), (4,)]
    assert len(full) == 264
    return candidates, full


def exhaustive():
    accepted = set()
    cube_free_count = 0
    witness_profile = Counter()
    for w in product(ALPHABET, repeat=11):
        if has_cube(w):
            continue
        cube_free_count += 1
        if set(w) != set(ALPHABET):
            continue
        witness = tuple(periods_after_append(w, x) for x in ALPHABET)
        if all(witness):
            accepted.add(w)
            witness_profile[witness] += 1
    assert cube_free_count == 50520
    assert len(accepted) == 264
    assert len(witness_profile) == 6
    assert set(witness_profile.values()) == {44}
    assert {tuple(p[0] for p in prof) for prof in witness_profile} == set(permutations((1, 2, 4)))
    return accepted, cube_free_count


def main():
    for n in range(11):
        shorter_crucial = 0
        for w in product(ALPHABET, repeat=n):
            if has_cube(w):
                continue
            if all(periods_after_append(w, x) for x in ALPHABET):
                shorter_crucial += 1
        assert shorter_crucial == 0, (n, shorter_crucial)
    print('PASS: no ternary crucial Abelian-cube-free words below length 11;')
    normalized, by_structure = construct()
    by_exhaustion, count = exhaustive()
    assert by_structure == by_exhaustion
    assert len({min(tuple(p[c] for c in w) for p in permutations(ALPHABET))
                for w in by_exhaustion}) == 44
    print('PASS: 3^11=177147 words checked; 50520 Abelian-cube-free;')
    print('PASS: 264 crucial words; 44 alphabet-relabeling orbits;')
    print('PASS: 12 x 4 - 4 = 44 canonical constructions;')
    print('PASS: all six length-witness permutations (1,2,4), 44 each;')
    print('PASS: exact agreement of exhaustive and structural descriptions.')


if __name__ == '__main__':
    main()
