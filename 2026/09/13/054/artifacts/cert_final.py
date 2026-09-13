"""Consolidated certificate script: proves mu32/sqrt(7) > mu16/sqrt(3).
Part A (mu16 upper): Voronoi vertex certificate.
  - A priori GS bound from interval LDL (upper-rounded).
  - Eigenvalue tail bound via RIGOROUS interval LDL of G16 - lam*I
    (lam=0.489): all pivots certified nonzero (inf>0) and all D infs>0,
    hence G16 - lam*I is positive definite, so lam_min(G16) >= lam;
    25*lam > Qlist puts all relevant vectors inside [-4,4]^3.
  - Exhaustive interval listing inside the box (inclusion margin 1e-9).
  - Vertices: exact-INTEGER adjugate solve V u = rhs (det != 0 checked in
    exact integer arithmetic; det==0 triples are truly singular and cannot
    isolate a vertex) followed by interval LDL forward/back substitution
    for G x = u (D infs > 0 asserted, so no pivot search anywhere and no
    vertex can be silently skipped). Feasibility exclusion uses a 1e-9
    margin (sound direction); suprema are upward-rounded.
Part B (mu32 >= 2.20): interval-LDL sphere-decoder DFS exclusion.
  - Branch ranges are formed from the FULL interval shift endpoints
    (slo/shi with 1e-9 padding) plus a +/-1 integer expansion, which
    rigorously dominates all float-rounding errors (relative ~1e-16).
  - Decoder threshold R2dec = 4.84 + 1e-6; prune test uses a 1e-9 margin,
    so every pruned or unenumerated branch is certified >= 4.84.
  - Any surviving leaf is exactly rechecked (fail-closed).
Uses mpmath.iv at dps=30. Run with PYTHONPATH="" (stray /tmp/enum.py).
"""
from mpmath import mp, iv
import itertools, math, sys, json, time

mp.dps = 30
sys.setrecursionlimit(10000)

FEAS_MARGIN = 1e-9   # feasibility-exclusion margin (Part A)
PRM = 1e-9           # prune/rounding margin (Part B)
R2T = 4.84           # target: 2.20^2
R2DEC = R2T + 1e-6   # decoder threshold (strictly above target)


def upfloat(x):
    return math.nextafter(float(x), math.inf)


def iv_log_sinrat(num, den):
    x = iv.mpf(num) / iv.mpf(den) * iv.pi
    return iv.log(iv.fabs(iv.sin(x)))


def build_iv(m):
    js = [j for j in range(1, m // 2, 2)]
    As = [a for a in js if a != 1]
    d = len(js)
    n = len(As)
    L = [[iv_log_sinrat(a * j, m) for a in js] for j in js]
    idx = {a: k for k, a in enumerate(js)}
    G = [[sum((L[i][idx[a]] - L[i][idx[1]]) * (L[i][idx[b]] - L[i][idx[1]])
              for i in range(d)) for b in As] for a in As]
    return js, As, G


def iv_ldl(G):
    n = len(G)
    Ld = [[iv.mpf(0)] * n for _ in range(n)]
    Dd = [iv.mpf(0)] * n
    for i in range(n):
        for j in range(i):
            Ld[i][j] = (G[i][j] - sum(Ld[i][k] * Ld[j][k] * Dd[k]
                                      for k in range(j))) / Dd[j]
        Dd[i] = G[i][i] - sum(Ld[i][k] ** 2 * Dd[k] for k in range(i))
        Ld[i][i] = iv.mpf(1)
    return Ld, Dd


out = {}
t0 = time.time()

# ============ PART A: mu16 upper bound ============
G16 = build_iv(16)[2]
Ld, Dd = iv_ldl(G16)
assert all(float(d.a) > 0 for d in Dd), "G16 LDL D infs must be > 0"
GSsup = sum(upfloat(d.b) for d in Dd) / 4 + 1e-12
out['mu16_GSsup_sq'] = GSsup
print("A0: GS mu16^2 <= %.10f" % GSsup)
Qlist = 4 * GSsup
print("A0: Qlist = 4*GSsup = %.10f" % Qlist)

# --- rigorous eigenvalue certificate: interval LDL of G16 - lam*I ---
LAM_STR = '0.489'
LAM = iv.mpf(LAM_STR)
H = [[(G16[i][j] - LAM) if i == j else G16[i][j]
      for j in range(3)] for i in range(3)]
HL = [[iv.mpf(0)] * 3 for _ in range(3)]
HD = [iv.mpf(0)] * 3
ok = True
for i in range(3):
    for j in range(i):
        if not (float(HD[j].a) > 0):
            ok = False
            break
        HL[i][j] = (H[i][j] - sum(HL[i][k] * HL[j][k] * HD[k]
                                  for k in range(j))) / HD[j]
    if not ok:
        break
    HD[i] = H[i][i] - sum(HL[i][k] ** 2 * HD[k] for k in range(i))
    HL[i][i] = iv.mpf(1)
    if not (float(HD[i].a) > 0):
        ok = False
        break
assert ok, "shifted LDL failed: lam certificate not obtained"
hd_infs = [float(d.a) for d in HD]
hd_sups = [float(d.b) for d in HD]
out['mu16_lam'] = float(LAM_STR)
out['mu16_shifted_LDL_D'] = [hd_infs, hd_sups]
print("A1: interval LDL of G16-%s*I: D infs = %s (all > 0)" % (LAM_STR,
      ["%.6f" % v for v in hd_infs]))
print("A1: hence G16-%s*I is positive definite, lam_min(G16) >= %s"
      % (LAM_STR, LAM_STR))
box_margin = 25 * float(LAM_STR) - 1e-9
print("A1: 25*lam - 1e-9 = %.6f > Qlist = %.6f ? %s"
      % (box_margin, Qlist, box_margin > Qlist))
assert box_margin > Qlist
out['mu16_box_check'] = [box_margin, Qlist]


def iv_q3(z):
    s = iv.mpf(0)
    for i in range(3):
        for j in range(3):
            s += G16[i][j] * iv.mpf(z[i]) * iv.mpf(z[j])
    return s


LIST = []
for z in itertools.product(range(-4, 5), repeat=3):
    if all(a == 0 for a in z):
        continue
    s = iv_q3(z)
    # sound inclusion: true q(z) <= float(s.a) + tiny, so this keeps every
    # z with true q <= Qlist (extra inclusions only shrink P; V subset P
    # still holds, so the upper bound stays valid).
    if float(s.a) <= Qlist + 1e-9:
        LIST.append((z, s))
out['mu16_list_size'] = len(LIST)
print("A2: LIST size=%d (every nonzero z outside [-4,4]^3 has "
      "q >= 25*lam > Qlist; inside, all q<=Qlist listed)" % len(LIST))


def det3_int(M):
    return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
            - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
            + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))


