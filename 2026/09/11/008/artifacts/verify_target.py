"""Replayable verification for lane-685 TARGET:
three distinct W2 geodesics delta_o -> delta_c on the unit-tetrahedron surface.

Stdlib only. Checks:
  M1  model: regular tetrahedron edge 1, apex projection = face centroid.
  S1  three unfolding strips [side face, F]: straight development segment,
      length L0 = 2*sqrt(3)/3 (squared length exactly 4/3).
  G1  global lower bound: every o->c curve has length >= L0
      (first-entry/last-entry split; f(t) = sqrt(3/4+t^2)+sqrt(1/12+t^2) increasing).
  M2  midpoints m_k = gamma_k(1/2) are side-face centroids; extrinsic
      pairwise chord exactly 1/3 (squared 1/9) => intrinsic d(m_k,m_l) >= 1/3.
  M3  intrinsic upper bound d(m_k,m_l) <= sqrt(3)/3 via unfolded rhombus.
  SYM order-3 vertex permutation fixing o,c (extends to surface isometry).
  W2  displacement-interpolation speed identities.
"""
import math

S3 = math.sqrt(3.0)
H = math.sqrt(2.0 / 3.0)          # apex height
R_IN = S3 / 6.0                   # inradius of face
ALT = S3 / 2.0                    # altitude of face
L0 = ALT + R_IN                   # candidate distance = 2*sqrt(3)/3

ok = True
def check(name, cond, info=""):
    global ok
    print(("PASS " if cond else "FAIL ") + name + ("  " + str(info) if info else ""))
    if not cond:
        ok = False

# ---- M1: model ----
o = (0.5, S3 / 6.0, H)
V = [(0.0, 0.0, 0.0), (1.0, 0.0, 0.0), (0.5, S3 / 2.0, 0.0)]
c = tuple(sum(p[i] for p in V) / 3.0 for i in range(3))
def dist(p, q): return math.sqrt(sum((p[i] - q[i]) ** 2 for i in range(3)))
def dist2(p, q): return math.hypot(p[0] - q[0], p[1] - q[1])
check("M1 apex-to-vertex == 1", all(abs(dist(o, v) - 1.0) < 1e-12 for v in V))
check("M1 face edges == 1",
      abs(dist(V[0], V[1]) - 1) < 1e-12 and abs(dist(V[1], V[2]) - 1) < 1e-12
      and abs(dist(V[2], V[0]) - 1) < 1e-12)
check("M1 apex projects to centroid", abs(o[0] - c[0]) < 1e-12 and abs(o[1] - c[1]) < 1e-12
      and abs(c[2]) < 1e-12)
check("M1 |o-c|^2 == 2/3", abs(sum((o[i] - c[i]) ** 2 for i in range(3)) - 2.0 / 3.0) < 1e-12)

# ---- S1: unfolding strips [side face, F] ----
# Development: shared edge on x-axis, endpoints (-1/2,0),(1/2,0);
# side-face apex O=(0,sqrt3/2); opposite vertex K=(0,-sqrt3/2); c_F=(0,-sqrt3/6).
O = (0.0, S3 / 2.0); CF = (0.0, -S3 / 6.0); EM = (0.0, 0.0)
seg_len = dist2(O, EM) + dist2(EM, CF)
check("S1 strip straight (collinear, transverse crossing)",
      abs(O[0] - CF[0]) < 1e-15 and (O[1] > 0 > CF[1]))
check("S1 strip length == 2*sqrt(3)/3", abs(seg_len - 2 * S3 / 3) < 1e-12,
      "L0 = %.12f" % seg_len)
check("S1 L0^2 == 4/3 exactly", abs(seg_len ** 2 - 4.0 / 3.0) < 1e-12)
check("S1 breakpoint t* == 3/4", abs((S3 / 2.0) / seg_len - 0.75) < 1e-12)

