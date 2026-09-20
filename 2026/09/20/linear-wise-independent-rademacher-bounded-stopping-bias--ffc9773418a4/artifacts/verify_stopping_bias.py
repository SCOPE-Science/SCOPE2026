from fractions import Fraction
from itertools import product
from math import comb


def parity(x):
    return x.bit_count() & 1


def rank_f2(columns, rows):
    v = list(columns)
    rank = 0
    for bit in range(rows):
        pivot = next((j for j in range(rank, len(v)) if (v[j] >> bit) & 1), None)
        if pivot is None:
            continue
        v[rank], v[pivot] = v[pivot], v[rank]
        for j in range(len(v)):
            if j != rank and ((v[j] >> bit) & 1):
                v[j] ^= v[rank]
        rank += 1
    return rank


def walk_max_mean(length):
    total = 0
    for steps in product((-1, 1), repeat=length):
        s = 0
        mx = 0
        for x in steps:
            s += x
            mx = max(mx, s)
        total += mx
    return Fraction(total, 1 << length)


def closed_form(length):
    if length % 2 == 0:
        r = length // 2
        c = Fraction(comb(2 * r, r), 4**r)
        return Fraction(4 * r + 1, 2) * c - Fraction(1, 2)
    r = (length - 1) // 2
    c = Fraction(comb(2 * r, r), 4**r)
    return (2 * r + 1) * c - Fraction(1, 2)


def explicit_half_basis(m):
    e = [1 << i for i in range(m)]
    if m % 2 == 0:
        ones = (1 << m) - 1
        f = [ones ^ e[i] for i in range(m)]
    else:
        f = [e[i] ^ e[m - 1] for i in range(m - 1)]
        f.append((1 << m) - 1)
    return e, f


def min_relation_distance_square(f, m):
    best = 2 * m + 1
    for y in range(1, 1 << m):
        ay = 0
        for j in range(m):
            if (y >> j) & 1:
                ay ^= f[j]
        best = min(best, y.bit_count() + ay.bit_count())
    return best


def check_explicit_halves(m):
    e, f = explicit_half_basis(m)
    assert rank_f2(f, m) == m
    assert len(set(e + f)) == 2 * m
    d = min_relation_distance_square(f, m)
    assert d >= 3
    if m % 2 == 0:
        assert d == 4

    nstates = 1 << m
    pair_counts = {(i, j): [0, 0, 0, 0]
                   for i in range(2 * m) for j in range(i + 1, 2 * m)}
    b_seen = set()
    stopped_sum = 0
    max_sum = 0
    for u in range(nstates):
        A = tuple(1 if parity(c & u) == 0 else -1 for c in e)
        B = tuple(1 if parity(c & u) == 0 else -1 for c in f)
        b_seen.add(B)
        X = A + B
        for i in range(2 * m):
            for j in range(i + 1, 2 * m):
                idx = (0 if X[i] == -1 else 2) + (0 if X[j] == -1 else 1)
                pair_counts[(i, j)][idx] += 1

        r = 0
        mx = 0
        kstar = 0
        for k, b in enumerate(B, 1):
            r += b
            if r > mx:
                mx = r
                kstar = k
        stopped_sum += sum(A) + sum(B[:kstar])
        max_sum += mx

    assert len(b_seen) == nstates
    target = nstates // 4
    assert all(c == [target] * 4 for c in pair_counts.values())
    stopped = Fraction(stopped_sum, nstates)
    mxmean = Fraction(max_sum, nstates)
    assert stopped == mxmean == walk_max_mean(m) == closed_form(m)
    return d, stopped


def gv_sufficient_k(total, past):
    rhs = (1 << past) - 1
    s = 0
    kmax = 1
    for k in range(2, total + 1):
        s += comb(total, k)
        if s < rhs:
            kmax = k
        else:
            break
    return kmax


def simplex_check(r):
    # The binary simplex code has all nonzero r-bit columns.
    cols = list(range(1, 1 << r))
    identity = [1 << i for i in range(r)]
    prefix = [c for c in cols if c not in identity]
    m = len(prefix)
    # A is m x r; its j-th column is the vector of j-th bits of prefix rows.
    Acols = []
    for j in range(r):
        col = 0
        for i, c in enumerate(prefix):
            if (c >> j) & 1:
                col |= 1 << i
        Acols.append(col)
    assert rank_f2(Acols, m) == r
    d = m + r + 1
    for y in range(1, 1 << r):
        ay = 0
        for j in range(r):
            if (y >> j) & 1:
                ay ^= Acols[j]
        d = min(d, y.bit_count() + ay.bit_count())
    N = (1 << r) - 1
    assert d == 1 << (r - 1)
    return N, d - 1, closed_form(r)


print("Exact two-equal-block checks")
for m in range(3, 11):
    d, bias = check_explicit_halves(m)
    print(f"m={m:2d} relation_distance={d:2d} exact_bias={bias}")

print("\nSimplex-code half-wise examples")
for r in range(3, 9):
    N, k, bias = simplex_check(r)
    print(f"N={N:3d} k={k:3d} predictable_tail={r:2d} exact_bias={bias}")

print("\nCoarse random-systematic-code guarantee for equal halves")
for m in (16, 32, 64, 128, 256):
    k = gv_sufficient_k(2 * m, m)
    print(f"N={2*m:3d} guaranteed_k={k:3d} fraction={k/(2*m):.6f}")

print("\nall exact checks passed")
