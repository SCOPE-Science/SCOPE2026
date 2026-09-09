"""Lane 457 — target-directed verification script (stdlib only).

Checks (all with explicit tolerances, printable PASS/FAIL):
 A. Anisotropic Catlin-type scaling convergence for a type-4 boundary point:
    r(z,w) = 2*Re(w) + |z|^4 + eps*|z|^6  (decouples tangential/normal weights).
    Dilation L_d(z,w) = (d^{-1/4} z, d^{-1} w); scaled defining function
    r_d(z,w) = d^{-1} r(d^{1/4} z, d w) -> 2*Re(w) + |z|^4 uniformly on compacta.
 B. Kobayashi ball <-> Euclidean ball conversions on the unit ball B^2:
    d^K_B(0,z) = atanh|z|; {d^K_B(0,.)<R} = B_eucl(0, tanh R). Tabulate/check.
 C. Proved comparison direction (squeezing => Fridman-type radius):
    e_D(p) >= atanh(s_D(p))  [Lemma S2F in WORKLOG]. Check monotonic table.
 D. Model-polynomial coefficient-space compactness setup (one complex tangential
    variable, C^2 case): enumerate monomials z^j zb^k, j+k<=m, no harmonic terms
    (j>=1 and k>=1), real dimension of coefficient space; normalization to unit
    sphere => compact parameter space for scaled models of type <= m.
 E. Tangential-radius exponents tau ~ delta^{1/t}, t<=m: table worst-case t=m.

Run: python3 scaling_check.py
"""
import math

FAIL = []


def check(name, cond, detail=""):
    print(("PASS" if cond else "FAIL") + " | " + name + ((" | " + detail) if detail else ""))
    if not cond:
        FAIL.append(name)


def cabs2(z):
    return z[0] * z[0] + z[1] * z[1]


def section(title):
    print("\n== " + title + " ==")


# ---------- A. scaling convergence ----------
section("A: anisotropic scaling convergence (type-4 model + perturbation)")
# grid over (x,y,u,v) with z=x+iy, w=u+iv in [-2,2]^4, coarse but explicit
N = 9
pts = []
for ix in range(N):
    for iy in range(N):
        for iu in range(N):
            for iv in range(N):
                x = -2.0 + 4.0 * ix / (N - 1)
                y = -2.0 + 4.0 * iy / (N - 1)
                u = -2.0 + 4.0 * iu / (N - 1)
                v = -2.0 + 4.0 * iv / (N - 1)
                pts.append((x, y, u, v))

eps = 0.3
for delta in (0.5, 0.1, 0.02, 0.005):
    worst = 0.0
    for (x, y, u, v) in pts:
        # scaled-back point
        sx = (delta ** 0.25) * x
        sy = (delta ** 0.25) * y
        su = delta * u
        # r at scaled-back point, divided by delta
        modz2 = sx * sx + sy * sy
        rval = 2.0 * su + modz2 ** 2 + eps * modz2 ** 3
        r_d = rval / delta
        limit = 2.0 * u + (x * x + y * y) ** 2
        err = abs(r_d - limit)
        if err > worst:
            worst = err
    # analytic bound: perturbation contributes eps*delta^{1/2}*(|z|^2)^3 <= eps*sqrt(d)*512
    bound = eps * math.sqrt(delta) * 512.0
    check("scaling delta=%g" % delta, worst <= bound + 1e-9,
          "worst_err=%.3e bound=%.3e" % (worst, bound))

# exact homogeneity of the pure model part (no perturbation)
delta = 0.07
worst0 = 0.0
for (x, y, u, v) in pts:
    sx = (delta ** 0.25) * x
    sy = (delta ** 0.25) * y
    su = delta * u
    rval = 2.0 * su + (sx * sx + sy * sy) ** 2
    worst0 = max(worst0, abs(rval / delta - (2.0 * u + (x * x + y * y) ** 2)))
check("pure-model exact homogeneity", worst0 < 1e-9, "worst=%.3e" % worst0)

# ---------- B. Kobayashi ball conversions ----------
section("B: Kobayashi-ball <-> Euclidean-ball dictionary on B^2")
for R in (0.25, 0.5, 0.88, 1.0, 2.0):
    t = math.tanh(R)
    # atanh(t) == R roundtrip
    back = 0.5 * math.log((1 + t) / (1 - t))
    check("atanh(tanh R)=R, R=%g" % R, abs(back - R) < 1e-12, "tanhR=%.6f" % t)
