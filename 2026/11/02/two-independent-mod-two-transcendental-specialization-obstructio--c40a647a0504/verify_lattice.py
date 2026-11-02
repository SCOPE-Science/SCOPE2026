#!/usr/bin/env python3
"""Exact integer checks for the rank-two lattice and specialization statement.

Mathematical proof is in RESULT.md; enumeration here is a supplementary
independent arithmetic check, not a substitute for the all-vector argument.
"""
from math import gcd

A = ((2, -1), (-1, 2))
R = ((0, -1), (1, -1))

def mul(A, B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(len(B)))
                       for j in range(len(B[0]))) for i in range(len(A)))

def tr(A):
    return tuple(zip(*A))

def gram_scale(M, n):
    return tuple(tuple(n*v for v in row) for row in M)

def det2(M):
    return M[0][0]*M[1][1]-M[0][1]*M[1][0]

def norm(v, G):
    return sum(v[i]*G[i][j]*v[j] for i in range(2) for j in range(2))

G = gram_scale(A, 4)
assert mul(mul(tr(R), G), R) == G
assert det2(A) == 3 and det2(G) == 48
assert gcd(*[abs(x) for row in G for x in row]) == 4
assert det2(G)//16 == 3  # Smith invariant factors of 4A2: (4,12).
assert sorted((4, det2(G)//4)) == [4, 12]

# Column Hermite normal form classifies index-four sublattices of Z^2.
all_hnf = []
for a in (1, 2, 4):
    d = 4//a
    for b in range(a):
        H = ((a, b), (0, d))
        e1 = (H[0][0], H[1][0])
        e2 = (H[0][1], H[1][1])
        norms = [norm(e1, A), norm(e2, A),
                 norm((e1[0]+e2[0], e1[1]+e2[1]), A)]
        all_hnf.append((H, norms))
compatible = [H for H, norms in all_hnf if all(n % 8 == 0 for n in norms)]
assert len(all_hnf) == 7
assert compatible == [((2, 0), (0, 2))], compatible
H = compatible[0]
assert mul(mul(tr(H), A), H) == G
assert gcd(*[abs(v) for row in H for v in row]) == 2
assert det2(H) == 4                  # Cokernel Smith invariants (2,2).
# The residue polynomial x^2-xy+y^2 mod 2 vanishes iff both entries even.
assert [(x, y) for x in range(2) for y in range(2)
        if (x*x-x*y+y*y) % 2 == 0] == [(0, 0)]
print('VERIFY_OK: 4A2, 7 index-four sublattices, unique 2A2, cokernel (2,2)')
