"""Symmetric dual certificate for Waldschmidt constant of M4: construct exact
rational dual solution y on the 16 minimal covers with value 29/19, and
verify strong duality pairing with primal x=(3/19,2/19,4/19)(V,U,w classes).

Primal (fractional cover): min sum x_v s.t. sum_{v in C} x_v >= 1 for all 16 covers.
Dual (fractional packing): max sum_C y_C s.t. sum_{C ni v} y_C <= 1 for all v.
By symmetry, set y constant per orbit type under D5 action on indices:
  A: (3,3,1) 5 covers; B: (3,5,0) 5 covers; C: (4,2,1) 5 covers; D: (5,0,1) 1 cover.
Incidence counts:
  A: complements of {v_i,v_k,u_j? ...} -> need exact per-vertex-type incidence per orbit.
Compute incidence by averaging: for orbit T with n_T covers: total V-slots = n_T*nv(T),
shared equally among 5 V-vertices => per-V load n_T*nv/5, similarly per-U, w.
Then solve symmetric dual LP exactly and verify <= 1 slacks and value 29/19.
"""
import sys
sys.path.insert(0, ".")
from fractions import Fraction
from m4_data import COVERS, ctype

# Group covers by type
groups = {}
for C in COVERS:
    groups.setdefault(ctype(C), []).append(set(C))
for t in sorted(groups):
    print(t, "count", len(groups[t]))

# Per-vertex incidence under full dihedral symmetry on 5 indices: check each
# vertex class has uniform load within orbit.
for t, Cs in sorted(groups.items()):
    for cls, verts in [("V", range(0, 5)), ("U", range(5, 10)), ("w", [10])]:
        loads = {v: sum(1 for C in Cs if v in C) for v in verts}
        assert len(set(loads.values())) == 1, (t, cls, loads)
        print(f"  type {t}: per-{cls}-vertex incidence = {list(loads.values())[0]}")

# Symmetric dual variables: a,b,c,d = weight per cover of type A,B,C,D
# Per-V load: (3a+3b+4c+5d ... each multiplied by count/5?) Let's just directly:
# per-V load = (3*5 a? no: per-vertex incidence of A on V = 3 (since 15 slots/5))
# from printout: compute programmatically.
import itertools

Tlist = sorted(groups)  # [A,B,C,D]
inc = {}  # inc[T][cls] = per-vertex incidence
for t, Cs in groups.items():
    inc[t] = {}
    for cls, verts in [("V", range(0, 5)), ("U", range(5, 10)), ("w", [10])]:
        loads = {v: sum(1 for C in Cs if v in C) for v in verts}
        inc[t][cls] = loads[verts[0]]

# counts
cnt = {t: len(groups[t]) for t in Tlist}
print("incidence:", inc)
print("counts:", cnt)

# Dual: max 5a+5b+5c+d s.t. (per-vertex incidences from table above)
#   V: 3a+3b+4c+1d <= 1
#   U: 3a+5b+2c+0d <= 1
#   w: 5a+0b+5c+1d <= 1, a,b,c,d >= 0
planes = [
    ([Fraction(3), Fraction(3), Fraction(4), Fraction(1)], Fraction(1)),  # V
    ([Fraction(3), Fraction(5), Fraction(2), Fraction(0)], Fraction(1)),  # U
    ([Fraction(5), Fraction(0), Fraction(5), Fraction(1)], Fraction(1)),  # w
    ([Fraction(1), Fraction(0), Fraction(0), Fraction(0)], Fraction(0)),  # a>=0
    ([Fraction(0), Fraction(1), Fraction(0), Fraction(0)], Fraction(0)),  # b>=0
    ([Fraction(0), Fraction(0), Fraction(1), Fraction(0)], Fraction(0)),  # c>=0
    ([Fraction(0), Fraction(0), Fraction(0), Fraction(1)], Fraction(0)),  # d>=0
]


def det4(M):
    # Laplace expansion
    def det3(r):
        (a, b, c), (d, e, f), (g, h, i) = r
        return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)

    D = Fraction(0)
    for j in range(4):
        minor = [[M[r][k] for k in range(4) if k != j] for r in range(1, 4)]
        D += ((-1) ** j) * M[0][j] * det3(minor)
    return D


def solve4(M, rhs):
    D = det4(M)
    if D == 0:
        return None
    out = []
    for col in range(4):
        Mm = [list(r) for r in M]
        for r in range(4):
            Mm[r][col] = rhs[r]
        out.append(det4(Mm) / D)
    return out


best = None
bestpt = None
bestcombo = None
P = len(planes)
for combo in itertools.combinations(range(P), 4):
    M = [planes[k][0] for k in combo]
    rhs = [planes[k][1] for k in combo]
    sol = solve4(M, rhs)
    if sol is None:
        continue
    ok = True
    for k in range(P):
        lhs = sum(planes[k][0][j] * sol[j] for j in range(4))
        if k <= 2:
            if lhs > planes[k][1]:
                ok = False
                break
        else:
            if lhs < planes[k][1]:
                ok = False
                break
    if not ok:
        continue
    val = 5 * sol[0] + 5 * sol[1] + 5 * sol[2] + sol[3]
    if best is None or val > best:
        best = val
        bestpt = sol
        bestcombo = combo
print("symmetric dual optimum:", best, "=", float(best))
print("at (a,b,c,d) =", bestpt, "combo", bestcombo)

# Full (non-symmetric) feasibility check: expand to 16 covers and verify all 11 slacks.
names = []
y = {}
for t, var in zip(Tlist, bestpt):
    for C in groups[t]:
        y[tuple(sorted(C))] = var
for v in range(11):
    load = sum(w for C, w in y.items() if v in C)
    print(f"  vertex {v}: load {load} {'OK' if load <= 1 else 'VIOLATION'}")
print("dual value:", sum(y.values()))

# Complementary slackness checks against primal x*=(3/19 V, 2/19 U, 4/19 w):
x = {v: Fraction(3, 19) for v in range(5)}
x.update({v: Fraction(2, 19) for v in range(5, 10)})
x[10] = Fraction(4, 19)
print("primal value:", sum(x.values()))
for C in COVERS:
    print("  ", ctype(C), "cover-sum:", sum(x[v] for v in C))
