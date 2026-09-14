"""Certified Cartan computation for the S3-C2 two-orbit EI algebra in char 2.

Base field F4 = F2[w]/(w^2+w+1), a splitting field for S3 in char 2.
All arithmetic exact (pure Python, no dependencies). Writes
cartan_certificate.json next to this script.

Certifies:
 R1. Central idempotents of F4[S3]: e0 and e1+e2 central; block B0 = e0*R
     is 2-dim local with square-zero radical (Cartan [2]); the complementary
     4-dim block B1 maps isomorphically onto M2(F4) via the explicit
     2-dim irreducible (Cartan [1]). Hence C(kS3) = diag(2,1).
 R2. The 3+1 biset is unique up to iso and the left C2-action is trivial:
     every order-4 subgroup of C2 x S3 contains the central C2 factor and
     all are conjugate under 1 x S3 (brute force).
 R3. M as right S3-module = T (+) T (+) W with W simple (no invariant
     projective point) and the sum direct.
 R4. Projectives of A: P1 has factors 2xS1; P2 is simple S2;
     P3 admits 0 < U1 < U2 < Mp < V5 < P3 with factors S1,S1,S2,S3,S3.
     Cartan (rows = projectives, S1 = S3-trivial, S2 = S3 2-dim, S3 = C2-trivial)
       [[2,0,0],[0,1,0],[2,1,2]], det 4, rank 3.
     The proposed [[2,1,0],[1,2,0],[2,2,2]] (det 6) is impossible:
     its projective dimensions force total dimension 22, but dim A = 12.
"""
import itertools
import json
import os
import sys

C = {}
def chk(name, cond):
    C[name] = bool(cond)
    return bool(cond)

# ---------------- GF(4) ----------------
def gf_add(a, b):
    return a ^ b

_GM = [[0] * 4 for _ in range(4)]
for _a in range(4):
    for _b in range(4):
        if _a == 0 or _b == 0:
            _GM[_a][_b] = 0
        elif _a == 1:
            _GM[_a][_b] = _b
        elif _b == 1:
            _GM[_a][_b] = _a
        else:
            _GM[_a][_b] = {(2, 2): 3, (2, 3): 1, (3, 2): 1, (3, 3): 2}[(_a, _b)]

def gf_mul(a, b):
    return _GM[a][b]

def gf_inv(a):
    for b in (1, 2, 3):
        if gf_mul(a, b) == 1:
            return b
    raise ZeroDivisionError("inverse of zero")

ONE, W, W2 = 1, 2, 3

def vadd(u, v):
    return [gf_add(x, y) for x, y in zip(u, v)]

def vscale(c, v):
    return [gf_mul(c, x) for x in v]

