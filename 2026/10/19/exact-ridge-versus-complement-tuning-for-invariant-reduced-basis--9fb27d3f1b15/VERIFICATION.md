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

# Reproducibility

Run `python verify.py` with Python 3 and NumPy. The deterministic program verifies exact preconditioned eigenvalue identities for Type I and II, lower bounds for every trial scalar, formula equality at optimum, endpoint cases, and the arbitrarily large separation family, reporting 153030 comparisons when complete. It uses 3000 pseudorandom diagonal SPD examples with a fixed seed, also enforcing repeated eigenvalues. These finite checks are corroboration only; the proof in `RESULT.md` establishes claims for all admissible dimensions and positive spectral endpoints.

Numerical comparisons have explicitly stated floating-point tolerances and do not certify infinite-dimensional behavior or numerical stability for nearly singular matrices.
