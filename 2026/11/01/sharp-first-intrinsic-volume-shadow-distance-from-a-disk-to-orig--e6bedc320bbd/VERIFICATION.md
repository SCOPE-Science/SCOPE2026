---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Reproduction and checks

Run the accompanying standard-library script using `python3 verify_shadow_polygon.py`. The actual script execution reported `PASS: 5376 checks`. It compares the analytic support-function minimizer with an independently integrated signed primitive, checks thousands of signed-cosine dual inequalities on random local cells, tests random irregular convex polygons containing the origin, checks finite differences of the strict-convexity formula, and checks large-vertex-number asymptotics.

Representative numerical values are \(F_3=0.454598272016\), \(F_4=0.250655662336\), \(F_{12}=0.027029330712\); the predicted leading scaled limit is \(\pi^3/8\approx3.875784585037\). The verified source code, not pasted terminal output, is embedded separately for reproducibility.

**Proof boundary:** finite samples cannot verify universal quantifiers. The analytic signed normal-cone witness, strict convexity, and exact equality arguments in `RESULT.md` are necessary for correctness. The scope excludes polygons that do not contain the disk center. No independent external mathematical audit has been performed.
