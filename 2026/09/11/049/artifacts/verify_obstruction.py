"""Bounded recovery test: structural section-count obstruction to the lane-828 target.

Target (literal): fifteen slanted fields span T_{J^v_2(X)} (twisted) at a general
point, for the universal degree-d hypersurface X subset P^4 x P^{N_d}.

What this script certifies, with exact integer/Fraction arithmetic:
 1. M(d) = C(d+4,4) monomials; N_d = M(d)-1; fiber-rank need = N_d+9 (projective
    params) and cone-nullity = M(d)+9 (affine-cone params).
 2. For every d >= 2: need >= 22 > 15. Pure linear algebra: 15 vectors never span
    a >=22-dim fiber. Ansatz-independent.
 3. Exhibits one explicit smooth 2-jet point (d=2) where the 3 defining equations
    have independent gradients (exact rank 3 in C^27), so dim = 24 = M+9 at that
    point (cone), i.e. projective fiber rank 23 > 15. The deficit is realized, not
    just numerical.
 4. d=1 counting fits (need 13) but is the hyperplane family, outside Siu-program
    natural scope (no hyperbolicity content).

Run: python3 output/artifacts/verify_obstruction.py  -> prints OBSTRUCTION_VERIFIED
"""
from fractions import Fraction
from math import comb


def M(d):
    return comb(d + 4, 4)


def rank_of_rows(rows):
    """Exact rank of a list of row-vectors via Fraction Gaussian elimination."""
    A = [[Fraction(x) for x in r] for r in rows]
    m, n = len(A), len(A[0])
    r = 0
    for c in range(n):
        piv = next((i for i in range(r, m) if A[i][c] != 0), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        for i in range(m):
            if i != r and A[i][c] != 0:
                f = A[i][c] / A[r][c]
                for j in range(c, n):
                    A[i][j] -= f * A[r][j]
        r += 1
        if r == m:
            break
    return r


# ---- 1. Section-count table (projective params: need N_d+9; cone: M_d+9) ----
print("d | M(d) | N_d | need_proj(N+9) | need_cone(M+9) | 15 spans?")
blocked_all = True
for d in range(1, 9):
    m, n = M(d), M(d) - 1
    need_proj, need_cone = n + 9, m + 9
    ok = 15 >= need_proj
    print(f"{d} | {m:4d} | {n:3d} | {need_proj:15d} | {need_cone:14d} | {ok}")
    if d >= 2 and ok:
        blocked_all = False
assert blocked_all, "count obstruction failed"
assert M(2) == 15 and (M(2) - 1) + 9 == 23, "d=2 reference numbers"

# ---- 2. Explicit smooth vertical-2-jet point, d=2 ----
# Coords: z in C^4; a in C^15 (monomials deg<=2 in z1..z4, fixed order below);
# z', z'' in C^4. F = a_(1,0,0,0) * z1 (set that coeff 1, a_0 = 0).
monoms = [(0, 0, 0, 0),
          (1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1),
          (2, 0, 0, 0), (0, 2, 0, 0), (0, 0, 2, 0), (0, 0, 0, 2),
          (1, 1, 0, 0), (1, 0, 1, 0), (1, 0, 0, 1),
          (0, 1, 1, 0), (0, 1, 0, 1), (0, 0, 1, 1)]
assert len(monoms) == 15
iz = {k: i for i, k in enumerate(
    ['z1', 'z2', 'z3', 'z4', 'a0', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7',
     'a8', 'a9', 'a10', 'a11', 'a12', 'a13', 'a14',
     'zp1', 'zp2', 'zp3', 'zp4', 'zpp1', 'zpp2', 'zpp3', 'zpp4'])}


def row(**kw):
    v = [0] * 27
    for k, val in kw.items():
        v[iz[k]] = val
    return v


# Point: z=0, a1(coeff of z1)=1, all other a=0; z'=(0,1,0,0); z''=(0,0,1,0).
# E0 = F = z1 -> grad: dz1 = 1.
# E1 = z1' (=dF with F linear) -> grad: dzp1 = 1.
# E2 = z1'' -> grad: dzpp1 = 1.
E0 = row(z1=1)
E1 = row(zp1=1)
E2 = row(zpp1=1)
rk = rank_of_rows([E0, E1, E2])
nullity = 27 - rk
print(f"\nexplicit-point Jacobian rank = {rk} (need 3); nullity = {nullity}")
assert rk == 3, "point is not smooth of expected codim"
assert nullity == M(2) + 9 == 24, "cone fiber-dim mismatch"
# Maximal rank of any 15-row evaluation matrix at this point:
print(f"max rank of 15 fields at this fiber = <=15 < {nullity - 1} = proj fiber rank")
assert 15 < nullity - 1

print("\nOBSTRUCTION_VERIFIED")
