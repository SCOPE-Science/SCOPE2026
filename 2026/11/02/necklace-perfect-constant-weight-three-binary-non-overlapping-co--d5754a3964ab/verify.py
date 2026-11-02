"""Definition-level verification of sparse non-overlapping binary codes.

This is finite evidence for the accompanying all-length combinatorial proof.
Run with: python3 verify.py
"""
from itertools import combinations
from math import comb


def encode(n, positions):
    s = ['0'] * n
    for j in positions:
        s[j] = '1'
    return ''.join(s)


def code(n):
    k = n // 3
    return {encode(n, (0, a, b))
            for a in range(1, k + 1)
            for b in range(a + 1, n - k)}


def necklace(w):
    return min(w[j:] + w[:j] for j in range(len(w)))


def primitive(w):
    n = len(w)
    return all(w != w[j:] + w[:j] for j in range(1, n))


def verify(n):
    words = code(n)
    expected = (n - 1) * (n - 2) // 6
    assert len(words) == expected, (n, len(words), expected)
    assert all(len(w) == n and w.count('1') == 3 for w in words)
    prefixes = set()
    suffixes = set()
    for w in words:
        for j in range(1, n):
            prefixes.add(w[:j])
            suffixes.add(w[j:])
    assert not prefixes.intersection(suffixes), n
    seen = {necklace(w) for w in words}
    assert len(seen) == len(words), n
    allclasses = {necklace(encode(n, pos))
                  for pos in combinations(range(n), 3)
                  if primitive(encode(n, pos))}
    assert seen == allclasses, (n, len(seen), len(allclasses))
    if n % 3:
        assert allclasses and len(allclasses) == comb(n, 3) // n
    else:
        assert len(allclasses) == (comb(n, 3) - n // 3) // n
    return len(words)


def main():
    values = [(n, verify(n)) for n in range(4, 41)]
    print('Lengths:', len(values), 'range:', values[0][0], '-', values[-1][0])
    print('Selected sizes:', [(n, m) for n, m in values if n in (4, 5, 6, 7, 8, 9, 10, 12, 20, 30, 40)])
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
