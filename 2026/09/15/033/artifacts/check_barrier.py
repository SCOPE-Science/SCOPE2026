"""Check the Dodson Sec.10 energy-bootstrap barrier for mass-critical NLS.

Verifies that the residual exponent in Dodson (10.41)-(10.44) cannot beat 2^{-2kn}
for d>=16, under the truncation/free-parameter generalization, while the companion
1+4/d term remains feasible. Pure arithmetic; no external data.
"""
import json, os

def min_deficit_needed(d):
    # Dodson d>=9 energy bootstrap: residual needs (8/d - 3/(5d) - 7/(10d^2) - c*delta...) ;
    # generalized feasibility: delta <= (77 - 5d)/39 for the 1+8/d remainder term.
    return (5*d - 77)/39.0  # >0 means infeasible; (77-5d)/39 < 0

def companion_max_deficit(d):
    # 1+4/d remainder term Young exponent 2d/(d-4): feasible iff delta <= 17/(5d-1)
    return 17.0/(5*d - 1)

def dodson_residual_exponent(d):
    # literal Dodson choice (delta=0): (8/d - 3/5d - 7/10d^2) * 2d/(d-8)
    # At d=8 the remainder is ||e||^{1+8/8}=||e||^2: absorbed directly, no Young loss.
    if d == 8:
        return float("inf")
    return (8.0/d - 3.0/(5*d) - 7.0/(10*d*d)) * (2*d/(d-8))

rows = []
for d in [8, 9, 10, 12, 15, 16, 17, 20, 30]:
    rows.append({
        "d": d,
        "dodson_residual_exponent": round(dodson_residual_exponent(d), 5),
        "beats_2kn": bool(dodson_residual_exponent(d) >= 2.0),
        "min_extra_deficit_for_feasibility": round(min_deficit_needed(d), 5),
        "generalized_feasible": bool(min_deficit_needed(d) <= 0),
        "companion_max_deficit": round(companion_max_deficit(d), 5),
    })

out = {"rows": rows,
       "conclusion": "Dodson literal residual beats 2^{-2kn} iff d<=15; "
                     "generalized 1+8/d-term feasibility requires (77-5d)/39>=0, "
                     "empty for d>=16; companion 1+4/d term stays feasible."}
print(json.dumps(out, indent=1))
os.makedirs(os.path.dirname(os.path.abspath(__file__)), exist_ok=True)
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "barrier_check.json"), "w") as f:
    json.dump(out, f, indent=1)
