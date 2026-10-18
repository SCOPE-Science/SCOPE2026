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

# Reproduction and verification

Run `python3 check.py` using Python 3 and its standard library. It verifies Gram-spectrum and pairwise determinant identities on deterministic pseudorandom samples for several measurement counts; confirms the exact \(m=2\) CDF by independent midpoint integration; and compares finite-sample simulations with exact mean determinants and small-tail leading coefficients. An actual replay from this package is required before relying on reported numerical checks.

The all-dimensional probability limit, the density-optimality statement, the exact inverse-moment boundary and the unique atomic expected-determinant optimum are mathematical deductions in RESULT.md, not finite computational certificates. The continuous-density and unconstrained-estimator hypotheses are essential. This is a self-review; no independent mathematical audit or certification has been performed.