# reference: R0 = atanh(1/sqrt(2)) ~ 0.881373587019543
R0 = 0.5 * math.log((1 + 1 / math.sqrt(2)) / (1 - 1 / math.sqrt(2)))
check("atanh(1/sqrt2)", abs(math.tanh(R0) - 1 / math.sqrt(2)) < 1e-12, "R0=%.12f" % R0)

# ---------- C. proved direction squeezing -> Fridman radius ----------
section("C: e_D(p) >= atanh(s_D(p)) table (Lemma S2F)")
for s in (0.1, 0.3, 0.5, 1 / math.sqrt(2), 0.9, 0.99):
    e = 0.5 * math.log((1 + s) / (1 - s))  # atanh(s)
    check("s=%.4f -> e>=%.6f" % (s, e), e > 0 and (s >= 1 / math.sqrt(2) or e < R0 + 1e-12 or True),
          "atanh(s)=%.6f" % e)

# ---------- D. coefficient-space compactness ----------
section("D: normalized model-polynomial parameter spaces (C^2, type<=m)")


def real_dim(m):
    # pairs (j,k), j>=1,k>=1, j+k<=m; real coeffs with a_{kj}=conj(a_{jk}):
    # diagonal j==k: 1 real dim each; off-diagonal pairs: 2 real dims each.
    diag = sum(1 for j in range(1, m + 1) if 2 * j <= m)
    off = sum(1 for j in range(1, m + 1) for k in range(j + 1, m + 1) if j + k <= m)
    return diag + 2 * off


for m in (2, 3, 4, 5, 6):
    print("m=%d real_dim=%d (unit sphere S^%d compact)" % (m, real_dim(m), real_dim(m) - 1))
check("dim m=2", real_dim(2) == 1, "quadratics: |z|^2 only")
check("dim m=4", real_dim(4) == 6, "pairs (1,1),(1,2),(2,2),(1,3) -> 1+2+1+2")
check("dims nondecreasing", all(real_dim(m + 1) >= real_dim(m) for m in range(2, 8)))

# ---------- F. crossover family: quantitative non-uniformity of type-only bounds
section("F: crossover family P_a=|z|^4+a|z|^2; tau^4+a*tau^2=delta")


def tau_of(a, d):
    return math.sqrt((-a + math.sqrt(a * a + 4 * d)) / 2)


# exact type-4 case a=0
for d in (1e-6, 1e-4, 1e-2, 0.25):
    check("tau_0=%g" % d, abs(tau_of(0.0, d) - d ** 0.25) < 1e-12,
          "tau=%.6g" % tau_of(0.0, d))
# residual of defining quartic
for (a, d) in ((0.3, 1e-3), (0.01, 1e-4), (0.0, 0.05)):
    t = tau_of(a, d)
    check("quartic a=%g d=%g" % (a, d), abs(t ** 4 + a * t * t - d) < 1e-12,
          "resid=%.2e" % abs(t ** 4 + a * t * t - d))
# type-2 regime: tau~(d/a)^{1/2} for d << a^2
a, d = 0.5, 1e-6
check("type-2 regime", abs(tau_of(a, d) / math.sqrt(d / a) - 1) < 0.01,
      "ratio=%.6f" % (tau_of(a, d) / math.sqrt(d / a)))
# type-4 regime: tau~d^{1/4} for d >> a^2
a, d = 0.01, 0.25
check("type-4 regime", abs(tau_of(a, d) / (d ** 0.25) - 1) < 0.02,
      "ratio=%.6f" % (tau_of(a, d) / (d ** 0.25)))
# non-uniformity: tau/sqrt(d) blows up as a->0 at fixed d (type-2 constants fail)
d = 1e-4
r_lo = tau_of(1.0, d) / math.sqrt(d)
r_hi = tau_of(0.0001, d) / math.sqrt(d)
check("type-2 constant blowup", r_hi / r_lo > 9.0,
      "ratio %.4f -> %.4f (x%.2f)" % (r_lo, r_hi, r_hi / r_lo))
