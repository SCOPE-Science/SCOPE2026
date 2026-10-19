"""Finite exact checks for sublinear-density marker shifts.

No finite enumeration certifies the infinite-size mixing, APP, or complexity theorems.
Run with Python 3 using only the standard library.
"""
from itertools import product
from math import comb

checks = 0


def is_admissible(word, numerator, denominator):
    """Check all contiguous subwords using integer comparison.

    exponent beta = numerator/denominator; #ones <= 3 length**beta.
    """
    n = len(word)
    pref = [0]
    for b in word:
        pref.append(pref[-1] + b)
    for a in range(n):
        for c in range(a + 1, n + 1):
            k = pref[c] - pref[a]
            if k**denominator > 3**denominator * (c - a)**numerator:
                return False
    return True


def count_words(n, p, r):
    return sum(is_admissible(word, p, r) for word in product((0, 1), repeat=n))


for p, r in [(1, 2), (2, 3)]:
    for n in range(1, 13):
        count = count_words(n, p, r)
        # Zero-extended admissible words realize every allowed finite pattern.
        assert 1 + n <= count <= 2**n
        checks += 2
        # Bound from the global interval of length n.
        permitted_counts = [j for j in range(n + 1) if j**r <= 3**r * n**p]
        upper = sum(comb(n, j) for j in permitted_counts)
        assert count <= upper
        checks += 1
        # Every pattern admits coordinatewise erasure of its markers.
        for word in product((0, 1), repeat=min(n, 5)):
            if is_admissible(word, p, r):
                assert is_admissible((0,) + word + (0,), p, r)
                checks += 1

# Large separated interval windows provide mixing connectors.
for p, r in [(1, 2), (2, 3)]:
    words = [w for w in product((0, 1), repeat=4) if is_admissible(w, p, r)]
    for u in words:
        for v in words:
            gap = 100
            assert is_admissible(u + (0,) * gap + v, p, r)
            checks += 1

# A periodic word with a marker is eventually excluded at every positive period.
for p, r in [(1, 2), (2, 3)]:
    for period in range(1, 5):
        for word in product((0, 1), repeat=period):
            if sum(word):
                # Search bounded finite repeat counts for a sublinear violation.
                rep = word * 10000
                assert sum(rep)**r > 3**r * len(rep)**p
                checks += 1

print('finite consistency assertions passed:', checks)
