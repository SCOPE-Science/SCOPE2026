#!/usr/bin/env python3
"""Exact certificates for Nash product manipulability with three projects.
Requires Python 3.11+ and SymPy (tested with SymPy 1.14).
Every comparison is made in Q or Q(sqrt(17)); no floating point is used.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations, permutations
from math import comb
import sympy as S

B = [tuple((mask >> j) & 1 for j in range(3)) for mask in range(1, 8)]
R = S.sqrt(17)
t = (7 - R) / 16


def compositions(total, size):
    if size == 1:
        yield (total,)
    else:
        for h in range(total + 1):
            for tail in compositions(total - h, size - 1):
                yield (h,) + tail


def utility(mask, p):
    return sum(p[j] for j in range(3) if (mask >> j) & 1)


def sign(x):
    x = S.simplify(x)
    if x.is_positive: return 1
    if x.is_negative: return -1
    if x.is_zero: return 0
    raise AssertionError('No exact algebraic sign: ' + str(x))


def kkt(c, p):
    if sign(sum(p) - 1) or any(sign(z) < 0 for z in p):
        return False
    us = [utility(mask, p) for mask in range(1, 8)]
    if any(count and sign(us[j]) <= 0 for j, count in enumerate(c)):
        return False
    for j in range(3):
        gain = sum((c[h] * B[h][j] / us[h] for h in range(7)
                    if c[h] and B[h][j]), 0)
        excess = sign(gain - sum(c))
        if (sign(p[j]) > 0 and excess != 0) or excess > 0:
            return False
    return True


@lru_cache(None)
def optimizer(c):
    # Full rational grid of denominator 24; a point is ACCEPTED only if
    # KKT is independently verified with exact rational arithmetic.
    for a in range(25):
        for b in range(25-a):
            p = (F(a, 24), F(b, 24), F(24-a-b, 24))
            if kkt(c, p):
                return p
    # Exactly three four-voter count vectors need quadratic certificates.
    if sum(c) == 4:
        for pair in ((0, 1), (0, 2), (1, 2)):
            p = [0, 0, 0]
            for j in pair: p[j] = t
            p[3 - pair[0] - pair[1]] = 1 - 2*t
            if kkt(c, p):
                return tuple(p)
    raise AssertionError('No exact globally optimal certificate for ' + str(c))


@lru_cache(None)
def optimal_face_vertices(c):
    # Any optimum induces the same reported utility vector. Conversely,
    # any allocation realizing that vector is an optimum. Enumerate all
    # extreme points to bound the deviator's TRUE utility under any tie break.
    p = optimizer(c)
    eq = [(S.Matrix([[1, 1, 1]]), S.Integer(1))]
    for j, count in enumerate(c):
        if count:
            eq.append((S.Matrix([list(B[j])]), utility(j+1, p)))
    equalities = len(eq)
    for j in range(3):
        row = [0, 0, 0]; row[j] = 1
        eq.append((S.Matrix([row]), S.Integer(0)))
    found = []
    for triple in combinations(range(len(eq)), 3):
        mat = S.Matrix.vstack(*(eq[i][0] for i in triple))
        if mat.det() == 0: continue
        vec = S.Matrix([eq[i][1] for i in triple])
        q = mat.inv() * vec
        if any(sign(z) < 0 for z in q): continue
        if any(sign((eq[i][0] * q)[0] - eq[i][1]) != 0
               for i in range(equalities)): continue
        values = tuple(q)
        if values not in found: found.append(values)
    assert found, ('Empty optimal face', c)
    return tuple(found)


def relabel(c, perm):
    output = [0] * 7
    for mask, count in enumerate(c, start=1):
        target = sum(((mask >> j) & 1) << perm[j] for j in range(3))
        output[target-1] = count
    return tuple(output)


def run():
    all_bad = set()
    ratios = set()
    for n in range(1, 5):
        bad = {}
        for c in compositions(n, 7):
            p = optimizer(c)
            for a, count in enumerate(c):
                if not count: continue
                old = utility(a+1, p)
                for b in range(7):
                    if a == b: continue
                    change = list(c)
                    change[a] -= 1; change[b] += 1
                    choices = optimal_face_vertices(tuple(change))
                    new = [utility(a+1, q) for q in choices]
                    if any(sign(v-old) > 0 for v in new):
                        # Profitable for EVERY selection from the Nash face.
                        assert all(sign(v-old) > 0 for v in new)
                        assert all(sign(v-new[0]) == 0 for v in new)
                        bad.setdefault(c, []).append((a+1, b+1))
                        ratios.add(S.simplify(new[0] / old))
        if n <= 3:
            assert not bad
        else:
            assert len(bad) == 6
            assert sum(map(len, bad.values())) == 12
            expected = set()
            for representative in (
                (0, 1, 1, 1, 1, 0, 0),  # B,AB,C,AC
                (0, 0, 1, 1, 1, 1, 0),  # AB,C,AC,BC
            ):
                expected.update(relabel(representative, p)
                                for p in permutations(range(3)))
            assert set(bad) == expected
            all_bad = set(bad)
        print('voters:', n, 'anonymous profiles:', comb(n+6, 6),
              'manipulable profiles:', len(bad),
              'profitable (ballot,report) pairs:', sum(map(len, bad.values())))
    assert len(all_bad) == 6
    assert ratios == {S.Rational(5, 4), (9-S.sqrt(17))/4}
    assert optimizer.cache_info().currsize == sum(comb(n+6, 6) for n in range(1, 5))
    print('Exact possible manipulation ratios:', sorted(map(str, ratios)))
    print('All KKT, face-vertex and deviation checks passed.')

if __name__ == '__main__':
    run()
