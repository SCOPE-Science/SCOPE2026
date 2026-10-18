"""Independent finite tests of the reversed-block maximal-subsequence theorem.

Requires only the Python standard library. Exhaustive tests are finite and do
not replace the proof supplied with the theorem.
"""
from collections import defaultdict
from math import comb


def subsequences(s):
    obtained = {()}
    for letter in s:
        obtained.update({word + (letter,) for word in tuple(obtained)})
    return obtained


def brute_maximal(q, m):
    inc = tuple(range(q)) * m
    dec = tuple(range(q - 1, -1, -1)) * m
    common = subsequences(inc) & subsequences(dec)
    maximal = set()
    for word in common:
        if not any(word[:j] + (c,) + word[j:] in common
                   for j in range(len(word) + 1)
                   for c in range(q)):
            maximal.add(word)
    return maximal


def classified(q, m):
    target = m - 1
    states = {(i, 0, 0): {(i,)} for i in range(q)}
    for length in range(1, 2 * m - 1):
        new = defaultdict(set)
        for (last, asc, desc), words in states.items():
            for nxt in range(q):
                if nxt == last:
                    continue
                aa, dd = asc + (last < nxt), desc + (last > nxt)
                if aa <= target and dd <= target:
                    new[(nxt, aa, dd)].update(w + (nxt,) for w in words)
        states = new
    return {w for (last, aa, dd), words in states.items()
            if aa == dd == target for w in words}


def dynamic_count(q, m):
    states = {(i, 0, 0): 1 for i in range(q)}
    for _ in range(2 * m - 2):
        new = defaultdict(int)
        for (last, asc, desc), multiplicity in states.items():
            for nxt in range(q):
                if nxt == last:
                    continue
                aa, dd = asc + (last < nxt), desc + (last > nxt)
                if aa < m and dd < m:
                    new[(nxt, aa, dd)] += multiplicity
        states = new
    return sum(v for (last, aa, dd), v in states.items()
               if aa == dd == m - 1)


def ternary_formula(m):
    return (comb(2 * m + 2, m + 1) - 2 * comb(2 * m, m)
            + comb(2 * m - 2, m - 1))


def main():
    exhaustive = 0
    for q in range(2, 6):
        for m in range(1, 4):
            lhs = brute_maximal(q, m)
            rhs = classified(q, m)
            assert lhs == rhs, (q, m, len(lhs), len(rhs), lhs ^ rhs)
            assert dynamic_count(q, m) == len(rhs)
            exhaustive += 1
    for m in range(4, 7):
        lhs = brute_maximal(3, m)
        rhs = classified(3, m)
        assert lhs == rhs and len(rhs) == ternary_formula(m)
        exhaustive += 1
    for m in range(1, 41):
        assert dynamic_count(3, m) == ternary_formula(m), m
    print('exhaustive structural cells:', exhaustive)
    print('ternary dynamic-formula cells:', 40)
    print('ternary m=1..12:', [ternary_formula(m) for m in range(1, 13)])
    print('q=2..5 m=1..3:',
          [[dynamic_count(q, m) for m in range(1, 4)] for q in range(2, 6)])
    print('all finite checks passed')


if __name__ == '__main__':
    main()
