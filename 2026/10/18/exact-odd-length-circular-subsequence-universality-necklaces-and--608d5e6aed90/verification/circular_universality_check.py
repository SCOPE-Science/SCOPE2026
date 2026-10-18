"""Reproducibility checks for maximum binary circular-subsequence universality.

Run with Python 3.9+: python circular_universality_check.py
No third-party packages are required. Finite checks supplement an all-length proof.
"""
from collections import Counter
from itertools import product
from math import gcd
from random import Random


def linear_index(w):
    arches = 0
    pending = -1
    for x in w:
        if pending < 0:
            pending = x
        elif x != pending:
            arches += 1
            pending = -1
    return arches


def circular_index(w):
    return max(linear_index(w[i:] + w[:i]) for i in range(len(w)))


def locally_maximal(w):
    n = len(w)
    if n < 2:
        return True
    edges = [w[i] ^ w[(i + 1) % n] for i in range(n)]
    if n % 2 == 0:
        return (all(edges[i] for i in range(0, n, 2)) or
                all(edges[i] for i in range(1, n, 2)))
    if all(edges):
        return False
    # Separate runs of transition edges by choosing a zero as a cut.
    start = edges.index(0)
    rotated = edges[start+1:] + edges[:start+1]
    blocks = []
    current = 0
    for e in rotated:
        if e:
            current += 1
        else:
            blocks.append(current)
            current = 0
    assert not current
    return sum(t % 2 == 0 for t in blocks) == 1


def expected_labeled(n):
    if n == 1:
        return 2
    if n % 2:
        return n * (1 << ((n - 1) // 2))
    return (1 << (n // 2 + 1)) - 2


def phi(n):
    return sum(gcd(n, j) == 1 for j in range(1, n + 1))


def expected_necklaces(n):
    if n == 1:
        return 2
    if n % 2:
        return 1 << ((n - 1) // 2)
    return sum(phi(n // d) * expected_labeled(d)
               for d in range(2, n + 1, 2) if n % d == 0) // n


def is_primitive(w):
    n = len(w)
    return not any(n % d == 0 and w == w[:d] * (n // d)
                   for d in range(1, n))


def necklace(w):
    return min(w[i:] + w[:i] for i in range(len(w)))


def full_check(n):
    total = 0
    lin_total = 0
    seen = set()
    for tup in product((0, 1), repeat=n):
        w = tuple(tup)
        actual = circular_index(w) == n // 2
        structural = locally_maximal(w)
        assert actual == structural, (n, w, actual, structural)
        if actual:
            total += 1
            seen.add(necklace(w))
            if n >= 3 and n % 2:
                assert is_primitive(w), (n, w)
        if linear_index(w) == n // 2:
            lin_total += 1
    assert total == expected_labeled(n), (n, total, expected_labeled(n))
    assert len(seen) == expected_necklaces(n), (n, len(seen), expected_necklaces(n))
    if n % 2:
        linear = (n // 2 + 2) * (1 << (n // 2)) if n >= 3 else 2
    else:
        linear = 1 << (n // 2)
    assert lin_total == linear, (n, lin_total, linear)
    return (n, total, len(seen), total - linear)


def random_check():
    rng = Random(20231014)
    for n in range(17, 81):
        for _ in range(100):
            w = tuple(rng.randrange(2) for _ in range(n))
            assert locally_maximal(w) == (circular_index(w) == n // 2)
            if n % 2 and locally_maximal(w):
                assert is_primitive(w)


def run():
    rows = [full_check(n) for n in range(1, 17)]
    random_check()
    print('Exhaustive n=1..16 and 6,400 seeded random n=17..80: PASS')
    print('n: (labeled maximum, necklaces, rotations rescued)')
    for n, a, b, c in rows:
        print(f'{n}: ({a}, {b}, {c})')
    print('ALL CHECKS PASSED')

if __name__ == '__main__':
    run()
