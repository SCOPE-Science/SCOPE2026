#!/usr/bin/env python3
"""Reproduce the hexad-avoiding Witt complex and its Mathieu homology character.

Python 3 standard library only. All checks are exact, with full group enumeration.
"""
from collections import Counter, defaultdict
from itertools import combinations
from math import comb

POINTS = tuple(range(12))  # 11 denotes infinity, other labels are F_11.
BASE = frozenset((11, 1, 3, 4, 5, 9))
T = tuple(((x + 1) % 11 if x < 11 else 11) for x in POINTS)
S = tuple(((-pow(x, -1, 11)) % 11 if 0 < x < 11 else (11 if x == 0 else 0)) for x in POINTS)
E = (0, 1, 2, 3, 5, 9, 10, 8, 6, 11, 7, 4)
IDENTITY = tuple(POINTS)


def orbit_of_blocks():
    result = [BASE]
    seen = {BASE}
    for b in result:
        for h in (T, S):
            c = frozenset(h[i] for i in b)
            if c not in seen:
                seen.add(c)
                result.append(c)
    return result


def generated_group(generators):
    group = [IDENTITY]
    seen = {IDENTITY}
    for g in group:
        for h in generators:
            product = tuple(h[g[i]] for i in POINTS)
            if product not in seen:
                seen.add(product)
                group.append(product)
    return group


def cycle_lengths(g):
    visited = set()
    lengths = []
    for i in POINTS:
        if i not in visited:
            j = i
            length = 0
            while j not in visited:
                visited.add(j)
                length += 1
                j = g[j]
            lengths.append(length)
    return tuple(sorted(lengths))


def parity(values):
    return -1 if sum(values[i] > values[j]
                     for i in range(len(values))
                     for j in range(i + 1, len(values))) % 2 else 1


def wedge_six_trace(lengths):
    # det(I+t*g | Q^12) = product_(cycles) (1 - (-t)^length).
    coefficient = [1] + [0] * 6
    for length in lengths:
        for i in range(6, length - 1, -1):
            coefficient[i] -= (-1) ** length * coefficient[i - length]
    # Remove the trivial summand from the 12-dimensional permutation space.
    previous = 0
    for i in range(7):
        previous = coefficient[i] - previous  # divide by (1+t)
    return previous


def hexad_trace(g, hexads):
    return sum(parity(tuple(g[i] for i in b))
               for b in hexads if frozenset(g[i] for i in b) == frozenset(b))


def direct_euler_character(g, hexad_masks):
    # Independent simplicial Lefschetz calculation, not using the exterior-power sequence.
    alternating = -1  # minus the reduced degree (-1)-chain contribution
    for k in range(1, 7):
        for face in combinations(POINTS, k):
            if k == 6 and sum(1 << x for x in face) in hexad_masks:
                continue
            transformed = tuple(g[i] for i in face)
            if set(transformed) == set(face):
                alternating += (-1) ** (k - 1) * parity(transformed)
    return -alternating  # homology concentrated in odd degree five


def run():
    hexads = [tuple(sorted(b)) for b in orbit_of_blocks()]
    hs = {frozenset(h) for h in hexads}
    masks = {sum(1 << x for x in h) for h in hs}
    assert len(hs) == 132
    assert all(frozenset(set(POINTS) - set(h)) in hs for h in hs)
    assert all({E[i] for i in h} in hs for h in hexads)
    incidence = Counter(frozenset(f) for h in hs for f in combinations(h, 5))
    assert len(incidence) == comb(12, 5) and set(incidence.values()) == {1}
    assert all(len(set(a) & set(b)) <= 4 for a, b in combinations(hexads, 2))
    assert all(sum(set(h) <= set(y) for h in hexads) == 1
               for y in combinations(POINTS, 7))
    facets = comb(12, 6) - len(hs)
    f = tuple(comb(12, k) if k < 6 else facets for k in range(1, 7))
    assert f == (12, 66, 220, 495, 792, 792)
    betti = -(sum((-1) ** (k - 1) * count for k, count in enumerate(f, 1)) - 1)
    assert betti == 330

    group = generated_group((T, S, E))
    assert len(group) == 95040
    expected = {
        (1,) * 12: (1, 462, 132, 330),
        (1, 1, 1, 1, 2, 2, 2, 2): (495, 14, 4, 10),
        (2, 2, 2, 2, 2, 2): (396, -10, 0, -10),
        (1, 1, 1, 3, 3, 3): (1760, 3, 6, -3),
        (3, 3, 3, 3): (2640, 3, 0, 3),
        (1, 1, 1, 1, 4, 4): (2970, -6, -4, -2),
        (2, 2, 4, 4): (2970, 2, 4, -2),
        (1, 1, 5, 5): (9504, 2, 2, 0),
        (1, 2, 3, 6): (15840, -1, -2, 1),
        (6, 6): (7920, -1, 0, -1),
        (1, 1, 2, 8): (11880, 0, 0, 0),
        (4, 8): (11880, 0, 0, 0),
        (2, 10): (9504, 0, 0, 0),
        (1, 11): (17280, 0, 0, 0),
    }
    observed = Counter()
    representatives = {}
    sumchi = sumchi2 = 0
    for g in group:
        ct = cycle_lengths(g)
        a = wedge_six_trace(ct)
        b = hexad_trace(g, hexads)
        chi = a - b
        observed[(ct, a, b, chi)] += 1
        representatives.setdefault(ct, g)
        sumchi += chi
        sumchi2 += chi * chi
    assert len(observed) == len(expected) == 14
    assert {ct: (count, a, b, c) for (ct, a, b, c), count in observed.items()} == expected
    assert sumchi == 0 and sumchi2 == 3 * len(group)

    # Three rows of the published ordinary character table, in the class order below.
    order = ((1,) * 12, (1, 1, 1, 1, 2, 2, 2, 2), (2,) * 6,
             (1, 1, 1, 3, 3, 3), (3,) * 4, (1, 1, 1, 1, 4, 4),
             (2, 2, 4, 4), (1, 1, 5, 5), (1, 2, 3, 6), (6, 6),
             (1, 1, 2, 8), (4, 8), (2, 10), (1, 11))
    chi55 = (55, 7, -5, 1, 1, -1, -1, 0, 1, 1, -1, -1, 0, 0)
    chi99 = (99, 3, -1, 0, 3, -1, -1, -1, 0, -1, 1, 1, -1, 0)
    chi176 = (176, 0, -4, -4, -1, 0, 0, 1, 0, -1, 0, 0, 1, 0)
    assert all(expected[ct][3] == chi55[i] + chi99[i] + chi176[i]
               for i, ct in enumerate(order))
    assert all(direct_euler_character(representatives[ct], masks) == expected[ct][3]
               for ct in order)
    print('WITT_HEXADS', len(hexads), 'FACES', f, 'TOP_BETTI', betti)
    print('DESIGN_FIVE_SUBSETS', len(incidence), 'SEVEN_SUBSETS', comb(12, 7))
    print('MATHIEU_GROUP_ORDER', len(group))
    print('CHARACTER_CLASS_TYPES', len(expected), 'SUM', sumchi,
          'INNER_SQUARE', sumchi2 // len(group))
    print('REPRESENTATION_DEGREES', chi55[0], chi99[0], chi176[0])
    print('DIRECT_SIMPLICIAL_LEFSCHETZ_CHECKS', len(order))
    print('VERIFY_OK')


if __name__ == '__main__':
    run()
