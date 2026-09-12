#!/usr/bin/env python3
"""Lane 1101 verification: sharp local dichotomy for rank-zero points in dim 4.

Part A: conformal germ pi_c = f*(d1^d2), f = |x|^2 on R^4.
  A1: Schouten [pi_c,pi_c] = 0.
  A2: Xc(0) = 0; A3: linearization DXc(0) != 0.
  A4: every coordinate Hamiltonian divisible by f (order >= 2).
  A5: structural 1-jet obstruction (see DRAFT.md).
Part B (germ J): C1 = x1*x3 + x2*x4, C2 = (x1^2+x2^2-x3^2-x4^2)/2,
  pi^{ij} = sum_{k,l} eps_{ijkl} dC1_k dC2_l.
  J1-J6: Jacobi, Casimirs, pencil det (s^2+t^2)^2, isolation pi13+pi24=|x|^2,
  identically zero modular field, vanishing 1-jet.
Exact rational arithmetic (sympy). Prints VERIFY_OK on success.
"""
import sympy as sp
import itertools

x1, x2, x3, x4 = sp.symbols('x1 x2 x3 x4')
X = [x1, x2, x3, x4]
s, t = sp.symbols('s t')


def check(name, cond):
    assert cond, f"FAIL: {name}"
    print(f"  ok: {name}")


def build_P(comps):
    P = sp.zeros(4)
    for (i, j), e in comps.items():
        P[i, j] = e
        P[j, i] = -e
    return sp.Matrix([[sp.expand(build_P_cell(P, i, j)) for j in range(4)]
                      for i in range(4)])


def build_P_cell(P, i, j):
    return P[i, j]


print("== Part A: conformal germ ==")
f = x1**2 + x2**2 + x3**2 + x4**2
Pc = build_P({(0, 1): f})


def schouten_up(P):
    out = {}
    for (i, j, k) in itertools.combinations(range(4), 3):
        val = 0
        for ell in range(4):
            val += (P[ell, i]*sp.diff(P[j, k], X[ell])
                    + P[ell, j]*sp.diff(P[k, i], X[ell])
                    + P[ell, k]*sp.diff(P[i, j], X[ell]))
        out[(i, j, k)] = sp.expand(val)
    return out


SA = schouten_up(Pc)
for key, val in SA.items():
    check(f"A1 Schouten {key} = 0", val == 0)
Xc = [sp.expand(sum(sp.diff(Pc[i, j], X[i]) for i in range(4))) for j in range(4)]
print(f"  Xc = {Xc}")
check("A2 Xc(0)=0",
      all(c.subs({x1: 0, x2: 0, x3: 0, x4: 0}) == 0 for c in Xc))
J = [[sp.diff(Xc[i], X[j]).subs({x1: 0, x2: 0, x3: 0, x4: 0})
      for j in range(4)] for i in range(4)]
print(f"  DXc(0) = {J}")
check("A3 linearization DXc(0) != 0",
      any(J[i][j] != 0 for i in range(4) for j in range(4)))
for m in range(4):
    Xh = [sp.expand(Pc[i, m]) for i in range(4)]
    for i in range(4):
        q, r = sp.div(sp.Poly(Xh[i], X), sp.Poly(f, X))
        check(f"A4 Hamiltonian-of-x{m+1} comp {i+1} divisible by f", r == 0)
print("  (A5) structural: X^c_g = f*X^0_g so all Hamiltonians are O(|x|^2);")
print("  a nonzero 1-jet of Xc can never be cancelled -> [Xc] != 0, no")
print("  invariant volume near 0 for any volume choice.")

print("== Part B: Jacobian unimodular germ ==")
C1 = x1*x3 + x2*x4
C2 = (x1**2 + x2**2 - x3**2 - x4**2)/2
dC1 = [sp.diff(C1, v) for v in X]
dC2 = [sp.diff(C2, v) for v in X]


def eps4(i, j, k, l):
    p = (i, j, k, l)
    if len(set(p)) < 4:
        return 0
    inv = 0
    for a in range(4):
        for b in range(a+1, 4):
            if p[a] > p[b]:
                inv += 1
    return 1 if inv % 2 == 0 else -1


P = sp.zeros(4)
for i in range(4):
    for j in range(4):
        P[i, j] = sum(eps4(i, j, k, l)*dC1[k]*dC2[l]
                      for k in range(4) for l in range(4))
P = sp.Matrix([[sp.expand(P[i, j]) for j in range(4)] for i in range(4)])
assert all(sp.expand(P[i, j] + P[j, i]) == 0 for i in range(4) for j in range(4))

print("-- J1 Jacobi --")
SJ = schouten_up(P)
for key, val in SJ.items():
    check(f"J1 Schouten {key} = 0", val == 0)

print("-- J2 Casimirs --")
for m, Cm in enumerate([C1, C2]):
    dC = [sp.diff(Cm, X[j]) for j in range(4)]
    img = [sp.expand(sum(P[i, j]*dC[j] for j in range(4))) for i in range(4)]
    check(f"J2 C{m+1} Casimir pi^#(dC{m+1})=0", all(v == 0 for v in img))

print("-- J3 pencil --")
A = sp.hessian(C1, X)
B = sp.hessian(C2, X)
M = s*A + t*B
detMt = sp.expand(M.det())
check("J3 det(sA+tB) = (s^2+t^2)^2", sp.expand(detMt - (s**2 + t**2)**2) == 0)
print(f"  det = {detMt}")

print("-- J4 isolated zero --")
comps = [sp.expand(P[i, j]) for i in range(4) for j in range(i+1, 4)]
idx = {(a, b): k for k, (a, b) in
       enumerate([(a, b) for a in range(4) for b in range(a+1, 4)])}
print(f"  nonzero components: {[str(c) for c in comps if c != 0]}")
norm = x1**2 + x2**2 + x3**2 + x4**2
sos = sp.expand(comps[idx[(0, 2)]] + comps[idx[(1, 3)]] - norm)
check("J4 pi13+pi24 = |x|^2 (real zero set is exactly {0})", sos == 0)
pt = {x1: 1, x2: 0, x3: 0, x4: 0}
check("J4 pi(1,0,0,0) != 0", any(c.subs(pt) != 0 for c in comps))
print("  (rank off origin is exactly 2: Casimirs force rank <= 2,")
print("  pi != 0 forces rank >= 2 for a skew matrix.)")

print("-- J5 unimodular --")
Xmod = [sp.expand(sum(sp.diff(P[i, j], X[i]) for i in range(4))) for j in range(4)]
check("J5 modular field identically zero", all(v == 0 for v in Xmod))
print(f"  Xmod = {Xmod}")

print("-- J6 vanishing 1-jet --")
pairs = [(a, b) for a in range(4) for b in range(a+1, 4)]
for (i, j) in pairs:
    c = comps[pairs.index((i, j))]
    lin = sum(sp.diff(c, X[k]).subs({x1: 0, x2: 0, x3: 0, x4: 0})*X[k]
              for k in range(4))
    check(f"J6 1-jet of pi^{i+1}{j+1} vanishes", sp.expand(lin) == 0)

print("VERIFY_OK")
