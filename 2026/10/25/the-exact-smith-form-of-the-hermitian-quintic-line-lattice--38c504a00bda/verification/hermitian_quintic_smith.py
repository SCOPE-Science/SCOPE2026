#!/usr/bin/env python3
"""Exact finite verification for the line-intersection Gram matrix on H(3,16).

Only the Python standard library is required.  GF(16) is represented as
F_2[a]/(a^4+a+1), and the Hermitian involution is x |-> x^4.
The script enumerates all projective points, the isotropic points, and the
maximal totally isotropic 2-spaces, then computes the line Gram matrix modulo
2, modulo 3, and modulo 4.  The algebraic rank bound and p-primary support are
supplied by the cited literature in RESULT.md; this script does not replace
those infinite/general theorems.
"""
from itertools import product

# GF(16) polynomial-basis arithmetic; bit i is the coefficient of a^i.
def mul_raw(x, y):
    z = 0
    while y:
        if y & 1:
            z ^= x
        y >>= 1
        x <<= 1
        if x & 0b10000:
            x ^= 0b10011  # a^4+a+1
    return z

MUL = [[mul_raw(x, y) for y in range(16)] for x in range(16)]
POW = [[1] * 15 for _ in range(16)]
for x in range(16):
    for e in range(1, 15):
        POW[x][e] = MUL[x][POW[x][e - 1]]
INV = [0] + [POW[x][14] for x in range(1, 16)]
CONJ = [POW[x][4] for x in range(16)]


def norm_projective(v):
    for x in v:
        if x:
            s = INV[x]
            return tuple(MUL[s][y] for y in v)
    return tuple(v)


def hermitian(v, w):
    out = 0
    for x, y in zip(v, w):
        out ^= MUL[x][CONJ[y]]
    return out


def rank_mod_p(A, p):
    M = [[x % p for x in row] for row in A]
    nr, nc = len(M), len(M[0])
    r = 0
    for c in range(nc):
        pivot = next((i for i in range(r, nr) if M[i][c] != 0), None)
        if pivot is None:
            continue
        M[r], M[pivot] = M[pivot], M[r]
        invp = pow(M[r][c], -1, p)
        M[r] = [(x * invp) % p for x in M[r]]
        for i in range(r + 1, nr):
            a = M[i][c]
            if a:
                M[i] = [(M[i][j] - a * M[r][j]) % p for j in range(nc)]
        r += 1
        if r == nr:
            break
    return r


def rank_mod2(A):
    M = [[x & 1 for x in row] for row in A]
    nr, nc = len(M), len(M[0])
    r = 0
    for c in range(nc):
        pivot = next((i for i in range(r, nr) if M[i][c]), None)
        if pivot is None:
            continue
        M[r], M[pivot] = M[pivot], M[r]
        for i in range(r + 1, nr):
            if M[i][c]:
                M[i] = [x ^ y for x, y in zip(M[i], M[r])]
        r += 1
        if r == nr:
            break
    return r


def local_smith_mod4(A):
    """Return counts (e=0, e=1, e>=2) from elimination over Z/4Z.

    Odd pivots are units and are eliminated by invertible row/column
    operations. The remaining block is even; its half reduced mod 2 counts
    the elementary divisors with valuation exactly one. Valuation >=2 entries
    vanish mod 4 and are counted by the independently known rational rank.
    """
    M = [[x % 4 for x in row] for row in A]
    n = len(M)
    k = 0
    while k < n:
        pos = None
        for i in range(k, n):
            for j in range(k, n):
                if M[i][j] & 1:
                    pos = (i, j)
                    break
            if pos is not None:
                break
        if pos is None:
            break
        i, j = pos
        M[k], M[i] = M[i], M[k]
        for row in M:
            row[k], row[j] = row[j], row[k]
        if M[k][k] == 3:
            M[k] = [(3 * x) % 4 for x in M[k]]
        assert M[k][k] == 1
        for i2 in range(k + 1, n):
            a = M[i2][k]
            if a:
                M[i2] = [(M[i2][j2] - a * M[k][j2]) % 4 for j2 in range(n)]
        for j2 in range(k + 1, n):
            a = M[k][j2]
            if a:
                for i2 in range(n):
                    M[i2][j2] = (M[i2][j2] - a * M[i2][k]) % 4
        k += 1
    residual = [row[k:] for row in M[k:]]
    assert all(x % 2 == 0 for row in residual for x in row)
    half_mod2 = [[(x // 2) % 2 for x in row] for row in residual]
    e1 = rank_mod2(half_mod2) if residual else 0
    return k, e1


def main():
    # Enumerate normalized projective points: first nonzero coordinate is 1.
    points = []
    for i in range(4):
        for tail in product(range(16), repeat=3 - i):
            points.append((0,) * i + (1,) + tail)
    assert len(points) == 4369
    isotropic = [v for v in points if hermitian(v, v) == 0]
    assert len(isotropic) == 1105

    # Every pair of orthogonal isotropic points spans a totally isotropic line.
    lines = set()
    for i, v in enumerate(isotropic):
        for w in isotropic[i + 1:]:
            if hermitian(v, w) != 0:
                continue
            span = set()
            for a in range(16):
                av = tuple(MUL[a][x] for x in v)
                for b in range(16):
                    if a == 0 and b == 0:
                        continue
                    z = tuple(av[t] ^ MUL[b][w[t]] for t in range(4))
                    span.add(norm_projective(z))
            assert len(span) == 17
            lines.add(tuple(sorted(span)))
    lines = sorted(lines)
    assert len(lines) == 325  # (q+1)(q^3+1) with q=4

    sets = [set(line) for line in lines]
    n = len(lines)
    G = [[0] * n for _ in range(n)]
    for i in range(n):
        G[i][i] = -3  # adjunction: C^2 = 2 - degree = -3 on a quintic surface
        for j in range(i + 1, n):
            inter = len(sets[i] & sets[j])
            assert inter in (0, 1)
            G[i][j] = G[j][i] = inter

    rank2 = rank_mod_p(G, 2)
    rank3 = rank_mod_p(G, 3)
    unit_count, exact_one_count = local_smith_mod4(G)
    # For the Hermitian surface, the linear-cycle classes span H^2 and b_2=53.
    rational_rank = 53
    exact_two_count = rational_rank - unit_count - exact_one_count
    assert (rank2, rank3, unit_count, exact_one_count, exact_two_count) == (37, 53, 37, 16, 0)
    print("POINTS=4369")
    print("ISOTROPIC_POINTS=1105")
    print("TOTALLY_ISOTROPIC_LINES=325")
    print("GRAM_DIAGONAL=-3; OFF_DIAGONAL=0_OR_1")
    print("RANK_MOD_2=37")
    print("RANK_MOD_3=53")
    print("RATIONAL_RANK_FROM_GEOMETRY=53")
    print("SMITH_2_ADIC_EXPONENT_COUNTS: e0=37, e1=16, e2=0")
    print("NONZERO_SMITH_FACTORS=1^37 * 2^16 (odd-prime support excluded by Shimada's theorem)")
    print("VERIFY_OK")

if __name__ == "__main__":
    main()