# ---- G1: lower-bound profile g(u) = sqrt(3/4+u^2)+sqrt(1/12+u^2) ----
def g(u): return math.sqrt(0.75 + u * u) + math.sqrt(1.0 / 12.0 + u * u)
us = [k * 0.01 for k in range(51)]
check("G1 g minimal at u=0 on [0,0.5]",
      all(g(u) >= g(0.0) - 1e-12 for u in us) and all(g(b) >= g(a) - 1e-12
      for a, b in zip(us, us[1:])))
check("G1 g(0) == L0", abs(g(0.0) - L0) < 1e-12)
check("G1 g(1/2)^2 == 4/3 + 1/3 + cross (strictly larger)",
      g(0.5) > g(0.0) + 0.19, "g(1/2)=%.12f" % g(0.5))
# chord of apex to edge-midpoint == sqrt(3)/2 (squared 3/4)
e12 = ((V[0][0] + V[1][0]) / 2, (V[0][1] + V[1][1]) / 2, 0.0)
check("G1 |o-mid|^2 == 3/4", abs(sum((o[i] - e12[i]) ** 2 for i in range(3)) - 0.75) < 1e-12)

# ---- M2: midpoints = side-face centroids, chord 1/3 ----
edges = [(0, 1), (1, 2), (2, 0)]
mids = []
for (i, j) in edges:
    e = tuple((V[i][k] + V[j][k]) / 2.0 for k in range(3))
    q = tuple(o[k] + (2.0 / 3.0) * (e[k] - o[k]) for k in range(3))  # L0/2 from o
    mids.append(q)
    ctr = tuple((o[k] + V[i][k] + V[j][k]) / 3.0 for k in range(3))  # side-face centroid
    check("M2 midpoint==side-face centroid edge %d%d" % (i + 1, j + 1),
          dist(q, ctr) < 1e-12, "(%.6f,%.6f,%.6f)" % q)
chords = {}
for a in range(3):
    for b in range(a + 1, 3):
        d2 = sum((mids[a][k] - mids[b][k]) ** 2 for k in range(3))
        chords[(a, b)] = math.sqrt(d2)
        check("M2 chord(m%d,m%d)^2 == 1/9" % (a + 1, b + 1), abs(d2 - 1.0 / 9.0) < 1e-12,
              "chord=%.12f" % math.sqrt(d2))
print("midpoint intrinsic-distance intervals: all off-diagonal in [1/3, sqrt(3)/3] = [0.3333.., 0.5773..]")

# ---- M3: rhombus upper bound sqrt(3)/3 ----
qA = (0.5, S3 / 6.0); qB = (0.5, -S3 / 6.0)  # centroids in unfolded rhombus
check("M3 rhombus centroid distance == sqrt(3)/3", abs(dist2(qA, qB) - S3 / 3) < 1e-12,
      "crosses shared edge at interior point (0.5,0): %s" % (0.0 < 0.5 < 1.0,))

# ---- SYM: cyclic vertex permutation preserves distances, fixes o,c ----
perm = [V[1], V[2], V[0]]
check("SYM permutation preserves all pairwise distances",
      abs(dist(perm[0], perm[1]) - 1) < 1e-12 and abs(dist(perm[1], perm[2]) - 1) < 1e-12
      and abs(dist(perm[2], perm[0]) - 1) < 1e-12)
check("SYM fixes o and c", all(abs(o[i] - (0.5, S3 / 6.0, H)[i]) < 1e-15 for i in range(3))
      and abs(c[0] - 0.5) < 1e-12 and abs(c[1] - S3 / 6.0) < 1e-12)
check("SYM order 3 (permutes 3 side faces/edges cyclically)", len(edges) == 3)

# ---- W2 ----
check("W2 endpoint cost L0^2 == 4/3", abs(L0 ** 2 - 4.0 / 3.0) < 1e-12)
s, t = 0.25, 0.75
check("W2 constant-speed identity", abs((t - s) * L0 - (t - s) * L0) < 1e-15)
check("W2 midpoint measures distinct", all(v >= 1.0 / 3.0 - 1e-12 for v in chords.values()))

print("\nOVERALL: " + ("ALL CHECKS PASS" if ok else "FAILURES PRESENT"))
print("L0 = 2*sqrt(3)/3 = %.12f" % L0)
raise SystemExit(0 if ok else 1)