def cof3_int(M, r, c):
    rows = [i for i in range(3) if i != r]
    cols = [j for j in range(3) if j != c]
    m = M[rows[0]][cols[0]] * M[rows[1]][cols[1]] \
        - M[rows[0]][cols[1]] * M[rows[1]][cols[0]]
    return -m if (r + c) % 2 else m


def vertex_of_triple(vs, rhs):
    """Solve V G x = rhs: first V u = rhs via exact integer adjugate,
    then G x = u via interval LDL substitution. Returns interval x or
    None if the triple is (exactly) singular."""
    V = [list(v) for v in vs]
    detV = det3_int(V)
    if detV == 0:
        return None  # dependent normals: cannot isolate a vertex
    # u_j = sum_k cof(k,j) rhs_k / detV
    u = []
    for j in range(3):
        uj = sum(iv.mpf(cof3_int(V, k, j)) * rhs[k]
                 for k in range(3)) / iv.mpf(detV)
        u.append(uj)
    # forward: L y = u
    y = [None] * 3
    for i in range(3):
        y[i] = u[i] - sum(Ld[i][k] * y[k] for k in range(i))
    # diagonal: D z = y
    z = [y[i] / Dd[i] for i in range(3)]
    # back: L^T x = z
    x = [None] * 3
    for i in (2, 1, 0):
        x[i] = z[i] - sum(Ld[j][i] * x[j] for j in range(i + 1, 3))
    return x


nvert = 0
nskipped_singular = 0
maxsup = 0.0
maxinf = 0.0
for combo in itertools.combinations(range(len(LIST)), 3):
    vs = [LIST[k][0] for k in combo]
    rhs = [LIST[k][1] / 2 for k in combo]
    x = vertex_of_triple(vs, rhs)
    if x is None:
        nskipped_singular += 1
        continue
    feasible = True
    for z, s in LIST:
        Gx = [sum(G16[ll][j] * x[j] for j in range(3)) for ll in range(3)]
        gx = sum(iv.mpf(z[ll]) * Gx[ll] for ll in range(3))
        # exclude only if certified infeasible (margin: sound direction;
        # float error ~1e-14 << 1e-9, so exclusion implies truly infeasible)
        if float((2 * gx - s).a) > FEAS_MARGIN:
            feasible = False
            break
    if not feasible:
        continue
    qx = sum(G16[i][j] * x[i] * x[j] for i in range(3) for j in range(3))
    nvert += 1
    sup_up = upfloat(qx.b) + 1e-9 * (1 + abs(float(qx.b)))
    if sup_up > maxsup:
        maxsup = sup_up
        maxinf = float(qx.a)
out['mu16_nvert'] = nvert
out['mu16_singular_triples'] = nskipped_singular
out['mu16_maxvert_q'] = [maxinf, maxsup]
print("A3: polytope vertices=%d (singular triples skipped: %d), "
      "max q in [%.10f, %.10f]" % (nvert, nskipped_singular, maxinf,
                                   maxsup))
