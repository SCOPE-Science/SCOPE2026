#!/usr/bin/env python3
"""Finite-state and direct 2-round game verification for two-colour words.

No external packages or external files are needed.  The words denote finite
strictly linearly ordered structures with exactly one of two unary colours
at each position.  The empty word and monochromatic words are included in
finite-state closure tests, but the main classification requires both colours.
"""
from collections import Counter, deque
from itertools import product


def point_types(word):
    """Compute 1-characters (letter, left-colour set, right-colour set)."""
    suffix = [0] * (len(word) + 1)
    for i in range(len(word) - 1, -1, -1):
        suffix[i] = suffix[i + 1] | (1 << int(word[i]))
    left, answer = 0, set()
    for i, ch in enumerate(word):
        ch = int(ch)
        answer.add((ch, left, suffix[i + 1]))
        left |= 1 << ch
    return frozenset(answer)


def to_mask(characters):
    mask = 0
    for c, left, right in characters:
        mask |= 1 << (16 * c + 4 * left + right)
    return mask


def decode(mask):
    answer = []
    for k in range(32):
        if mask & (1 << k):
            c, k0 = divmod(k, 16)
            left, right = divmod(k0, 4)
            answer.append((c, left, right))
    return answer


def append_colour(mask, letter):
    """Exact transition under appending letter to any word of this type."""
    used = 0
    old = decode(mask)
    for c, _, _ in old:
        used |= 1 << c
    return to_mask(([(c, left, right | (1 << letter))
                    for c, left, right in old] + [(letter, used, 0)]))


def reverse_type(mask):
    return to_mask((c, right, left) for c, left, right in decode(mask))


def same_pair_pattern(w, v, i, j, ii, jj):
    return (w[i] == v[j] and w[ii] == v[jj]
            and (i < ii) == (j < jj)
            and (i == ii) == (j == jj))


def two_move_equivalent(w, v):
    """Direct, independent, unrestricted two-move EF-game check."""
    def response_exists(first_in_w, i, j):
        if first_in_w:
            a, b, ia, ib = w, v, i, j
        else:
            a, b, ia, ib = v, w, j, i
        # Spoiler may choose any second point in either structure.
        for k in range(len(a)):
            if not any(same_pair_pattern(a, b, ia, ib, k, l)
                       for l in range(len(b))):
                return False
        for l in range(len(b)):
            if not any(same_pair_pattern(a, b, ia, ib, k, l)
                       for k in range(len(a))):
                return False
        return True
    for i in range(len(w)):
        if not any(response_exists(True, i, j)
                   for j in range(len(v)) if w[i] == v[j]):
            return False
    for j in range(len(v)):
        if not any(response_exists(False, i, j)
                   for i in range(len(w)) if w[i] == v[j]):
            return False
    return True


def main():
    # BFS over complete 2-round theories: transition closure proves there are
    # no further theories from words of arbitrarily large finite length.
    shortest = {0: ''}
    queue = deque([0])
    while queue:
        state = queue.popleft()
        for a in (0, 1):
            nxt = append_colour(state, a)
            word = shortest[state] + str(a)
            assert nxt == to_mask(point_types(word))
            if nxt not in shortest:
                shortest[nxt] = word
                queue.append(nxt)
    assert len(shortest) == 97, len(shortest)
    both = {state: word for state, word in shortest.items()
            if {int(c) for c in word} == {0, 1}}
    assert len(both) == 90
    assert max(len(word) for word in shortest.values()) == 8
    assert all(append_colour(s, a) in shortest
               for s in shortest for a in (0, 1))

    symmetric = {state for state in both if reverse_type(state) == state}
    assert len(symmetric) == 20, len(symmetric)
    pal_first = {}
    for n in range(10):
        for prefix in product('01', repeat=(n + 1) // 2):
            p = ''.join(prefix)
            pal = p + p[::-1][n % 2:]
            assert pal == pal[::-1] and len(pal) == n
            state = to_mask(point_types(pal))
            if state in both:
                pal_first.setdefault(state, pal)
    assert set(pal_first) == symmetric
    lengths = Counter(len(w) for w in pal_first.values())
    assert dict(sorted(lengths.items())) == {3: 2, 4: 2, 5: 6,
                                             6: 2, 7: 6, 9: 2}
    extremal = sorted(w for w in pal_first.values() if len(w) == 9)
    assert extremal == ['001010100', '110010011']
    for state in symmetric:
        pal = pal_first[state]
        assert two_move_equivalent(shortest[state], pal)
        assert to_mask(point_types(pal)) == state
    for pal in extremal:
        state = to_mask(point_types(pal))
        assert len(decode(state)) == 8
        assert all(len(w) >= 9 for w in pal_first.values()
                   if to_mask(point_types(w)) == state)
        assert len(shortest[state]) == 8
        assert any(c == 0 and left == right == 3
                   for c, left, right in decode(state))
        assert any(c == 1 and left == right == 3
                   for c, left, right in decode(state))

    print('ALL_RANK2_TYPES', len(shortest))
    print('BICOLOUR_RANK2_TYPES', len(both))
    print('REVERSAL_INVARIANT_BICOLOUR_TYPES', len(symmetric))
    print('PALINDROME_WITNESSES', len(pal_first))
    print('PAL_MINIMUM_LENGTH_DISTRIBUTION', dict(sorted(lengths.items())))
    print('EXTREMAL_PALINDROMES', extremal)
    print('BFS_CLOSURE_AND_DIRECT_EF_GAME', 'OK')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
