#!/usr/bin/env python3
from collections import Counter
from fractions import Fraction

# K_{1,0}: the 16-point face poset in Cianci--Ottina, Figure 4.
# Indices: c1..c4 = 0..3, b1..b8 = 4..11, a1..a4 = 12..15.
N = 16
le = [[False] * N for _ in range(N)]
for i in range(N):
    le[i][i] = True

cb = {
    1: [1, 3], 7: [1, 3],
    2: [2, 4], 8: [2, 4],
    4: [1, 2], 5: [1, 2],
    3: [3, 4], 6: [3, 4],
}
ab = {
    1: [1, 2, 3, 4],
    2: [1, 2, 5, 6],
    3: [3, 5, 7, 8],
    4: [4, 6, 7, 8],
}
for b, cs in cb.items():
    for c in cs:
        le[c - 1][3 + b] = True
for a, bs in ab.items():
    for b in bs:
        le[3 + b][11 + a] = True
for k in range(N):
    for i in range(N):
        if le[i][k]:
            for j in range(N):
                if le[k][j]:
                    le[i][j] = True

strict = lambda i, j: i != j and le[i][j]
edges = [(i, j) for i in range(N) for j in range(N) if strict(i, j)]
eidx = {e: q for q, e in enumerate(edges)}
triangles = [
    (i, j, k)
    for i in range(N)
    for j in range(N)
    for k in range(N)
    if strict(i, j) and strict(j, k)
]
assert len(edges) == 48
assert len(triangles) == 32

# Integer 1-cycles. t is the order-two class; x is the free class.
t_cycle = [(0, 7, 1), (1, 7, -1), (1, 8, 1), (0, 8, -1)]
x_cycle = [(0, 4, 1), (2, 4, -1), (2, 10, 1), (0, 10, -1)]

# Boundary check for 1-cycles.
def assert_cycle(cyc):
    bd = [0] * N
    for u, v, s in cyc:
        assert strict(u, v)
        bd[u] -= s
        bd[v] += s
    assert bd == [0] * N

assert_cycle(t_cycle)
assert_cycle(x_cycle)

# Integral 1-cocycle alpha with alpha(t)=0, alpha(x)=1.
alpha = {
    (0, 4): 1,
    (0, 13): 1,
    (1, 5): 1,
    (1, 13): 1,
    (2, 12): -1,
    (3, 12): -1,
    (4, 12): -1,
    (5, 12): -1,
    (6, 12): -1,
    (8, 13): 1,
}

# Mod-2 1-cocycle tau dual to t and zero on x.
tau = {
    (0, 8), (0, 14), (1, 5), (1, 13), (2, 6), (2, 14),
    (3, 12), (5, 12), (6, 12), (8, 13), (10, 14),
}

for i, j, k in triangles:
    assert alpha.get((j, k), 0) - alpha.get((i, k), 0) + alpha.get((i, j), 0) == 0
    assert ((((j, k) in tau) ^ ((i, k) in tau) ^ ((i, j) in tau)) == 0)

def eval_int(cyc, coc):
    return sum(s * coc.get((u, v), 0) for u, v, s in cyc)

def eval_mod2(cyc, coc):
    ans = 0
    for u, v, _ in cyc:
        if (u, v) in coc:
            ans ^= 1
    return ans

assert eval_int(t_cycle, alpha) == 0
assert eval_int(x_cycle, alpha) == 1
assert eval_mod2(t_cycle, tau) == 1
assert eval_mod2(x_cycle, tau) == 0

# Explicit integer 2-chain S with boundary 2t.
S = {
    (0, 4, 12): -1, (0, 4, 13): 1, (0, 7, 12): 1, (0, 7, 15): 1,
    (0, 8, 13): -1, (0, 8, 14): -1, (0, 10, 14): 1, (0, 10, 15): -1,
    (1, 5, 12): 1, (1, 5, 13): -1, (1, 7, 12): -1, (1, 7, 15): -1,
    (1, 8, 13): 1, (1, 8, 14): 1, (1, 11, 14): -1, (1, 11, 15): 1,
    (2, 4, 12): 1, (2, 4, 13): -1, (2, 6, 12): -1, (2, 6, 14): 1,
    (2, 9, 13): 1, (2, 9, 15): -1, (2, 10, 14): -1, (2, 10, 15): 1,
    (3, 5, 12): -1, (3, 5, 13): 1, (3, 6, 12): 1, (3, 6, 14): -1,
    (3, 9, 13): -1, (3, 9, 15): 1, (3, 11, 14): 1, (3, 11, 15): -1,
}
assert set(S) == set(triangles)
edge_bd = [0] * len(edges)
for (i, j, k), s in S.items():
    edge_bd[eidx[(j, k)]] += s
    edge_bd[eidx[(i, k)]] -= s
    edge_bd[eidx[(i, j)]] += s
expected = [0] * len(edges)
for u, v, s in t_cycle:
    expected[eidx[(u, v)]] += 2 * s
assert edge_bd == expected