print("A4: mu16 <= sqrt(%.10f) = %.10f" % (maxsup, math.sqrt(maxsup)))
out['mu16_ub'] = math.sqrt(maxsup)
assert maxsup <= 1.60, "need mu16^2<=1.60"

# ============ PART B: mu32 >= 2.20 ============
G32 = build_iv(32)[2]
n = 7
Ld7, Dd7 = iv_ldl(G32)
assert all(float(d.a) > 0 for d in Dd7), "G32 LDL D infs must be > 0"
# safe (rounded-down) D lower bounds; float error ~1e-16 << 1e-9 factor
Dlo = [float(d.a) * (1 - 1e-9) for d in Dd7]
t = [iv.mpf(1) / 2 if i in (0, 2, 3, 5, 6) else iv.mpf(0)
     for i in range(n)]
w = [None] * n
nodes = [0]
leaves_cert = [0]
fail = [False]
failinfo = [None]


def rec(i, acc):
    if fail[0]:
        return
    nodes[0] += 1
    if i < 0:
        # full-sum leaf: certify directly (fail-closed)
        if float(acc.a) - PRM >= R2T:
            leaves_cert[0] += 1
        else:
            fail[0] = True
            failinfo[0] = ("leaf", [float(v.a) for v in w],
                           float(acc.a), float(acc.b))
        return
    # interval shift from already-fixed trailing coords
    s = sum((Ld7[j][i] * w[j] for j in range(i + 1, n)), iv.mpf(0))
    alo = float(acc.a) - PRM
    if alo >= R2DEC:
        return  # certified: true partial sum >= R2DEC > target
    rem = R2DEC - alo  # > 0 here
    W = math.sqrt(rem / Dlo[i]) * (1 + 1e-9) + 1e-9
    # FULL interval endpoints (diameters rigorously accounted) plus 1e-9
    # padding; the +/-1 integer expansion below dominates every
    # float-rounding error (relative ~1e-16), so no integer k that could
    # come within the decoder radius is ever omitted.
    slo = float(s.a) - PRM
    shi = float(s.b) + PRM
    c = 0.5 if i in (0, 2, 3, 5, 6) else 0.0
    klo = math.ceil(c - W - shi) - 1
    khi = math.floor(c + W - slo) + 1
    for k in range(klo, khi + 1):
        w[i] = iv.mpf(k) - t[i]  # exact point interval (integer/half grid)
        y = w[i] + s
        newacc = acc + Dd7[i] * y * y
        if float(newacc.a) - PRM >= R2DEC:
            continue  # rigorously excluded subtree
        rec(i - 1, newacc)
    w[i] = None


rec(n - 1, iv.mpf(0))
print("B: nodes=%d certified_leaves=%d fail=%s %s"
      % (nodes[0], leaves_cert[0], fail[0], failinfo[0]))
assert not fail[0]
out['mu32_decoder'] = {'R2DEC': R2DEC, 'PRM': PRM, 'nodes': nodes[0],
                       'leaves_cert': leaves_cert[0]}
# hole value interval
zh = (1, 0, 0, 0, 1, 1, 0)
xh = [t[i] - iv.mpf(zh[i]) for i in range(n)]
qh = sum(G32[i][j] * xh[i] * xh[j] for i in range(n) for j in range(n))
print("B: hole q in [%.10f, %.10f]" % (float(qh.a), float(qh.b)))
out['mu32_hole_q'] = [float(qh.a), float(qh.b)]
out['mu32_lb'] = 2.20

# ============ CONCLUSION ============
nu16 = math.sqrt(maxsup) / math.sqrt(3)
nl32 = 2.20 / math.sqrt(7)
print("mu16/sqrt(3) <= %.10f; mu32/sqrt(7) >= %.10f" % (nu16, nl32))
print("GAP: %.6f > 0 => CLAIM PROVED" % (nl32 - nu16))
out['nu16_ub'] = nu16
out['nl32_lb'] = nl32
out['gap'] = nl32 - nu16
assert nl32 > nu16
# safely rounded display numbers for the write-up
out['display'] = {
    'mu16_ub_8': math.ceil(math.sqrt(maxsup) * 1e8 + 1e-4) / 1e8,
    'nu16_ub_8': math.ceil(nu16 * 1e8 + 1e-4) / 1e8,
    'nl32_lb_8': math.floor(nl32 * 1e8 - 1e-4) / 1e8,
    'gap_lb_6': math.floor((nl32 - nu16) * 1e6 - 1e-2) / 1e6,
}
print("display:", out['display'])
print("elapsed %.1fs" % (time.time() - t0))
with open('output/artifacts/cert_summary.json', 'w') as f:
    json.dump(out, f, indent=2)
print("wrote output/artifacts/cert_summary.json")
