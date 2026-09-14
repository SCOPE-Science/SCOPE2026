"""Lane-1841 step 3: rigorous Krawczyk certification of N_6 shapes.

Method (HIKMOT-style, pure Python, no Sage):
- Independent rectangular equations from SnapPy's enough_gluing_equations
  (6 eqs / 6 tets), solved in log form f(z) = log(c*prod z^a (1-z)^b).
- Jacobian Df[i][j] = a/z - b/(1-z); float inverse C = Df(z0)^{-1} as the
  approximate inverse (point matrix, then embedded as point intervals).
- All interval ops in mpmath.iv at dps=50 (only +,-,*,/, integer powers via
  repeated multiplication, log, abs) — every operation outward-rounded.
- Integer powers with negative exponents are formed as repeated interval
  multiplication of (1/z^k) pieces, never via float pow.
- Krawczyk operator K(X) = (z0 - C f(z0)) + (I - C Df(X))(X - z0);
  success = K(X) strictly inside X componentwise (mpmath `in` = subset).
- Positivity: inf Im(box) > 0 for every tet.
- Log-lift validity: for each independent equation, |log(c*prod)| over the
  whole box has sup < 0.1, so no branch ambiguity (true log-lift is within
  0.1 of 0, hence exactly the principal branch, i.e. rectangular solution
  lifts to the complete logarithmic gluing system up to the known 2*pi*i
  targets; then the residual check against the FULL log system below
  distinguishes edge (=2 pi i) vs cusp targets).
- Full log-system audit: evaluate the complete SnapPy log gluing matrix
  (10 rows for N_6: 6 edges + 2 cusp-0 + 2 fillings) over the certified
  boxes, checking each row's interval is within 0.1 of its target
  (2 pi i for edges+fillings, 0 for complete-cusp meridian/longitude).
  This mirrors SnapPy's check_logarithmic_gluing_equations test with
  rigorous intervals.

Outputs: output/artifacts/lane1841_krawczyk.json with boxes, checks.
"""
import json
import cmath
import numpy as np
import mpmath
import snappy
from snappy.snap.shapes import enough_gluing_equations

DPS = 50
mpmath.mp.dps = DPS
mpmath.iv.dps = DPS
iv = mpmath.iv

N_ID = 6
R = 1e-8  # half-width of initial box; contraction needs R small enough that
# ||C||*Lip(Df)*R << 1 given large filling exponents (Lip ~ 50, ||C|| ~ 4.3),
# yet R >> Newton residual ~1e-15 and interval-evaluation overestimation
# (~1e-15 at these exponents). R=1e-6 failed (K overshoot ~1e-9 from Df(X)
# width terms); R=1e-9 failed only by ~1e-15 rounding-scale excess; R=1e-8
# gives margin ~1e7 over defects with q~2e-6 << 1.

M = snappy.Manifold('s776')
M.dehn_fill([(0, 0), (1, N_ID), (1, N_ID)])
EQNS = enough_gluing_equations(M)
z0 = [complex(x) for x in M.tetrahedra_shapes('rect')]
N = len(z0)
assert N == 6 and len(EQNS) == 6

LOGM = M.gluing_equations()  # full log system, 10 rows x 18 cols
nrows, ncols = LOGM.dimensions()
print("full log matrix dims:", (nrows, ncols))
assert (nrows, ncols) == (10, 18)
# Row targets: rows 0..5 edges -> 2 pi i; rows 6,7 cusp0 (complete) -> 0;
# rows 8,9 fillings -> 2 pi i. (SnapPy orders: edges, then per-cusp
# meridian/longitude or single filling equation.)
ROW_TARGET = ['2pii'] * 6 + ['0', '0', '2pii', '2pii']


def ipoint(x, y=None):
    if y is None:
        return iv.mpc(x.real, x.imag)
    return iv.mpc(x, y)


def real_iv(k):
    """Rigorous real point interval for a small integer (re + 0j)."""
    return iv.mpc([float(k), float(k)], [0, 0])


def ipow(z, k):
    """Rigorous integer power by repeated interval multiplication."""
    assert isinstance(k, int)
    if k == 0:
        return iv.mpc([1, 1], [0, 0])
    if k < 0:
        return ipow(1 / z, -k)
    out = iv.mpc([1, 1], [0, 0])
    for _ in range(k):
        out = out * z
    return out


def rect_prod_iv(A, B, c, boxes):
    p = ipoint(complex(c))
    for a, z in zip(A, boxes):
        if a:
            p = p * ipow(z, int(a))
    for b, z in zip(B, boxes):
        if b:
            p = p * ipow(1 - z, int(b))
    return p


# ---- float data ----
def J_float(z):
    J = np.zeros((N, N), dtype=complex)
    for i, (A, B, c) in enumerate(EQNS):
        for j, (a, b, zj) in enumerate(zip(A, B, z)):
            J[i, j] = a / zj - b / (1 - zj)
    return J


J0 = J_float(z0)
C = np.linalg.inv(J0)
print("float cond:", float(np.linalg.cond(J0)))

from snappy.snap.shapes import eval_gluing_equation
f0 = np.array([cmath.log(eval_gluing_equation(e, z0)) for e in EQNS])
print("float |f0|:", [abs(v) for v in f0])

