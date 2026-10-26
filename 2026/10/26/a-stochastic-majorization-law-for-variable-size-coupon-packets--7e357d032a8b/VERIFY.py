"""Exact checks of the finite packet-size majorization theorem.

Python 3 standard library only. Tests are finite, not a proof of generality.
"""
from fractions import Fraction
from itertools import combinations, product
from math import comb

COUNT = 0

def check(statement):
    global COUNT
    assert statement
    COUNT += 1

def pair_law(n, a, b):
    lo, hi = max(0, a + b - n), min(a, b)
    return [Fraction(comb(a, j) * comb(n - a, b - j), comb(n, b))
            if lo <= j <= hi else Fraction(0) for j in range(n + 1)]

def missing_law(n, packs):
    dist = [Fraction(0)] * (n + 1)
    dist[n] = Fraction(1)
    for s in packs:
        m = n - s
        nxt = [Fraction(0)] * (n + 1)
        for t, weight in enumerate(dist):
            if not weight:
                continue
            for j in range(max(0, t + m - n), min(t, m) + 1):
                nxt[j] += weight * Fraction(
                    comb(t, j) * comb(n - t, m - j), comb(n, m))
        dist = nxt
    return dist

def direct_law(n, packs):
    choices = [list(combinations(range(n), s)) for s in packs]
    dist = [0] * (n + 1)
    total = 1
    for c in choices:
        total *= len(c)
    for selected in product(*choices):
        covered = set().union(*map(set, selected))
        dist[n - len(covered)] += 1
    return [Fraction(x, total) for x in dist]

def main():
    for n in range(2, 18):
        for a in range(n + 1):
            for b in range(a + 2, n + 1):
                old, new = pair_law(n, a, b), pair_law(n, a + 1, b - 1)
                check(sum(old) == sum(new) == 1)
                check(all(sum(old[j:]) <= sum(new[j:]) for j in range(n + 1)))
                check(sum(j * old[j] for j in range(n + 1)) <
                      sum(j * new[j] for j in range(n + 1)))
                for j in range(n + 1):
                    if old[j]:
                        check(new[j] / old[j] == Fraction(
                            (a + 1) * (b - j) * (n - b + 1),
                            (a + 1 - j) * (n - a) * b))
    for n in range(3, 9):
        for sizes in product(range(n + 1), repeat=3):
            for i in range(3):
                for j in range(i + 1, 3):
                    if sizes[j] - sizes[i] >= 2:
                        more_equal = list(sizes)
                        more_equal[i] += 1
                        more_equal[j] -= 1
                        before = missing_law(n, sizes)
                        after = missing_law(n, more_equal)
                        check(all(sum(before[r:]) <= sum(after[r:])
                                  for r in range(n + 1)))
    for n in range(2, 5):
        for sizes in product(range(n + 1), repeat=3):
            check(missing_law(n, sizes) == direct_law(n, sizes))
    check(missing_law(4, (1, 3)) ==
          [Fraction(1, 4), Fraction(3, 4), Fraction(0), Fraction(0), Fraction(0)])
    check(missing_law(4, (2, 2)) ==
          [Fraction(1, 6), Fraction(2, 3), Fraction(1, 6), Fraction(0), Fraction(0)])
    print(f"PASS: {COUNT} exact assertions")

if __name__ == "__main__":
    main()