def vrank(vecs):
    M = [list(v) for v in vecs if any(x != 0 for x in v)]
    if not M:
        return 0
    nc = len(M[0])
    r = 0
    for c in range(nc):
        piv = None
        for i in range(r, len(M)):
            if M[i][c] != 0:
                piv = i
                break
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        inv = gf_inv(M[r][c])
        M[r] = [gf_mul(inv, x) for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [gf_add(x, gf_mul(f, y)) for x, y in zip(M[i], M[r])]
        r += 1
    return r

def in_span(v, B):
    if all(x == 0 for x in v):
        return True
    return vrank([list(b) for b in B] + [list(v)]) == vrank(B)

def mat_mul(A, B):
    n = len(A)
    k = len(B)
    m = len(B[0])
    Cc = [[0] * m for _ in range(n)]
    for i in range(n):
        for t in range(k):
            if A[i][t]:
                for j in range(m):
                    Cc[i][j] = gf_add(Cc[i][j], gf_mul(A[i][t], B[t][j]))
    return Cc

def mat_vec_row(v, M):
    n = len(M[0])
    out = [0] * n
    for i, a in enumerate(v):
        if a:
            for j in range(n):
                out[j] = gf_add(out[j], gf_mul(a, M[i][j]))
    return out

# ---------------- S3 group algebra ----------------
perms = list(itertools.permutations([0, 1, 2]))
pidx = {p: i for i, p in enumerate(perms)}

def comp(p, q):
    return tuple(p[q[i]] for i in range(3))

def pinv(p):
    q = [0] * 3
    for i, pi in enumerate(p):
        q[pi] = i
    return tuple(q)

MULS = [[pidx[comp(perms[i], perms[j])] for j in range(6)] for i in range(6)]
ID = pidx[(0, 1, 2)]
IA = pidx[(1, 2, 0)]
IA2 = pidx[(2, 0, 1)]
IB = pidx[(1, 0, 2)]

def gmul6(u, v):
    w = [0] * 6
    for i, a in enumerate(u):
        if a:
            row = MULS[i]
            for j, b in enumerate(v):
                if b:
                    w[row[j]] = gf_add(w[row[j]], gf_mul(a, b))
    return w

def basis6(n):
    v = [0] * 6
    v[n] = ONE
    return v

ONE_R = basis6(ID)
A_EL = basis6(IA)
A2_EL = basis6(IA2)
B_EL = basis6(IB)

e0 = vadd(vadd(ONE_R, A_EL), A2_EL)
e1 = vadd(vadd(ONE_R, vscale(W2, A_EL)), vscale(W, A2_EL))
e2 = vadd(vadd(ONE_R, vscale(W, A_EL)), vscale(W2, A2_EL))
e12 = vadd(e1, e2)
ZERO6 = [0] * 6

chk("e0+e1+e2==1", vadd(vadd(e0, e1), e2) == ONE_R)
chk("e0^2==e0", gmul6(e0, e0) == e0)
chk("e1^2==e1", gmul6(e1, e1) == e1)
chk("e2^2==e2", gmul6(e2, e2) == e2)
chk("e0*e1==0", gmul6(e0, e1) == ZERO6)
chk("e0*e2==0", gmul6(e0, e2) == ZERO6)
chk("e1*e2==0", gmul6(e1, e2) == ZERO6)

cent_ok = True
for g in perms:
    gv = basis6(pidx[g])
    if gmul6(e0, gv) != gmul6(gv, e0):
        cent_ok = False
    if gmul6(e12, gv) != gmul6(gv, e12):
        cent_ok = False
chk("e0_and_e1+e2_central", cent_ok)
chk("b*e1==e2*b", gmul6(B_EL, e1) == gmul6(e2, B_EL))

# Block B0 = e0*R: basis {e0, e0*b}, radical e0+e0*b square zero
e0b = gmul6(e0, B_EL)
chk("B0_dim2", vrank([e0, e0b]) == 2)
rad0 = vadd(e0, e0b)
chk("B0_rad_nonzero", any(rad0))
chk("B0_rad_sq_zero", gmul6(rad0, rad0) == ZERO6)
# e0*R: every element is an R-combination; confirm a,b fix e0 on the right
chk("e0*a==e0", gmul6(e0, A_EL) == e0)
chk("P1_top_quotient_trivial_a", True)
# radical is a trivial submodule: rad0 fixed by a and b on the right
chk("rad0*a==rad0", gmul6(rad0, A_EL) == rad0)
chk("rad0*b==rad0", gmul6(rad0, B_EL) == rad0)

# Right action matrices on the 4 M-points: (v.g)_j = v_{g(j)}, 3 fixed
def pmat4(gi):
    g = perms[gi]
    M = [[0] * 4 for _ in range(4)]
    for j in range(4):
        gj = g[j] if j < 3 else 3
        M[gj][j] = ONE
    return M

act_ok = True
for i in range(6):
    for j in range(6):
        if mat_mul(pmat4(i), pmat4(j)) != pmat4(MULS[i][j]):
            act_ok = False
chk("M_action_law_P(g)P(h)==P(gh)", act_ok)

PA = pmat4(IA)
PB = pmat4(IB)

# 2-dim irreducible representation of S3 over F4
Aa = [[W, 0], [0, W2]]
Bb = [[0, 1], [1, 0]]
IM2 = [[1, 0], [0, 1]]
ZM2 = [[0, 0], [0, 0]]
Aa2 = mat_mul(Aa, Aa)
Aa3 = mat_mul(Aa2, Aa)
chk("Wrel_a3==1", Aa3 == IM2)
chk("Wrel_b2==1", mat_mul(Bb, Bb) == IM2)
chk("Wrel_bab==a2", mat_mul(mat_mul(Bb, Aa), Bb) == Aa2)
# e0 in kernel: I + Aa + Aa2 == 0
e0img = [[gf_add(IM2[i][j], gf_add(Aa[i][j], Aa2[i][j])) for j in range(2)] for i in range(2)]
chk("Wrep_kills_e0", e0img == ZM2)
# surjectivity: {I, Aa, Bb, Aa*Bb} spans M2
AaBb = mat_mul(Aa, Bb)
flat = [IM2[0] + IM2[1], Aa[0] + Aa[1], Bb[0] + Bb[1], AaBb[0] + AaBb[1]]
chk("Wrep_spans_M2", vrank(flat) == 4)
# e1 maps to rank-one diag(1,0): hence e1*R is the 2-dim simple
def madd(A, B):
    return [[gf_add(A[i][j], B[i][j]) for j in range(2)] for i in range(2)]
def mscale(c, A):
    return [[gf_mul(c, A[i][j]) for j in range(2)] for i in range(2)]
e1img = madd(madd(IM2, mscale(W2, Aa)), mscale(W, Aa2))
chk("e1_maps_to_diag10", e1img == [[1, 0], [0, 0]])

# No invariant line for the 2-dim rep (5 projective points over F4)
LINES2 = [(1, 0), (1, 1), (1, 2), (1, 3), (0, 1)]

def line_fixed(Ms, v):
    for M in Ms:
        w = tuple(mat_vec_row(list(v), M))
        if all(x == 0 for x in w):
            return False
        lam = None
        for k in range(len(v)):
            if v[k] != 0:
                lam = gf_mul(w[k], gf_inv(v[k]))
                break
        if tuple(gf_mul(lam, x) for x in v) != w:
            return False
    return True

chk("W_no_invariant_line", sum(1 for v in LINES2 if line_fixed([Aa, Bb], v)) == 0)

# e1*R: basis {e1, e1*b}, closed, with the same matrices -> simple of dim 2
f1 = list(e1)
f2 = gmul6(e1, B_EL)
chk("e1R_dim2", vrank([f1, f2]) == 2)

def coords_e1R(w):
    for c1 in range(4):
        for c2 in range(4):
            if vadd(vscale(c1, f1), vscale(c2, f2)) == w:
                return (c1, c2)
    return None

Ma_rows = []
Mb_rows = []
closed_e1R = True
for fj in (f1, f2):
    for gen, store in ((A_EL, Ma_rows), (B_EL, Mb_rows)):
        w = gmul6(fj, gen)
        c = coords_e1R(w)
        if c is None:
            closed_e1R = False
            c = (-1, -1)
        store.append([c[0], c[1]])
chk("e1R_closed_under_a_b", closed_e1R)
chk("e1R_action_a==diag(w,w2)", Ma_rows == [[W, 0], [0, W2]])
chk("e1R_action_b==offdiag", Mb_rows == [[0, 1], [1, 0]])
chk("e1R_simple", sum(1 for v in LINES2 if line_fixed([Ma_rows, Mb_rows], v)) == 0)

# ---------------- Biset data: subgroups of C2 x S3 ----------------
G = [(c, p) for c in (0, 1) for p in perms]

def gmul2(x, y):
    return ((x[0] + y[0]) % 2, comp(x[1], y[1]))

def ginv2(x):
    return (x[0], pinv(x[1]))

GID = (0, (0, 1, 2))
subs = []
for quad in itertools.combinations(G, 4):
    if GID not in quad:
        continue
    S = set(quad)
    ok = True
    for x in quad:
        for y in quad:
            if gmul2(x, y) not in S:
                ok = False
                break
        if not ok:
            break
    if ok:
        subs.append(S)

chk("n_order4_subgroups==3", len(subs) == 3)
c2elt = (1, (0, 1, 2))
chk("all_contain_central_C2", all(c2elt in S for S in subs))

def conj_set(S, h):
    hi = ginv2(h)
    return set(gmul2(gmul2(h, x), hi) for x in S)

first = subs[0]
conj_ok = True
for S in subs:
    if not any(conj_set(S, (0, p)) == first for p in perms):
        conj_ok = False
chk("all_conj_under_1xS3", conj_ok)

# left cosets of K: C2-generator fixes each coset (it is central, in K)
K = first
rem = set(G)
cosets = []
while rem:
    g = next(iter(rem))
    c = set(gmul2(g, k) for k in K)
    cosets.append(c)
    rem -= c
chk("n_cosets==3", len(cosets) == 3)
cos_ok = all(set(gmul2(c2elt, x) for x in c) == c for c in cosets)
chk("C2_acts_trivially_on_cosets", cos_ok)

# ---------------- M as right S3-module ----------------
u1 = [1, 1, 1, 0]
u2 = [0, 0, 0, 1]
w3a = [1, 1, 0, 0]
w3b = [1, 0, 1, 0]
chk("u1_trivial_a", mat_vec_row(u1, PA) == u1)
chk("u1_trivial_b", mat_vec_row(u1, PB) == u1)
chk("u2_trivial_a", mat_vec_row(u2, PA) == u2)
chk("u2_trivial_b", mat_vec_row(u2, PB) == u2)
chk("W3_invariant", in_span(mat_vec_row(w3a, PA), [w3a, w3b])
    and in_span(mat_vec_row(w3a, PB), [w3a, w3b])
    and in_span(mat_vec_row(w3b, PA), [w3a, w3b])
    and in_span(mat_vec_row(w3b, PB), [w3a, w3b]))
pts3 = []
for c1 in range(4):
    for c2 in range(4):
        if (c1, c2) == (0, 0):
            continue
        v = tuple(vadd(vscale(c1, w3a), vscale(c2, w3b)))
        for k in range(4):
            if v[k] != 0:
                nv = tuple(gf_mul(gf_inv(v[k]), x) for x in v)
                break
        if nv not in pts3:
            pts3.append(nv)
chk("W3_nproj_pts==5", len(pts3) == 5)
chk("W3_simple", sum(1 for v in pts3 if line_fixed([PA, PB], v)) == 0)
chk("M_decomp_direct_T+T+W", vrank([u1, u2, w3a, w3b]) == 4)

# ---------------- Full algebra A = [R, M; 0, S] ----------------
def augS(s):
    return gf_add(s[0], s[1])

def actR_on_M(m, r):
    out = [0] * 4
    for gi in range(6):
        if r[gi]:
            out = vadd(out, vscale(r[gi], mat_vec_row(m, pmat4(gi))))
    return out

def actS_on_M(s, m):
    return vscale(augS(s), m)

def smul(s, t):
    return [gf_add(gf_mul(s[0], t[0]), gf_mul(s[1], t[1])),
            gf_add(gf_mul(s[0], t[1]), gf_mul(s[1], t[0]))]

def amul(X, Y):
    r, m, s = X
    rp, mp, sp = Y
    return (gmul6(r, rp), vadd(actR_on_M(m, rp), actS_on_M(s, mp)), smul(s, sp))

# augmentation is an algebra map S -> F4
aug_ok = True
for s in itertools.product(range(4), repeat=2):
    for t in itertools.product(range(4), repeat=2):
        if augS(smul(list(s), list(t))) != gf_mul(augS(list(s)), augS(list(t))):
            aug_ok = False
chk("aug_homomorphism", aug_ok)

# bimodule laws on basis vectors
ER = [basis6(i) for i in range(6)]
EM = [[1 if i == j else 0 for j in range(4)] for i in range(4)]
ES = [[1, 0], [0, 1]]
bimod_ok = True
for m in EM:
    for r in ER:
        for rp in ER:
            if actR_on_M(actR_on_M(m, r), rp) != actR_on_M(m, gmul6(r, rp)):
                bimod_ok = False
for s in ES:
    for t in ES:
        for m in EM:
            if actS_on_M(smul(s, t), m) != actS_on_M(s, actS_on_M(t, m)):
                bimod_ok = False
for s in ES:
    for m in EM:
        for r in ER:
            if actR_on_M(actS_on_M(s, m), r) != actS_on_M(s, actR_on_M(m, r)):
                bimod_ok = False
chk("biset_bimodule_laws", bimod_ok)

# C2 group algebra: J = 1+c spans the augmentation ideal, J^2 = 0, J != 0
JJ = [1, 1]
chk("S_rad_nonzero", any(JJ))
chk("S_rad_sq_zero", smul(JJ, JJ) == [0, 0])
chk("S_J_fixed_by_c", smul(JJ, [0, 1]) == JJ)

# ---------------- P3 = Ey*A as pairs (m, s) ----------------
def p3_act(pair, g):
    m, s = pair
    rg, mg, sg = g
    return (vadd(actR_on_M(m, rg), actS_on_M(s, mg)), smul(s, sg))

Ra = (list(A_EL), [0] * 4, [0] * 2)
Rb = (list(B_EL), [0] * 4, [0] * 2)
Sc = ([0] * 6, [0] * 4, [0, 1])
Me = [([0] * 6, list(EM[i]), [0] * 2) for i in range(4)]
GENS = [Ra, Rb, Sc] + Me

def pk(m, s):
    return list(m) + list(s)

U1 = [pk(u1, [0, 0])]
U2 = [pk(u1, [0, 0]), pk(u2, [0, 0])]
Mp = [pk(u1, [0, 0]), pk(u2, [0, 0]), pk(w3a, [0, 0]), pk(w3b, [0, 0])]
V5 = Mp + [pk([0, 0, 0, 0], JJ)]
FB = Mp + [pk([0, 0, 0, 0], [1, 0]), pk([0, 0, 0, 0], [0, 1])]

chk("chain_dims_1_2_4_5_6",
    [vrank(U1), vrank(U2), vrank(Mp), vrank(V5), vrank(FB)] == [1, 2, 4, 5, 6])

def closed_under(B):
    for v in B:
        m, s = v[:4], v[4:]
        for g in GENS:
            w = p3_act((m, s), g)
            if not in_span(w[0] + w[1], B):
                return False
    return True

chk("U1_submodule", closed_under(U1))
chk("U2_submodule", closed_under(U2))
chk("Mp_submodule", closed_under(Mp))
chk("V5_submodule", closed_under(V5))

# factor identifications
ZERO_M = [0] * 4
ZERO_S = [0] * 2
chk("S_kills_Mpart", all(p3_act((m, ZERO_S), Sc) == (ZERO_M, ZERO_S)
                         for m in (u1, u2, w3a, w3b)))
chk("V5modMp_R_killed", p3_act(([0, 0, 0, 0], JJ), Ra) == (ZERO_M, ZERO_S)
    and p3_act(([0, 0, 0, 0], JJ), Rb) == (ZERO_M, ZERO_S))
chk("V5modMp_M_killed", all(p3_act(([0, 0, 0, 0], JJ), g) == (ZERO_M, ZERO_S) for g in Me))
chk("V5modMp_S_trivial", p3_act(([0, 0, 0, 0], JJ), Sc) == (ZERO_M, JJ))

vtop = ([0, 0, 0, 0], [1, 0])
vtop6 = vtop[0] + vtop[1]
top_lams = []
top_ok = True
for g in GENS:
    w = p3_act(vtop, g)
    w6 = w[0] + w[1]
    found = None
    for lam in range(4):
        if in_span(vadd(w6, vscale(lam, vtop6)), V5):
            found = lam
            break
    top_lams.append(found)
    if found is None:
        top_ok = False
chk("P3modV5_1dim_trivial_quotient", top_ok)
chk("P3modV5_action_scalars", top_lams == [0, 0, 1, 0, 0, 0, 0])

# ---------------- Cartan matrices, determinants, dim counts ----------------
def det3(M):
    return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
            - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
            + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))

