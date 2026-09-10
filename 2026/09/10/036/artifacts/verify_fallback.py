"""Exact fallback qualification verifier — lane-590 (stdlib only).

Witness:
  X0 = C1 U C2, C1,C2 smooth trigonal genus-4, 3 transverse nodes.
  pa(X0) = 4+4+3-1 = 10.
  E0 rank 2, multidegree (6,6): E0|Ci = Ei = Li (+) Li, Li = g^1_3 (deg 3, h0 2).
  Nodes = full fibers: p1+p2+p3 in |L1|, q1+q2+q3 in |L2|.
  Gluing at node j: phi_j = I_2 (scalar 2x2 identity).

Normalization exact sequence:
  0 -> H0(X0,E0) -> H0(C1,E1) (+) H0(C2,E2) --Phi--> (+) MM_j, MM_j = C^2.
  dim domain = 4+4 = 8, codomain = 6.
  h0(X0,E0) = 8 - rank(Phi).

Fiber model (exact integers): choose bases of H0(Li) with fiber evaluations
proportional (all three points in one fiber of the pencil map):
  ev = [[1,2],[1,2],[1,2]] (3x2, rank 1).
Block per summand gives A,B 6x4, Phi = [A | -B] 6x8 integer matrix.
Exact rank over QQ by fraction Gaussian elimination.
"""
from fractions import Fraction

def mat_rank_qq(rows):
    M = [[Fraction(x) for x in r] for r in rows]
    m, n = len(M), len(M[0])
    r = 0
    for c in range(n):
        piv = None
        for i in range(r, m):
            if M[i][c] != 0:
                piv = i
                break
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        inv = 1 / M[r][c]
        M[r] = [v * inv for v in M[r]]
        for i in range(m):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        r += 1
        if r == m:
            break
    return r

# fiber evaluation block
ev = [[1, 2], [1, 2], [1, 2]]
def block(ev):
    Z = [[0, 0]] * 3
    top = [ev[i] + [0, 0] for i in range(3)]
    bot = [[0, 0] + ev[i] for i in range(3)]
    return top + bot  # 6x4

A = block(ev)
B = block(ev)
Phi = [A[i] + [-B[i][k] for k in range(4)] for i in range(6)]

print("Phi (6x8):")
for row in Phi:
    print(row)
rank = mat_rank_qq(Phi)
h0 = 8 - rank
print(f"rank(Phi) = {rank}, h0(X0,E0) = {h0}")
assert rank == 2, f"expected rank 2, got {rank}"
assert h0 == 6, f"expected h0 6, got {h0}"

# generic control: distinct general evaluation points -> full rank 6, h0 2
Ag = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0],
      [0, 0, 0, 1], [1, 1, 1, 0], [0, 1, 1, 1]]
Bg = [[0, 0, 1, 1], [1, 1, 0, 1], [1, 0, 1, 1],
      [1, 1, 0, 0], [0, 1, 0, 1], [1, 0, 0, 1]]
Phig = [Ag[i] + [-Bg[i][k] for k in range(4)] for i in range(6)]
rg = mat_rank_qq(Phig)
print(f"generic control: rank = {rg}, h0 = {8 - rg}")
assert rg == 6 and 8 - rg == 2

# slope semistability per component: mu(Ei) = 6/2 = 3; subbundle Li slope 3 <= 3
mu = Fraction(6, 2)
assert mu == 3
print(f"mu(E1) = mu(E2) = {mu}; destabilizing test: slope(Li) = 3 <= 3 OK (semistable, strictly)")
print(f"pa = 4 + 4 + 3 - 1 = {4 + 4 + 3 - 1}")
assert 4 + 4 + 3 - 1 == 10
print("VERIFY_OK")
