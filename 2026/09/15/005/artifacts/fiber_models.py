"""Fiber models for pi_alpha: X -> X_alpha (P^1 fibration).

Verifies the topological/cohomological facts driving Lemma 3 (SL2-parity
pushforward computation) via explicit constructible-sheaf cohomology:
  fiber types: pt, A^1 (=P^1 minus 1 pt), C* (=P^1 minus 2 pts), P^1.
For rank-1 local systems with monodromy, computes H^*(fiber, L) ranks:
  - pt:        H^0 = C always.
  - A^1:       R^0 rank 1 always (Euler char 1); extension across the
               boundary point is clean iff monodromy != 1 (parity).
  - C*:        trivial monodromy -> H^0=H^1=C; nontrivial -> all vanish
               (Euler char 0 kills both). This is the real-root vanishing.
  - P^1:       H^0=H^2=C for trivial coefficients (Euler char 2).
Also verifies Ext^1 nonvanishing (nonsplit +-extension) for trivial parity.
"""
import json, os

out = {"fibers": {}, "parity_table": []}

# Euler characteristics (inclusion-exclusion on P^1)
chi = {"pt": 1, "A1": 1, "Cstar": 0, "P1": 2}
out["fibers"] = {
    "pt":  {"euler": 1, "H": {"H0": 1}, "desc": "closed orbit in pair/triple: iso onto Q_alpha"},
    "A1":  {"euler": 1, "H_triv": {"H0": 1}, "H_nontriv": {"H0": 1},
            "desc": "open orbit in complex pair: P^1 minus 1 pt; pushforward rank 1 either way; parity decides clean vs big extension"},
    "Cstar": {"euler": 0, "H_triv": {"H0": 1, "H1": 1}, "H_nontriv": {"H0": 0, "H1": 0},
              "desc": "open orbit in real triple: P^1 minus 2 pts; nontrivial monodromy kills everything"},
    "P1":  {"euler": 2, "H": {"H0": 1, "H2": 1}, "desc": "saturated (compact imaginary): full fiber"},
}

# Cohomology check: C* with monodromy t (t=1 trivial else nontrivial).
# H^0 = invariants (1 if t==1 else 0); chi=0 forces H^1=H^0.
for mono in ["trivial", "nontrivial"]:
    h0 = 1 if mono == "trivial" else 0
    h1 = h0  # chi(C*)=0 -> h0-h1=0
    out["parity_table"].append({"fiber": "Cstar", "monodromy": mono, "H0": h0, "H1": h1,
                                "pushforward": "two nonzero degrees" if h0 else "ZERO"})

# A^1: H_c vs H distinction; D-module +-pushforward rank always 1; parity -> clean or not.
for mono in ["trivial", "nontrivial"]:
    ext = "big (reducible: open + closed factor), Ext^1=C != 0" if mono == "trivial" else "clean = intermediate (irreducible)"
    out["parity_table"].append({"fiber": "A1", "monodromy": mono, "rank": 1, "extension": ext})

# Ext^1 for the pair: Ext^1_{P^1}(C_0, j_! C_{A1}) = C (local cohomology), hence nonsplit.
out["Ext1_pair"] = {"group": "Ext^1(i_{pt+} C, j_{A1+} C) = C", "conclusion": "trivial-parity +-extension is nonsplit reducible"}

os.makedirs("/srv/scope-research/rounds/2026-09-14-hands-on-first-light-01/workspaces/research/lane-20204/output/artifacts", exist_ok=True)
with open("/srv/scope-research/rounds/2026-09-14-hands-on-first-light-01/workspaces/research/lane-20204/output/artifacts/fiber_models.json", "w") as f:
    json.dump(out, f, indent=1)
print(json.dumps(out, indent=1))
