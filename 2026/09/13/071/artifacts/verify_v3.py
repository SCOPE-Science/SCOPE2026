"""Exact verification for lane-1788: V_3 of the De Laet quotient Q = T_1.

Zero-dependency check over the Eisenstein integers Z[w]/(w^2+w+1).
An element is a pair (a,b) meaning a + b*w with integers a,b.

Checks:
  A. cubic term tables and their C_i restrictions (E_i equations);
  B. D_i components lie in V_3 (per-monomial zero-factor check);
  C. the point P=(q1,q0,q1) satisfies all V_3 equations;
  D. component membership of P (only E_0 and D_1 contain it);
  E. full pairwise incidence (K_{3,3} minus matching) with equation check;
  F. affine-chart Jacobian at P: linear parts, 4x4 minor = +/-1, rank 4,
     tangent dimension 2 > local dimension 1 (singularity certificate).
"""

import sys

# ---------- Eisenstein integers ----------
O = lambda a, b: (a, b)
ZERO = (0, 0)
ONE = (1, 0)
W = (0, 1)          # primitive cube root of unity, w^2 + w + 1 = 0
W2 = (-1, -1)       # w^2 = -1 - w


def add(p, q):
    return (p[0] + q[0], p[1] + q[1])


def neg(p):
    return (-p[0], -p[1])


def mul(p, q):
    a, b = p
    c, d = q
    return (a * c - b * d, a * d + b * c - b * d)


def eq(p, q):
    return p[0] == q[0] and p[1] == q[1]


assert eq(add(add(mul(W, W), W), ONE), ZERO)  # w^2+w+1=0 sanity

out = []


def log(s=""):
    out.append(s)


# ---------- cubic relations (t = 1), Table 1 ----------
# each term: (coeff, ((var, pos), ...)) with pos in {0,1,2}
F1 = [
    (ONE, (("Z", 0), ("X", 1), ("Y", 2))),
    (W, (("X", 0), ("Y", 1), ("Z", 2))),
    (W2, (("Y", 0), ("Z", 1), ("X", 2))),
    (ONE, (("Y", 0), ("X", 1), ("Z", 2))),
    (W, (("Z", 0), ("Y", 1), ("X", 2))),
    (W2, (("X", 0), ("Z", 1), ("Y", 2))),
]
F2 = [
    (ONE, (("Z", 0), ("X", 1), ("Y", 2))),
    (W2, (("X", 0), ("Y", 1), ("Z", 2))),
    (W, (("Y", 0), ("Z", 1), ("X", 2))),
    (ONE, (("Y", 0), ("X", 1), ("Z", 2))),
    (W2, (("Z", 0), ("Y", 1), ("X", 2))),
    (W, (("X", 0), ("Z", 1), ("Y", 2))),
]

# points and lines
QPT = [
    {"X": 1, "Y": 0, "Z": 0},  # q0
    {"X": 0, "Y": 1, "Z": 0},  # q1
    {"X": 0, "Y": 0, "Z": 1},  # q2
]
LINE_ZERO = ["X", "Y", "Z"]  # L_i = V(coord i)


def eval_cubic(terms, pts):
    """Evaluate cubic sum at a triple of points (int coords -> Eisenstein)."""
    tot = ZERO
    for c, facs in terms:
        m = c
        for v, i in facs:
            m = mul(m, (pts[i][v], 0))
        tot = add(tot, m)
    return tot


# ---------- B. D_j containment: every monomial has a zero factor ----------
# D_0 = {q0} x L0 x {q0}: zeros {Y0,Z0,X1,Y2,Z2}
# D_1 = {q1} x L1 x {q1}: zeros {X0,Z0,Y1,X2,Z2}
# D_2 = {q2} x L2 x {q2}: zeros {X0,Y0,Z1,X2,Y2}
DZERO = [
    {("Y", 0), ("Z", 0), ("X", 1), ("Y", 2), ("Z", 2)},
    {("X", 0), ("Z", 0), ("Y", 1), ("X", 2), ("Z", 2)},
    {("X", 0), ("Y", 0), ("Z", 1), ("X", 2), ("Y", 2)},
]
log("B. D_j containment in V_3 (zero-factor per monomial):")
for j in range(3):
    ok = all(
        any(f in DZERO[j] for f in facs) for _, facs in F1
    ) and all(any(f in DZERO[j] for f in facs) for _, facs in F2)
    log("  D_%d: all 12 monomials vanish: %s" % (j, ok))
    assert ok

# ---------- A. C_i restrictions ----------
# C_0 = L0 x {q0} x L0: zeros {X0,Y1,Z1,X2}; free ends in (Y,Z), X1=1
# C_1 = L1 x {q1} x L1: zeros {Y0,X1,Z1,Y2}; free ends in (X,Z), Y1=1
# C_2 = L2 x {q2} x L2: zeros {Z0,X1,Y1,Z2}; free ends in (X,Y), Z1=1
CZERO = [
    {("X", 0), ("Y", 1), ("Z", 1), ("X", 2)},
    {("Y", 0), ("X", 1), ("Z", 1), ("Y", 2)},
    {("Z", 0), ("X", 1), ("Y", 1), ("Z", 2)},
]


