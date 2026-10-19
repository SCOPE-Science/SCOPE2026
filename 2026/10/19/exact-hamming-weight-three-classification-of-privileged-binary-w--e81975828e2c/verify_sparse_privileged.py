#!/usr/bin/env python3
"""Self-contained finite checks of exact weight-three privileged-word formulas.

No experimental result substitutes for the all-length proof in RESULT.md.
"""
from functools import lru_cache
from itertools import combinations


@lru_cache(maxsize=None)
def privileged(word):
    if len(word) <= 1:
        return True
    for k in range(1, len(word)):
        u = word[:k]
        if word[-k:] != u or not privileged(u):
            continue
        occ = sum(word[j:j + k] == u for j in range(len(word) - k + 1))
        if occ == 2:
            return True
    return False


def classified(word):
    positions = [j for j, ch in enumerate(word) if ch == '1']
    if len(positions) != 3:
        return False
    i, j, k = positions
    a, b, c, d = i, j - i - 1, k - j - 1, len(word) - k - 1
    return (a == d and b == c) or (a == d and a > max(b, c))


def from_rational_formula(n):
    pal = (n - 1) // 2 if n >= 3 and n % 2 else 0
    nonpal = 0
    if n >= 8:
        target = n - 8
        for x in range(target // 2 + 1):
            for y in range(target // 3 + 1):
                rest = target - 2 * x - 3 * y
                if rest >= 0 and rest % 4 == 0:
                    nonpal += 2
    return pal, nonpal


def check(max_n=37):
    pairs = []
    for n in range(3, max_n + 1):
        total = pal_count = 0
        for p, q, r in combinations(range(n), 3):
            w = ('0' * p + '1' + '0' * (q - p - 1) + '1'
                 + '0' * (r - q - 1) + '1' + '0' * (n - r - 1))
            truth = privileged(w)
            structure = classified(w)
            assert truth == structure, ('classification', n, w, truth, structure)
            if truth:
                total += 1
                pal_count += (w == w[::-1])
        pal_expected, nonpal_expected = from_rational_formula(n)
        assert (pal_count, total - pal_count) == (pal_expected, nonpal_expected), n
        pairs.append((n, pal_count, total - pal_count))

    # Independently test the stated rational generating function through n=256.
    # (1-z^2)(1-z^3)(1-z^4)F(z)=z^3+z^5-z^6+z^8.
    den = {0: 1, 2: -1, 3: -1, 4: -1, 5: 1, 6: 1, 7: 1, 9: -1}
    num = {3: 1, 5: 1, 6: -1, 8: 1}
    coefficients = []
    for n in range(257):
        v = num.get(n, 0) - sum(coef * coefficients[n - degree]
                                for degree, coef in den.items()
                                if 0 < degree <= n)
        coefficients.append(v)
        p, q = from_rational_formula(n)
        assert v == p + q, ('rational identity', n, v, p + q)
    print('PASS: independent recursive definition versus gap classification n=3..%d' % max_n)
    print('PASS: palindromic and nonpalindromic exact counts n=3..%d' % max_n)
    print('PASS: rational generating-function coefficients n=0..256')
    print('Sample (n, palindromic, nonpalindromic):', pairs[:15])


if __name__ == '__main__':
    check()