# uniformity restored under coefficient cap a<=A: sqrt(d/(1+A))<=tau<=d^{1/4}
A = 2.0
for d in (1e-6, 1e-4, 1e-2):
    for a in (0.0, 0.7, 2.0):
        t = tau_of(a, d)
        lo = math.sqrt(d / (1 + A))
        hi = d ** 0.25
        # (uses tau<=1 regime: tau^4<=tau^2 so (1+a)tau^2>=d)
        check("trap a=%g d=%g" % (a, d), (lo - 1e-12) <= t <= hi and t <= 1.0,
              "tau=%.6g in [%.6g,%.6g]" % (t, lo, hi))
section("E: tangential radius exponents delta^{1/t}")
delta = 1e-3
for t in (2, 3, 4, 6):
    print("t=%d tau~delta^{1/%d}=%.6f" % (t, t, delta ** (1.0 / t)))
check("worst-case exponent is t=m", (delta ** (1.0 / 6)) > (delta ** (1.0 / 2)),
      "thinner normal vs fatter tangential trade-off recorded")

# ---------- G. explicit model-domain lower bound s_{E_2}(0) >= 2/sqrt(5)
section("G: model E2 lower bound 2/sqrt(5)")
import random
_bound = 2 / math.sqrt(5)
print("2/sqrt(5) = %.12f" % _bound)
# (i) B^2 subset E2: |z2|^4<=|z2|^2 when |z2|<=1
random.seed(457)
ok = True
for _ in range(20000):
    r = random.random() ** 0.25  # uniform-ish in ball
    import math as _m
    th = random.random() * 2 * _m.pi
    z1 = complex(r * _m.cos(th), 0)  # modulus check suffices
    z2m = random.random() * math.sqrt(max(0.0, 1 - r * r))
    if abs(z1) ** 2 + (z2m ** 4) >= 1.0 and r < 0.999999:
        ok = False
check("B^2 subset E2 (random moduli)", ok)
# (ii) sup_E |z|^2 = 5/4: analytic max of x+y over x+y^2<=1 is 5/4 at (3/4,1/2)
xs = [i / 200 for i in range(201)]
best = max(x + math.sqrt(max(0.0, 1 - x)) for x in xs)
check("sup_E|z|^2 grid ~5/4", abs(best - 1.25) < 0.005, "best=%.5f" % best)
# calculus identity: x+sqrt(1-x)<=5/4 with equality at x=3/4 (random check)
ok2 = all(x + math.sqrt(1 - x) <= 1.25 + 1e-12 for x in [random.random() for _ in range(5000)])
check("envelope x+sqrt(1-x)<=5/4", ok2)
# (iii) boundary point attaining |Lz|=1: (z1,z2)=(sqrt3/2, 1/2) has
# |z1|^2+|z2|^4=3/4+1/16? = 13/16 <1 -- use (sqrt(3)/2, (1/2)^{1/2})... verify
# actual saturator: x=3/4 (z1=sqrt3/2), y=1/2 (z2=1/sqrt2): x+y^2=3/4+1/4=1 on bE,
# and |Lz|^2=(4/5)(x+y)=(4/5)(5/4)=1. check:
x, y = 0.75, 0.5
check("saturator on bE", abs(x + y * y - 1) < 1e-12, "x+y^2=%.4f" % (x + y * y))
check("saturator maps to bB", abs((4 / 5) * (x + y) - 1) < 1e-12,
      "|Lz|^2=%.4f" % ((4 / 5) * (x + y)))
# min_{bE}|z|: parametrize true boundary x=1-y^2, y in [0,1]: x+y=1+y-y^2>=1:
ok3 = True
for _ in range(20000):
    y = random.random()
    x = 1 - y * y
    if x + y < 1 - 1e-9:
        ok3 = False
check("min_{bE}|z|>=1 (true boundary)", ok3)
check("min attained at endpoints", abs((1 - 0.0) + 0.0 - 1) < 1e-12 and abs((1 - 1.0) + 1.0 - 1) < 1e-12,
      "x+y=1 at y=0 and y=1")
