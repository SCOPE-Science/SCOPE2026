"""Exact-arithmetic verification for a binary Parikh-class sandwich profile.

Uses the Python standard library. Run: python check.py
"""
from collections import Counter, defaultdict
from itertools import combinations
from math import comb


def poly_add(p, q):
    out = Counter(p)
    for k, v in q.items():
        out[k] += v
    return +out


def gaussian(n, k):
    """Coefficient dictionary for the Gaussian binomial [n choose k]_z."""
    if not 0 <= k <= n:
        return Counter()
    tab = [Counter({0: 1})] + [Counter() for _ in range(k)]
    for nn in range(1, n + 1):
        new = [Counter({0: 1})] + [Counter() for _ in range(k)]
        for kk in range(1, min(k, nn) + 1):
            if kk == nn:
                new[kk] = Counter({0: 1})
            else:
                new[kk] = poly_add(tab[kk], {j + nn - kk: v for j, v in tab[kk - 1].items()})
        tab = new
    return tab[k]


def predicted(a, b):
    """Polynomial coefficients indexed by (interior-b count, ab count)."""
    ans = Counter()
    for s in range(b + 1):
        h = gaussian(s + a - 2, a - 2)
        for z in range(b - s + 1):
            for exponent, coefficient in h.items():
                ans[(s, s + a * z + exponent)] += coefficient
    return ans


def observed(a, b):
    """Independent direct enumeration of actual words and pair positions."""
    result = Counter()
    N = a + b
    for pa in combinations(range(N), a):
        aset = set(pa)
        word = ''.join('a' if i in aset else 'b' for i in range(N))
        interior = sum(ch == 'b' for ch in word[pa[0] + 1:pa[-1]])
        ab = sum(sum(word[i] == 'a' for i in range(j))
                 for j, ch in enumerate(word) if ch == 'b')
        result[(interior, ab)] += 1
    return result


def spectrum(a, b, c):
    M = min(b, c, a*b - c)
    if a == 2:
        return {s for s in range(M + 1) if (s-c) % 2 == 0}
    result = set(range(2, M + 1))
    result.add(0 if c % a == 0 else 1)
    return result


def subsequence(pattern, word):
    p = 0
    for char in word:
        if p < len(pattern) and char == pattern[p]:
            p += 1
    return p == len(pattern)


def check():
    cases = 0
    checked_words = 0
    cells = 0
    spectrum_cases = 0
    tests = 0
    for a in range(2, 8):
        for b in range(0, 8):
            obs = observed(a, b)
            pred = predicted(a, b)
            assert obs == pred, ('coefficient discrepancy', a, b, obs - pred, pred - obs)
            assert sum(obs.values()) == comb(a+b, a)
            observed_marginal = Counter()
            for (s,c), v in obs.items():
                observed_marginal[c] += v
            assert observed_marginal == gaussian(a+b, a), ('marginal discrepancy', a,b)
            for c in range(a*b + 1):
                support = {s for (s, cc), v in obs.items() if cc == c and v > 0}
                assert support == spectrum(a, b, c), ('spectrum discrepancy',a,b,c,support)
                spectrum_cases += 1
            cases += 1
            cells += len(obs)
            checked_words += comb(a+b, a)
    for a in range(2, 6):
        for b in range(0, 6):
            N = a+b
            for pa in combinations(range(N), a):
                aset = set(pa)
                word = ''.join('a' if i in aset else 'b' for i in range(N))
                interior = sum(ch == 'b' for ch in word[pa[0]+1:pa[-1]])
                for t in range(1, b+2):
                    assert subsequence('a'+'b'*t+'a', word) == (interior>=t)
                    tests += 1
    for a,b,c in ((3,4,6),(3,4,5),(2,3,3),(4,4,8)):
        o = observed(a,b)
        dist = {s:o[(s,c)] for s in range(b+1) if o[(s,c)]}
        print('example',a,b,c,dict(sorted(dist.items())))
    print('PASS: exact joint Gaussian-binomial polynomial against independent exhaustive word enumeration')
    print('PASS: all Gaussian-binomial marginals and exact support spectra')
    print('PASS: scattered-pattern occurrence iff interior count threshold')
    print('parameter_pairs',cases, 'enumerated_words', checked_words, 'nonzero_joint_coefficients',cells)
    print('verified_spectra',spectrum_cases, 'direct_pattern_tests',tests)


if __name__ == '__main__':
    check()
