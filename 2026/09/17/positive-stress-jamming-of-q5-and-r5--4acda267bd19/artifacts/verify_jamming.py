#!/usr/bin/env python3
"""Exact verifier for infinitesimal jamming of Q5 and R5.

Uses only Python's standard library.  Coordinates are kept in Fraction arithmetic;
the rigidity rank is certified modulo a prime.  A rank of 190 modulo p proves
rank at least 190 over Q, while the 10-dimensional rotation space gives rank at
most 200-10=190.
"""
from fractions import Fraction as F
from itertools import combinations, product

P = 1_000_003


def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d*d <= n:
        if n % d == 0:
            return n == d
        d += 1 if d == 2 else 2
    return True


assert is_prime(P)


def dot(x, y):
    return sum(a*b for a, b in zip(x, y))


def d5():
    pts = set()
    for i, j in combinations(range(5), 2):
        for a, b in product((-1, 1), repeat=2):
            v = [F(0)] * 5
            v[i], v[j] = F(a), F(b)
            pts.add(tuple(v))
    return sorted(pts)


def reflect_sum_zero(v):
    s = sum(v)
    return tuple(a - F(2*s, 5) for a in v)


def q5():
    D = d5()
    zero = [v for v in D if sum(v) == 0]
    minus = [v for v in D if sum(v) == -2]
    return sorted(set(zero + minus + [reflect_sum_zero(v) for v in minus]))


def l5():
    D = [v for v in d5() if v[4] != 1]
    for signs in product((-1, 1), repeat=4):
        if sum(s < 0 for s in signs) % 2 == 1:
            D.append(tuple(F(s, 2) for s in signs) + (F(1),))
    return sorted(set(D))


def r5():
    L = l5()
    zero = [v for v in L if sum(v) == 0]
    minus = [v for v in L if sum(v) == -2]
    return sorted(set(zero + minus + [reflect_sum_zero(v) for v in minus]))


def swap(a, b):
    def g(v):
        w = list(v)
        w[a], w[b] = w[b], w[a]
        return tuple(w)
    return g


def edge_orbit(seed, generators, point_index):
    seen = set()
    todo = [seed]
    while todo:
        e = todo.pop()
        if e in seen:
            continue
        seen.add(e)
        for g in generators:
            a = point_index[g(e[0])]
            b = point_index[g(e[1])]
            # return coordinate pair in canonical point order
            x, y = sorted((a, b))
            ep = (POINTS[x], POINTS[y])
            if ep not in seen:
                todo.append(ep)
    return seen


def frac_mod(x):
    return (x.numerator % P) * pow(x.denominator % P, P-2, P) % P


def rank_mod_p(rows, ncols):
    A = [[frac_mod(x) for x in row] for row in rows]
    r = 0
    for c in range(ncols):
        pivot = next((i for i in range(r, len(A)) if A[i][c]), None)
        if pivot is None:
            continue
        A[r], A[pivot] = A[pivot], A[r]
        inv = pow(A[r][c], P-2, P)
        A[r] = [(z*inv) % P for z in A[r]]
        for i in range(len(A)):
            if i != r and A[i][c]:
                q = A[i][c]
                A[i] = [(u - q*v) % P for u, v in zip(A[i], A[r])]
        r += 1
        if r == len(A):
            break
    return r


def rigidity_rows(points, contacts):
    N = len(points)
    rows = []
    for i, x in enumerate(points):
        row = [F(0)] * (5*N)
        for a in range(5):
            row[5*i+a] = x[a]
        rows.append(row)
    for i, j in contacts:
        row = [F(0)] * (5*N)
        for a in range(5):
            row[5*i+a] = points[j][a]
            row[5*j+a] = points[i][a]
        rows.append(row)
    return rows


