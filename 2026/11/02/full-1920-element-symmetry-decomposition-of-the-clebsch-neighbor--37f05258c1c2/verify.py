#!/usr/bin/env python3
"""Exact finite verification of affine-equivariant rational neighborhood homology.

Only Python's standard library is required.  All graphs, simplices, matrices,
actions and characters are generated from the printed finite definitions.
"""
from collections import Counter, defaultdict
from itertools import combinations, permutations

V = tuple(x for x in range(32) if x.bit_count() % 2 == 0)
T = V
IDENTITY = tuple(range(5))
NEIGHBOR = {x: frozenset(y for y in V if (x ^ y).bit_count() == 4) for x in V}
assert len(V) == 16 and all(len(NEIGHBOR[x]) == 5 for x in V)
assert all(x not in NEIGHBOR[x] for x in V)
assert all((x in NEIGHBOR[y]) == (y in NEIGHBOR[x]) for x in V for y in V)
assert all(len(NEIGHBOR[x] & NEIGHBOR[y]) == (5 if x == y else 0 if y in NEIGHBOR[x] else 2)
           for x in V for y in V)
# The five neighbors of 0 uniquely determine the other ten vertices,
# as the ten different pairwise sums of the five generators.
S = tuple(sorted(NEIGHBOR[0]))
assert len({a ^ b for a, b in combinations(S, 2)}) == 10
assert {a ^ b for a, b in combinations(S, 2)} == set(V) - set(S) - {0}
F = {tuple(sorted(t)) for s in V for k in range(1, 6) for t in combinations(NEIGHBOR[s], k)}
C = {k: sorted(f for f in F if len(f) == k + 1) for k in range(5)}
assert tuple(len(C[k]) for k in range(5)) == (16, 80, 160, 80, 16)
assert len(F) == 352
for f in F:
    for i in range(len(f)):
        assert f[:i] + f[i + 1:] in F or len(f) == 1


def boundary(k):
    if k == 0:
        return None
    index = {f: i for i, f in enumerate(C[k - 1])}
    return [
        {index[f[:j] + f[j + 1:]]: (-1) ** j for j in range(k + 1)}
        for f in C[k]
    ]

B = {k: boundary(k) for k in range(1, 5)}
for k in range(2, 5):
    for col in B[k]:
        out = defaultdict(int)
        for row, coefficient in col.items():
            for r2, coefficient2 in B[k - 1][row].items():
                out[r2] += coefficient * coefficient2
        assert all(value == 0 for value in out.values())


def modular_rank(cols, p):
    basis = {}
    for initial in cols:
        col = {j: (a % p) for j, a in initial.items() if a % p}
        while col:
            pivot = min(col)
            if pivot not in basis:
                coeff = pow(col[pivot], -1, p)
                basis[pivot] = {j: (a * coeff) % p for j, a in col.items()}
                break
            factor = col[pivot]
            for j, a in basis[pivot].items():
                val = (col.get(j, 0) - factor * a) % p
                if val:
                    col[j] = val
                else:
                    col.pop(j, None)
    return len(basis)

for p in (2, 3, 5, 101):
    ranks = tuple(modular_rank(B[k], p) for k in range(1, 5))
    assert ranks == (15, 65, 64, 16), (p, ranks)
# These mod-p lower bounds are exact over Q: rank(d1)+rank(d2) <= 80,
# rank(d3)+rank(d4) <= 80, and both lower bounds already attain 80.
ranks = (15, 65, 64, 16)
betti = (16 - 15, 80 - 15 - 65, 160 - 65 - 64,
         80 - 64 - 16, 16 - 16)
assert betti == (1, 0, 31, 0, 0)


def bit_permutation(x, p):
    return sum(1 << p[i] for i in range(5) if (x >> i) & 1)


def group_map(a, p):
    return {v: a ^ bit_permutation(v, p) for v in V}


def sign_perm(perm):
    inversions = sum(x > y for i, x in enumerate(perm) for y in perm[i + 1:])
    return -1 if inversions % 2 else 1


