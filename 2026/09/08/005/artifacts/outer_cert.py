"""Outer-circle winding certificate (disc arithmetic + exact polygon winding).

For n in 10..14, R = 3n/4: shows winding number of s_n around |z|=R equals n,
hence all n zeros lie in |z|<R. Method:
  * Nodes t_j = 2*pi*j/N (N=16384). Disc arithmetic (center=complex float,
    radius=float, rigorously inflated) encloses f(t_j)=s_n(R e^{it_j}).
    Assumptions (documented): IEEE-754 correct rounding of +,-,*,/ (rel err
    <= eps=2^-53); math.cos/sin/hypot absolute error <= 8 ulp. Every radius
    update is inflated by (1+32eps) plus 1e-300 to dominate rounding of the
    radius computation itself; magnitude overestimates use L1-inflation.
  * Exact rational Lipschitz bound L_n = R*sum_{k<n} R^k/k! (Fractions) and
    rigorous pi upper bound (Machin, alternating-series remainder) give the
    inter-node tube radius L*Dt. Per-node check
        |c_j|_low > r_j + L*Dt_up + |c_{j+1}-c_j|_up
    implies the true arc + polygon segment convex hull avoids 0, so the true
    curve is homotopic to the polygon in C\\{0}.
  * Exact winding of the polygon (exact Fraction vertices from the stored
    doubles, positive-real-axis crossing count) equals n.
"""
from fractions import Fraction
import math, json

EPS = 2.0**-53
INFL = 1.0 + 32*EPS

def umag(re_, im_):
    """Rigorous upper bound on |(re,im)| (L1 majorant, inflated)."""
    return (abs(re_) + abs(im_)) * INFL + 1e-300

def cadd(c1, r1, c2, r2):
    re_ = (c1[0] + c2[0]); im_ = (c1[1] + c2[1])
    m1 = umag(*c1); m2 = umag(*c2)
    r = (r1 + r2 + 2*EPS*(m1 + m2)) * INFL + 1e-300
    return (re_, im_), r

def cmul(c1, r1, c2, r2):
    re_ = (c1[0]*c2[0] - c1[1]*c2[1]); im_ = (c1[0]*c2[1] + c1[1]*c2[0])
    m1 = umag(*c1); m2 = umag(*c2)
    r = (m1*r2 + m2*r1 + r1*r2 + 8*EPS*m1*m2) * INFL + 1e-300  # 8eps: 4 prods + Re/Im adds
    return (re_, im_), r

def atan_up(x, M):
    """Rigorous UPPER bound on atan(x), 0<x<1: Leibniz partial sum through an
    even index M (last included term positive) overestimates the alternating
    decreasing series; exact Fraction arithmetic."""
    assert M % 2 == 0
    return sum((Fraction(-1)**k * x**(2*k+1)) / Fraction(2*k+1) for k in range(M+1))

def atan_lo(x, M):
    """Rigorous LOWER bound on atan(x), 0<x<1: Leibniz partial sum through an
    odd index M (last included term negative) underestimates; exact Fractions."""
    assert M % 2 == 1
    return sum((Fraction(-1)**k * x**(2*k+1)) / Fraction(2*k+1) for k in range(M+1))

# Machin: pi = 16*atan(1/5) - 4*atan(1/239); upper bound needs U(1/5) and L(1/239).
PIU = 16*atan_up(Fraction(1,5), 8) - 4*atan_lo(Fraction(1,239), 3)
print("rigorous pi upper bound:", float(PIU), "(math.pi =", math.pi, ")")
assert float(PIU) >= math.pi and float(PIU) - math.pi < 1e-9

N = 16384
Dt_up = 2*PIU / N + 64*Fraction(2)**-53  # upper bound on max inter-node
                                     # spacing incl. rounding slack of fl(2*pi*j/N)
TRIG = 8*2.0**-53         # assumed libm abs err bound (8 ulp, generous)
PH = 16*EPS*2*float(PIU)  # phase error bound |t_tilde - t| (rounding of 2*pi*j/N + pi err)

results = {}
for n in range(10, 15):
    Rf = 0.75*n
    R = Fraction(3*n, 4)
    # exact Lipschitz bound L = R * sum_{k<=n-1} R^k/k!
    S = sum((R**k) / Fraction(math.factorial(k)) for k in range(n))
    L = R * S
    tube = L * Dt_up  # exact Fraction
    a = []
    for k in range(n+1):
        v = 1.0/math.factorial(k)
        a.append(((v, 0.0), 2*EPS*v))
    centers = []
    radii = []
    for j in range(N):
        t = 2*math.pi*j/N
        ct = math.cos(t); st = math.sin(t)
        zc = (Rf*ct, Rf*st)
        m = umag(*zc)
        rz = (Rf*(TRIG + PH) + 2*EPS*m) * INFL + 1e-300
        p, rp = a[n]
        for k in range(n-1, -1, -1):
            (p, rp) = cmul(p, rp, zc, rz)
            (p, rp) = cadd(p, rp, a[k][0], a[k][1])
        centers.append(p); radii.append(rp)
    centers.append(centers[0]); radii.append(radii[0])
    tube_f = float(tube)
    min_abs = min(math.hypot(*c) for c in centers)
    max_r = max(radii)
    worst = 0.0; ok = True
    for j in range(N):
        c0 = centers[j]; c1 = centers[j+1]
        lo = math.hypot(*c0)*(1-16*EPS) - 1e-300  # 8 ulp abs err <= 16eps rel (ulp(x)<=2eps|x|)
        seg = math.hypot(c1[0]-c0[0], c1[1]-c0[1])*(1+16*EPS) + 1e-300
        need = radii[j] + tube_f + seg
        worst = max(worst, need/lo)
        if not (lo > need):
            ok = False; print(f"n={n}: FAIL at j={j}"); break
    Cf = [(Fraction(c[0]), Fraction(c[1])) for c in centers]
    wind = 0
    for j in range(N):
        (x0, y0), (x1, y1) = Cf[j], Cf[j+1]
        if (y0 <= 0 < y1) or (y1 <= 0 < y0):
            xc = (x0*y1 - x1*y0)/(y1 - y0)
            if xc > 0:
                wind += 1 if (y0 <= 0 < y1) else -1
    print(f"n={n} R={Rf}: L={float(L):.3e} tube={tube_f:.3e} min|c|={min_abs:.2f} "
          f"max_r={max_r:.2e} worst_need/lo={worst:.4f} homotopy_ok={ok} EXACT_winding={wind}")
    results[n] = {"R": Rf, "N": N, "L": float(L), "tube": tube_f, "min_abs": min_abs,
                  "max_radius": max_r, "worst_ratio": worst, "homotopy_ok": ok, "winding": wind}

with open("outer_cert_summary.json", "w") as f:
    json.dump(results, f, indent=1)
assert all(v["homotopy_ok"] and v["winding"] == k for k, v in results.items())
print("OUTER CERTIFICATE: PASS (all n, winding == n)")
