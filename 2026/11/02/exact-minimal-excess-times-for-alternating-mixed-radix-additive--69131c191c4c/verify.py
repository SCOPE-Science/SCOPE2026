"""Finite cross-check of exact return times for alternating mixed-radix complements.

This script verifies bounded instances only. The infinite classification is proved
by the digit argument in RESULT.md.
"""
from bisect import bisect_right


def check(radices):
    places = [1]
    for base in radices:
        assert base >= 2
        places.append(places[-1] * base)
    left = {0}
    right = {0}
    for i, base in enumerate(radices):
        place = places[i]
        if i % 2 == 0:
            left = {v + j * place for v in left for j in range(base)}
        else:
            right = {v + j * place for v in right for j in range(base)}
    L = sorted(left)
    R = sorted(right)
    total = places[-1]
    assert len(L) * len(R) == total
    # Independent uniqueness and cover check, not derived from the theorem.
    seen = bytearray(total)
    for a in L:
        for b in R:
            assert seen[a + b] == 0
            seen[a + b] = 1
    assert all(seen)
    exact = {n for n in range(total)
             if bisect_right(L, n) * bisect_right(R, n) == n + 1}
    predicted = {t * places[i] - 1 for i, base in enumerate(radices)
                 for t in range(1, base)}
    predicted.add(total - 1)
    assert exact == predicted, (radices, sorted(exact), sorted(predicted))
    assert len(exact) == 1 + sum(b - 1 for b in radices)
    return total, len(exact)


def main():
    cases = [
        (2,) * 15,
        (3,) * 8,
        (4,) * 6,
        (5,) * 6,
        (2, 3, 4, 5, 3, 2),
        (3, 2, 5, 2),
        (4, 7, 2, 3),
        (7, 2, 2, 4),
        (2, 3, 2, 5, 3, 2, 2),
    ]
    for bases in cases:
        modulus, matches = check(bases)
        print('case', ','.join(map(str, bases)),
              'integers', modulus, 'minimal_excess', matches, 'PASS')
    print('VERIFY_OK cases', len(cases), 'scope finite_only')


if __name__ == '__main__':
    main()
