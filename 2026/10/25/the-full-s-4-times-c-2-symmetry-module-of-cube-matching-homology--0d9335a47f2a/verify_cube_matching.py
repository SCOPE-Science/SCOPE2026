#!/usr/bin/env python3
"""Exact finite verification of the rational automorphism-homology character
of the ordinary matching complex of the 3-cube. Python 3 standard library only.
"""
from collections import defaultdict
from itertools import combinations, permutations

V = range(8)
E = tuple(sorted((v, v ^ (1 << i)) for v in V for i in range(3)
                 if v < (v ^ (1 << i))))
assert len(E) == 12 and len(set(E)) == 12
EINDEX = {e: j for j, e in enumerate(E)}

# Include the empty simplex: augmented complex in degree -1.
F = {0: [()]}
for r in range(1, 5):
    F[r] = [s for s in combinations(range(12), r)
            if len({u for j in s for u in E[j]}) == 2 * r]
assert [len(F[r]) for r in range(5)] == [1, 12, 42, 44, 9]
assert len({s for f in F.values() for s in f}) == 108

# Boundary matrices over F_2 are enough for rank lower bounds over Q;
# the chain-complex relation and known upper bounds force equality.
def binary_rank(cols):
    piv = {}
    for col in cols:
        while col:
            j = col.bit_length() - 1
            if j in piv:
                col ^= piv[j]
            else:
                piv[j] = col
                break
    return len(piv)

ranks = [1]
for r in range(2, 5):
    ridx = {s: k for k, s in enumerate(F[r - 1])}
    cols = [sum(1 << ridx[s[:i] + s[i + 1:]] for i in range(r))
            for s in F[r]]
    ranks.append(binary_rank(cols))
# ∂_1: C_1 -> C_0 (index r=2), ∂_2: C_2 -> C_1 (r=3), ∂_3: C_3 -> C_2 (r=4)
assert ranks == [1, 11, 31, 9], ranks
# Check orientation cancellation ∂^2=0 over Z on each basis face.
for r in range(2, 5):
    for s in F[r]:
        coeff = defaultdict(int)
        for i in range(r):
            t = s[:i] + s[i + 1:]
            for j in range(r - 1):
                u = t[:j] + t[j + 1:]
                coeff[u] += (-1) ** (i + j)
        assert all(z == 0 for z in coeff.values())

# Rank_Q(∂1)=11 by (mod 2) rank ≥11 and row-sum zero => ≤11.
# Rank_Q(∂2) ≥31 by mod 2, ≤42-11=31 by ∂1∂2=0.
# Rank_Q(∂3) ≥9 by mod 2, ≤dim(C3)=9.
# Augmented reduced Q-homology: (0,0,4,0).
assert len(F[1]) - 1 - 11 == 0
assert len(F[2]) - 11 - 31 == 0
assert len(F[3]) - 31 - 9 == 4
assert len(F[4]) - 9 == 0
print('EXACT_RATIONAL_HOMOLOGY_VERIFIED', [1, 12, 42, 44, 9], ranks)

def vimage(v, p, b):
    return sum(((v >> i) & 1) << p[i] for i in range(3)) ^ b

def edge_action(p, b):
    return tuple(EINDEX[tuple(sorted((vimage(a, p, b), vimage(z, p, b))))]
                 for a, z in E)

def sign_of_list(v):
    return -1 if sum(v[i] > v[j] for i in range(len(v))
                     for j in range(i + 1, len(v))) % 2 else 1

# Four antipodal body diagonals, one from each complementary pair.
DIAGONALS = tuple(tuple(sorted((v, v ^ 7))) for v in range(4))
assert len(set(DIAGONALS)) == 4

def diagonal_action(p, b):
    return tuple(DIAGONALS.index(tuple(sorted((vimage(a, p, b),
                                               vimage(z, p, b)))))
                 for a, z in DIAGONALS)

def cycle_type(d):
    seen = set()
    out = []
    for v in range(len(d)):
        if v in seen:
            continue
        cur, length = v, 0
        while cur not in seen:
            seen.add(cur)
            length += 1
            cur = d[cur]
        out.append(length)
    return tuple(sorted(out, reverse=True))

def signed_lefschetz(g):
    result = 0
    for r in range(5):
        # A simplex of r vertices has degree r-1; the empty face has degree -1.
        for s in F[r]:
            mapped = [g[j] for j in s]
            if tuple(sorted(mapped)) == s:
                result += (1 if r % 2 else -1) * sign_of_list(mapped)
    return result

# Rational S_4 irreducible characters indexed by partitions of four.
PARTS = ((1,1,1,1), (2,1,1), (2,2), (3,1), (4,))
IRREPS = {
    '(4)':           (1, 1, 1, 1, 1),
    '(1,1,1,1)':     (1,-1, 1, 1,-1),
    '(3,1)':         (3, 1,-1, 0,-1),
    '(2,1,1)':       (3,-1,-1, 0, 1),
    '(2,2)':         (2, 0, 2,-1, 0),
}
G = []
seen_images = set()
for p in permutations(range(3)):
    for b in range(8):
        g = edge_action(p, b)
        assert tuple(sorted(g)) == tuple(range(12))
        assert g not in seen_images
        seen_images.add(g)
        # Automorphisms preserve all matching faces.
        assert all(tuple(sorted(g[j] for j in s)) in F[r]
                   for r in range(5) for s in F[r])
        dg = diagonal_action(p, b)
        assert tuple(sorted(dg)) == tuple(range(4))
        ct = cycle_type(dg)
        assert ct in PARTS
        eps = -1 if b.bit_count() % 2 else 1
        # S^(2,1,1) = (permutation module minus trivial) tensor sign.
        pred = eps + sign_of_list(dg) * (sum(dg[i] == i for i in range(4)) - 1)
        observed = signed_lefschetz(g)
        assert observed == pred, (p, b, observed, pred)
        G.append((p, b, ct, eps, observed))
assert len(G) == 48
assert len({(dg, ep) for p,b,ct,ep,c in G for dg in [diagonal_action(p,b)]}) == 48
print('ALL_48_SIGNED_LEFSCHETZ_TRACES_VERIFIED')

mult = {}
for name, vals in IRREPS.items():
    for parity in (0,1):
        inner_product_num = sum(c * vals[PARTS.index(ct)] * (ep if parity else 1)
                                for p,b,ct,ep,c in G)
        assert inner_product_num % 48 == 0
        mult[(name,parity)] = inner_product_num//48
assert {(name,par):m for (name,par),m in mult.items() if m} == {
    ('(4)', 1): 1, ('(2,1,1)', 0): 1}, mult
assert sum(c for p,b,ct,ep,c in G) == 0
assert sum(c for p,b,ct,ep,c in G if ep == 1) == 24
assert [c for p,b,ct,ep,c in G if p == (0,1,2) and b == 7] == [2]
print('FULL_S4_TIMES_C2_MODULE_VERIFIED', {str(k):v for k,v in mult.items() if v})
print('CENTRAL_INVERSION_TRACE_VERIFIED',2)
print('QUOTIENT_H2_INVARIANTS_VERIFIED', {'full_group':0,'even_flips':1})
print('ALL_CUBE_MATCHING_SYMMETRY_CHECKS_PASSED')
