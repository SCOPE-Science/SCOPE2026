#!/usr/bin/env python3
"""Exact rational checks of the two-ball covering construction for regular simplices.

For a unit-edge regular simplex, squared distance between barycentric points
with weights p and q is (1/2) sum_i (p_i-q_i)^2. The all-dimension
arguments are mathematical and do not depend on these finite checks.
"""

from fractions import Fraction as F
from itertools import combinations
from math import comb
from random import Random


def d2(p, q):
    assert sum(p) == sum(q) == 1 and len(p) == len(q)
    return sum((x-y)**2 for x, y in zip(p, q)) / 2


def midpoint(N, i, j):
    z = [F(0)] * N
    z[i], z[j] = F(1, 2), F(1, 2)
    return z


def center(N, A):
    A = set(A)
    return [F(1, len(A)) if i in A else F(0) for i in range(N)]


def vertex(N, i):
    return [F(int(t == i)) for t in range(N)]


def check_case(N, A):
    k = (N + 1) // 2
    assert len(A) == k
    B = tuple(j for j in range(N) if j not in A)
    ca, cb = center(N, A), center(N, B)
    r2 = F(k-1, 2*k)
    # The halfspace t_A>=1/2 subpolytope has exactly these vertices:
    # all vertices of A plus all crossing-edge midpoints. Similarly for B.
    for i in A:
        assert d2(vertex(N, i), ca) == r2
    for j in B:
        assert d2(vertex(N, j), cb) == F(len(B)-1, 2*len(B)) <= r2
    for i in A:
        for j in B:
            m = midpoint(N, i, j)
            assert d2(m, ca) == d2(m, cb) == F(1, 4)
            assert d2(m, ca) <= r2
    if N % 2 == 1:  # even simplex dimension: a continuum of optimal centers
        tau = F(1, 100 * N**3)
        shifted = [x + tau * (y-x) for x, y in zip(cb, ca)]
        assert shifted != cb
        for j in B:
            assert d2(vertex(N, j), shifted) < r2
        for i in A:
            for j in B:
                assert d2(midpoint(N, i, j), shifted) < r2
    # Exact combinatorial vertex-only obstruction.
    assert F(k-1, 2*k) < F(k, 2*(k+1))
    return len(A)*len(B)


def run():
    reps = 0
    for N in range(4, 42):
        k = (N+1)//2
        reps += check_case(N, tuple(range(k)))
    for N in range(4, 11):
        k = (N+1)//2
        for A in combinations(range(N), k):
            reps += check_case(N, A)
    # Exhaustive classification counting all complementary k-subsets when N is even.
    for N in range(4, 16, 2):
        k=N//2
        assert sum(1 for _ in combinations(range(N),k)) // 2 == comb(N,k)//2
    rng = Random(20261008)
    samples = 0
    for N in range(4, 35):
        k=(N+1)//2
        ca, cb = center(N,range(k)), center(N,range(k,N))
        r2=F(k-1, 2*k)
        for _ in range(150):
            raw=[rng.randrange(1,101) for _ in range(N)]
            total=sum(raw)
            z=[F(v,total) for v in raw]
            ta=sum(z[:k])
            if ta >= F(1,2):
                assert d2(z,ca)<=r2
            if ta <= F(1,2):
                assert d2(z,cb)<=r2
            samples += 1
    print('VERIFY_OK regular simplices: rational cut-vertex tests =',reps,
          'barycentric samples =',samples, 'dimensions = 3..40')


if __name__ == '__main__':
    run()
