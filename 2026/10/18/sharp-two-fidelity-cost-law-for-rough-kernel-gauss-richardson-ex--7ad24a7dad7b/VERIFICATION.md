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

The algebraic proof in RESULT.md establishes the global finite-budget lower bound, matching asymptotic construction, and uniqueness of the asymptotic optimal ratio. Execute `python checker.py` to replay the symbolic covariance-inverse, normalization and extremizer identities, together with 114 completed symbolic/numerical consistency assertions. Numerical tests are supporting checks, not substitutes for the uniform inequality or limiting-uniqueness argument.

The result assumes a fixed Gaussian-process scale and a known exponential normalized-error kernel. Neither frequentist coverage nor independent mathematical validation is certified here.
