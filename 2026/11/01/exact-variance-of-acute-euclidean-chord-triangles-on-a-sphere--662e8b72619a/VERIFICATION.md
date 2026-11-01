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

# Reproduction and scope of verification

Run the embedded standard-library checker using `python3 verify.py` (Python 3.8 or later; no third-party packages required). The program contains deterministic exact rational checks of the coefficient identities, exhaustive finite counting of pairs of three-element subsets for \(3\le n\le9\), midpoint numerical quadrature of the exact conditional formula, and seeded direct spherical-point simulations at \(n=4,5,6\). The final printed line in the original run was `ALL_CHECKS_PASSED`.

The exact mean and covariance formulas are proved analytically in `RESULT.md`. The checker verifies related finite identities, implementation normalizations, and stochastic agreement; finite tests and numerical quadrature do not establish identities for every sample size or historical originality. The independent mathematical audit is not performed.
