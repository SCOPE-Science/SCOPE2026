#!/usr/bin/env python3
"""Exhaustive verification of the terminal ternary curling-number profile.

Python 3 standard library only. The reduced search uses the symmetry of
simultaneous alphabet relabeling, with first appearances in order 0,1,2.
All comparisons are literal string comparisons, not heuristics.
"""
from collections import Counter, defaultdict

ALPHABET = '012'
TERMINAL_LENGTH = 84
H = (
    '11211221211212211221211221121221122121121221211221121221122121122112122121121221121'
)
assert len(H) == 83


def newly_overlapping(word):
    """True iff an overlap ends at the last symbol of word."""
    n = len(word)
    for period in range(1, (n - 1) // 2 + 1):
        left = word[n - (2 * period + 1): n - period]
        right = word[n - (period + 1): n]
        if left == right:
            return True
    return False


def end_curl(word):
    """For an overlap-free word, this is its actual curling number."""
    n = len(word)
    for root_length in range(1, n // 2 + 1):
        if word[n - 2 * root_length: n - root_length] == word[n - root_length: n]:
            return '2'
    return '1'


def allowed_letters(prefix):
    """All letters for restricted-growth canonical words."""
    if not prefix:
        return '0'
    if '1' not in prefix:
        return '01'
    return ALPHABET


def main():
    states = [('', '')]
    counts = {}
    for n in range(1, TERMINAL_LENGTH + 2):
        next_states = []
        for word, transformed in states:
            for letter in allowed_letters(word):
                candidate = word + letter
                if newly_overlapping(candidate):
                    continue
                candidate_transform = transformed + end_curl(candidate)
                if newly_overlapping(candidate_transform):
                    continue
                next_states.append((candidate, candidate_transform))
        states = next_states
        counts[n] = len(states)
        if n == TERMINAL_LENGTH:
            terminal = tuple(states)
    assert counts[84] == 1008, counts[84]
    assert counts[85] == 0
    assert all(set(word) == set(ALPHABET) for word, transform in terminal)
    assert len(set(word for word, transform in terminal)) == 1008
    prefix_families = defaultdict(list)
    transforms = Counter()
    for word, transform in terminal:
        assert len(word) == len(transform) == TERMINAL_LENGTH
        transforms[transform] += 1
        prefix_families[word[:-1]].append((word[-1], transform[-1]))
        assert transform[:-1] == H
    assert transforms == {H + '1': 672, H + '2': 336}, transforms
    assert len(prefix_families) == 336
    for extensions in prefix_families.values():
        assert len(extensions) == 3
        assert {symbol for symbol, digit in extensions} == set(ALPHABET)
        assert Counter(digit for symbol, digit in extensions) == {'1': 2, '2': 1}
    # Every canonical terminal word uses all three letters. Its relabeling
    # orbit is therefore exactly 3!=6, with unchanged curling transform.
    print('terminal_length=84; canonical_words=1008; relabelings=6')
    print('full_words=6048; valid_length_85=0')
    print('canonical_extendable_83_prefixes=336; full_prefixes=2016')
    print('every_extendable_prefix_has_three_distinct_valid_extensions=true')
    print('every_extendable_prefix_final_curl_counts=1:2,2:1')
    print('common_transform_prefix_length=83')
    print('H=' + H)
    print('C1=' + H + '1; full_fiber_size=4032')
    print('C2=' + H + '2; full_fiber_size=2016')
    print('PASS')


if __name__ == '__main__':
    main()
