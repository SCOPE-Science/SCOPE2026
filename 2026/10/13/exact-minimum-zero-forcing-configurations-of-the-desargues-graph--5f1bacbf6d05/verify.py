#!/usr/bin/env python3
"""Exact zero-forcing census and symmetry certificate for the Desargues graph.

Run: python3 verify.py
Only the Python standard library is required.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations
from pathlib import Path
import csv

GROUND = tuple(range(5))
VERTICES = [tuple(s) for k in (2, 3) for s in combinations(GROUND, k)]
INDEX = {x: i for i, x in enumerate(VERTICES)}
N = len(VERTICES)
FULL = (1 << N) - 1


def adjacency():
    rows = [0] * N
    for i, a in enumerate(VERTICES):
        for j, b in enumerate(VERTICES):
            if abs(len(a) - len(b)) == 1 and (set(a) <= set(b) or set(b) <= set(a)):
                rows[i] |= 1 << j
    return rows

ADJ = adjacency()


def simultaneous_closure(mask):
    """Set-valued synchronous application of all possible color changes."""
    while True:
        new = 0
        for v in range(N):
            if mask & (1 << v):
                white = ADJ[v] & (FULL ^ mask)
                if white and (white & (white - 1)) == 0:
                    new |= white
        grown = mask | new
        if grown == mask:
            return mask
        mask = grown


def sequential_closure(mask):
    """Independent sequential routine, restarting after each legal force."""
    while True:
        changed = False
        for v in range(N):
            if mask & (1 << v):
                white = ADJ[v] & (FULL ^ mask)
                if white and white.bit_count() == 1:
                    mask |= white
                    changed = True
                    break
        if not changed:
            return mask


def rank_integer(matrix):
    a = [[Fraction(t) for t in row] for row in matrix]
    m = len(a)
    n = len(a[0])
    pivot_row = 0
    for j in range(n):
        k = next((i for i in range(pivot_row, m) if a[i][j]), None)
        if k is None:
            continue
        a[pivot_row], a[k] = a[k], a[pivot_row]
        t = a[pivot_row][j]
        for h in range(j, n):
            a[pivot_row][h] /= t
        for i in range(m):
            if i != pivot_row and a[i][j]:
                t = a[i][j]
                for h in range(j, n):
                    a[i][h] -= t * a[pivot_row][h]
        pivot_row += 1
    return pivot_row


def oriented_boundary_matrix():
    edges = VERTICES[:10]
    triangles = VERTICES[10:]
    matrix = [[0] * 10 for _ in range(10)]
    for j, t in enumerate(triangles):
        for h in range(3):
            edge = tuple(t[r] for r in range(3) if r != h)
            matrix[INDEX[edge]][j] = (-1) ** h
    return matrix


def automorphisms():
    group = []
    for p in permutations(GROUND):
        for dual in (False, True):
            trans = []
            for x in VERTICES:
                image = tuple(sorted(p[i] for i in x))
                if dual:
                    image = tuple(i for i in GROUND if i not in image)
                trans.append(INDEX[image])
            assert all(((ADJ[i] >> j) & 1) == ((ADJ[trans[i]] >> trans[j]) & 1)
                       for i in range(N) for j in range(N))
            group.append(tuple(trans))
    assert len(group) == len(set(group)) == 240
    return group


def relabel(mask, permutation):
    y = 0
    while mask:
        low = mask & -mask
        y |= 1 << permutation[low.bit_length() - 1]
        mask ^= low
    return y


def main():
    assert N == 20 and sum(x.bit_count() for x in ADJ) == 60
    assert all(x.bit_count() == 3 for x in ADJ)
    assert all(((ADJ[i] >> j) & 1) == ((ADJ[j] >> i) & 1)
               for i in range(N) for j in range(N))
    B = oriented_boundary_matrix()
    assert sum(sum(abs(x) for x in row) for row in B) == 30
    assert all(sum(x != 0 for x in row) == 3 for row in B)
    assert all(sum(B[i][j] != 0 for i in range(10)) == 3 for j in range(10))
    assert rank_integer(B) == 6
    for i in range(10):
        for j in range(10):
            assert (B[i][j] != 0) == bool(ADJ[i] & (1 << (j + 10)))
    # Check d1*d2=0, one boundary identity used in the analytical proof.
    d1 = [[(-1 if x[0] == i else 1 if x[1] == i else 0)
           for x in VERTICES[:10]] for i in GROUND]
    assert rank_integer(d1) == 4
    assert all(sum(d1[i][e] * B[e][t] for e in range(10)) == 0
               for i in GROUND for t in range(10))
    good = set()
    # Every 8-set is necessarily balanced by the exact rank argument.
    for a in combinations(range(10), 4):
        mask_a = sum(1 << i for i in a)
        for b in combinations(range(10, 20), 4):
            mask = mask_a | sum(1 << i for i in b)
            first = simultaneous_closure(mask) == FULL
            second = sequential_closure(mask) == FULL
            assert first == second
            if first:
                good.add(mask)
    assert len(good) == 13520
    # The orbit census is independent of the zero-forcing enumeration loop.
    group = automorphisms()
    remaining = set(good)
    orbits = []
    while remaining:
        representative = min(remaining)
        orbit = {relabel(representative, p) for p in group}
        assert orbit <= remaining
        remaining.difference_update(orbit)
        orbits.append((representative, len(orbit)))
    assert not remaining and len(orbits) == 67
    assert Counter(size for _, size in orbits) == {20: 1, 60: 1, 120: 18, 240: 47}
    assert sum(size for _, size in orbits) == 13520
    # The optional CSV is a compact independent orbit-reconstruction certificate.
    here = Path(__file__).resolve().parent
    with (here / "orbit_representatives.csv").open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    assert len(rows) == 67
    expected = [(int(r["mask_decimal"]), int(r["orbit_size"])) for r in rows]
    assert expected == orbits
    print("VERIFY_OK vertices=20 edges=30 signed_boundary_rank=6 side_kernel_dims=4+4")
    print("VERIFY_OK balanced_candidates=44100 forcing_8_sets=13520 sequential_parallel_agree=yes")
    print("VERIFY_OK automorphisms=240 orbits=67 sizes=20x1+60x1+120x18+240x47")


if __name__ == "__main__":
    main()
