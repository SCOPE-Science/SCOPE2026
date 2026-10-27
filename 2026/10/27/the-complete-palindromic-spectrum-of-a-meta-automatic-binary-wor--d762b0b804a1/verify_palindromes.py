#!/usr/bin/env python3
"""Finite, exact verification of the palindromic-factor theorem for a 4-uniform coding."""
from functools import lru_cache
import json

MORPH = ('0112', '1230', '2301', '3023')
CODING = ('0', '1', '0', '1')
EXPECTED_PAIRS = ('01','02','03','11','12','13','21','22','23','30')
EXPECTED_COUNTS = (2,2,2,2,2,2,2,2,2,3,0,3,0,2,0,2,0,0)
EXPECTED_LONGEST = ('1010010110100101', '1010101001010101')

def subst(s):
    return ''.join(MORPH[int(c)] for c in s)

def iterate(s, k):
    for _ in range(k):
        s = subst(s)
    return s

def code(s):
    return ''.join(CODING[int(c)] for c in s)

def neighbors(s):
    return {s[j:j+2] for j in range(len(s)-1)}

def palindromes_in(s, maxlen):
    acc = {n: set() for n in range(1,maxlen+1)}
    for n in range(1, maxlen+1):
        for j in range(len(s)-n+1):
            w=s[j:j+n]
            if w == w[::-1]:
                acc[n].add(w)
    return acc

def main():
    # A finite closed alphabet of possible pairs, proved by substitution induction.
    seed = iterate('0', 4)
    pairs = tuple(sorted(neighbors(seed)))
    assert pairs == EXPECTED_PAIRS, pairs
    closure = set()
    for xy in pairs:
        closure |= neighbors(subst(xy))
    assert closure == set(pairs), sorted(closure)

    # Every factor of length <= 18 is contained in two adjacent length-64 blocks.
    # Every admissible two-letter state factor occurs in the fixed point.
    spectra = {n:set() for n in range(1,19)}
    for xy in pairs:
        segment = code(iterate(xy, 3))
        assert len(segment) == 128
        local = palindromes_in(segment, 18)
        for n in spectra: spectra[n].update(local[n])
    counts = tuple(len(spectra[n]) for n in range(1,19))
    assert counts == EXPECTED_COUNTS, counts
    assert tuple(sorted(spectra[16])) == EXPECTED_LONGEST
    assert not spectra[11] and not spectra[18]
    all_pals = set().union(*spectra.values())
    assert len(all_pals) == 28

    # The finite prefix below supplies first occurrences of all 28 words.
    prefix = code(seed)
    assert len(prefix) == 256
    first = {w:prefix.find(w) for w in all_pals}
    assert all(j >= 0 for j in first.values())
    first_end = {w: j+len(w) for w,j in first.items()}
    assert max(first_end.values()) == 196
    assert sum(e <= 195 for e in first_end.values()) == 27
    assert first['1010101001010101'] == 180

    # Independent representation check: OEIS's recursive definition of M1.
    @lru_cache(None)
    def nested(n):
        if n < 2: return n
        q,r = divmod(n,4)
        if r == 0: return nested(q)
        if r == 1: return 1-nested(q)
        val = nested(2*q+1-nested(q))
        return val if r == 2 else 1-val
    sampled = code(iterate('0', 6))
    assert len(sampled) == 4096
    assert sampled == ''.join(str(nested(i)) for i in range(4096))

    # Direct prefix enumeration independently rechecks the exact finite spectrum.
    direct = palindromes_in(sampled, 18)
    assert direct == spectra
    print(json.dumps({
        'admissible_state_pairs': list(pairs),
        'closure_verified': True,
        'distinct_nonempty_palindromes': len(all_pals),
        'first_all_present_prefix_length': 196,
        'length_16_palindromes': list(EXPECTED_LONGEST),
        'nested_recurrence_prefix_checked': 4096,
        'palindromic_complexity_n_1_to_18': list(counts),
        'palindrome_free_lengths_11_and_18': True,
        'substitution_block_length': 64,
        'test_segment_count': len(pairs),
        'test_segment_length': 128,
        'verified': True,
    }, sort_keys=True, separators=(',',':')))

if __name__ == '__main__': main()