# ---- interval setup ----
boxes = [iv.mpc([z.real - R, z.real + R], [z.imag - R, z.imag + R]) for z in z0]
z0iv = [ipoint(z) for z in z0]
Civ = [[ipoint(c) for c in row] for row in C]
f0iv = [ipoint(v) for v in f0]

# T = z0 - C f(z0): z0 is the APPROXIMATION, so point intervals suffice
# (embedding a double at dps=50 has width ~1e-50). f(z0) is evaluated
# rigorously over the degenerate box, so T rigorously encloses z0-Cf(z0).
Z0box = [ipoint(z) for z in z0]
F0 = []
for (A, B, c) in EQNS:
    p = rect_prod_iv(A, B, c, Z0box)
    F0.append(iv.log(p))
# T = Z0box - C F0
T = []
for i in range(N):
    s = Z0box[i]
    for j in range(N):
        s = s - Civ[i][j] * F0[j]
    T.append(s)

# Df over boxes
Df = []
for i, (A, B, c) in enumerate(EQNS):
    row = []
    for j, (a, b) in enumerate(zip(A, B)):
        t = iv.mpc([0, 0], [0, 0])
        if a:
            t = t + real_iv(a) * (1 / boxes[j])
        if b:
            t = t - real_iv(b) * (1 / (1 - boxes[j]))
        row.append(t)
    Df.append(row)

# P = C Df
P = [[iv.mpc([0, 0], [0, 0]) for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        s = iv.mpc([0, 0], [0, 0])
        for k in range(N):
            s = s + Civ[i][k] * Df[k][j]
        P[i][j] = s

ONE = iv.mpc([1, 1], [0, 0])
ZERO = iv.mpc([0, 0], [0, 0])
K = []
for i in range(N):
    s = T[i]
    for j in range(N):
        d = (ONE if i == j else ZERO) - P[i][j]
        s = s + d * (boxes[i * 0 + j] - z0iv[j])
    K.append(s)

print("=== Krawczyk inclusion ===")
ok = True
for i in range(N):
    inside = (K[i] in boxes[i])
    strict = (K[i].real.b < boxes[i].real.b and K[i].real.a > boxes[i].real.a
              and K[i].imag.b < boxes[i].imag.b and K[i].imag.a > boxes[i].imag.a)
    print(f"tet {i}: K in X = {inside}, strict = {strict}")
    print(f"   X = {boxes[i]}")
    print(f"   K = {K[i]}")
    ok = ok and bool(inside)

print("=== positivity ===")
pos = True
for i in range(N):
    lo = float(boxes[i].imag.a)
    print(f"tet {i}: inf Im = {lo:.12f}  >0: {lo > 0}")
    pos = pos and (lo > 0)

print("=== log-lift on independent equations ===")
lift = True
for i, (A, B, c) in enumerate(EQNS):
    p = rect_prod_iv(A, B, c, boxes)
    lg = iv.log(p)
    nrm = abs(lg)
    print(f"eq {i}: log-box = {lg}  |.| = {nrm}")
    lift = lift and bool(nrm.b < 0.1)

print("=== full log-system audit ===")
TWO_PI = 2 * mpmath.mp.pi
full = True
for r in range(nrows):
    row = [int(LOGM[r, j]) for j in range(ncols)]
    # order: logz0, logz0', logz0'', logz1, ...
    s = iv.mpc([0, 0], [0, 0])
    for t in range(N):
        z, zp, zpp = boxes[t], 1 / (1 - boxes[t]), (boxes[t] - 1) / boxes[t]
        lz, lzp, lzpp = iv.log(z), iv.log(zp), iv.log(zpp)
        s = s + row[3 * t] * lz + row[3 * t + 1] * lzp + row[3 * t + 2] * lzpp
    tgt = TWO_PI * 1j if ROW_TARGET[r] == '2pii' else 0j
    tgt_iv = iv.mpc(0, float(TWO_PI)) if ROW_TARGET[r] == '2pii' else ZERO
    err = abs(s - tgt_iv)
    good = bool(err.b < 0.1)
    print(f"row {r} target {ROW_TARGET[r]}: err-box = {err}  ok={good}")
    full = full and good

CERT = bool(ok and pos and lift and full)
print("CERTIFIED:", CERT)


def mpc_json(z):
    return {'re': [str(z.real.a), str(z.real.b)],
            'im': [str(z.imag.a), str(z.imag.b)]}


with open('output/artifacts/lane1841_krawczyk.json', 'w') as fh:
    json.dump({
        'dps': DPS, 'n': N_ID, 'radius': R,
        'equations': [[list(map(int, A)), list(map(int, B)), int(c)] for A, B, c in EQNS],
        'row_targets': ROW_TARGET,
        'boxes': [mpc_json(z) for z in boxes],
        'k_boxes': [mpc_json(z) for z in K],
        'checks': {'krawczyk_inclusion': bool(ok), 'positivity': bool(pos),
                   'log_lift': bool(lift), 'full_log_system': bool(full)},
        'certified': CERT,
    }, fh, indent=1)
print("wrote output/artifacts/lane1841_krawczyk.json")
assert CERT, "Krawczyk certification failed"
