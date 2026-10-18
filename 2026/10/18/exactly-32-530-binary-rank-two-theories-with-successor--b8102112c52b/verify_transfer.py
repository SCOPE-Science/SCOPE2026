#!/usr/bin/env python3
"""Exact finite-state census for rank-two theories of binary ordered words with successor.

The state is the bitset of realized local profiles. This program uses the
proved append transition, not enumeration of strings to a fixed length.
Run with Python 3.10+ and no third-party dependencies.
"""
import hashlib
import json
from collections import Counter, deque


def append_profile_set(mask: int, letter: int) -> int:
    """Append one letter (0 or 1) to the abstract complete profile set."""
    assert letter in (0, 1)
    if mask == 0:
        return 1 << (1 << letter)
    result = 0
    last = None
    remaining = mask
    while remaining:
        bit = remaining & -remaining
        p = bit.bit_length() - 1
        remaining ^= bit
        # The right-neighbor field occupies bits 6 and 7.
        if ((p >> 6) & 3) == 0:
            assert last is None, 'more than one last-position type'
            last = p
            updated = p | (1 << (6 + letter))
        else:
            updated = p | (1 << (8 + letter))
        result |= 1 << updated
    assert last is not None, 'last-position type is missing'
    before_last = ((last >> 2) & 3) | ((last >> 4) & 3)
    appended = (1 << letter) | (before_last << 2) | ((last & 3) << 4)
    return result | (1 << appended)


def direct_signature(word: tuple[int, ...]) -> int:
    """Independently evaluate the same state from word positions."""
    result = 0
    n = len(word)
    for i, c in enumerate(word):
        pre = 0
        post = 0
        for j in range(i - 1):
            pre |= 1 << word[j]
        for j in range(i + 2, n):
            post |= 1 << word[j]
        p = ((1 << c) | (pre << 2) | (post << 8)
             | ((1 << word[i - 1]) << 4 if i else 0)
             | ((1 << word[i + 1]) << 6 if i + 1 < n else 0))
        result |= 1 << p
    return result


def calculate():
    seen = {0: ()}
    pending = deque([0])
    counts = Counter({0: 1})
    while pending:
        s = pending.popleft()
        word = seen[s]
        assert direct_signature(word) == s
        for a in (0, 1):
            new_state = append_profile_set(s, a)
            new_word = word + (a,)
            assert direct_signature(new_word) == new_state
            if new_state not in seen:
                seen[new_state] = new_word
                pending.append(new_state)
                counts[len(new_word)] += 1
    canonical_states = sorted(s.to_bytes(128, 'big') for s in seen)
    digest = hashlib.sha256(b''.join(canonical_states)).hexdigest()
    maximum = max(counts)
    evidence = {
        'all_states_including_empty_word': len(seen),
        'nonempty_theories': len(seen) - 1,
        'two_colour_theories': sum(len(set(w)) == 2 for w in seen.values()),
        'sharp_shortest_representative_length': maximum,
        'minimum_representative_length_distribution': [counts[i] for i in range(maximum + 1)],
        'longest_shortest_representatives': sorted(''.join(map(str, w)) for w in seen.values() if len(w) == maximum),
        'canonical_state_set_sha256': digest,
        'state_encoding': '1024-bit big-endian per state, sorted lexicographically',
    }
    assert len(seen) == 32541
    assert evidence['two_colour_theories'] == 32530
    assert maximum == 24 and counts[24] == 16
    return evidence


if __name__ == '__main__':
    print(json.dumps(calculate(), indent=2, sort_keys=True))