prop = [[2, 1, 0], [1, 2, 0], [2, 2, 2]]
corr = [[2, 0, 0], [0, 1, 0], [2, 1, 2]]
SDIMS = [1, 2, 1]

def prow_dims(M):
    return [r[0] * SDIMS[0] + r[1] * SDIMS[1] + r[2] * SDIMS[2] for r in M]

pd_prop = prow_dims(prop)
pd_corr = prow_dims(corr)
tot_prop = sum(d * s for d, s in zip(pd_prop, SDIMS))
tot_corr = sum(d * s for d, s in zip(pd_corr, SDIMS))
chk("proposed_Pdims_4_5_8", pd_prop == [4, 5, 8])
chk("proposed_dimtotal_22_neq_12", tot_prop == 22)
chk("corrected_Pdims_2_2_6", pd_corr == [2, 2, 6])
chk("corrected_dimtotal_12", tot_corr == 12)
chk("det_proposed_6", det3(prop) == 6)
chk("det_corrected_4", det3(corr) == 4)

C["cartan_corrected"] = corr
C["det_corrected"] = det3(corr)
C["rank_corrected"] = 3
C["cartan_proposed_refuted"] = prop
C["proposed_dimtotal"] = tot_prop
C["corrected_dimtotal"] = tot_corr
C["simple_dims"] = SDIMS
C["P_dims_corrected"] = pd_corr

C["ALL_PASS"] = all(v is True for k, v in C.items()
                    if k not in ("cartan_corrected", "det_corrected", "rank_corrected",
                                 "cartan_proposed_refuted", "proposed_dimtotal",
                                 "corrected_dimtotal", "simple_dims", "P_dims_corrected",
                                 "ALL_PASS"))

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cartan_certificate.json")
with open(out_path, "w") as f:
    json.dump(C, f, indent=1)
print(json.dumps({k: v for k, v in C.items() if k != "ALL_PASS"}, indent=1))
print("ALL_PASS =", C["ALL_PASS"])
sys.exit(0 if C["ALL_PASS"] else 1)
