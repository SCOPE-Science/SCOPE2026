#!/usr/bin/env python3
"""Independent exact finite checks of Walsh-shell ranks and observable subspaces.

Standard library only. Finite tests corroborate, but do not substitute for,
the all-dimension incidence/harmonic proof.
"""
from itertools import combinations
from math import comb

PRIME = 1_000_003


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def krawtchouk(N, d, z):
    return sum((-1)**j * choose(z, j) * choose(N-z, d-j)
               for j in range(d+1))


def harmonic_rank(n, r, w):
    t = min(r, n-r, w, n-w)
    return sum((choose(n, i)-choose(n, i-1))
               for i in range(t+1)
               if krawtchouk(n-2*i, w-i, r-i) != 0)


def gf_rank(matrix):
    if not matrix:
        return 0
    rows = [list(map(lambda v: v % PRIME, row)) for row in matrix]
    height, width = len(rows), len(rows[0])
    pivot = 0
    for col in range(width):
        choice = next((j for j in range(pivot, height) if rows[j][col]), None)
        if choice is None:
            continue
        rows[pivot], rows[choice] = rows[choice], rows[pivot]
        inv = pow(rows[pivot][col], -1, PRIME)
        rows[pivot][col:] = [v * inv % PRIME for v in rows[pivot][col:]]
        for j in range(pivot+1, height):
            v = rows[j][col]
            if v:
                rows[j][col:] = [(a-v*b) % PRIME
                                 for a,b in zip(rows[j][col:], rows[pivot][col:])]
        pivot += 1
        if pivot == height:
            break
    return pivot


def levels(n):
    return [[sum(1 << j for j in indices)
             for indices in combinations(range(n), k)]
            for k in range(n+1)]


def direct_spectral_rank(shell, frequency):
    return gf_rank([[1 if (s & v).bit_count() % 2 == 0 else -1
                     for v in frequency] for s in shell])


def observability_rank(n, trap_vertices):
    """Rank of [P_T; P_T A; ...; P_T A^n] over a prime field."""
    dim = 1 << n
    rows = []
    for source in trap_vertices:
        row = [0] * dim
        row[source] = 1
        for k in range(n+1):
            rows.append(row)
            row = [sum(row[v ^ (1 << j)] for j in range(n)) % PRIME
                   for v in range(dim)]
    return gf_rank(rows)


def tests():
    c = {"spectral": 0, "krylov": 0, "parity": 0, "two_shell": 0}
    for n in range(1, 9):
        shells = levels(n)
        for r in range(n+1):
            for w in range(n+1):
                expected = harmonic_rank(n, r, w)
                actual = direct_spectral_rank(shells[r], shells[w])
                assert actual == expected, (n,r,w,expected,actual)
                c["spectral"] += 1
        center = n // 2
        if n % 2:
            assert sum(harmonic_rank(n, center, w) for w in range(n+1)) == 2**n
        else:
            m = center
            central = sum(harmonic_rank(n,m,w) for w in range(n+1))
            lower = sum(harmonic_rank(n,m-1,w) for w in range(n+1))
            assert central == 2**(n-1) + comb(n,m)//2
            assert lower == 2**n - comb(n,m)//2
            for w in range(n+1):
                if w != m:
                    assert harmonic_rank(n,m-1,w) == comb(n,w)
                combined = direct_spectral_rank(shells[m-1]+shells[m],shells[w])
                assert combined == comb(n,w), (n,w,combined)
                c["two_shell"] += 1
        c["parity"] += 1
    # Independently assess absorption with block observability on the *site* basis,
    # without using the Walsh transform or harmonic formula in the construction.
    for n in range(1, 7):
        shells = levels(n)
        for r in range(n+1):
            predicted = sum(harmonic_rank(n,r,w) for w in range(n+1))
            actual = observability_rank(n,shells[r])
            assert actual == predicted, (n,r,predicted,actual)
            c["krylov"] += 1
        if n % 2 == 0:
            m=n//2
            actual = observability_rank(n,shells[m-1]+shells[m])
            assert actual == 2**n, (n,actual)
            c["krylov"] += 1
    return c


if __name__ == "__main__":
    counts = tests()
    print("VERIFY_OK " + " ".join(f"{key}={counts[key]}" for key in sorted(counts)))
