"""Exhaustive finite checks for the threshold-one contextual deletion map.

Run with Python 3: python verify.py
"""
from itertools import product
from math import comb


def channel(word):
    # Delete each position following a change of symbol in the original input.
    return tuple(word[i] for i in range(len(word))
                 if i == 0 or word[i] == word[i - 1])


def transition_count(word):
    return sum(a != b for a, b in zip(word, word[1:]))


def canonical_preimage(output, n):
    assert output and len(output) + transition_count(output) <= n
    blocks = []
    for c in output:
        if blocks and blocks[-1][0] == c:
            blocks[-1][1] += 1
        else:
            blocks.append([c, 1])
    word = [blocks[0][0]] * blocks[0][1]
    for c, length in blocks[1:]:
        word += [c] * (length + 1)
    while len(word) < n:
        word.append((word[-1] + 1) % q_for_symbol)
    return tuple(word)


def predicted_count(q, n):
    return sum(q * comb(m - 1, t) * (q - 1) ** t
               for m in range(1, n + 1)
               for t in range(m)
               if m + t <= n)


for q_for_symbol, maximum_n in [(2, 14), (3, 9), (4, 7), (5, 6)]:
    alphabet = range(q_for_symbol)
    counts = []
    for n in range(1, maximum_n + 1):
        observed = {channel(word) for word in product(alphabet, repeat=n)}
        predicted = {y for m in range(1, n + 1)
                     for y in product(alphabet, repeat=m)
                     if m + transition_count(y) <= n}
        assert observed == predicted, (q_for_symbol, n)
        assert len(observed) == predicted_count(q_for_symbol, n)
        if n <= 7:
            for y in predicted:
                assert channel(canonical_preimage(y, n)) == y
        counts.append(len(observed))
    print(f'q={q_for_symbol}: image counts {counts}')
print('VERIFY_OK')
