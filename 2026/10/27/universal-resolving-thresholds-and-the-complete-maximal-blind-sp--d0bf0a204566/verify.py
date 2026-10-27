"""Independent finite checks of equal-distance obstructions in Hamming graphs.

Usage: python3 verify.py
Only Python's standard library is required.
"""
from itertools import combinations, permutations, product
from math import comb


def predicted(d, q):
    vertices = list(product(range(q), repeat=d))
    families = set()
    if q == 2 and d == 1:
        families.add(frozenset())
    elif q == 2:
        for i, j in combinations(range(d), 2):
            for parity in range(2):
                families.add(frozenset(z for z in vertices
                                       if (z[i] ^ z[j]) == parity))
    elif q == 3:
        for i in range(d):
            for a in range(q):
                families.add(frozenset(z for z in vertices if z[i] == a))
        for i, j in combinations(range(d), 2):
            for p in permutations(range(q)):
                families.add(frozenset(z for z in vertices if z[j] == p[z[i]]))
    else:
        for i in range(d):
            for a, b in combinations(range(q), 2):
                families.add(frozenset(z for z in vertices
                                       if z[i] not in (a, b)))
    return families


def expected_resolving_number(d, q):
    if q == 2:
        return 1 if d == 1 else (2 ** (d - 1) + 1)
    return (q - 2) * q ** (d - 1) + 1


def equalizer_count_by_distance(d, q, r):
    # Direct coefficient extraction from (t^(-1) + q - 2 + t)^r.
    return q ** (d-r) * sum(
        comb(r, j) * comb(r-j, j) * (q-2) ** (r-2*j)
        for j in range(r//2+1)
    )


def actual_maximal_nonresolving_sets(d, q):
    vertices = list(product(range(q), repeat=d))
    n = len(vertices)
    table = [[sum(a != b for a, b in zip(x, z))
              for z in vertices] for x in vertices]
    maximal_size = -1
    winners = set()
    for a in range(n):
        for b in range(a+1, n):
            eq = frozenset(vertices[z] for z in range(n)
                           if table[a][z] == table[b][z])
            if len(eq) > maximal_size:
                maximal_size = len(eq)
                winners = {eq}
            elif len(eq) == maximal_size:
                winners.add(eq)
    return maximal_size, winners


def check(d, q):
    size, actual = actual_maximal_nonresolving_sets(d, q)
    expected = predicted(d, q)
    max_formula = max(equalizer_count_by_distance(d, q, r)
                      for r in range(1, d+1))
    assert size == max_formula == expected_resolving_number(d, q) - 1
    assert actual == expected, (d, q, size, len(actual), len(expected))
    print(f"PASS q={q} d={d}: res={size+1}, maximal failures={len(actual)}")


if __name__ == '__main__':
    for q, high_d in ((2, 5), (3, 4), (4, 3), (5, 3)):
        for d in range(1, high_d + 1):
            check(d, q)
    print('All finite regression tests passed.')
