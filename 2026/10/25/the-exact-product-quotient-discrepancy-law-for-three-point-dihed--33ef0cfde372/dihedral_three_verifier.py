"""Exact finite checks for the three-point product/quotient spectrum of D_n.

Run with Python 3: python dihedral_three_verifier.py
Theorem for all n>=3 is established mathematically, not by this finite test.
"""
from collections import Counter, defaultdict
from itertools import combinations
from math import comb


def predicted(n):
    assert n >= 3
    triple_ap = n * (n - (1 if n % 2 else 2)) // 2
    if n % 3 == 0:
        triple_ap -= 2 * n // 3
    out = {0: Counter({0: comb(n, 3)}), 3: Counter({0: triple_ap,
                                             -1: comb(n, 3) - triple_ap})}
    if n % 2:
        v = Counter({0: n * (n - 1) // 2,
                     1: n * (n - 1),
                     3: n * (n - 1) * (n - 3) // 2})
        out[1] = v.copy()
        out[2] = v.copy()
    else:
        if n % 4:
            out[1] = Counter({0: n * (n - 1),
                              1: n * (n - 2),
                              3: n * (n - 2) * (n - 3) // 2})
        else:
            out[1] = Counter({0: n * n,
                              1: n * (n - 4),
                              3: n * (n * n - 5 * n + 8) // 2})
        out[2] = Counter({0: n * n // 2,
                          1: 2 * n * (n - 2),
                          3: n * (n - 2) * (n - 4) // 2})
    for x in out.values():
        for k in list(x):
            if not x[k]:
                del x[k]
    return out


def independently_enumerated(n):
    group = [(i, e) for e in range(2) for i in range(n)]

    def multiply(x, y):
        a, parity = x
        b, other = y
        return ((a + (b if parity == 0 else -b)) % n, parity ^ other)

    def inverse(x):
        a, parity = x
        return ((-a if parity == 0 else a) % n, parity)

    counts = defaultdict(Counter)
    for subset in combinations(group, 3):
        rotations = sum(e == 0 for _, e in subset)
        products = {multiply(x, y) for x in subset for y in subset}
        quotients = {multiply(x, inverse(y)) for x in subset for y in subset}
        counts[rotations][len(products) - len(quotients)] += 1
    return dict(counts)


def main():
    for n in range(3, 37):
        expected = predicted(n)
        obtained = independently_enumerated(n)
        assert obtained == expected, (n, expected, obtained)
        assert sum(map(sum, (v.values() for v in obtained.values()))) == comb(2 * n, 3)
    for n in [3, 4, 5, 6, 12, 24, 36]:
        freq = Counter()
        for row in predicted(n).values():
            freq.update(row)
        print('n=', n, 'distribution=', dict(sorted(freq.items())))
    print('VERIFY_OK n=3..36')


if __name__ == '__main__':
    main()