def restrict(terms, zeros):
    """Return sorted residual (coeff, factors) after killing zero-factor terms."""
    res = []
    for c, facs in terms:
        if any(f in zeros for f in facs):
            continue
        res.append((c, tuple(sorted(facs))))
    return sorted(res)


log("A. C_i restrictions:")
r = restrict(F1, CZERO[0])
log("  f1|C_0 = %s" % (r,))
assert r == sorted([(ONE, (("X", 1), ("Y", 2), ("Z", 0))),
                    (ONE, (("X", 1), ("Y", 0), ("Z", 2)))])
r = restrict(F2, CZERO[0])
assert r == sorted([(ONE, (("X", 1), ("Y", 2), ("Z", 0))),
                    (ONE, (("X", 1), ("Y", 0), ("Z", 2)))])
log("  f1|C_0 = f2|C_0 = Z0*Y2 + Y0*Z2  ->  E_0: V(Y0Z2+Z0Y2), smooth (1,1).")
r1 = restrict(F1, CZERO[1])
log("  f1|C_1 = %s" % (r1,))
assert r1 == sorted([(W, (("X", 0), ("Y", 1), ("Z", 2))),
                     (W, (("X", 2), ("Y", 1), ("Z", 0)))])
r2 = restrict(F2, CZERO[1])
assert r2 == sorted([(W2, (("X", 0), ("Y", 1), ("Z", 2))),
                     (W2, (("X", 2), ("Y", 1), ("Z", 0)))])
log("  f1|C_1 = w*(X0Z2+Z0X2), f2|C_1 = w^2*(X0Z2+Z0X2)  ->  E_1.")
r1 = restrict(F1, CZERO[2])
log("  f1|C_2 = %s" % (r1,))
assert r1 == sorted([(W2, (("X", 0), ("Y", 2), ("Z", 1))),
                     (W2, (("X", 2), ("Y", 0), ("Z", 1)))])
r2 = restrict(F2, CZERO[2])
assert r2 == sorted([(W, (("X", 0), ("Y", 2), ("Z", 1))),
                     (W, (("X", 2), ("Y", 0), ("Z", 1)))])
log("  f1|C_2 = w^2*(Y0X2+X0Y2), f2|C_2 = w*(Y0X2+X0Y2)  ->  E_2.")

# ---------- C. P = (q1,q0,q1) satisfies everything ----------
P = (QPT[1], QPT[0], QPT[1])
QUADS = [(("X", 0), ("X", 1)), (("Y", 0), ("Y", 1)), (("Z", 0), ("Z", 1)),
         (("X", 1), ("X", 2)), (("Y", 1), ("Y", 2)), (("Z", 1), ("Z", 2))]
log("C. P = (q1,q0,q1) on V_3:")
for v, i, j in [(a, b, c) for (a, b), (c, d) in [] ]:
    pass
for (a, i), (b, j) in QUADS:
    assert P[i][a] * P[j][b] == 0
log("  all 6 pair quadrics vanish: True")
assert eq(eval_cubic(F1, P), ZERO) and eq(eval_cubic(F2, P), ZERO)
log("  f1(P) = f2(P) = 0: True")

# ---------- D. only E_0 and D_1 contain P ----------
# E_i: middle must be q_i and ends in L_i and bilinear eq holds.
# D_j: ends must be q_j and middle in L_j.
BILIN = [
    lambda A, C: A["Y"] * C["Z"] + A["Z"] * C["Y"],  # E_0
    lambda A, C: A["X"] * C["Z"] + A["Z"] * C["X"],  # E_1
    lambda A, C: A["X"] * C["Y"] + A["Y"] * C["X"],  # E_2
]
log("D. component membership of P:")
for i in range(3):
    mid_ok = (P[1] == QPT[i])
    ends_ok = (P[0][LINE_ZERO[i]] == 0 and P[2][LINE_ZERO[i]] == 0)
    eq_ok = (BILIN[i](P[0], P[2]) == 0)
    member = mid_ok and ends_ok and eq_ok
    log("  P in E_%d: mid_ok=%s ends_ok=%s eq=%s -> %s"
        % (i, mid_ok, ends_ok, eq_ok, member))
    assert member == (i == 0)
for j in range(3):
    ends_ok = (P[0] == QPT[j] and P[2] == QPT[j])
    mid_ok = (P[1][LINE_ZERO[j]] == 0)
    member = ends_ok and mid_ok
    log("  P in D_%d: ends_ok=%s mid_ok=%s -> %s" % (j, ends_ok, mid_ok, member))
    assert member == (j == 1)

