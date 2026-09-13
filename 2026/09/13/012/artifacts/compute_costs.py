"""Exact arithmetic: helper-site counts, surface isoperimetry (cube vs gamma=2 box),
and Poisson face-growth cost model for the 5D 2-distinct-axes rule."""
import json, math

out = {}

# 1. Helper sites for a face-interior vertex (exactly 1 droplet neighbour on normal axis).
# Distinct rule needs >=1 more infected neighbour OFF the normal axis:
#   in-layer neighbours along the 4 in-face axes = 8 sites.
# Standard 2-neighbour rule needs >=1 more anywhere else: 8 off-axis + 1 above = 9 sites.
out["helper_sites"] = {"distinct_off_axis": 8, "standard_anywhere_else": 9}

# 2. Same-volume surface comparison: cube vs (L,L,L,L,gamma*L) box, gamma=2.
# Cube side s, V=s^5, F=10 s^4 -> F = 10 V^{4/5}.
# Box: V = gamma L^5, F = 8*(gamma L^4) + 2*(L^4) = (8g+2) L^4
#    -> F = (8g+2) (V/g)^{4/5} = (8g+2) g^{-4/5} V^{4/5}.
gamma = 2.0
cube_coef = 10.0
box_coef = (8 * gamma + 2) * (gamma ** (-4.0 / 5.0))
out["surface_coef_per_V45"] = {"cube": cube_coef, "gamma2_box": box_coef,
                               "ratio_box_over_cube": box_coef / cube_coef}
# Same-edge-L comparison (different volumes): cube F=10 L^4, box F=18 L^4.
out["surface_same_L"] = {"cube": 10.0, "gamma2_box": 8 * gamma + 2}

# 3. Single-face failure exponents (periodic-layer cascade model, proved in WORKLOG):
# P(face fails) = (1-p)^A [distinct] vs (1-p)^{2A} [standard], A = face area.
# Cost ratio per unit pA -> 1 vs 2.
for p, A in [(0.03, 81), (0.015, 256), (0.06, 16)]:
    cd = -math.log((1 - p) ** A)
    cs = -math.log((1 - p) ** (2 * A))
    out.setdefault("face_costs", []).append(
        {"p": p, "A": A, "distinct_cost": cd, "standard_cost": cs,
         "distinct_per_pA": cd / (p * A), "standard_per_pA": cs / (p * A)})

# 4. Poisson sufficient-event cost: S*(1-p)^h, h=8 vs 9 (in-layer helpers only).
for p, S in [(0.1, 256), (0.05, 625)]:
    out.setdefault("poisson_helper_cost", []).append(
        {"p": p, "S": S, "h8": S * (1 - p) ** 8, "h9": S * (1 - p) ** 9,
         "ratio_h8_h9": (1 - p) ** -1})

with open("output/artifacts/results_costs.json", "w") as f:
    json.dump(out, f, indent=2)
print(json.dumps(out, indent=2))
