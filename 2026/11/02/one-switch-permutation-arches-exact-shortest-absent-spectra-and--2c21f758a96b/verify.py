"""Independent finite checks for permutation-block shortest absent subsequences.

This test exhausts candidate patterns and separately constructs all subsequences
for small instances. Finite checks are not an infinite proof.
"""
from itertools import permutations, product
from math import comb


def embeds_greedily(source, target):
    j = 0
    for letter in source:
        if j < len(target) and target[j] == letter:
            j += 1
    return j == len(target)


def all_length_subsequences(source, length):
    sets = [set() for _ in range(length + 1)]
    sets[0].add(())
    for letter in source:
        for r in range(length, 0, -1):
            sets[r].update(t + (letter,) for t in sets[r - 1])
    return sets[length]


def formula(p, r, a, b):
    q = len(p)
    rp = {c: i + 1 for i, c in enumerate(p)}
    rr = {c: i + 1 for i, c in enumerate(r)}
    return sum(comb(a + q - rp[c], a) * comb(b + rr[c] - 1, b)
               for c in p)


def criterion(v, p, r, a, b):
    rp = {c: i for i, c in enumerate(p)}
    rr = {c: i for i, c in enumerate(r)}
    return (all(rp[v[i]] >= rp[v[i + 1]] for i in range(a)) and
            all(rr[v[i]] >= rr[v[i + 1]] for i in range(a, a + b)))


def main():
    candidate_cases = 0
    candidate_patterns = 0
    independent_set_cases = 0
    strict_extrema_cases = 0
    for q in (2, 3, 4, 5):
        p = tuple(range(q))
        ranges = range(1, 4) if q <= 4 else range(1, 3)
        for r in permutations(p):
            for a in ranges:
                for b in ranges:
                    n = a + b + 1
                    source = p * a + r * b
                    got = 0
                    for v in product(p, repeat=n):
                        absent = not embeds_greedily(source, v)
                        assert absent == criterion(v, p, r, a, b), (q, r, a, b, v)
                        got += absent
                        candidate_patterns += 1
                    assert got == formula(p, r, a, b), (q, r, a, b, got)
                    candidate_cases += 1
                    if (q <= 3 and a <= 2 and b <= 2) or (q == 4 and a == b == 1):
                        subs = all_length_subsequences(source, n)
                        independent_count = q ** n - len(subs)
                        assert independent_count == got, (q, r, a, b)
                        independent_set_cases += 1
        for a, b in ((1, 1), (1, 2), (2, 3)):
            scores = [(formula(p, r, a, b), r) for r in permutations(p)]
            assert [r for score, r in scores if score == min(s[0] for s in scores)] == [p]
            assert [r for score, r in scores if score == max(s[0] for s in scores)] == [p[::-1]]
            strict_extrema_cases += 1
    balancing_cases = 0
    for q in range(2, 11):
        for k in range(2, 51):
            v = [sum(comb(s + a - 1, a) * comb(s + (k - a) - 1, k - a)
                     for s in range(1, q + 1)) for a in range(1, k)]
            best = max(v)
            maximizing = {a + 1 for a, val in enumerate(v) if val == best}
            assert maximizing == {k // 2, (k + 1) // 2}
            balancing_cases += 1
    print('VERIFY_OK candidate_cases=%d candidate_patterns=%d independent_set_cases=%d '
          'strict_extrema_cases=%d balancing_cases=%d' %
          (candidate_cases, candidate_patterns, independent_set_cases,
           strict_extrema_cases, balancing_cases))


if __name__ == '__main__':
    main()