def signed_face(f, g):
    return sign_perm([g[v] for v in f])


def character(g):
    # Reduced Lefschetz number, hence trace on H_2 because the only
    # nonzero reduced rational homology is in degree two.
    tr = -1
    for k in range(5):
        tr += (-1) ** k * sum(signed_face(f, g) for f in C[k]
                               if {g[v] for v in f} == set(f))
    return tr


G = {}
for p in permutations(range(5)):
    for a in T:
        g = group_map(a, p)
        assert len(set(g.values())) == 16
        assert all({g[v] for v in NEIGHBOR[u]} == set(NEIGHBOR[g[u]]) for u in V)
        key = (a, p)
        G[key] = character(g)
assert len(G) == 1920
assert len({tuple(group_map(a, p)[v] for v in V) for a, p in G}) == 1920
# Since a graph automorphism fixing 0 permutes its five neighbors and these
# determine its other ten vertices, Aut(C) has at most 16*5! elements.
assert G[(0, IDENTITY)] == 31


def order(a, p):
    m = group_map(a, p)
    h = {x: x for x in V}
    for i in range(1, 61):
        h = {v: m[h[v]] for v in V}
        if all(h[v] == v for v in V):
            return i
    raise AssertionError('group order not found')

classes = Counter((order(a, p), sum(group_map(a, p)[v] == v for v in V), tr)
                  for (a, p), tr in G.items())
assert sum(classes.values()) == 1920
assert sum(G.values()) == 0
assert sum(t * t for t in G.values()) == 5760
assert sum(G[(a, IDENTITY)] for a in T) == 96


def little_char(lam, p):
    # Fourier projection to the theta_lam-isotypic component for T.
    total = sum(((-1) ** ((lam & a).bit_count() % 2)) * G[(a, p)] for a in T)
    assert total % 16 == 0
    return total // 16


for p in permutations(range(5)):
    # The invariant-under-T summand is exterior-square of the standard S5 module.
    t = sum(p[i] == i for i in range(5)) - 1
    t2 = sum(p[p[i]] == i for i in range(5)) - 1
    assert little_char(0, p) == (t * t - t2) // 2

    # The stabilizer of a weight-one dual character is S4;
    # its three-dimensional little representation is sign*standard.
    if p[0] == 0:
        perm4 = tuple(p[i] for i in range(1, 5))
        assert little_char(1, p) == sign_perm(perm4) * (sum(p[i] == i for i in range(1, 5)) - 1)

    # The stabilizer of a weight-two character is S2 x S3;
    # its one-dimensional little representation is trivial x sign.
    if {p[0], p[1]} == {0, 1}:
        perm3 = tuple(p[i] for i in range(2, 5))
        assert little_char(3, p) == sign_perm(perm3)

# Across the three T-dual S5-orbits, the little modules are irreducible,
# yielding three pairwise distinct irreducible summands of ranks 6,15,10.
assert 6 + 15 + 10 == 31
expected = {
    (1, 16, 31): 1,
    (2, 0, -1): 5, (2, 0, 3): 60, (2, 0, 7): 10,
    (2, 4, -5): 60, (2, 8, -5): 20,
    (3, 4, 1): 80, (4, 0, -1): 260, (4, 2, 1): 240,
    (5, 1, 1): 384, (6, 0, -1): 160, (6, 0, 1): 80,
    (6, 2, 1): 160, (8, 0, -1): 240, (12, 0, -1): 160,
}
assert classes == expected, (classes - expected, expected - classes)
print('CLEBSCH_NEIGHBORHOOD_FULL1920_THREE_IRREDUCIBLES_VERIFIED')
print('faces=(16,80,160,80,16); ranks=(15,65,64,16); Betti=(1,0,31,0,0)')
print('group=1920; irreducibles=(6,15,10); invariants=0; norm=3')
for (order_, fixed, tr), count in sorted(classes.items()):
    print(f'order={order_} fixed_vertices={fixed} trace={tr} count={count}')