# ---------- E. incidence: E_i -- D_j iff i != j ----------
log("E. pairwise incidence:")
for i in range(3):
    for j in range(3):
        if i == j:
            # middles: q_i vs L_i (q_i not in L_i) -> empty
            assert QPT[i][LINE_ZERO[i]] != 0
            log("  E_%d cap D_%d = empty (middle q_%d not in L_%d): True"
                % (i, j, i, j))
        else:
            cand = (QPT[j], QPT[i], QPT[j])
            inC = (cand[1] == QPT[i] and cand[0][LINE_ZERO[i]] == 0
                   and cand[2][LINE_ZERO[i]] == 0)
            inD = (cand[0] == QPT[j] and cand[2] == QPT[j]
                   and cand[1][LINE_ZERO[j]] == 0)
            onE = (BILIN[i](cand[0], cand[2]) == 0)
            assert inC and inD and onE
            log("  E_%d cap D_%d = {(q_%d,q_%d,q_%d)} (bilinear=%d): True"
                % (i, j, j, i, j, BILIN[i](cand[0], cand[2])))
# E_i cap E_j empty (middles differ), D_i cap D_j empty (ends differ)
for i in range(3):
    for j in range(i + 1, 3):
        assert QPT[i] != QPT[j]
log("  E_i cap E_j = empty (i!=j, middles q_i!=q_j): True")
log("  D_i cap D_j = empty (i!=j, ends q_i!=q_j): True")
log("  incidence graph = K_{3,3} minus perfect matching: CONNECTED.")

# ---------- F. Jacobian at P in chart Y0=X1=Y2=1 ----------
# chart vars: a0=X0 c0=Z0 b1=Y1 c1=Z1 a2=X2 c2=Z2 ; Y0=X1=Y2=1
VARS = ["a0", "b1", "c0", "c1", "a2", "c2"]


def sub(term):
    """Rewrite a cubic ((var,pos)) triple into chart monomial (coeff, varlist)."""
    c, facs = term
    vl = []
    for v, i in facs:
        if (v, i) == ("Y", 0) or (v, i) == ("X", 1) or (v, i) == ("Y", 2):
            continue  # chart 1s
        vl.append({"X": "a", "Y": "b", "Z": "c"}[v] + str(i))
    return (c, tuple(sorted(vl)))


GENS = [  # (name, Eisenstein-poly as list of (coeff, varlist))
    ("X0X1", [(ONE, ("a0",))]),
    ("Y0Y1", [(ONE, ("b1",))]),
    ("Z0Z1", [(ONE, ("c0", "c1"))]),
    ("X1X2", [(ONE, ("a2",))]),
    ("Y1Y2", [(ONE, ("b1",))]),
    ("Z1Z2", [(ONE, ("c1", "c2"))]),
    ("F1", [sub(t) for t in F1]),
    ("F2", [sub(t) for t in F2]),
]
log("F. chart Jacobian at P (vars a0,b1,c0,c1,a2,c2):")
linrows = {}
for name, poly in GENS:
    const = ZERO
    lin = {v: ZERO for v in VARS}
    for c, vl in poly:
        if len(vl) == 0:
            const = add(const, c)
        elif len(vl) == 1:
            lin[vl[0]] = add(lin[vl[0]], c)
    assert eq(const, ZERO), name  # P lies on the scheme
    linrows[name] = [lin[v] for v in VARS]
    log("  d(%s)|_P = %s" % (name, [(VARS[k], linrows[name][k])
                                    for k in range(6)
                                    if not eq(linrows[name][k], ZERO)] or ["zero"]))
e = lambda p: "0" if eq(p, ZERO) else ("1" if eq(p, ONE) else ("w" if eq(p, W) else ("w2" if eq(p, W2) else str(p))))
assert [e(p) for p in linrows["X0X1"]] == ["1", "0", "0", "0", "0", "0"]
assert [e(p) for p in linrows["Y0Y1"]] == ["0", "1", "0", "0", "0", "0"]
assert [e(p) for p in linrows["X1X2"]] == ["0", "0", "0", "0", "1", "0"]
assert [e(p) for p in linrows["F1"]] == ["0", "0", "1", "0", "0", "1"]
assert [e(p) for p in linrows["F2"]] == ["0", "0", "1", "0", "0", "1"]
assert all(eq(p, ZERO) for p in linrows["Z0Z1"])
assert all(eq(p, ZERO) for p in linrows["Z1Z2"])
log("  4x4 minor (rows X0X1,Y0Y1,F1,X1X2; cols a0,b1,c0,a2) = identity, det = +/-1.")
log("  rows Z0Z1, Z1Z2 are zero; row F2 = row F1; Y1Y2 duplicates Y0Y1.")
log("  rank = 4 exactly; tangent dim = 6 - 4 = 2 > local dim 1: P SINGULAR.")
log("  P lies on exactly two components (E_0, D_1), both smooth curves: done.")

log("")
log("ALL EXACT CHECKS PASSED.")

with open("verify_results.txt", "w") as f:
    f.write("\n".join(out) + "\n")
print("\n".join(out))
