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

# Reproducibility and verification

Run `python verify.py` using Python 3.9 or later. It has no third-party package dependencies. The script checks 108 exact-rational four-agent vector-field reductions using nontrivial within-camp weights, rejects a non-equitable exposure configuration via distinct initial signed derivatives, reconstructs the exactly solvable critical trajectory, checks the supercritical leader limit, and checks the predicted subcritical square-root asymptotics for two distinct sets of parameters with a fourth-order Runge–Kutta integrator. The observed run output was:

```
PASS: 108 exact four-node vector-field comparisons; nonconstant cross-exposure countercheck; exact critical solution; four numerical asymptotic checks
```

These are tests of arithmetic, formulas and finite-time numerics. The proof in RESULT.md—not this script—establishes all quantified assertions and limits as time grows without bound. The numerical integration does not certify full-space attraction or historical originality.
