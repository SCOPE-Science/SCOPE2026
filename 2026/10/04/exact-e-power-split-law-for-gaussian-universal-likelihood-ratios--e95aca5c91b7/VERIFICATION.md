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

# Verification

The proof reduces to exact Gaussian expectations and a one-line forward-difference identity. `verify.py` checks the algebraic forward difference, exhaustive finite-sample agreement with the threshold characterization, the positivity threshold, representative local limits, and the fixed-signal scaling.

The numerical program is not used to infer an infinite statement. The proof in `RESULT.md` establishes the theorem for all stated \(n,m,\mu\); the program is a reproducibility check on exact formulas and representative limits.

Unproved extensions include unknown variance, multivariate means, composite nulls, data-dependent split selection, and equivalence between e-power optimality and finite-threshold rejection-power optimality.
