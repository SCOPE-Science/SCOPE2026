#!/usr/bin/env python3
"""Exact verifier for binary length-five cyclic-permutation balls.

Only Python's standard library is used.  All assertions are finite integer tests.
The infinite conclusion follows from the six-vector max-plus identity,
not from a finite extrapolation.
"""
from itertools import product

K = 5
ALPHABET = '01'


def rotation_outputs(word, start):
    """The distinct nonidentity cyclic shifts of one five-bit window."""
    block = word[start:start + K]
    answer = set()
    for t in range(1, K):
        candidate = word[:start] + block[t:] + block[:t] + word[start + K:]
        if candidate != word:
            answer.add(candidate)
    return answer


def direct_ball(word):
    answer = {word}
    for i in range(len(word) - K + 1):
        answer.update(rotation_outputs(word, i))
    return answer


def fresh_last_window(word):
    """New outputs first arising in the rightmost length-five window.

    This routine is called on prefixes of lengths five through nine.
    The leftmost relevant preceding window starts no more than four
    positions before the rightmost window; earlier windows are disjoint.
    """
    n = len(word)
    assert K <= n <= 9
    i = n - K
    fresh = rotation_outputs(word, i)
    for h in range(max(0, i - K + 1), i):
        fresh.difference_update(rotation_outputs(word, h))
    return len(fresh)


def words(length):
    return (''.join(bits) for bits in product(ALPHABET, repeat=length))


def periodic_witness(n):
    return ('001101' * ((n + 5) // 6))[:n]


def predicted(n):
    assert n >= K
    if n == 5:
        return 5
    return 3 * n - 9 + (n - 4) // 6


STATES = list(words(8))
WEIGHT = {p: fresh_last_window(p) for p in words(9)}


def initial_vector():
    return {s: sum(fresh_last_window(s[:length])
                   for length in range(5, 9)) for s in STATES}


def advance(vector):
    next_vector = {state: -10**9 for state in STATES}
    for state in STATES:
        for bit in ALPHABET:
            successor = state[1:] + bit
            candidate = vector[state] + WEIGHT[state + bit]
            if candidate > next_vector[successor]:
                next_vector[successor] = candidate
    return next_vector


def verify():
    # Check the locality identity against a separately formed full ball.
    # This exhausts all binary words of each length 5..14, not a sample.
    for n in range(5, 15):
        maximum = 0
        for word in words(n):
            full = len(direct_ball(word))
            local = 1 + sum(fresh_last_window(word[max(0, i - 4):i + K])
                            for i in range(n - K + 1))
            assert full == local, (n, word, full, local)
            maximum = max(maximum, full)
        assert maximum == predicted(n), (n, maximum, predicted(n))

    # Exhaustive maxima at lengths 5..7, and all 256 suffix-state
    # dynamic-programming entries at lengths 8..23.
    for n in (5, 6, 7):
        assert max(len(direct_ball(word)) for word in words(n)) == predicted(n)

    vectors = {8: initial_vector()}
    assert max(vectors[8].values()) + 1 == predicted(8)
    for n in range(9, 24):
        vectors[n] = advance(vectors[n - 1])
        assert max(vectors[n].values()) + 1 == predicted(n), n

    # Six exact componentwise relations certify an all-length recurrence:
    # max-plus homogeneity propagates equality from V_(n+6) = V_n + 19
    # to the next n; the six bases cover every residue modulo six.
    for n in range(12, 18):
        assert all(vectors[n + 6][s] == vectors[n][s] + 19
                   for s in STATES), n

    # Explicit periodic extremizer: score four at positions 0,1,5,11,...,
    # and three everywhere else, for all windows in length >= 6 prefixes.
    witness = periodic_witness(30)
    for i in range(26):
        piece = witness[max(0, i - 4):i + 5]
        expected = 4 if i in (0, 1) or (i >= 5 and i % 6 == 5) else 3
        assert fresh_last_window(piece) == expected, (i, piece)

    # Optional longer finite sanity test; logically redundant to recurrence.
    v = vectors[23]
    for n in range(24, 61):
        v = advance(v)
        assert max(v.values()) + 1 == predicted(n), n
        assert len(direct_ball(periodic_witness(n))) == predicted(n), n

    print('LOCAL_IDENTITY: verified for all binary words of lengths 5..14')
    print('STATE_SPACE: 256 suffixes; 512 transitions')
    print('VECTOR_IDENTITY: V_(n+6) = V_n + 19, n=12..17')
    print('PERIODIC_EXTREMIZER: prefix of (001101)^infinity')
    print('EXACT_PROFILE_5_TO_23:', [predicted(n) for n in range(5, 24)])
    print('VERIFY_OK')


if __name__ == '__main__':
    verify()
