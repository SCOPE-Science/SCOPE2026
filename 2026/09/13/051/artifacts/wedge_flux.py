"""Wedge-flux verification for the fixed-s 120-degree-law calculation.

Computes the unnormalized 2D fractional mean curvature of
S(beta)={0<=arg<=beta} at p=(1,0), then multiplies by the exact
cylinder factor B(s) for S(beta) x R in R^3.

The subtraction is from the tangent half-plane T={v>0}.  For beta<pi,
S(beta) is a subset of T and H=+2 int_{beta<arg<pi} K.  For beta>pi,
T is a subset of S(beta) and H=-2 int_{pi<arg<beta} K.  Both difference
wedges are a positive distance from p for beta in (0,2pi), beta != 0,2pi,
so the displayed difference integrals are absolutely convergent.

The tail substitution r=1/u is implemented with the correct scaled
kernel, which also makes the off-center scaling test H_d=d^{-s}H_1
numerically exact up to quadrature error.
"""
import json
import math
import numpy as np

trapz = np.trapz

def _wedge_interval(beta):
    if abs(beta - math.pi) < 1e-12:
        return None
    if beta < math.pi:
        return beta, math.pi, 1.0
    return math.pi, beta, -1.0

def H_wedge(beta, s, d=1.0, Rmult=10.0, Nr=6000, Np=720):
    """2D fractional curvature of S(beta) at p=(d,0), d>0."""
    assert 0.0 < beta < 2.0 * math.pi
    assert 0.0 < s < 1.0 and d > 0.0
    interval = _wedge_interval(beta)
    if interval is None:
        return 0.0
    a0, a1, sign = interval
    phi = np.linspace(a0, a1, Np)
    c = np.cos(phi)
    Rmax = Rmult * d

    r = np.linspace(0.0, Rmax, Nr + 1)
    D = r[None, :] ** 2 - 2.0 * d * r[None, :] * c[:, None] + d * d
    with np.errstate(divide="ignore", invalid="ignore"):
        bulk_dens = r[None, :] * D ** (-(2.0 + s) / 2.0)
    bulk_dens[:, 0] = 0.0
    bulk = trapz(bulk_dens, r, axis=1)

    # Tail r in [Rmax,infinity).  With r=1/u:
    # r dr / (r^2-2 d r cos(phi)+d^2)^((2+s)/2)
    # = u^(s-1) (1-2 d u cos(phi)+d^2 u^2)^(-(2+s)/2) du.
    # Regularize u=(1/Rmax)t^(1/s).
    t = np.linspace(0.0, 1.0, Nr // 4 + 1)
    u = (1.0 / Rmax) * t ** (1.0 / s)
    G = (1.0 - 2.0 * d * u[None, :] * c[:, None]
         + (d * u[None, :]) ** 2) ** (-(2.0 + s) / 2.0)
    tail = ((1.0 / Rmax) ** s / s) * trapz(G, t, axis=1)
    return float(sign * 2.0 * trapz(bulk + tail, phi))

def B_const(s):
    """int_R (1+u^2)^(-(3+s)/2) du."""
    return math.sqrt(math.pi) * math.gamma(1.0 + s / 2.0) / math.gamma((3.0 + s) / 2.0)

def analytic_LB_2d(s):
    Dmax = math.hypot(1.0 + math.sqrt(3.0) / 2.0, 0.5) + 0.5
    return (math.pi / 2.0) / (Dmax ** (2.0 + s))

if __name__ == "__main__":
    beta120 = 2.0 * math.pi / 3.0
    out = {}

    rows = []
    for s in [0.75, 0.8, 0.85, 0.9, 0.95]:
        num = H_wedge(beta120, s)
        lb = analytic_LB_2d(s)
        b = B_const(s)
        rows.append({
            "s": s,
            "H2d_numeric": num,
            "H2d_analytic_LB": lb,
            "B": b,
            "H3d_analytic_LB": b * lb,
            "LB_holds": bool(num >= lb),
        })
    out["beta120_sweep"] = rows

    sweep = []
    for deg in [90, 100, 110, 120, 130, 150, 180, 210, 240, 270]:
        sweep.append({"deg": deg, "H": H_wedge(math.radians(deg), 0.75)})
    out["angle_sweep_s075"] = sweep

    h1 = H_wedge(beta120, 0.75)
    scaling = []
    for d in [0.5, 1.0, 2.0]:
        hd = H_wedge(beta120, 0.75, d=d)
        pred = h1 * d ** (-0.75)
        scaling.append({
            "d": d,
            "Hd": hd,
            "predicted": pred,
            "rel_err": abs(hd - pred) / abs(pred),
        })
    out["scaling_s075"] = scaling

    Dmax = math.hypot(1.0 + math.sqrt(3.0) / 2.0, 0.5) + 0.5
    h2_uniform = (math.pi / 2.0) / (Dmax ** 3.0)
    bs = [B_const(s) for s in np.linspace(0.75, 0.999, 25)]
    out["uniform"] = {
        "H2d_uniform_LB": h2_uniform,
        "B_min": min(bs),
        "B_max": max(bs),
        "H3d_uniform_LB": min(bs) * h2_uniform,
        "note": "analytic lower bound from an inscribed radius-1/2 disk in the beta=120deg difference wedge",
    }

    with open("wedge_flux_results.json", "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, allow_nan=False)
        f.write("\n")
    print(json.dumps(out, indent=2, allow_nan=False))
