"""Exact symbolic first-order rigid-unfolding analysis at the flat state of A8.
Sector angle alpha=pi/4. Fold angles rho_k = s_k*pi (flat), s_k=+-1.
Closure C(rho) = prod_k Rz(alpha) Rx(rho_k). Tangent columns computed
exactly with sympy: col j = skew(P_j Rz(alpha) E S_j), E = dRx(+-pi).
Result: even columns (t,t,0), t=1/sqrt(2); odd columns (1,0,0).
Hence J u = 0 with u = D_s v reads: sum over evens s_i v_i = 0 AND sum
over odds s_i v_i = 0. A strictly positive v exists iff s is mixed on
both parities. Also verifies F^2 = I and F^8 = I exactly.
"""
import sympy as sp

t = sp.sqrt(2) / 2
Rz = sp.Matrix([[t, -t, 0], [t, t, 0], [0, 0, 1]])
D = sp.diag(1, -1, -1)
F = Rz * D
print("F =")
sp.pprint(F)
print("F^2 - I =", (F * F - sp.eye(3)))
assert F * F == sp.eye(3)
print("F^8 - I =", (F**8 - sp.eye(3)))
assert F**8 == sp.eye(3)

E = sp.Matrix([[0, 0, 0], [0, 0, 1], [0, -1, 0]])  # dRx(pi) = dRx(-pi)


def ax(M):
    return sp.Matrix([M[2, 1] - M[1, 2], M[0, 2] - M[2, 0], M[1, 0] - M[0, 1]]) / 2


I3 = sp.eye(3)
cols = []
for j in range(8):
    dC = (F**j) * Rz * E * (F**(7 - j))
    c = sp.simplify(ax(dC))
    cols.append(tuple(c))
    print("col", j, "=", tuple(c))
for j in (0, 2, 4, 6):
    assert cols[j] == (sp.sqrt(2) / 2, sp.sqrt(2) / 2, 0), cols[j]
for j in (1, 3, 5, 7):
    assert cols[j] == (1, 0, 0), cols[j]
print("JACOBIAN PARITY STRUCTURE VERIFIED EXACTLY")
print("First-order system J D_s v = 0, v > 0  <=>  "
      "sum_{even} s_i v_i = 0 and sum_{odd} s_i v_i = 0.")
print("Strictly positive solution exists iff s takes both signs on evens "
      "and both signs on odds (mixed-parity criterion).")
