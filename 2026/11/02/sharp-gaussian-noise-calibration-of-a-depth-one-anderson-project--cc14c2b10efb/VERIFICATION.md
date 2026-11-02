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

The complete derivation is in `RESULT.md`. Exact algebra verifies the independent midpoint/difference Gaussian decomposition, the projection-error identity, the mean-square integrand, and its derivative. The proof of the unregularized moment threshold uses positivity of a Gaussian density at zero; the tail constant follows from conditional density integration and dominated convergence.

The standalone `verify.py` uses rational arithmetic for a family of pointwise identities and numerical Gaussian quadrature for several numerical parameter sets. Finite numerical checks are corroboration, not a substitute for the analytic arguments. The independent audit has not been performed.
