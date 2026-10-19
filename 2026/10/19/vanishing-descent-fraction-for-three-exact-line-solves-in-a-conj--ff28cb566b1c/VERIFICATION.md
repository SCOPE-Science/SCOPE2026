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

# Reproducibility and proof limits

Run `python verify.py` with Python 3 standard library. The verifier recomputes exact rational coefficients for each integer \(3\le N\le256\), confirms the preconditioned proximal-gradient optimality certificate, Hessian conjugacy, strict line-minimizer conditions, exact values along the resulting directions, the independent full-model optimality certificate, and the rational relative-decrease identity. It also checks exact benchmark values and algebraically bounded asymptotic scaling. Its checks use decoded embedded source bytes from the deliverable package and do not depend on external files or services.

The symbolic proof in `RESULT.md` establishes the statement for all integers \(N\ge3\). The finite executable sample cannot certify an infinite quantifier or prove originality. The reference's claimed convergence behavior and the model-level quantified approximation gap are distinct statements. Scientific self-review passed; independent audit is not performed.
