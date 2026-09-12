"""Recovery test (OT sign convention): exactly-solvable 1D Gaussian Schrodinger bridge.

H(rho|m) = int rho log rho (OT sign: NEGATIVE Shannon entropy, up to constants
that cancel in differences). mu0 = N(m0,s0^2), mu1 = N(m1,s1^2), reference
Brownian diffusivity eps. Static optimizer covariance c solves
c/(s0^2 s1^2 - c^2) = 1/eps. Dynamic marginal mu_t = N(mean_t, v_t),
  v_t = (1-t)^2 s0^2 + t^2 s1^2 + 2 t(1-t) c + eps t(1-t).
OT gap(t) = H(mu_t) - [(1-t) H0 + t H1]
         = -{ 0.5*log(v_t) - [(1-t)*0.5*log(s0^2) + t*0.5*log(s1^2)] }.
K=0 theory: exact convexity (H''>=0), so max OT gap <= 0.
eps-mechanism: excess(t) = gap(t) - gap_lim(t) should be O(eps) with
Fisher-scaled constant; report max|excess|/eps.
"""
import numpy as np, json

def bridge(s0, s1, m0=0.0, m1=1.0, eps=0.01, nt=20001):
    c = (-eps + np.sqrt(eps**2 + 4*s0**2*s1**2)) / 2.0
    t = np.linspace(0, 1, nt)
    v = (1-t)**2 * s0**2 + t**2 * s1**2 + 2*t*(1-t)*c + eps*t*(1-t)
    v0 = ((1-t)*s0 + t*s1)**2  # eps=0 limit (c -> s0*s1)
    chord = (1-t)*0.5*np.log(s0**2) + t*0.5*np.log(s1**2)
    gap_OT = -(0.5*np.log(v) - chord)      # OT sign
    gap_lim_OT = -(0.5*np.log(v0) - chord)  # limit geodesic profile (<=0 by -log convexity)
    excess = gap_OT - gap_lim_OT
    return t, gap_OT, gap_lim_OT, excess

out = {}
for name, (s0, s1, m0, m1) in {"symmetric_narrow": (0.1, 0.1, -0.5, 0.5),
                               "asymmetric": (0.1, 0.3, 0.0, 1.0),
                               "wide": (0.5, 0.5, -0.5, 0.5)}.items():
    print(f"{name} (s0={s0}, s1={s1}):")
    rows = []
    for eps in [0.05, 0.02, 0.01, 0.005, 0.002]:
        t, gap, glim, exc = bridge(s0, s1, m0, m1, eps)
        rows.append(dict(eps=eps, max_OT_gap=float(gap.max()),
                         max_abs_excess=float(np.abs(exc).max()),
                         excess_ratio=float(np.abs(exc).max()/eps),
                         lim_profile_max=float(glim.max())))
        print(f"  eps={eps:<7} max OT gap={gap.max():+.6f} (exact K=0 bnd: <=0)  "
              f"max|excess|={np.abs(exc).max():.6f}  ratio/eps={np.abs(exc).max()/eps:.4f}")
    out[name] = rows

with open('output/artifacts/gaussian_bridge.json', 'w') as f:
    json.dump({"sign": "OT (H = int rho log rho)", "cases": out}, f, indent=2)
print("saved output/artifacts/gaussian_bridge.json")
