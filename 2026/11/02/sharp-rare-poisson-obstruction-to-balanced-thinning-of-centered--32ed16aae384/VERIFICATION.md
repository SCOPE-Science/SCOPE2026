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

# Verification of the stated rare-event theorem

The standalone script `verification/poisson_thinning_verify.py` was executed with Python 3 from the delivered package, and `verification/output.txt` records its output: 2,210 assertions passed. Finite-row enumeration evaluates joint Bernoulli-selector probabilities in exact rational arithmetic and checks centering; Poisson absolute-deviation values and integer-supremum inequalities are cross-compared numerically. Exact numerical sample checks at finitely many inputs are not proof of the continuum optimization. The proof instead uses a Poisson convergence and uniform-integrability argument, a telescoping Poisson deviation identity, convexity of the logarithm of the ratio on each integer interval, and explicit Robbins factorial bounds at all integer endpoints. The public result is not independently audited or validated.
