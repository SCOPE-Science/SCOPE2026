"""Wedge-flux verification for fixed-s 120-degree-law disproof.

Computes the (unnormalized) 2D fractional mean curvature of a wedge sector
S(beta) = {0 <= arg <= beta} at boundary point p=(1,0):

  H(beta,s) = p.v. int_{R^2} (1 - 2*1_S(y)) / |p-y|^{2+s} dy.

Method: subtract the tangent half-plane T={v>0} (whose curvature is 0).
For beta<pi: H = +2 * int_{W} K dy, W = {beta < arg < pi} (angle pi-beta).
For beta>pi: H = -2 * int_{W'} K dy, W' below-axis wedge (angle beta-pi).
W is at positive distance from p, so the integral is absolutely convergent
(no principal value needed). Radial integral split at Rmax with exact
u=1/r tail transform for the tail piece. Pure numpy + math only.
"""
import math
import json
import numpy as np

trapz = np.trapz

def H_wedge(beta, s, Rmax=10.0, Nr=20000, Np=1440):
    """Unnormalized 2D fractional curvature of wedge of angle beta at p=(1,0)."""
    assert 0.0 < beta < 2.0 * math.pi
    if abs(beta - math.pi) < 1e-12:
        return 0.0
    if beta < math.pi:
        a0, a1, sign = beta, math.pi, 1.0
    else:
        # S\T wedge below axis: angles (-(beta-pi), 0) i.e. (2pi-(beta-pi), 2pi)
        a0, a1, sign = 2.0 * math.pi - (beta - math.pi), 2.0 * math.pi, -1.0
    phi = np.linspace(a0, a1, Np)
    c = np.cos(phi)  # shape (Np,)
    # bulk r in [0, Rmax]
    r = np.linspace(0.0, Rmax, Nr + 1)
    D = r[None, :] ** 2 - 2.0 * r[None, :] * c[:, None] + 1.0
    with np.errstate(divide="ignore", invalid="ignore"):
        bulk_dens = r[None, :] * D ** (-(2.0 + s) / 2.0)
    bulk_dens[:, 0] = 0.0
    bulk = trapz(bulk_dens, r, axis=1)
    # tail r in [Rmax, inf): u=1/r gives int_0^{1/Rmax} u^{s-1} G(u) du.
    # Regularize via u = (1/Rmax) t^{1/s}: tail = (1/Rmax)^s (1/s) int_0^1 G dt.
    t = np.linspace(0.0, 1.0, Nr // 4 + 1)
    uu = (1.0 / Rmax) * t ** (1.0 / s)
    G = (1.0 - 2.0 * uu[None, :] * c[:, None] + uu[None, :] ** 2) ** (-(2.0 + s) / 2.0)
    tail = ((1.0 / Rmax) ** s / s) * trapz(G, t, axis=1)
    return float(sign * 2.0 * trapz(bulk + tail, phi))

def B_const(s):
    """Exact R-integration factor: int_R (1+u^2)^{-(3+s)/2} du."""
    a = (3.0 + s) / 2.0
    return math.sqrt(math.pi) * math.gamma(a - 0.5) / math.gamma(a)

def analytic_LB_2d(s):
    Dmax = math.hypot(1.0 + math.sqrt(3.0) / 2.0, 0.5) + 0.5
    return (math.pi / 2.0) / (Dmax ** (2.0 + s))

if __name__ == "__main__":
    out = {}
    # 1. headline: beta = 2pi/3 across s in [3/4, 1)
    beta120 = 2.0 * math.pi / 3.0
    rows = []
    for s in [0.75, 0.8, 0.85, 0.9, 0.95]:
        num = H_wedge(beta120, s)
        lb = analytic_LB_2d(s)
        B = B_const(s)
        rows.append({"s": s, "H2d_numeric": num, "H2d_analytic_LB": lb,
                     "B": B, "I3d_LB": B * lb, "LB_holds": bool(num >= lb)})
    out["beta120_sweep"] = rows
    # 2. angle sweep at s=0.75 (zero only at pi)
    sweep = []
    for deg in [90, 100, 110, 120, 130, 150, 180, 210, 240]:
        b = math.radians(deg)
        sweep.append({"deg": deg, "H": H_wedge(b, 0.75)})
    out["angle_sweep_s075"] = sweep
    # 3. scaling check H(d) = d^{-s} H(1): via change of variables identity,
    # verify numerically by recomputing at p=(d,0) for the 120 wedge.
    def H_at_d(d, s):
        beta = beta120
        Np, Nr = 720, 12000
        Rmax = 10.0 * d
        phi = np.linspace(beta, math.pi, Np)
        c = np.cos(phi)
        r = np.linspace(0.0, Rmax, Nr + 1)
        D = r[None, :] ** 2 - 2.0 * d * r[None, :] * c[:, None] + d * d
        with np.errstate(divide="ignore", invalid="ignore"):
            bulk_dens = r[None, :] * D ** (-(2.0 + s) / 2.0)
        bulk_dens[:, 0] = 0.0
        bulk = trapz(bulk_dens, r, axis=1)
        t = np.linspace(0.0, 1.0, Nr // 4 + 1)
        umax = 1.0 / Rmax
        uu = umax * t ** (1.0 / s)
        G = (d * d - 2.0 * d * uu[None, :] * c[:, None] + uu[None, :] ** 2) ** (-(2.0 + s) / 2.0)
        tail = (umax ** s / s) * trapz(G, t, axis=1)
        return float(2.0 * trapz(bulk + tail, phi))
    sc = []
    H1 = H_wedge(beta120, 0.75)
    for d in [0.5, 1.0, 2.0]:
        Hd = H_at_d(d, 0.75)
        sc.append({"d": d, "Hd": Hd, "predicted": H1 * d ** (-0.75),
                   "rel_err": abs(Hd - H1 * d ** (-0.75)) / abs(H1 * d ** (-0.75))})
    out["scaling_s075"] = sc
    # 4. uniform bounds over [3/4,1)
    Dmax = math.hypot(1.0 + math.sqrt(3.0) / 2.0, 0.5) + 0.5
    uni_2d = (math.pi / 2.0) / (Dmax ** 3.0)
    Bs = [B_const(s) for s in np.linspace(0.75, 0.999, 25)]
    out["uniform"] = {"H2d_uniform_LB": uni_2d, "B_min": min(Bs),
                      "B_max": max(Bs), "I3d_uniform_LB": min(Bs) * uni_2d}
    print(json.dumps(out, indent=2))
    with open("wedge_flux_results.json", "w") as f:
        json.dump(out, f, indent=2)
    print("saved wedge_flux_results.json")
