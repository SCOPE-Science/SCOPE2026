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
# Verification notes

Execute `python verify.py` in an environment with Python 3 standard library. The script uses `fractions.Fraction` for exact constrained minimizers and recurrences. It independently computes the capped least-squares step, compares its result with the hypothetical linear recurrence, and checks the analytic first-crossing formula for cap three against exact rational trajectories over a parameter grid. It also checks affine-translation and initial-error-sign invariance, a repeated-root instance, and the rational witness at \(q=9/10\).

Observed result: `VERIFY_OK; exact-rational supplementary checks: 2580`.

These finite tests are not proofs of the assertions for all real parameters or indefinitely many iterations. Their proof is the monotone scalar projection and exhaustive real/complex characteristic-root classification in `RESULT.md`. The cosine stopping formula and square-root asymptotic are derived analytically. This verification does not test floating-point precision, perturbations, nonlinear mappings, or higher-dimensional Anderson acceleration. Independent audit has not been performed.
