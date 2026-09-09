# Series-step conditioning analysis for TARGET.
# Background terminals: u0,v0,v1,x0,y0,x1,y1 (7 nodes).
# w-edges: a0=(x0-w0), b0=(w0-y0), a1=(x1-w1), b1=(w1-y1), q=(w0-w1), indep prob p.
# For each set-partition pi of the 7 background nodes, compute
#   f(pi,p) = P_w(u0~v0 | pi) - P_w(u0~v1 | pi)
# as degree<=5 polynomial, and symmetrized g(pi,p)=f(pi)+f(swap(pi)).
# Goal: test pointwise nonnegativity (raw and symmetrized).
from fractions import Fraction
import math
import itertools

NODES = ['u0', 'v0', 'v1', 'x0', 'y0', 'x1', 'y1']
IDX = {s: i for i, s in enumerate(NODES)}
# swap map: layer swap on x,y,v; u0 fixed? Global swap sends u0->u1. But our query
# fixes source u0. Symmetrization pairs R with swapped R and simultaneously swaps
# query? Careful: D = E_R[d(R)] with d(R)=P_w(u0~v0|R)-P_w(u0~v1|R).
# Under global swap S: u0<->u1, v0<->v1, x0<->x1, y0<->y1. Then d(S(R)) =
# P_w(u1~v1|R)-P_w(u1~v0|R) by relabeling w-layers too. This is NOT f(swap(pi))
# with same query; need extended partition including u1. So include u1: 8 nodes.
NODES8 = ['u0', 'u1', 'v0', 'v1', 'x0', 'y0', 'x1', 'y1']
IDX8 = {s: i for i, s in enumerate(NODES8)}
SWAP8 = [1, 0, 3, 2, 6, 7, 4, 5]  # image index


def partitions_of(n):
    # generate set partitions as restricted growth strings
    if n == 0:
        yield []
        return
    rgs = [0] * n

    def rec(i, mx):
        if i == n:
            yield list(rgs)
            return
        for v in range(mx + 2 if mx + 1 < n else mx + 1):
            if v > mx + 1:
                continue
            rgs[i] = v
            yield from rec(i + 1, max(mx, v))
    yield from rec(1, 0)


def blocks_of(rgs):
    d = {}
    for i, b in enumerate(rgs):
        d.setdefault(b, []).append(i)
    return list(d.values())


def poly_f(rgs):
    # returns std coeffs (Fractions) degree<=5 of f over w-edges (a0,b0,a1,b1,q)
    # order bits: 0:a0,1:b0,2:a1,3:b1,4:q
    # background DSU from rgs over NODES (7). w0,w1 fresh ids 7,8.
    nb = len(NODES)
    W0, W1 = nb, nb + 1
    coeff = [Fraction(0)] * 6  # number of open w-edges k -> summed diff
    for mask in range(32):
        k = bin(mask).count('1')
        parent = list(range(nb + 2))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb
        for blk in blocks_of(rgs):
            for j in blk[1:]:
                union(blk[0], j)
        a0 = mask & 1
        b0 = mask & 2
        a1 = mask & 4
        b1 = mask & 8
        q = mask & 16
        if a0:
            union(IDX['x0'], W0)
        if b0:
            union(W0, IDX['y0'])
        if a1:
            union(IDX['x1'], W1)
        if b1:
            union(W1, IDX['y1'])
        if q:
            union(W0, W1)
        i00 = 1 if find(IDX['u0']) == find(IDX['v0']) else 0
        i01 = 1 if find(IDX['u0']) == find(IDX['v1']) else 0
        coeff[k] += Fraction(i00 - i01)
    # convert binom basis (counts over k) to std: P = sum_k coeff[k] p^k (1-p)^{5-k}
    std = [Fraction(0)] * 6
    for k, ck in enumerate(coeff):
        for j in range(5 - k + 1):
            std[k + j] += ck * math.comb(5 - k, j) * ((-1) ** j)
    return std, coeff


def min_on_01(std, n=2001):
    return min(sum(float(a) * (i / (n - 1)) ** k for k, a in enumerate(std)) for i in range(n))


def swap_rgs8_to_7(rgs8):
    # swap labels then restrict to 7 nodes (drop u1)? For symmetrization we need
    # d(S(R)): query becomes u1~v1 minus u1~v0. Compute directly with 8-node DSU.
    return rgs8


def poly_d_sym(rgs8):
    # rgs over 8 nodes. E over w-edges of [(I(u0~v0)-I(u0~v1)) + (I(u1~v1)-I(u1~v0))]/2
    nb = 8
    W0, W1 = nb, nb + 1
    coeff = [Fraction(0)] * 6
    for mask in range(32):
        parent = list(range(nb + 2))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb
        for blk in blocks_of(rgs8):
            for j in blk[1:]:
                union(blk[0], j)
        if mask & 1:
            union(IDX8['x0'], W0)
        if mask & 2:
            union(W0, IDX8['y0'])
        if mask & 4:
            union(IDX8['x1'], W1)
        if mask & 8:
            union(W1, IDX8['y1'])
        if mask & 16:
            union(W0, W1)
        a = (1 if find(IDX8['u0']) == find(IDX8['v0']) else 0) - \
            (1 if find(IDX8['u0']) == find(IDX8['v1']) else 0) + \
            (1 if find(IDX8['u1']) == find(IDX8['v1']) else 0) - \
            (1 if find(IDX8['u1']) == find(IDX8['v0']) else 0)
        coeff[bin(mask).count('1')] += Fraction(a, 2)
    std = [Fraction(0)] * 6
    for k, ck in enumerate(coeff):
        for j in range(5 - k + 1):
            std[k + j] += ck * math.comb(5 - k, j) * ((-1) ** j)
    return std


# Test 1: raw f over 7-node partitions (B7=877)
import time
t0 = time.time()
worst = Fraction(0)
worst_ex = None
neg_count = 0
total = 0
for rgs in partitions_of(7):
    total += 1
    std, _ = poly_f(rgs)
    mn = min_on_01(std)
    if mn < -1e-9:
        neg_count += 1
        if mn < float(worst):
            worst = Fraction(mn).limit_denominator(10**9)
            worst_ex = (list(rgs), [str(a) for a in std], mn)
print(f"7-node partitions: total={total} neg_raw={neg_count} worst_gridmin={float(worst_ex[2]) if worst_ex else 0:.6f} time={time.time()-t0:.1f}s")
if worst_ex:
    print("  worst rgs:", worst_ex[0], "std:", worst_ex[1])

# Test 2: symmetrized over 8-node partitions (B8=4140) -- heavier; sample + full if fast
t0 = time.time()
neg2 = 0
total2 = 0
worst2 = None
for rgs in partitions_of(8):
    total2 += 1
    std = poly_d_sym(rgs)
    mn = min_on_01(std, n=501)
    if mn < -1e-9:
        neg2 += 1
        if worst2 is None or mn < worst2[0]:
            worst2 = (mn, list(rgs), [str(a) for a in std])
print(f"8-node sym partitions: total={total2} neg_sym={neg2} time={time.time()-t0:.1f}s")
if worst2:
    print(f"  worst sym gridmin={worst2[0]:.6f} rgs={worst2[1]} std={worst2[2]}")
else:
    print("  SYM POINTWISE HOLDS on grid (all >= 0).")
