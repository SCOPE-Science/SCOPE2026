"""Finite exhaustive certificate for the first nonunique ternary subsequence covers.
Run with Python 3.9+ and no external dependencies.
"""
from itertools import product, combinations
from collections import defaultdict
from hashlib import sha256

ALPHABET = '012'


def subsequence_cover(pattern, word):
    """Check that every word position lies in a subsequence embedding of pattern.

    prefix[i] is the longest pattern prefix embedded before word[i].
    suffix[i] is the longest pattern suffix embedded from word[i] onward.
    """
    m, n = len(pattern), len(word)
    if not (1 <= m <= n) or pattern[0] != word[0] or pattern[-1] != word[-1]:
        return False
    prefix = [0] * (n + 1)
    j = 0
    for i, ch in enumerate(word):
        if j < m and ch == pattern[j]:
            j += 1
        prefix[i + 1] = j
    if j != m:
        return False
    suffix = [0] * (n + 1)
    j = m - 1
    for i in range(n - 1, -1, -1):
        if j >= 0 and word[i] == pattern[j]:
            j -= 1
        suffix[i] = m - 1 - j
    return all(any(pattern[k] == ch and k <= prefix[i]
                   and m - 1 - k <= suffix[i + 1]
                   for k in range(m))
               for i, ch in enumerate(word))


def positional_cover(pattern, word):
    """Independent small-case test by enumerating ALL embeddings as index tuples."""
    m, n = len(pattern), len(word)
    mask = 0
    for indices in combinations(range(n), m):
        if ''.join(word[i] for i in indices) == pattern:
            for i in indices:
                mask |= 1 << i
    return mask == (1 << n) - 1


def primitive_candidates():
    """Build exactly the s-primitive words of lengths 1 through 9.

    Adjacent equal letters make a word nonprimitive. A shortest s-cover
    is s-primitive, by transitivity of subsequence covers. Hence the
    previously found primitive words test primitivity without omissions.
    """
    primitive = []
    counts = []
    for length in range(1, 10):
        added = 0
        for letters in product(ALPHABET, repeat=length):
            if any(letters[i] == letters[i+1] for i in range(length-1)):
                continue
            word = ''.join(letters)
            if any(subsequence_cover(c, word) for c in primitive):
                continue
            primitive.append(word)
            added += 1
        counts.append(added)
    return primitive, counts


def main():
    # Independent direct embedding test for every pattern/word over 3 letters
    # with pattern length <= 4 and word length <= 6.
    independent_pairs = 0
    for n in range(1, 7):
        for tup in product(ALPHABET, repeat=n):
            word = ''.join(tup)
            for m in range(1, min(n, 4)+1):
                for p in product(ALPHABET, repeat=m):
                    pattern = ''.join(p)
                    assert subsequence_cover(pattern, word) == positional_cover(pattern, word)
                    independent_pairs += 1

    primitive, counts = primitive_candidates()
    assert counts == [3, 6, 12, 18, 30, 36, 30, 12, 0], counts
    assert len(primitive) == 147

    by_endpoints = defaultdict(list)
    for p in primitive:
        by_endpoints[(p[0], p[-1])].append(p)
    for cands in by_endpoints.values():
        cands.sort(key=len)

    totals = []
    exceptional = []
    for n in range(1, 12):
        nonunique = 0
        for tup in product(ALPHABET, repeat=n):
            word = ''.join(tup)
            shortest_length = n + 1
            shortest = []
            for p in by_endpoints[(word[0], word[-1])]:
                m = len(p)
                if m > n or m > shortest_length:
                    break
                if subsequence_cover(p, word):
                    if m < shortest_length:
                        shortest_length, shortest = m, []
                    shortest.append(p)
            assert shortest, ('no s-cover', word)
            if len(shortest) > 1:
                nonunique += 1
                exceptional.append((word, tuple(shortest)))
                assert n == 11 and shortest_length == 6 and len(shortest) == 2
        totals.append(nonunique)
    assert totals == [0] * 10 + [6], totals
    expected = {
        ('01012021010', ('010210', '012010')),
        ('02021012020', ('020120', '021020')),
        ('10102120101', ('101201', '102101')),
        ('12120102121', ('120121', '121021')),
        ('20201210202', ('201202', '202102')),
        ('21210201212', ('210212', '212012')),
    }
    assert set(exceptional) == expected
    for word, covers in exceptional:
        for c in covers:
            assert positional_cover(c, word)
        # Independently exclude every candidate of length at most five.
        for length in range(1, 6):
            for p in product(ALPHABET, repeat=length):
                assert not positional_cover(''.join(p), word)
    printed = '\n'.join(w + ' ' + ','.join(cs) for w, cs in exceptional)
    print('INDEPENDENT_EMBEDDING_TESTS', independent_pairs)
    print('PRIMITIVE_COUNTS_LENGTHS_1_TO_9', *counts)
    print('NONUNIQUE_COUNTS_LENGTHS_1_TO_11', *totals)
    print('SHORTEST_NONUNIQUE_LENGTH', 11)
    print('EXCEPTIONAL_WORDS', len(exceptional))
    print('EXCEPTIONAL_RECORDS_SHA256', sha256(printed.encode('utf-8')).hexdigest())
    print(printed)
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