def verify(name, points, generators, stress_seeds):
    global POINTS
    POINTS = points
    assert len(points) == 40
    assert all(dot(x, x) == 2 for x in points)
    contacts = [(i, j) for i, j in combinations(range(40), 2)
                if dot(points[i], points[j]) == 1]
    assert len(contacts) == 240
    assert max(dot(points[i], points[j]) for i, j in combinations(range(40), 2)) == 1

    pindex = {x: i for i, x in enumerate(points)}
    weights = {}
    orbit_sizes = []
    for x, y, w, expected_size in stress_seeds:
        assert x in pindex and y in pindex and dot(x, y) == 1 and w > 0
        orbit = edge_orbit((x, y), generators, pindex)
        assert len(orbit) == expected_size
        orbit_sizes.append(len(orbit))
        for a, b in orbit:
            e = tuple(sorted((pindex[a], pindex[b])))
            if e in weights:
                assert weights[e] == w
            weights[e] = F(w)
    assert set(weights) == set(contacts)
    assert min(weights.values()) > 0

    # Exact equilibrium: sum_{j~i} w_ij x_j = 30 x_i for every i.
    for i, x in enumerate(points):
        s = [F(0)] * 5
        for j in range(40):
            e = tuple(sorted((i, j)))
            if e not in weights:
                continue
            w = weights[e]
            for a in range(5):
                s[a] += w * points[j][a]
        assert tuple(s) == tuple(30*a for a in x)

    span_rank = rank_mod_p([list(x) for x in points], 5)
    assert span_rank == 5

    rows = rigidity_rows(points, contacts)
    rank = rank_mod_p(rows, 200)
    assert rank == 190
    print(f"{name}: points=40 contacts=240 span_rank={span_rank} "
          f"stress=min{min(weights.values())} equilibrium=30*x "
          f"rank_mod_{P}={rank} nullity=10")


Q_GENS = [swap(0,1), swap(1,2), swap(2,3), swap(3,4), reflect_sum_zero]
R_GENS = [swap(0,1), swap(1,2), swap(2,3), reflect_sum_zero]

Q_STRESS = [
    ((F(-1),F(-1),0,0,0), (F(-1),0,F(-1),0,0), 5, 60),
    ((F(-1),F(-1),0,0,0), (F(-1),0,0,0,F(1)), 5, 120),
    ((F(-1),0,0,0,F(1)), (F(-1),0,0,F(1),0), 4, 30),
    ((F(-1),0,0,0,F(1)), (0,F(-1),0,0,F(1)), 6, 30),
]

R_STRESS = [
    ((F(-1),F(-1),0,0,0), (F(-1),0,F(-1),0,0), 5, 24),
    ((F(-1),F(-1),0,0,0), (F(-1),0,0,0,F(-1)), 5, 24),
    ((F(-1),F(-1),0,0,0), (F(-1),0,0,F(1),0), 5, 48),
    ((F(-1),F(-1),0,0,0), (F(-1,2),F(-1,2),F(-1,2),F(1,2),F(1)), 5, 24),
    ((F(-1),0,0,0,F(-1)), (F(-1),0,0,F(1),0), 5, 24),
    ((F(-1),0,0,0,F(-1)), (0,F(-1),0,0,F(-1)), 5, 12),
    ((F(-1),0,0,0,F(-1)), (0,0,0,F(1),F(-1)), 5, 24),
    ((F(-1),0,0,F(1),0), (F(-1),0,F(1),0,0), 5, 12),
    ((F(-1),0,0,F(1),0), (F(-1,2),F(-1,2),F(-1,2),F(1,2),F(1)), 4, 12),
    ((F(-1),0,0,F(1),0), (0,F(-1),0,F(1),0), 5, 12),
    ((F(-1),0,0,F(1),0), (0,0,0,F(1),F(-1)), 6, 12),
    ((F(-1,2),F(-1,2),F(-1,2),F(1,2),F(1)), (F(-1,2),F(-1,2),F(1,2),F(-1,2),F(1)), 6, 6),
    ((0,0,0,F(1),F(-1)), (0,0,F(1),0,F(-1)), 4, 6),
]

if __name__ == '__main__':
    verify('Q5', q5(), Q_GENS, Q_STRESS)
    verify('R5', r5(), R_GENS, R_STRESS)
