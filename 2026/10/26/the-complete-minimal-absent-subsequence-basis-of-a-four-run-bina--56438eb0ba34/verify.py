#!/usr/bin/env python3
"""Check the four-run minimal-absent-subsequence basis by independent enumeration.
Run with Python 3.9+ and no external dependencies.
"""
from collections import Counter
from itertools import product
from math import comb


def proposed(a, b, c, d):
    """The symbolic eight-template candidate basis."""
    words = [
        '0' * (a + c + 1),
        '1' * (b + d + 1),
        '0' * (a + 1) + '1' * (d + 1),
        '1' * (b + 1) + '0',
        '1' + '0' * (c + 1),
    ]
    if c >= 2:
        words.append('0' * (a + 1) + '10')
    if b >= 2:
        words.append('10' + '1' * (d + 1))
    if b >= 2 and c >= 2:
        words.append('1010')
    return set(words)


def independent_subsequences(word):
    """Construct all distinct subsequences by position-by-position inclusion."""
    known = {''}
    for letter in word:
        known |= {u + letter for u in tuple(known)}
    return known


def independent_minimal_absent(word):
    """Generate all MAS without using a run formula or greedy embedding.

    Any minimal absent word has its proper prefix present; hence it is an
    extension of an observed subsequence by one symbol. Membership is tested
    from the independently constructed entire subsequence set.
    """
    present = independent_subsequences(word)
    out = set()
    for p in present:
        for ch in '01':
            u = p + ch
            if u in present:
                continue
            if all(u[:i] + u[i + 1:] in present for i in range(len(u))):
                out.add(u)
    return out


def embedded(word, subword):
    j = 0
    for symbol in word:
        if j < len(subword) and symbol == subword[j]:
            j += 1
    return j == len(subword)


def distribution(n):
    totals = Counter()
    for a in range(1, n-2):
        for b in range(1, n-a-1):
            for c in range(1, n-a-b):
                d = n-a-b-c
                if d < 1:
                    continue
                totals[len(proposed(a,b,c,d))] += 1
    return totals


def main():
    checked = 0
    for a,b,c,d in product(range(1,5), repeat=4):
        word = '0'*a + '1'*b + '0'*c + '1'*d
        observed = independent_minimal_absent(word)
        predicted = proposed(a,b,c,d)
        if observed != predicted:
            raise AssertionError((a,b,c,d,sorted(observed-predicted),sorted(predicted-observed)))
        assert len(predicted) == 5 + (b>=2) + (c>=2) + (b>=2 and c>=2)
        checked += 1

    # Longer configurations: verify individual predicted words by direct greedy
    # embedding; this is not used as proof that unlisted words do not exist.
    examples = 0
    for a,b,c,d in product((1,2,3,7,11),repeat=4):
        word = '0'*a + '1'*b + '0'*c + '1'*d
        for u in proposed(a,b,c,d):
            assert not embedded(word, u)
            assert all(embedded(word,u[:i]+u[i+1:]) for i in range(len(u)))
        examples += 1

    for n in range(4,41):
        actual = distribution(n)
        expected = {
            5: n-3,
            6: 2*comb(n-3,2) if n>=5 else 0,
            8: comb(n-3,3) if n>=6 else 0,
        }
        assert actual == Counter({k:v for k,v in expected.items() if v})
        assert sum(actual.values()) == comb(n-1,3)
    print(f'VERIFY_OK exhaustive_quadruples={checked} long_witness_checks={examples} composition_lengths=4..40')


if __name__ == '__main__':
    main()
