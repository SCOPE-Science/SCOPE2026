"""Reproduce finite checks for dyadic-prefix power-of-two string attractors.

The infinite theorem is established in RESULT.md; this program checks
finite instances and the stated unique-factor lower-bound certificates.
Python standard library only; one-based indexing throughout mathematics.
"""


def prefix(k):
    n = 1 << k
    return ''.join('1' if i & (i - 1) == 0 else '0' for i in range(1, n + 1))


def marks(k):
    n = 1 << k
    return sorted(set([1 << t for t in range(1, k, 2)] + [n // 2, n - 1]))


def unique_witnesses(k):
    assert k >= 2
    n = 1 << k
    certificates = []
    for j in range(k // 2):
        a = 1 << (2 * j)
        b = 2 * a
        certificates.append((a, b, '1' + '0' * (a - 1) + '1'))
    if k % 2 == 0:
        certificates.append((n // 2 + 1, n - 1, '0' * (n // 2 - 1)))
    else:
        m = (k - 1) // 2
        q = 1 << (2 * m - 2)
        certificates.append((3 * q, 4 * q + 1, '0' * q + '10'))
        certificates.append((6 * q, 8 * q, '0' * (2 * q) + '1'))
    return certificates


def verify_covered(word, gamma):
    # Enumerate every distinct factor and check whether some occurrence
    # intersects a selected position. O(n^2) factor enumeration.
    seen = set()
    for i in range(len(word)):
        crosses = False
        for j in range(i, len(word)):
            crosses = crosses or (j + 1 in gamma)
            factor = word[i:j + 1]
            if factor not in seen:
                seen.add(factor)
                if crosses:
                    continue
                if not any(factor == word[t:t + len(factor)]
                           and any(t < z <= t + len(factor) for z in gamma)
                           for t in range(len(word) - len(factor) + 1)):
                    return False, factor
    return True, len(seen)


def verify(k, coverage):
    word = prefix(k)
    gamma = marks(k)
    assert len(gamma) == (k + 1) // 2 + 1
    witnesses = unique_witnesses(k)
    assert len(witnesses) == len(gamma)
    last_end = 0
    for a, b, factor in witnesses:
        assert a > last_end, (k, a, last_end)
        assert word[a - 1:b] == factor, (k, a, b)
        assert sum(word[t:t + len(factor)] == factor
                   for t in range(len(word) - len(factor) + 1)) == 1, (k, a, b)
        last_end = b
    if coverage:
        ok, info = verify_covered(word, set(gamma))
        assert ok, (k, info)
        print('k=%d, n=%d, optimum=%d, covered_factors=%d, witnesses=%d' %
              (k, len(word), len(gamma), info, len(witnesses)))
    else:
        print('k=%d, n=%d, optimum=%d, unique_disjoint_witnesses=%d' %
              (k, len(word), len(gamma), len(witnesses)))


if __name__ == '__main__':
    assert prefix(1) == '11'
    for k in range(2, 11):
        verify(k, coverage=(k <= 9))
    print('PASS: all tested construction and lower-certificate instances')