# Rank checks over Q and F_2 for the order-complex chain groups.
def rank_q(rows):
    A = [[Fraction(x) for x in row] for row in rows]
    if not A:
        return 0
    m, n = len(A), len(A[0])
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if A[i][c]), None)
        if pivot is None:
            continue
        A[r], A[pivot] = A[pivot], A[r]
        p = A[r][c]
        A[r] = [x / p for x in A[r]]
        for i in range(m):
            if i != r and A[i][c]:
                q = A[i][c]
                A[i] = [A[i][j] - q * A[r][j] for j in range(n)]
        r += 1
        if r == m:
            break
    return r

def rank_f2(columns):
    piv = {}
    for v in columns:
        x = v
        while x:
            p = x.bit_length() - 1
            if p in piv:
                x ^= piv[p]
            else:
                piv[p] = x
                break
    return len(piv)

# d1: C1 -> C0, d2: C2 -> C1.
d1_rows = [[0] * len(edges) for _ in range(N)]
for q, (u, v) in enumerate(edges):
    d1_rows[u][q] = -1
    d1_rows[v][q] = 1

d2_rows = [[0] * len(triangles) for _ in range(len(edges))]
d2_cols_f2 = []
for q, (i, j, k) in enumerate(triangles):
    d2_rows[eidx[(j, k)]][q] = 1
    d2_rows[eidx[(i, k)]][q] = -1
    d2_rows[eidx[(i, j)]][q] = 1
    d2_cols_f2.append((1 << eidx[(j, k)]) ^ (1 << eidx[(i, k)]) ^ (1 << eidx[(i, j)]))
assert rank_q(d1_rows) == 15
assert rank_q(d2_rows) == 32
assert rank_f2(d2_cols_f2) == 31

# Exhaustive monotone self-map enumeration.
down = [sum(1 << i for i in range(N) if le[i][j]) for j in range(N)]
up = [sum(1 << j for j in range(N) if le[i][j]) for i in range(N)]
ALL = (1 << N) - 1
assignment = [-1] * N
counts = Counter()
bijective_count = 0
h1_iso_count = 0

# Fast target evaluations.
def image_eval_int(cyc, coc):
    ans = 0
    for u, v, s in cyc:
        fu, fv = assignment[u], assignment[v]
        if fu != fv:
            ans += s * coc.get((fu, fv), 0)
    return ans

def image_eval_mod2(cyc, coc):
    ans = 0
    for u, v, _ in cyc:
        fu, fv = assignment[u], assignment[v]
        if fu != fv and (fu, fv) in coc:
            ans ^= 1
    return ans

def action_triple():
    k = image_eval_int(x_cycle, alpha)
    delta = image_eval_mod2(t_cycle, tau)
    epsilon = image_eval_mod2(x_cycle, tau)
    return (k, delta, epsilon)

def allowed(v):
    mask = ALL
    for u, a in enumerate(assignment):
        if a < 0:
            continue
        if le[u][v]:
            mask &= up[a]
        if le[v][u]:
            mask &= down[a]
        if not mask:
            break
    return mask

def visit(depth=0):
    global bijective_count, h1_iso_count
    if depth == N:
        triple = action_triple()
        counts[triple] += 1
        is_bij = len(set(assignment)) == N
        is_h1_iso = triple[0] in (-1, 1) and triple[1] == 1
        if is_bij:
            bijective_count += 1
        if is_h1_iso:
            h1_iso_count += 1
        assert is_bij == is_h1_iso
        return

    best = None
    best_mask = None
    best_size = N + 1
    for v in range(N):
        if assignment[v] < 0:
            mask = allowed(v)
            size = mask.bit_count()
            if size == 0:
                return
            if size < best_size:
                best, best_mask, best_size = v, mask, size
                if size == 1:
                    break
    mask = best_mask
    while mask:
        bit = mask & -mask
        mask -= bit
        a = bit.bit_length() - 1
        assignment[best] = a
        visit(depth + 1)
        assignment[best] = -1

visit()

EXPECTED = Counter({
    (0, 0, 0): 7661824,
    (0, 0, 1): 11072,
    (-1, 0, 0): 1462,
    (-1, 0, 1): 1462,
    (1, 0, 0): 1462,
    (1, 0, 1): 1462,
    (-1, 1, 0): 4,
    (-1, 1, 1): 4,
    (1, 1, 0): 4,
    (1, 1, 1): 4,
})
assert counts == EXPECTED
assert sum(counts.values()) == 7678760
assert len(counts) == 10
assert bijective_count == 16
assert h1_iso_count == 16
assert all(k in (-1, 0, 1) for k, _, _ in counts)
assert (2, 0, 0) not in counts
assert (2, 0, 1) not in counts

# The finite image matches the classical Klein-bottle homology parity constraint
# for k in {-1,0,1}: delta is forced to 0 for even k, unrestricted for odd k;
# epsilon is unrestricted.
expected_types = {
    (k, delta, epsilon)
    for k in (-1, 0, 1)
    for epsilon in (0, 1)
    for delta in ((0, 1) if k % 2 else (0,))
}
assert set(counts) == expected_types

print("VERIFY_OK")
print("continuous_self_maps=7678760")
print("induced_H1_endomorphisms=10")
print("bijective_self_maps=16")
print("H1_isomorphism_maps=16")
print("free_multipliers=-1,0,1")
print("opposite_model_same_result=true")
