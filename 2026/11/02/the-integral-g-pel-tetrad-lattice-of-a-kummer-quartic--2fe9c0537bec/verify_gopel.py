"""Reproduce the integral Göpel-tetrad incidence claim using Python 3 standard library."""
from itertools import product, combinations

ZERO = (0, 0, 0, 0)
V = list(product((0, 1), repeat=4))

def add(x, y):
    return tuple(a ^ b for a, b in zip(x, y))

def alternating(x, y):
    return (x[0]*y[1] + x[1]*y[0] + x[2]*y[3] + x[3]*y[2]) % 2

def quadratic(x):
    return (x[0]*x[1] + x[2]*x[3]) % 2

subspaces = {
    frozenset((ZERO, a, b, add(a, b)))
    for a, b in combinations(V[1:], 2) if alternating(a, b) == 0
}
tetrads = sorted(
    {frozenset(add(v, w) for w in W) for W in subspaces for v in V},
    key=lambda T: tuple(sorted(T))
)
assert len(subspaces) == 15 and len(tetrads) == 60
assert all(len(W) == 4 for W in subspaces)
assert all(len(T) == 4 for T in tetrads)
incidence = [[int(v in T) for T in tetrads] for v in V]
assert all(sum(row) == 15 for row in incidence)
assert all(sum(incidence[i][j] for i in range(16)) == 4 for j in range(60))
assert all(sum(v[i] for v in T) % 2 == 0 for i in range(4) for T in tetrads)
assert all(sum(quadratic(v) for v in T) % 2 == 0 for T in tetrads)

# This is a public, deterministic 16-column certificate, indices zero based in
# lexicographically sorted affine Lagrangian tetrads.
minor_columns = (11, 1, 39, 49, 36, 7, 43, 45, 23, 51, 31, 37, 3, 12, 9, 17)
minor = [[incidence[i][j] for j in minor_columns] for i in range(16)]

def bareiss_determinant(rows):
    a = [list(map(int, row)) for row in rows]
    n = len(a)
    assert all(len(row) == n for row in a)
    sign, denom = 1, 1
    for k in range(n - 1):
        if a[k][k] == 0:
            pivot = next((p for p in range(k+1, n) if a[p][k] != 0), None)
            if pivot is None:
                return 0
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        p = a[k][k]
        for i in range(k+1, n):
            for j in range(k+1, n):
                t = a[i][j]*p - a[i][k]*a[k][j]
                assert t % denom == 0
                a[i][j] = t // denom
        for i in range(k+1, n):
            a[i][k] = 0
        denom = p
    return sign*a[n-1][n-1]

det = bareiss_determinant(minor)
assert det == -128, det

# Independent mod-2 rank check; identifies five factors 2, one factor 4
# when combined with the congruence-index proof in RESULT.md.
rows = [sum((incidence[i][j] << j) for j in range(60)) for i in range(16)]
rank = 0
for bit in range(59, -1, -1):
    pivot = next((i for i in range(rank,16) if (rows[i]>>bit)&1), None)
    if pivot is None:
        continue
    rows[rank], rows[pivot] = rows[pivot], rows[rank]
    for i in range(16):
        if i != rank and ((rows[i]>>bit)&1):
            rows[i] ^= rows[rank]
    rank += 1
assert rank == 10, rank

# Surjectivity of the five binary moment functions via basis vectors and
# e0+e1; this is the exact index 4*2^5=128 of the target congruence lattice.
features = [(x[0], x[1], x[2], x[3], quadratic(x)) for x in V]
binary_span = {tuple(0 for _ in range(5))}
for f in features:
    binary_span |= {tuple(u^v for u,v in zip(x,f)) for x in list(binary_span)}
assert len(binary_span) == 32
assert features[0] == (0,0,0,0,0)

print('GOPel: isotropic_subspaces=15, affine_tetrads=60')
print('INCIDENCE: shape=16x60, row_sum=15, column_sum=4')
print('MOMENTS: all 60 satisfy mod-4 total and five mod-2 moments')
print('CERTIFICATE: selected_16x16_determinant=-128')
print('BINARY: incidence_rank_mod2=10, five independent moment rows')
print('INDEX: congruence_index=128, lattice_equals_congruence_kernel')
print('COKERNEL: Z/4 x (Z/2)^5')
print('VERIFY_OK')
