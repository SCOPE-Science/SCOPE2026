"""Reproduce the fixed-content Simon-congruence counts independently.

Usage: python checker.py
Only the Python standard library is required.
"""
from itertools import product
from math import comb
from collections import defaultdict


def subsequence_spectrum(word: str, depth: int):
    # Enumerate scattered subsequences directly by left-to-right dynamic programming.
    states = {""}
    for letter in word:
        extension = {s + letter for s in states if len(s) < depth}
        states.update(extension)
    return frozenset(states)


def invariant(a, b, c, depth):
    assert depth >= 3
    q = depth - 2
    return (min(a, q), min(b, q), min(c, q),
            int(a + b >= q + 1), int(b + c >= q + 1))


def truncated_binom(n, r):
    return comb(n, r) if n >= r and r >= 0 else 0


def predicted_count(m, depth):
    q = depth - 2
    B = sum((-1)**j * comb(3,j) *
            (truncated_binom(m - j*(q+1) + 3, 3) -
             truncated_binom(m - j*q + 2, 3))
            for j in range(4))
    return B + 3*int(m >= 2*q+1) + int(m >= 2*q+2)


def main():
    word_tests = 0
    count_tests = 0
    for depth in range(3, 10):
        q = depth - 2
        for m in range(0, 3*q + 6):
            # No use of the theorem to calculate the spectra.
            spectrum_to_invariant = {}
            invariant_to_spectrum = {}
            for a in range(m + 1):
                for b in range(m - a + 1):
                    c = m-a-b
                    w = '0'*a + '1' + '0'*b + '1' + '0'*c
                    direct = subsequence_spectrum(w, depth)
                    key = invariant(a,b,c,depth)
                    if direct in spectrum_to_invariant:
                        assert spectrum_to_invariant[direct] == key, (depth,m,a,b,c)
                    else:
                        spectrum_to_invariant[direct] = key
                    if key in invariant_to_spectrum:
                        assert invariant_to_spectrum[key] == direct, (depth,m,a,b,c)
                    else:
                        invariant_to_spectrum[key] = direct
                    word_tests += 1
            assert len(spectrum_to_invariant) == predicted_count(m,depth), (depth,m)
            assert len(invariant_to_spectrum) == predicted_count(m,depth), (depth,m)
            count_tests += 1
        stable = 4 if depth == 3 else 3*q
        expected = 3*q*q+3*q+5
        assert predicted_count(stable,depth) == expected
        assert predicted_count(stable-1,depth) < expected
        for m in (stable+10,stable+50,stable+1000):
            assert predicted_count(m,depth) == expected
    for m in range(30):
        cls={subsequence_spectrum('0'*a+'1'+'0'*b+'1'+'0'*(m-a-b),2)
            for a in range(m+1) for b in range(m-a+1)}
        assert len(cls)==(1 if m==0 else 3)
    print(f'PASS: {word_tests} independently constructed spectra, '
          f'{count_tests} exact count comparisons, '
          'saturation tests, and depth-two boundary cases.')


if __name__ == '__main__':
    main()
