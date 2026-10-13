#!/usr/bin/env python3
import collections
import itertools
import math

MOD = 0b1011  # u^3 + u + 1 over F_2


def gf_mul(a, b):
    out = 0
    aa, bb = a, b
    while bb:
        if bb & 1:
            out ^= aa
        bb >>= 1
        aa <<= 1
        if aa & 0b1000:
            aa ^= MOD
    return out & 0b111


def gf_pow(a, n):
    out = 1
    while n:
        if n & 1:
            out = gf_mul(out, a)
        a = gf_mul(a, a)
        n >>= 1
    return out


def tr(a):
    return a ^ gf_pow(a, 2) ^ gf_pow(a, 4)


def norm(a):
    return 0 if a == 0 else gf_pow(a, 7)


# Reconstruct the m=3 defining set S from the primary paper.
S = []
for x in range(8):
    for y in range(8):
        f = tr(gf_mul(x, y)) ^ norm(x ^ y)
        assert f in (0, 1)
        if f == 0:
            S.append((x, y))
assert len(S) == 28

basis = (1, 2, 4)
columns = []
for x, y in S:
    bits = [1]
    bits += [tr(gf_mul(b, x)) for b in basis]
    bits += [tr(gf_mul(b, y)) for b in basis]
    v = sum((bit & 1) << i for i, bit in enumerate(bits))
    columns.append(v)
assert len(set(columns)) == 28
assert 0 not in columns

# Reproduce the published ordinary weight distribution.
weight_hist = collections.Counter()
for m in range(128):
    w = sum(((m & c).bit_count() & 1) for c in columns)
    weight_hist[w] += 1
assert dict(sorted(weight_hist.items())) == {0: 1, 12: 63, 16: 63, 28: 1}


def rref_subspace_bases(n, k):
    """Yield one row-mask basis for every k-subspace of F_2^n."""
    if k == 0:
        yield ()
        return
    for pivots in itertools.combinations(range(n), k):
        pivot_set = set(pivots)
        free_positions = []
        for i, p in enumerate(pivots):
            for j in range(p + 1, n):
                if j not in pivot_set:
                    free_positions.append((i, j))
        for mask in range(1 << len(free_positions)):
            rows = [1 << p for p in pivots]
            for q, (i, j) in enumerate(free_positions):
                if (mask >> q) & 1:
                    rows[i] |= 1 << j
            yield tuple(rows)


def span(rows):
    vals = {0}
    for r in rows:
        vals |= {v ^ r for v in tuple(vals)}
    return vals


def gaussian_binomial_2(n, k):
    if k < 0 or k > n:
        return 0
    num = den = 1
    for i in range(k):
        num *= (1 << (n - i)) - 1
        den *= (1 << (k - i)) - 1
    return num // den

expected_hist = {
    0: {0: 1},
    1: {0: 99, 1: 28},
    2: {0: 1281, 1: 1008, 2: 378},
    3: {0: 2340, 1: 3360, 2: 3780, 3: 2016, 4: 315},
    4: {0: 722, 1: 448, 2: 2436, 3: 2240, 4: 3745, 5: 1344, 6: 812, 7: 64},
    5: {0: 63, 4: 315, 6: 1008, 8: 945, 10: 336},
    6: {0: 1, 12: 63, 16: 63},
    7: {28: 1},
}

intersection_hist = {}
for t in range(8):
    h = collections.Counter()
    count = 0
    for rows in rref_subspace_bases(7, t):
        W = span(rows)
        h[sum(c in W for c in columns)] += 1
        count += 1
    assert count == gaussian_binomial_2(7, t)
    intersection_hist[t] = dict(sorted(h.items()))
    assert intersection_hist[t] == expected_hist[t]

# U -> U^perp is a bijection between r-subcodes and (7-r)-subspaces.
# A coordinate vanishes on U exactly when the corresponding generator
# column belongs to U^perp. Hence support(U)=28-|columns cap U^perp|.
d = []
M = []
max_intersections = []
for r in range(1, 8):
    t = 7 - r
    mx = max(intersection_hist[t])
    d.append(28 - mx)
    M.append(intersection_hist[t][mx])
    if r <= 6:
        max_intersections.append(mx)

assert d == [12, 18, 21, 24, 26, 27, 28]
assert M == [63, 336, 64, 315, 378, 28, 1]
assert max_intersections == [16, 10, 7, 4, 2, 1]

print("VERIFY_OK")
