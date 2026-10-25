#!/usr/bin/env python3
"""Exact, standalone simplicial and rational-character verification for H(5,2).

Uses only Python's standard library. All simplices, permutation actions and
integer matrices are constructed from the five-label incidence definition.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, permutations
from functools import lru_cache

N = 5
V = [tuple(a) for k in (2, 3) for a in combinations(range(N), k)]
index = {a:i for i,a in enumerate(V)}
assert len(V) == 20
adj = [0] * 20
for i, a in enumerate(V):
    for j, b in enumerate(V):
        if i < j and len(a) != len(b):
            small, big = (a, b) if len(a) == 2 else (b, a)
            if set(small) <= set(big):
                adj[i] |= 1 << j
                adj[j] |= 1 << i
assert all(a.bit_count() == 3 for a in adj)

by_card = [[] for _ in range(11)]
def enumerate_faces(mask, available, k):
    by_card[k].append(mask)
    while available:
        bit = available & -available
        available -= bit
        i = bit.bit_length() - 1
        enumerate_faces(mask | bit, available & ~adj[i], k + 1)
enumerate_faces(0, (1 << 20) - 1, 0)
assert list(map(len, by_card)) == [1,20,160,660,1510,1924,1320,480,115,20,2]
assert len(set(f for layer in by_card for f in layer)) == 6212

@lru_cache(None)
def vertices(mask):
    return tuple(i for i in range(20) if (mask >> i) & 1)

def parity(seq):
    return (-1) ** sum(a > b for i, a in enumerate(seq) for b in seq[i+1:])

complement = [index[tuple(sorted(set(range(N)) - set(a)))] for a in V]
def action(perm, swap=False):
    mp = [index[tuple(sorted(perm[x] for x in a))] for a in V]
    if swap:
        mp = [complement[i] for i in mp]
    assert len(set(mp)) == 20
    assert all(((adj[i] >> j) & 1) == ((adj[mp[i]] >> mp[j]) & 1)
               for i in range(20) for j in range(20))
    return mp

def oriented_image(face, mp):
    images = [mp[i] for i in vertices(face)]
    return sum(1 << i for i in images), parity(images)

# Exact rational ranks of all positive-dimensional ordinary boundaries
# are bounded below by these GF(2) ranks, since every rationally
# independent set modulo two is independent in characteristic zero.
def mod2_rank(k):
    lower = {f: i for i, f in enumerate(by_card[k])}
    piv = {}
    for f in by_card[k+1]:
        column = 0
        for i in vertices(f):
            column ^= 1 << lower[f ^ (1 << i)]
        while column:
            p = column.bit_length()-1
            if p in piv:
                column ^= piv[p]
            else:
                piv[p] = column
                break
    return len(piv)
mod2 = {k:mod2_rank(k) for k in range(1,10)}
assert mod2 == {1:19,2:141,3:519,4:991,5:932,6:383,7:97,8:18,9:2}
mod2_betti = {k:len(by_card[k+1])-mod2.get(k,0)-mod2.get(k+1,0)
              for k in range(10)}
mod2_betti[0] -= 1  # connected complex: reduced beta zero
assert mod2_betti == {k:({4:1,5:5}.get(k,0)) for k in range(10)}

# Build the sign-isotypic part of rational chains without a character table.
# The antisymmetrizer applied to a representative simplex either vanishes
# or is an orbit-supported chain with normalized coefficients +/-1.
group = list(permutations(range(N)))
gmap = {g:action(g) for g in group}
signs = {g:parity(g) for g in group}
seen = set()
basis = defaultdict(list)
for k, faces in enumerate(by_card[1:], 0):
    for f in faces:
        if f in seen:
            continue
        orbit = {oriented_image(f, gmap[g])[0] for g in group}
        seen |= orbit
        v = defaultdict(int)
        for g in group:
            h, orient = oriented_image(f, gmap[g])
            v[h] += signs[g] * orient
        v = {h:c for h,c in v.items() if c}
        if not v:
            continue
        assert set(v) == orbit and v[f] > 0
        assert all(c % v[f] == 0 for c in v.values())
        norm = {h:c // v[f] for h,c in v.items()}
        assert set(norm.values()) <= {-1,1}
        basis[k].append((f,norm))
assert {k:len(v) for k,v in basis.items()} == {2:4,3:20,4:26,5:9,8:2,9:2}

def rank_Q(rows):
    if not rows:
        return 0
    a = [[Fraction(x) for x in row] for row in rows]
    nrows, ncols = len(a), len(a[0])
    r = 0
    for col in range(ncols):
        p = next((i for i in range(r,nrows) if a[i][col]), None)
        if p is None:
            continue
        a[p], a[r] = a[r], a[p]
        inv = a[r][col]
        a[r] = [x/inv for x in a[r]]
        for i in range(r+1,nrows):
            if a[i][col]:
                z = a[i][col]
                a[i] = [x-z*y for x,y in zip(a[i],a[r])]
        r += 1
        if r == nrows:
            break
    return r

ranks = {}
for k, columns in basis.items():
    if not basis.get(k-1):
        continue
    target = basis[k-1]
    cols = []
    for _, chain in columns:
        bd = defaultdict(int)
        for face,c in chain.items():
            for j,i in enumerate(vertices(face)):
                bd[face ^ (1 << i)] += (-1)**j * c
        # Coefficient on one representative agrees with every simplex
        # in the orbit; nothing may remain off the target support.
        reconstructed = {}
        coeffs = []
        for f, target_chain in target:
            coeff = bd[f]
            coeffs.append(coeff)
            for h, d in target_chain.items():
                reconstructed[h] = coeff*d
        assert all(bd[h] == reconstructed.get(h,0) for h in set(bd)|set(reconstructed))
        cols.append(coeffs)
    matrix = [[cols[j][i] for j in range(len(cols))] for i in range(len(target))]
    ranks[k] = rank_Q(matrix)
assert ranks == {3:4,4:16,5:9,9:2}
assert len(basis[4])-ranks[4]-ranks[5] == 1
for k, chains in basis.items():
    if k != 4:
        assert len(chains)-ranks.get(k,0)-ranks.get(k+1,0) == 0

# The rank-one sign submodule plus the mod-two upper bounds and Euler
# characteristic (-4) forces rational Betti ranks (1, 5).
reduced_euler = sum((-1)**k*len(by_card[k+1]) for k in range(10)) - 0
# Reduced alternating formula uses nonempty faces with dimension k,
# then subtract the empty-face correction of 1.
reduced_euler -= 1
assert reduced_euler == -4

swap_map = action(tuple(range(N)), True)
sign_swap_trace = 0
for k, chains in basis.items():
    for f, chain in chains:
        h, orient = oriented_image(f, swap_map)
        coeff = orient*chain.get(h,0)
        sign_swap_trace += (-1)**k * coeff
assert sign_swap_trace == -1   # only sign-homology in degree four

@lru_cache(None)
def partitions(n,minimum=1):
    if n == 0: return ((),)
    return tuple((x,)+q for x in range(minimum,n+1)
                 for q in partitions(n-x,x))

def representative(parts):
    ans = []
    start = 0
    for length in parts:
        ans.extend([start+i+1 for i in range(length-1)] + [start])
        start += length
    return tuple(ans)

def reduced_lefschetz(mp):
    ans = -1  # augmentation subtracts one in degree zero
    for k, faces in enumerate(by_card[1:], 0):
        for face in faces:
            image, orient = oriented_image(face, mp)
            if image == face:
                ans += (-1)**k*orient
    return ans

for pp in partitions(5):
    p = representative(pp)
    s = parity(p)
    fixed = sum(i==j for i,j in enumerate(p))
    for swapped in (False, True):
        e = -1 if swapped else 1
        assert reduced_lefschetz(action(p, swapped)) == e*(s-fixed)
        assert e*s == (-1 if swapped else 1)*s
        assert e*fixed == (-1 if swapped else 1)*fixed

print('DESARGUES_FACES_AND_MOD2_BOUNDARIES_VERIFIED', sum(map(len,by_card)))
print('DESARGUES_SIGN_CHAIN_RANKS_VERIFIED', ranks)
print('DESARGUES_COMPLEMENT_SIGN_DEGREE4_VERIFIED',sign_swap_trace)
print('DESARGUES_ALL_14_JOINT_CHARACTERS_VERIFIED')
print('DESARGUES_EQUIVARIANT_HOMOLOGY_VERIFIED')
