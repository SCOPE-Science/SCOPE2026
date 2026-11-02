#!/usr/bin/env python3
"""Independent finite checks for the circle-square consensus controllability theorem.

Only Python's standard library is needed. Numerical checks are diagnostic;
the general theorem rests on the written cyclotomic/PBH proof.
"""
from math import cos, pi

PRIME = 1_000_003
assertions = 0


def expected(n):
    if n % 5 == 0 or n % 12 == 0:
        return 4
    if n % 6 == 0:
        return 3
    return 2


def adj(n):
    return [[int((j-i) % n in (1, 2, n-1, n-2)) for j in range(n)]
            for i in range(n)]


def rank_mod(matrix, p=PRIME):
    a = [list(map(lambda x: x % p, row)) for row in matrix]
    rows = len(a)
    cols = len(a[0]) if a else 0
    rank = 0
    for j in range(cols):
        pivot = next((i for i in range(rank, rows) if a[i][j]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][j], -1, p)
        a[rank][j:] = [(x*inv) % p for x in a[rank][j:]]
        for i in range(rank+1, rows):
            if a[i][j]:
                q = a[i][j]
                a[i][j:] = [(x-q*y) % p for x, y in zip(a[i][j:],a[rank][j:])]
        rank += 1
        if rank == rows:
            break
    return rank


def controllability(n, locations):
    a = adj(n)
    powers = [[int(i == loc) for loc in locations] for i in range(n)]
    mat = [row[:] for row in powers]
    q = len(locations)
    for step in range(1, n):
        powers = [[sum(a[i][j]*powers[j][k] for j in range(n)) % PRIME
                   for k in range(q)] for i in range(n)]
        for i in range(n):
            mat[i].extend(powers[i])
    return rank_mod(mat)


for n in range(5, 251):
    # Group independently evaluated trigonometric adjacency eigenvalues.
    vals = sorted(2*cos(2*pi*k/n)+2*cos(4*pi*k/n) for k in range(n))
    groups = []
    for v in vals:
        if groups and abs(groups[-1][-1]-v) < 2e-9:
            groups[-1].append(v)
        else:
            groups.append([v])
    assert max(map(len, groups)) == expected(n), (n, [len(z) for z in groups])
    assertions += 1
    assert sum(map(len,groups)) == n
    assertions += 1

for n in range(5, 35):
    q = expected(n)
    assert controllability(n, list(range(q))) == n, n
    assertions += 1
    if q > 1:
        assert controllability(n, list(range(q-1))) < n, n
        assertions += 1

# Exact algebraic certificate: the only exceptional Fourier orders are
# (2,6), (3,4), and the two distinct order-5 conjugate pairs.
for n in range(5, 181):
    c = [cos(2*pi*k/n) for k in range(n)]
    collisions = [(i,j) for i in range(n) for j in range(i+1,n)
                  if abs(c[i]+c[j]+0.5) < 3e-10]
    for i,j in collisions:
        from math import gcd
        r,s = n//gcd(n,i), n//gcd(n,j)
        assert tuple(sorted((r,s))) in ((2,6),(3,4),(5,5)), (n,i,j,r,s)
        assertions += 1

print(f"PASS: {assertions} checks; Fourier dimensions 5..250, modular Kalman dimensions 5..34, and collision orders 5..180")
