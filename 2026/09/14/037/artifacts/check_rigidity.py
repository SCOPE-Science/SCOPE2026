"""Rigidity checks for K4 skeleton with distinct edge lengths 1..6 (lane-1918).

Checks:
 1. Trivial metric automorphism group: only identity in S4 preserves edge labels.
 2. Vertex signatures (incident length triples) pairwise distinct -> canonical labels.
 3. Monodromy/cycle pairing matrix M for a fixed spanning tree; det(M) = 571 (odd,
    hence invertible over Z_2) -- used in Tate-module distinguishing argument.
 4. Unit-pattern matrix S (edges containing e12 in cycle pairings) nonzero mod 2.
"""
import itertools


def bareiss_det(M):
    n = len(M)
    A = [row[:] for row in M]
    prev = 1
    for k in range(n - 1):
        piv = A[k][k]
        assert piv != 0, "zero pivot; reorder needed"
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                A[i][j] = (A[i][j] * piv - A[i][k] * A[k][j]) // prev
            A[i][k] = 0
        prev = piv
    return A[n - 1][n - 1]


verts = [0, 1, 2, 3]
edges = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
# Fixed bijection edge -> length (1..6), all distinct.
length = {(0, 1): 1, (0, 2): 2, (0, 3): 3, (1, 2): 4, (1, 3): 5, (2, 3): 6}
assert sorted(length.values()) == [1, 2, 3, 4, 5, 6]

def apply_perm(p, e):
    a, b = e
    return tuple(sorted((p[a], p[b])))

stabilizer = []
for p in itertools.permutations(verts):
    ok = all(length[apply_perm(p, e)] == length[e] for e in edges)
    if ok:
        stabilizer.append(p)
print("metric stabilizer in S4:", stabilizer)
assert stabilizer == [(0, 1, 2, 3)], "metric automorphism group must be trivial"

sigs = {}
for v in verts:
    sigs[v] = frozenset(length[tuple(sorted((v, w)))] for w in verts if w != v)
print("vertex incident-length signatures:", {v: sorted(s) for v, s in sigs.items()})
assert len(set(sigs.values())) == 4, "vertices must be canonically distinguishable"

# Cycle basis from star spanning tree at 0: tree edges (0,1),(0,2),(0,3).
# Fundamental cycles (oriented):
#   c1: 0->1->2->0 uses e01(+), e12(+), e02(-)
#   c2: 0->1->3->0 uses e01(+), e13(+), e03(-)
#   c3: 0->2->3->0 uses e02(+), e23(+), e03(-)
# Pairing <ci,cj> = sum over shared edges of +/- L_e (signs by orientation).
M = [
    [1 + 4 + 2, 1, -2],
    [1, 1 + 5 + 3, 3],
    [-2, 3, 2 + 6 + 3],
]
print("pairing matrix M =", M)
d = bareiss_det(M)
print("det(M) =", d)
assert d == 571, "determinant must be 571"
assert d % 2 == 1, "det must be odd (M in GL(3,Z_2))"
assert d % 5 != 0

# Exponent pattern of distinguished edge e01 (length 1) in cycle pairings:
# cycles containing e01: c1, c2 (not c3).
S = [[1, 1, 0], [1, 1, 0], [0, 0, 0]]
assert any(x % 2 for row in S for x in row), "S must be nonzero mod 2"
print("S pattern nonzero mod 2: OK")

# Unit u=2 in Q5: 2^2=4 != 1, 2^4=16 = 1 mod 5 -> Teichmueller element of order 4.
assert pow(2, 2, 5) == 4 and pow(2, 4, 5) == 1
print("order of 2 in F5^× is 4: OK")
print("ALL RIGIDITY CHECKS PASSED")
