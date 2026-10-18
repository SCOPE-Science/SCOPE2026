#!/usr/bin/env python3
"""Exact finite-state closure for rank-two FO profiles of binary vertex-coloured paths.

Only Python's standard library is needed.  The algorithm explores *every*
reachable state, rather than stopping at a guessed word-length cutoff.
"""
import json
from collections import Counter, deque
from pathlib import Path
import sys

END = 2
PATTERNS = tuple((left, centre, right)
                 for left in (0, 1, END)
                 for centre in (0, 1)
                 for right in (0, 1, END))
INDEX = {p: i for i, p in enumerate(PATTERNS)}


def append(state, letter):
    c0, c1, windows, penultimate, last = state
    windows |= 1 << INDEX[(penultimate, last, letter)]
    return (min(4, c0 + (letter == 0)),
            min(4, c1 + (letter == 1)),
            windows, last, letter)


def logical_signature(state):
    c0, c1, windows, penultimate, last = state
    # The old final vertex becomes finalized only after appending a letter.
    # Until then, its right-hand neighbour is absent.
    all_windows = windows | (1 << INDEX[(penultimate, last, END)])
    types = 0
    for index, (left, colour, right) in enumerate(PATTERNS):
        if not (all_windows & (1 << index)):
            continue
        local_counts = ((left == 0) + (colour == 0) + (right == 0),
                        (left == 1) + (colour == 1) + (right == 1))
        neigh0 = left == 0 or right == 0
        neigh1 = left == 1 or right == 1
        far0 = c0 > local_counts[0]
        far1 = c1 > local_counts[1]
        # Bit label: centre colour, neighbours' colour set, far colour set.
        label = 16 * colour + int(neigh0) + 2 * int(neigh1) + 4 * int(far0) + 8 * int(far1)
        types |= 1 << label
    return types


def enumerate_states():
    seen = {}
    queue = deque()
    for letter in (0, 1):
        initial = (int(letter == 0), int(letter == 1), 0, END, letter)
        seen[initial] = (None, letter, 1)
        queue.append(initial)
    minimal = {}
    counts = Counter()
    while queue:
        state = queue.popleft()
        depth = seen[state][2]
        key = logical_signature(state)
        if key not in minimal:
            minimal[key] = state
            counts[depth] += 1
        for letter in (0, 1):
            nxt = append(state, letter)
            if nxt not in seen:
                seen[nxt] = (state, letter, depth + 1)
                queue.append(nxt)
    return seen, minimal, counts


def recover(state, seen):
    letters = []
    while state is not None:
        previous, letter, _ = seen[state]
        letters.append(str(letter))
        state = previous
    return ''.join(reversed(letters))


def main():
    seen, minimal, counts = enumerate_states()
    witness_by_sig = {k: recover(s, seen) for k, s in minimal.items()}
    assert len(seen) == 760
    assert len(minimal) == 70
    assert dict(sorted(counts.items())) == {1: 2, 2: 3, 3: 6, 4: 10, 5: 14,
                                             6: 18, 7: 10, 8: 5, 10: 2}
    longest = sorted(w for w in witness_by_sig.values() if len(w) == 10)
    assert longest == ['0011001100', '1100110011']
    mixed = sum('0' in w and '1' in w for w in witness_by_sig.values())
    assert mixed == 62
    print('reachable_states=760')
    print('rank_two_theories=70')
    print('minimum_length_distribution=' + str(dict(sorted(counts.items()))))
    print('mixed_colour_theories=62')
    print('max_minimum_length=10')
    print('length_ten_witnesses=' + ','.join(longest))
    print('VERIFY_OK')
    if len(sys.argv) == 3 and sys.argv[1] == '--write-certificate':
        entries = [{'word': w,
                    'length': len(w),
                    'rank_two_type_hex': hex(k)}
                   for k, w in witness_by_sig.items()]
        entries.sort(key=lambda x: (x['length'], x['word']))
        cert = {
            'description': 'All distinct rank-two profile sets, in minimal-word order',
            'states_explored': len(seen),
            'theory_count': len(entries),
            'entries': entries
        }
        Path(sys.argv[2]).write_text(json.dumps(cert, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    elif len(sys.argv) != 1:
        raise SystemExit('usage: python3 enumerate_profiles.py [--write-certificate OUTPUT.json]')


if __name__ == '__main__':
    main()
