"""Independent direct-partition check for short binary reverse shuffle squares.

Checks every input word, rather than constructing outputs from given roots.
"""
from itertools import combinations, product
from math import comb


def direct_counts(n):
    positions = range(2 * n)
    supports = [frozenset(c) for c in combinations(positions, n)]
    hist = {}
    maxima = []
    max_count = -1
    for bits in product('01', repeat=2 * n):
        w = ''.join(bits)
        roots = set()
        for selected in supports:
            left = ''.join(w[i] for i in positions if i in selected)
            right = ''.join(w[i] for i in positions if i not in selected)
            if left == right[::-1]:
                roots.add(left)
        k = len(roots)
        if k:
            hist[k] = hist.get(k, 0) + 1
            if k > max_count:
                max_count = k
                maxima = [w]
            elif k == max_count:
                maxima.append(w)
    assert sum(hist.values()) == comb(2*n, n)
    return max_count, sorted(maxima), hist


def test():
    expected = (1, 2, 3, 5, 9, 16, 29)
    for n, target in enumerate(expected, 1):
        # Complete direct-word, direct-partition check through n=6;
        # the second generator algorithm covers n=7 through n=10.
        if n == 7: break
        max_count, maximizers, hist = direct_counts(n)
        assert max_count == target, (n, max_count, target)
        assert len(maximizers) == (2 if n == 1 else 4 if n == 2 else 8)
        print(f'DIRECT n={n} maximum={max_count} maximizers={len(maximizers)}')
    print('INDEPENDENT DIRECT CHECKS PASSED')


if __name__ == '__main__':
    test()
