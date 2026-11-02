"""Standalone checks for exact cyclic binary sliding-weight read fibers.

Run: python3 verify.py
No external dependencies; all arithmetic uses exact integers.
"""
from collections import Counter, defaultdict
from itertools import combinations
from math import comb, gcd


def read_vector(word, ell):
    n = len(word)
    return tuple(sum(word[(i + j) % n] for j in range(ell))
                 for i in range(n))


def histogram_formula(n, ell):
    d = gcd(n, ell)
    L = n // d
    m = 2**L - 2
    H = Counter()
    for p in range(d + 1):
        for h in range(p + 1):
            H[comb(p, h)] += comb(d, p) * m ** (d - p)
    return H


def weight_polynomial_formula(n, ell):
    d = gcd(n, ell)
    L = n // d
    mixed = [0] * (L + 1)
    for s in range(1, L):
        mixed[s] = comb(L, s)
    def times(a, b):
        z = [0] * (len(a) + len(b) - 1)
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                z[i + j] += x * y
        return z
    powers = [[1]]
    for i in range(d):
        powers.append(times(powers[-1], mixed))
    answer = [0] * (n + 1)
    for p in range(d + 1):
        for h in range(p + 1):
            for w, count in enumerate(powers[d - p]):
                if w + L * h <= n:
                    answer[w + L * h] += comb(d, p) * count
    return answer


def inverse_words(y, ell):
    """Recover *all* binary inputs from indexed cyclic window sums."""
    n = len(y)
    d = gcd(n, ell)
    L = n // d
    base = [None] * n
    pure = []
    for r in range(d):
        locations = []
        increments = []
        pos = r
        value = 0
        for _ in range(L):
            locations.append(pos)
            increments.append(value)
            value += y[(pos + 1) % n] - y[pos]
            pos = (pos + ell) % n
        if pos != r or value != 0:
            return []
        allowed = [shift for shift in (0, 1)
                   if all(value + shift in (0, 1) for value in increments)]
        if len(allowed) == 0:
            return []
        if len(allowed) == 2:
            pure.append(locations)
        else:
            for loc, inc in zip(locations, increments):
                base[loc] = inc + allowed[0]
    # All ell-long windows meet every residue class ell/d times.
    known_at_zero = sum(base[i] for i in range(ell) if base[i] is not None)
    q = ell // d
    deficit = y[0] - known_at_zero
    if deficit % q:
        return []
    h = deficit // q
    if h < 0 or h > len(pure):
        return []
    output = []
    for selected in combinations(range(len(pure)), h):
        selected = set(selected)
        word = base.copy()
        for r, locations in enumerate(pure):
            for loc in locations:
                word[loc] = int(r in selected)
        if read_vector(word, ell) == tuple(y):
            output.append(tuple(word))
    return output


def check_all():
    word_count = 0
    profile_count = 0
    inverse_cases = 0
    for n in range(2, 15):
        for ell in range(1, n + 1):
            groups = defaultdict(list)
            for mask in range(1 << n):
                word = tuple((mask >> i) & 1 for i in range(n))
                groups[read_vector(word, ell)].append(word)
                word_count += 1
            profile_count += len(groups)
            d = gcd(n, ell)
            L = n // d
            m = 2**L - 2
            A = (m + 1)**d + d * (m + 1)**(d - 1)
            S = 2 * (m + 1)**d - m**d
            assert len(groups) == A, (n, ell, 'capacity')
            assert sum(len(v) == 1 for v in groups.values()) == S
            assert max(map(len, groups.values())) == comb(d, d // 2)
            assert Counter(map(len, groups.values())) == histogram_formula(n, ell)
            got_weight = Counter(sum(words[0]) for words in groups.values())
            assert [got_weight[w] for w in range(n + 1)] == weight_polynomial_formula(n, ell)
            assert sum(len(v) for v in groups.values()) == 2**n
            if n <= 8:
                for y, words in groups.items():
                    assert sorted(inverse_words(y, ell)) == sorted(words), (n, ell, y)
                    inverse_cases += 1
    # Check the explicit rate example with n=12, ell=6.
    assert histogram_formula(12, 6)[20] == 1
    print('VERIFY_OK', 'source_words=', word_count,
          'profiles=', profile_count, 'inverse_cases=', inverse_cases,
          'all_n=2..14', 'all_ell=1..n')


if __name__ == '__main__':
    check_all()