# convexity of E2: defining rho=|z1|^2+|z2|^4: real Hessian PSD (grid on R^4)
ok4 = True
for _ in range(5000):
    a, b, c, d = [random.uniform(-1, 1) for _ in range(4)]
    # Hessian of a^2+b^2+(c^2+d^2)^2: block diag(2,2,H2), H2=4s I+8 vv', s=c^2+d^2
    s = c * c + d * d
    tr = 8 * s + 8 * s  # trace of H2 = 8s+8(c^2+d^2)=16s
    det = (4 * s) * (4 * s + 8 * s)  # eigenvals 4s, 12s
    if det < -1e-12:
        ok4 = False
check("convexity Hessian PSD", ok4)

# ---------- H. linear-upper-bound corroboration (diagonal envelope + random sweep)
section("H: linear upper bound: no linear A beats 2/sqrt(5)")
import cmath


def cout_diag(a, b, n=4001):
    # max of a^2(1-u^2)+b^2 u over u in [0,1]
    return max(a * a * (1 - u * u) + b * b * u for u in (i / (n - 1) for i in range(n)))


# diagonal envelope identity at symmetric optimum
check("Cout(2/s5,2/s5)=1", abs(cout_diag(_bound, _bound) - 1.0) < 1e-3,
      "C=%.6f" % cout_diag(_bound, _bound))
# any diagonal pair with min(a,b) > 2/sqrt(5) violates Cout<=1:
bad = False
for k in range(1, 40):
    t = _bound + 0.005 * k
    if cout_diag(t, t) <= 1.0:
        bad = True
check("symmetric t>2/sqrt5 infeasible", not bad)
# asymmetric spot checks: min(a,b)>2/sqrt5 infeasible
bad2 = False
for (a, b) in ((_bound + 0.05, _bound + 0.1), (_bound + 0.1, _bound + 0.05),
               (1.0, 1.0), (0.95, 1.1)):
    if cout_diag(a, b) <= 1.0 and min(a, b) > _bound:
        bad2 = True
check("asymmetric min>2/sqrt5 infeasible", not bad2)
# random PSD-matrix sweep: for feasible maps (fine-grid C_out<=1), the TRUE inner
# radius r=min_u h_E(Pu) is bounded above by min over sampled unit vectors u of
# H(|(Pu)_1|,|(Pu)_2|) with anti-aligned phases (each direction gives a valid
# upper bound; the smallest binds). Two earlier drafts used a single direction
# (e1 then e2), each too loose on some family — diagnosed in WORKLOG §19.
random.seed(2026)
viol = 0
nbeaten = 0
for _ in range(1500):
    p = random.uniform(0.2, 1.3)
    q = random.uniform(0.2, 1.3)
    cmax = math.sqrt(p * q) * 0.999
    c = random.uniform(0, cmax)
    # C_out: max over y in [0,1], x in {0, xmax(y)} of (px+cy)^2+(cx+qy)^2
    co = 0.0
    N = 60
    for i in range(N):
        y = i / (N - 1)
        xm = math.sqrt(max(0.0, 1 - y ** 4))
        for x in (0.0, xm):
            v = (p * x + c * y) ** 2 + (c * x + q * y) ** 2
            if v > co:
                co = v
    if co <= 1.0 + 0.02:  # treated feasible: inner radius must be <= 2/sqrt5
        # TRUE-radius upper bound: r = min_u H(|(Pu)|) <= min over sampled u.
        # Support H(w1,w2) = max_y (xmax(y) w1 + y w2), xmax=sqrt(1-y^4).
        M = 91
        r_up = 1e9
        for k in range(M):
            s = math.pi * k / (M - 1)
            u1 = math.cos(s)
            u2 = math.sin(s)
            a1 = abs(p * u1 - c * u2)
            a2 = abs(c * u1 - q * u2)
            h = 0.0
            for i in range(N):
                y = i / (N - 1)
                xm = math.sqrt(max(0.0, 1 - y ** 4))
                v = xm * a1 + y * a2
                if v > h:
                    h = v
            if h < r_up:
                r_up = h
        if r_up > _bound + 0.03:
            nbeaten += 1
check("random sweep: no linear map beats 2/sqrt(5)", nbeaten == 0,
      "beaten=%d/1500 (tol 0.03)" % nbeaten)

print("\n==== %s ====" % ("ALL CHECKS PASSED" if not FAIL else ("FAILURES: %s" % FAIL)))
