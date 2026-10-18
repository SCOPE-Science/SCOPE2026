"""Independent, exhaustive checks for balanced scattered-palindrome maximizers.
Run with Python 3.10+: python research38_scattered_palindromes_check.py
The mathematical proof is self-contained; finite tests are corroboration only.
"""
from collections import Counter
from itertools import combinations, permutations


def pair_matchings(positions):
    if not positions:
        yield ()
        return
    first = positions[0]
    for second in positions[1:]:
        remaining = tuple(i for i in positions[1:] if i != second)
        for tail in pair_matchings(remaining):
            yield ((first, second),) + tail


def word_from_pairs(pairs):
    q = len(pairs)
    result = [-1] * (2 * q)
    for letter, (i, j) in enumerate(sorted(pairs)):
        result[i] = result[j] = letter
    return tuple(result)


def direct_palindromes(word, histogram=False):
    """Count distinct nonempty palindromic subsequence VALUES, not embeddings."""
    subsequences = {()}
    for letter in word:
        subsequences |= {sub + (letter,) for sub in tuple(subsequences)}
    pals = [v for v in subsequences if v and v == v[::-1]]
    return Counter(map(len, pals)) if histogram else len(pals)


def support_formula(word, histogram=False):
    """Different method: sum valid nested double occurrence pairs and centers."""
    q = len(word) // 2
    endpoints = [[] for _ in range(q)]
    for i, c in enumerate(word):
        endpoints[c].append(i)
    assert all(len(p) == 2 for p in endpoints)

    def nested(letters):
        ordered = sorted(letters, key=lambda c: endpoints[c][0])
        return all(endpoints[a][1] > endpoints[b][1]
                   for a, b in zip(ordered, ordered[1:]))

    total = 0
    lengths = Counter()
    for size in range(1, q + 1):
        for chosen in combinations(range(q), size):
            if nested(chosen):
                total += 1  # even palindrome, exactly once
                lengths[2 * size] += 1
            for center in chosen:
                others = tuple(c for c in chosen if c != center)
                if not nested(others):
                    continue
                if not others:
                    total += 1
                    lengths[1] += 1
                    continue
                innermost = max(others, key=lambda c: endpoints[c][0])
                left, right = endpoints[innermost]
                if any(left < site < right for site in endpoints[center]):
                    total += 1  # odd palindrome with this center
                    lengths[2 * size - 1] += 1
    return lengths if histogram else total


def canonical(word):
    recode = {}
    return tuple(recode.setdefault(x, len(recode)) for x in word)


def expected(q):
    begin = tuple(range(q))
    reverse = tuple(range(q - 1, -1, -1))
    if q == 1:
        return {begin + reverse}
    return {begin + reverse,
            begin + reverse[:0] + (q - 2, q - 1) + reverse[2:]}


def main():
    for q in range(1, 6):
        maxima = set()
        total = 0
        for matching in pair_matchings(tuple(range(2 * q))):
            word = word_from_pairs(matching)
            exact = direct_palindromes(word)
            other = support_formula(word)
            assert exact == other, (q, word, exact, other)
            assert direct_palindromes(word, histogram=True) == support_formula(word, histogram=True)
            assert exact <= (1 << (q + 1)) - 2
            if exact == (1 << (q + 1)) - 2:
                maxima.add(canonical(word))
            total += 1
        assert maxima == expected(q), (q, maxima, expected(q))
        for word in expected(q):
            lengths = support_formula(word, histogram=True)
            for k in range(1, q + 1):
                from math import comb
                tail_swap = q > 1 and word[q] == q - 2
                shifted = comb(q - 2, k - 2) if tail_swap and k >= 2 else 0
                assert lengths[2*k] == comb(q, k) - shifted
                assert lengths[2*k-1] == comb(q, k) + shifted
        print('Full matching enumeration: q=%d, matchings=%d, canonical maximizers=%d, MATCHED' %
              (q, total, len(maxima)))

    for q in (6, 7):
        maxima = set()
        prefix = tuple(range(q))
        for tail in permutations(range(q)):
            word = prefix + tail
            value = support_formula(word)
            assert value <= (1 << (q + 1)) - 2
            if value == (1 << (q + 1)) - 2:
                maxima.add(word)
        assert maxima == expected(q), (q, maxima)
        print('Independent permutation scan: q=%d, permutations=%d, maximizers=2, MATCHED' %
              (q, __import__('math').factorial(q)))
    print('ALL_SCATTERED_PALINDROME_CHECKS_PASSED')


if __name__ == '__main__':
    main()
