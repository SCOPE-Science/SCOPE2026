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
The proof is analytic. The support-function formula follows from an exact one-variable maximization, and the mean-width identity follows from the exact density of \(|U_1|\) and elementary substitutions. No finite experiment is used to infer an infinite statement.

The packaged `verify.py` carries out supplementary numerical checks. It compares the piecewise support function against direct numerical maximization over the feasible meridian, numerically integrates mean width for several dimensions and separations, verifies the \(n=3\) specialization against Finch's formula, and checks strict decrease on sampled grids. Its success condition is `VERIFY_OK`.

The checker does not establish literature originality and does not replace the analytic proof. The unresolved historical risk concerning equivalent quermassintegral formulas is recorded in the review materials.
