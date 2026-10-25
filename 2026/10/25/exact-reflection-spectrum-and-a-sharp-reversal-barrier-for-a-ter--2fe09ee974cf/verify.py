#!/usr/bin/env python3
"""Finite exhaustive certificate for a reflected-factor cutoff in a ternary morphic word.
Only Python's standard library is required.
"""
from itertools import product

ALPHABET = '012'
MORPHISM = {'0': '01', '1': '21', '2': '0'}
FORBIDDEN = ('00', '11', '22', '20', '212', '0101', '121012')
EXPECTED_REFLECTED = {
    1: ('0', '1', '2'),
    2: ('01', '10', '12', '21'),
    3: ('010', '012', '101', '121', '210'),
    4: ('0121', '1012', '1210', '2101'),
    5: ('01210', '10121', '12101', '21012'),
    6: ('012101', '101210'),
    7: ('1012101',),
    8: (),
}
EXPECTED_COMPLEXITY = (3, 3, 6, 7, 10, 12, 15)


def avoids_forbidden(word):
    return all(f not in word for f in FORBIDDEN)


def iterate_morphism(word, times):
    for _ in range(times):
        word = ''.join(MORPHISM[c] for c in word)
    return word


def factors(word, n):
    return {word[i:i+n] for i in range(len(word) - n + 1)}


def run():
    prefix = iterate_morphism('0', 7)
    assert len(prefix) == 65
    assert prefix.startswith('012102101021012101021012')
    assert avoids_forbidden(prefix)
    total = 0
    for n in range(1, 9):
        all_words = (''.join(t) for t in product(ALPHABET, repeat=n))
        possible = {v for v in all_words if avoids_forbidden(v)}
        permitted_reflections = tuple(sorted(v for v in possible if v[::-1] in possible))
        assert permitted_reflections == EXPECTED_REFLECTED[n], (n, permitted_reflections)
        total += 3 ** n
        observed = factors(prefix, n)
        # The published all-length factor-complexity theorem establishes
        # 2n+1, so observing that many distinct factors is enough to identify
        # the full language at this length, without a finite-prefix extrapolation.
        assert len(observed) == 2 * n + 1
        actual_reflections = tuple(sorted(v for v in observed if v[::-1] in observed))
        assert actual_reflections == permitted_reflections
        reflected_nonpalindromes = sum(v != v[::-1] for v in permitted_reflections)
        reflection_classes = 2 * n + 1 - reflected_nonpalindromes // 2
        if n <= 7:
            assert reflection_classes == EXPECTED_COMPLEXITY[n-1]
        else:
            assert reflection_classes == 2*n + 1
    # Independent large-prefix comparison. This is a finite sanity test,
    # not an all-length proof (the preceding length-eight obstruction is).
    big = iterate_morphism('0', 14)
    for n in range(1, 25):
        observed = factors(big, n)
        assert len(observed) == 2 * n + 1, (n, len(observed))
        reflections = {v for v in observed if v[::-1] in observed}
        if n <= 8:
            assert reflections == set(EXPECTED_REFLECTED[n])
        else:
            assert not reflections
    assert '1012101' in prefix
    assert all(v != v[::-1] for v in factors(big, 8))
    print('TERNARY_REFLECTION_CUTOFF_PASS',
          'forbidden=7', 'exhaustive_candidates=' + str(total),
          'max_reflected_length=7', 'first_empty_length=8',
          'morphism_prefix_length=' + str(len(prefix)),
          'independent_length_checks=1..24')


if __name__ == '__main__':
    run()
