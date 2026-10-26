#!/usr/bin/env python3
"""Exhaustive exact arithmetic for the Hessian quartic in characteristics five.

For q=5 and q=25 the script counts normalized points in the linear
hyperplane sum(x_i)=0 satisfying e4(x)=0. It independently checks the count
using all coordinate multisets weighted by permutation-orbit sizes.
"""
from collections import Counter
from itertools import product, combinations_with_replacement
from math import factorial


def field(q):
    assert q in (5, 25)
    p = 5
    if q == 5:
        def unpack(x): return x, 0
        def pack(a, b):
            assert b % 5 == 0
            return a % 5
    else:
        def unpack(x): return x % 5, x // 5
        def pack(a, b): return a % 5 + 5 * (b % 5)
    plus = [[0] * q for _ in range(q)]
    times = [[0] * q for _ in range(q)]
    minus = [0] * q
    for a in range(q):
        aa, ab = unpack(a)
        minus[a] = pack(-aa, -ab)
        for b in range(q):
            ba, bb = unpack(b)
            plus[a][b] = pack(aa + ba, ab + bb)
            times[a][b] = pack(aa * ba + 2 * ab * bb, aa * bb + ab * ba)
    if q == 25:
        assert times[5][5] == 2  # theta^2 = 2
        assert all(times[t][t] != 2 for t in range(5))
    return plus, times, minus


def e4(xs, plus, times):
    coeff = [1, 0, 0, 0, 0]
    for x in xs:
        for k in (4, 3, 2, 1):
            coeff[k] = plus[coeff[k]][times[x][coeff[k - 1]]]
    return coeff[4]


def count_by_charts(q, plus, times, minus):
    total = 0
    each = []
    # The sum-zero hyperplane is P^3, with one coordinate eliminated.
    # The first nonzero among x0,x1,x2,x3 is scaled to 1.
    for lead in range(4):
        count = 0
        for tail in product(range(q), repeat=3 - lead):
            xs = [0] * lead + [1] + list(tail)
            summed = 0
            for x in xs:
                summed = plus[summed][x]
            xs.append(minus[summed])
            assert len(xs) == 5
            if e4(xs, plus, times) == 0:
                count += 1
        each.append(count)
        total += count
    return total, each


def count_by_permutation_orbits(q, plus, times):
    # Independent projective counting: enumerate all sorted five-tuples
    # (multisets) with sum 0, weight each by its S5 orbit, divide by q-1.
    weighted = 0
    orbit_count = 0
    for xs in combinations_with_replacement(range(q), 5):
        if not any(xs):
            continue
        summed = 0
        for x in xs:
            summed = plus[summed][x]
        if summed or e4(xs, plus, times):
            continue
        orbit_count += 1
        denom = 1
        for mult in Counter(xs).values():
            denom *= factorial(mult)
        weighted += factorial(5) // denom
    assert weighted % (q - 1) == 0
    return weighted // (q - 1), orbit_count, weighted


def main():
    want = {5: 41, 25: 901}
    for q in (5, 25):
        plus, times, minus = field(q)
        charts, by_lead = count_by_charts(q, plus, times, minus)
        orbits, num_orbits, weighted = count_by_permutation_orbits(q, plus, times)
        assert charts == orbits == want[q], (q, charts, orbits)
        print(f"F_{q}: points={charts}, charts={by_lead}, sorted_affine_orbits={num_orbits}, weighted_nonzero={weighted}")
    surface_F5 = want[5] + 11 * 5
    surface_F25 = want[25] + 11 * 25
    assert (surface_F5, surface_F25) == (96, 1176)
    tr1 = surface_F5 - 1 - 25
    tr2 = surface_F25 - 1 - 625
    assert (tr1, tr2) == (70, 550)
    pos = (22 + tr1 // 5) // 2
    neg = 22 - pos
    assert (pos, neg) == (18, 4)
    print(f"Y: F_5={surface_F5}, F_25={surface_F25}, traces={tr1},{tr2}; eigenvalues +5 x{pos}, -5 x{neg}")
    print("CHECK_OK")


if __name__ == "__main__":
    main()
