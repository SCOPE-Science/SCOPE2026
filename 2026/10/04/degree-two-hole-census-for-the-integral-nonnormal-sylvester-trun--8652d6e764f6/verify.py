#!/usr/bin/env python3
"""Exhaustive verifier for the degree-two hole census of the Sylvester P_{5,1}."""
import numpy as np
from collections import deque

D = 15
N = 16
POW3 = 3 ** np.arange(D, dtype=np.int64)

# Sylvester character rows r=0,...,15 on nonzero four-bit columns j=1,...,15.
V = np.empty((N, D), dtype=np.int8)
for r in range(N):
    for jj, j in enumerate(range(1, N)):
        V[r, jj] = -1 if ((r & j).bit_count() & 1) else 1

# Source-lattice points are exactly sign vectors in P_{5,1}.
nums = np.arange(1 << D, dtype=np.uint16)
bits = ((nums[:, None] >> np.arange(D, dtype=np.uint16)) & 1).astype(np.int8)
signs = (2 * bits - 1).astype(np.int8)
feas = ((signs.astype(np.int16) @ V.astype(np.int16).T) >= -5).all(axis=1)
Sbits = bits[feas]
Scodes = (Sbits.astype(np.int64) * POW3).sum(axis=1)
assert len(Scodes) == 9552
assert len(np.unique(Scodes)) == 9552

# If E(x)=sum b_i 3^i for sign bits b_i in {0,1}, then
# C((x+y)/2)=E(x)+E(y); there are no carries in base 3.
T = 3 ** D
decomp = np.zeros(T, dtype=np.bool_)
for i in range(0, len(Scodes), 256):
    sums = Scodes[i:i+256, None] + Scodes[None, :]
    decomp[sums.ravel()] = True
assert int(decomp.sum()) == 6215123

# Enumerate every ternary q in {-1,0,1}^15.  The degree-two target is z=2q.
holes = []
feasible_count = 0
chunk = 200000
for start in range(0, T, chunk):
    c = np.arange(start, min(T, start + chunk), dtype=np.int64)
    tmp = c.copy()
    q = np.empty((len(c), D), dtype=np.int8)
    for k in range(D):
        q[:, k] = (tmp % 3).astype(np.int8) - 1
        tmp //= 3
    good = ((q.astype(np.int16) @ V.astype(np.int16).T) >= -5).all(axis=1)
    feasible_count += int(good.sum())
    holes.extend(c[good & (~decomp[c])].tolist())
assert feasible_count == 6350363
assert len(holes) == 135240


def decode(code):
    q = []
    for _ in range(D):
        q.append(code % 3 - 1)
        code //= 3
    return tuple(q)


def encode(q):
    return sum((v + 1) * (3 ** i) for i, v in enumerate(q))


def swapmap(a, b):
    out = {}
    for j in range(1, 16):
        ba, bb = (j >> a) & 1, (j >> b) & 1
        k = j
        if ba != bb:
            k ^= (1 << a) | (1 << b)
        out[j] = k
    return out


def shearmap(dst, src):
    out = {}
    for j in range(1, 16):
        k = j
        if (j >> src) & 1:
            k ^= 1 << dst
        out[j] = k
    return out


def apply(code, Lmap, a):
    # T_{L,a}: y_{Lj}=(-1)^{a dot j} x_j.
    q = decode(code)
    y = [None] * D
    for j in range(1, 16):
        s = -1 if ((a & j).bit_count() & 1) else 1
        y[Lmap[j] - 1] = s * q[j - 1]
    return encode(y)

# Adjacent basis swaps and one transvection generate GL(4,2); basis translations
# generate F_2^4.  Hence these eight maps generate AGL(4,2).
idmap = {j: j for j in range(1, 16)}
gens = [(swapmap(b, b + 1), 0) for b in range(3)]
gens += [(shearmap(0, 1), 0)]
gens += [(idmap, 1 << b) for b in range(4)]

H = set(holes)
unseen = set(H)
orbits = []
while unseen:
    seed = min(unseen)
    orb = {seed}
    todo = deque([seed])
    while todo:
        c = todo.popleft()
        for g in gens:
            d = apply(c, *g)
            assert d in H
            if d not in orb:
                orb.add(d)
                todo.append(d)
    unseen.difference_update(orb)
    orbits.append((len(orb), seed, decode(seed)))
orbits.sort()
expected = [
    (840,   (0,0,0,0,0,0,0,0,0,0,0,1,-1,-1,-1)),
    (13440, (1,0,0,0,0,0,0,1,0,-1,-1,-1,-1,-1,-1)),
    (26880, (1,1,0,1,0,0,-1,1,-1,-1,-1,-1,-1,-1,-1)),
    (40320, (1,1,0,0,0,0,0,1,-1,-1,-1,-1,-1,-1,-1)),
    (53760, (1,1,1,0,0,0,-1,1,-1,-1,-1,-1,-1,-1,-1)),
]
assert [(s, r) for s, _, r in orbits] == expected
assert sum(s for s, _, _ in orbits) == 135240

# The explicit hole in Proposition 3.3 of arXiv:2609.32950v1 belongs to the
# orbit of size 26880.
source_q = (0,0,0,-1,1,1,1,-1,1,1,1,1,1,1,1)
source_code = encode(source_q)
source_orbit_size = None
for size, seed, _ in orbits:
    orb = {seed}
    todo = deque([seed])
    while todo:
        c = todo.popleft()
        for g in gens:
            d = apply(c, *g)
            if d not in orb:
                orb.add(d)
                todo.append(d)
    if source_code in orb:
        source_orbit_size = size
        break
assert source_orbit_size == 26880

print('source_lattice_points=9552')
print('degree_two_feasible_targets=6350363')
print('degree_two_decomposable_targets=6215123')
print('degree_two_holes=135240')
print('orbit_sizes=840,13440,26880,40320,53760')
print('source_witness_orbit=26880')
print('VERIFY_OK')
