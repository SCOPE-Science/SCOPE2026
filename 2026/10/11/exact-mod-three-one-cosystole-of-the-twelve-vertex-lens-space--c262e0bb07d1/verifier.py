from itertools import combinations, product
from collections import Counter
from pathlib import Path

P = 3
V = tuple(range(1, 13))

def decode(token):
    hits = [c for c in combinations(V, 4) if ''.join(map(str, c)) == token]
    assert len(hits) == 1, (token, hits)
    return hits[0]

facets = sorted(decode(s) for s in Path(__file__).with_name('source_facets.txt').read_text().split())
edges = sorted({e for F in facets for e in combinations(F, 2)})
triangles = sorted({t for F in facets for t in combinations(F, 3)})
assert (len(V), len(edges), len(triangles), len(facets)) == (12, 66, 108, 54)
edge_index = {e:i for i,e in enumerate(edges)}

# Boundary rows from oriented edges to vertices, and triangles to edges.
D1 = [[0] * len(edges) for _ in V]
for j, (a,b) in enumerate(edges):
    D1[a-1][j] = -1
    D1[b-1][j] = 1
D2 = [[0] * len(triangles) for _ in edges]
for j, t in enumerate(triangles):
    for q in range(3):
        e = t[:q] + t[q+1:]
        D2[edge_index[e]][j] = 1 if q % 2 == 0 else -1

def rank_mod(A, p=P):
    A = [[x % p for x in row] for row in A if any(x % p for x in row)]
    if not A:
        return 0
    m, n = len(A), len(A[0])
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if A[i][c] % p), None)
        if pivot is None:
            continue
        A[r], A[pivot] = A[pivot], A[r]
        inv = pow(A[r][c], -1, p)
        A[r] = [(x * inv) % p for x in A[r]]
        for i in range(m):
            if i != r and A[i][c] % p:
                f = A[i][c] % p
                A[i] = [(x - f*y) % p for x,y in zip(A[i], A[r])]
        r += 1
        if r == m:
            break
    return r

r1 = rank_mod(D1)
r2 = rank_mod(D2)
assert (r1, r2) == (11, 54)
# dim H^1 = dim ker(delta_1) - dim im(delta_0) = (66-rank D2)-rank D1 = 1.
assert len(edges) - r2 - r1 == 1

# One minimum representative. Coefficient 2 means -1 in F_3.
c0_data = {
    (1,2):2, (1,3):2, (1,4):2, (1,9):1, (1,10):2,
    (2,5):1, (2,6):1, (2,9):2, (2,11):1,
    (3,5):2, (3,6):2, (3,7):1, (3,8):1,
    (4,5):2, (4,6):2, (4,7):1, (4,9):2, (4,10):2,
    (5,8):2, (5,9):1, (5,11):1,
    (6,7):2, (6,8):2,
    (7,9):1, (7,11):1,
    (8,9):2, (8,10):2,
    (10,11):1,
}
c0 = [c0_data.get(e, 0) for e in edges]
assert sum(x != 0 for x in c0) == 28

# Cocycle condition on every oriented triangle.
for a,b,c in triangles:
    val = c0[edge_index[(b,c)]] - c0[edge_index[(a,c)]] + c0[edge_index[(a,b)]]
    assert val % P == 0
# c0 is not a coboundary.
assert rank_mod(D1 + [c0]) == 12

# Every cocycle in [c0] is c0 + delta p. Fixing p(1)=0 parametrizes the 3^11
# coboundaries without repetition because the 1-skeleton is connected.
weights = Counter()
minimum = len(edges) + 1
min_supports = set()
for tail in product(range(P), repeat=11):
    pot = (0,) + tail
    values = []
    supp = []
    for e, base in zip(edges, c0):
        a,b = e
        x = (base + pot[b-1] - pot[a-1]) % P
        values.append(x)
        if x:
            supp.append(e)
    w = len(supp)
    weights[w] += 1
    if w < minimum:
        minimum = w
        min_supports = {frozenset(supp)}
    elif w == minimum:
        min_supports.add(frozenset(supp))

expected_weights = {
    28:18,29:66,30:162,31:336,32:489,33:714,34:957,35:1596,36:2418,
    37:3477,38:4701,39:6543,40:9021,41:11820,42:14322,43:16797,
    44:18462,45:19392,46:18129,47:15888,48:12411,49:9111,50:5673,
    51:3027,52:1200,53:354,54:60,55:3,
}
assert dict(sorted(weights.items())) == expected_weights
assert sum(weights.values()) == 3**11
assert minimum == 28
assert len(min_supports) == 18

# Negation bijects the two nonzero cohomology classes and preserves edge supports,
# so the same 18 supports are minimum for both nonzero classes.

# Check the published S_3 generators preserve the facet set and classify minimum supports.
def make_perm(cycles):
    p = {i:i for i in V}
    for cyc in cycles:
        for a,b in zip(cyc, cyc[1:] + cyc[:1]):
            p[a] = b
    return tuple(p[i] for i in V)

g1 = make_perm([(1,2),(3,6),(4,5),(7,8),(10,11)])
g2 = make_perm([(1,3,5),(2,4,6),(7,8,9),(10,11,12)])
def compose(p,q):
    return tuple(p[q[i]-1] for i in range(12))
G = {tuple(V)}
while True:
    old = len(G)
    for p in list(G):
        for g in (g1,g2):
            G.add(compose(p,g))
    if len(G) == old:
        break
assert len(G) == 6
facet_set = set(facets)
for p in G:
    assert {tuple(sorted(p[v-1] for v in F)) for F in facets} == facet_set

def perm_support(S,p):
    return frozenset(tuple(sorted((p[a-1],p[b-1]))) for a,b in S)
remaining = set(min_supports)
orbit_sizes = []
while remaining:
    S = next(iter(remaining))
    orb = {perm_support(S,p) for p in G}
    assert orb <= min_supports
    orbit_sizes.append(len(orb))
    remaining -= orb
assert sorted(orbit_sizes) == [3,3,6,6]

print('VERIFY_OK')
print('f_vector=12,66,108,54')
print('H1_F3_dim=1')
print('nonzero_projective_classes=1')
print('cosystole_edge_weight=28')
print('minimum_supports=18')
print('minimum_cocycles_each_nonzero_class=18')
print('minimum_support_S3_orbits=3,3,6,6')
print('coset_size=177147')
print('weight_enumerator=' + ','.join(f'{w}:{expected_weights[w]}' for w in sorted(expected_weights)))
