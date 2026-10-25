"""Standalone direct-enumeration verifier of the finite and parametric SUPS assertions.

Run with Python 3: python verify_sups.py
This checks finite examples; the unbounded theorem rests on RESULT.md's proof.
"""
from collections import Counter
from itertools import combinations, product
import random


def runs(word):
    return 1 + sum(x != y for x, y in zip(word, word[1:]))


def unique_palindromic_occurrences(word):
    n = len(word)
    freq = Counter(word[i:j] for i in range(n) for j in range(i + 1, n + 1))
    return [(i, j - 1) for i in range(n) for j in range(i + 1, n + 1)
            if word[i:j] == word[i:j][::-1] and freq[word[i:j]] == 1]


def sups(word, lo, hi, unique=None):
    if unique is None:
        unique = unique_palindromic_occurrences(word)
    covered = [(i, j) for i, j in unique if i <= lo <= hi <= j]
    if not covered:
        return []
    minimum = min(j - i + 1 for i, j in covered)
    return [(i, j) for i, j in covered if j - i + 1 == minimum]


def all_five_run_words(n):
    for cuts in combinations(range(1, n), 4):
        pts = (0,) + cuts + (n,)
        lengths = tuple(pts[k + 1] - pts[k] for k in range(5))
        base = ''.join(str(k & 1) * value for k, value in enumerate(lengths))
        yield base
        yield base.translate(str.maketrans('01', '10'))


def finite_exhaustion():
    examined = 0
    sharp = set()
    triples = []
    for n in range(1, 15):
        # Exhaust all binary words of length n with at most five runs.
        # To avoid iterating all 2^n possibilities, enumerate all run cuts.
        for r in range(1, min(5, n) + 1):
            for cuts in combinations(range(1, n), r - 1):
                pts = (0,) + cuts + (n,)
                lengths = tuple(pts[k + 1] - pts[k] for k in range(r))
                for start in ('0', '1'):
                    word = ''.join((start if k % 2 == 0 else
                                    ('1' if start == '0' else '0')) * value
                                   for k, value in enumerate(lengths))
                    assert len(word) == n and runs(word) == r
                    unique = unique_palindromic_occurrences(word)
                    for lo in range(n):
                        for hi in range(lo, n):
                            answer = sups(word, lo, hi, unique)
                            assert len(answer) <= (2 if r <= 4 else 3), (word, lo, hi, answer)
                            if len(answer) == 3:
                                assert n == 14 and r == 5, (word, lo, hi)
                                triples.append((word, lo, hi, answer))
                                sharp.add(word)
                    examined += 1
    expected = '0' * 7 + '1' + '0' * 3 + '1' + '0' * 2
    orbit = {expected, expected[::-1],
             expected.translate(str.maketrans('01','10')),
             expected[::-1].translate(str.maketrans('01','10'))}
    assert sharp == orbit, (sharp, orbit)
    assert len(triples) == 4
    for word, lo, hi, answer in triples:
        assert lo == hi
    return examined, len(triples)


def infinite_family_tests():
    checks = 0
    for b in range(1, 9):
        for e in range(b + 1, b + 7):
            a = b + 2 * e + 2
            c = 2 * e - b
            word = '0' * a + '1' * b + '0' * c + '1' * b + '0' * e
            expected = [(0, a - 1), (a-e-1, a-e-1+a-1), (a-1, a-1+a-1)]
            got = sorted(sups(word, a - 1, a - 1))
            assert got == sorted(expected), (b,e,word,got,expected)
            checks += 1
    return checks


def larger_random_tests():
    rng = random.Random(8274725)
    cnt = 0
    for _ in range(400):
        r = rng.randint(1, 5)
        lengths = [rng.randint(1, 8) for _ in range(r)]
        start = rng.randint(0, 1)
        word = ''.join(str((k + start) % 2) * x for k, x in enumerate(lengths))
        unique = unique_palindromic_occurrences(word)
        n = len(word)
        for _ in range(6):
            lo = rng.randrange(n)
            hi = rng.randrange(lo, n)
            assert len(sups(word, lo, hi, unique)) <= (2 if r <= 4 else 3)
            cnt += 1
    return cnt

if __name__ == '__main__':
    n_words, triples = finite_exhaustion()
    parametric = infinite_family_tests()
    random_queries = larger_random_tests()
    print('VERIFY_OK low_run_words=%d minimal_triples=%d family_members=%d random_interval_queries=%d' %
          (n_words, triples, parametric, random_queries))
