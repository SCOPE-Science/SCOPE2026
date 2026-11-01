"""Exhaustive canonical ternary-word certificate for a 9/10 adjacent-LCS obstruction.

Usage: python verify_exact.py [--json]
All arithmetic in the acceptance test is integral. No external dependencies.
"""
import json


def lcs(a, b):
    previous = [0] * (len(b) + 1)
    for x in a:
        row = [0]
        for j, y in enumerate(b, 1):
            row.append(previous[j - 1] + 1 if x == y else max(row[-1], previous[j]))
        previous = row
    return previous[-1]


def violating_split(word):
    n = len(word)
    for j in range(1, n):
        for i in range(j):
            value = lcs(word[i:j], word[j:])
            if 20 * value > 9 * (n - i):
                return [i, j, n, value]
    return None


def enumerate_words():
    current = [('0', 0)]
    counts = {1: 1}
    level32 = None
    rejected33 = []
    for n in range(2, 34):
        following = []
        for word, maximum in current:
            for symbol in range(min(2, maximum + 1) + 1):
                trial = word + str(symbol)
                counterexample = violating_split(trial)
                if counterexample is None:
                    following.append((trial, max(maximum, symbol)))
                elif n == 33:
                    rejected33.append({'word': trial, 'split': counterexample})
        counts[n] = len(following)
        if n == 32:
            level32 = [word for word, _ in following]
        current = following
    # A strict synchronization witness must satisfy 20*LCS < 9*length for
    # every adjacent pair, not just the weak threshold used for exclusion.
    witness = level32[0]
    strict_margin = min(
        9 * (k-i) - 20 * lcs(witness[i:j], witness[j:k])
        for k in range(2, 33) for j in range(1, k) for i in range(j)
    )
    assert strict_margin > 0
    return {'threshold': '20*LCS <= 9*total_length', 'canonical_counts': counts,
            'level32': level32, 'extensions33_rejected': rejected33,
            'strict_length32_witness': witness,
            'strict_min_integer_margin': strict_margin}


if __name__ == '__main__':
    data = enumerate_words()
    assert data['canonical_counts'][32] == len(data['level32'])
    assert data['canonical_counts'][33] == 0
    assert len(data['extensions33_rejected']) >= 20
    print(json.dumps(data, ensure_ascii=False, sort_keys=True, indent=2))
