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

The theorem is certified here by a direct analytic derivation: Gram normal equations for the affine projection, exact coefficient sums for each product geometric kernel, uniformly bounded cross sums when boundary points are distinct, and the finite-coefficient high-degree weight limit for each positive parameter.

The script `check_moments.py` was executed with Python's standard library and completed successfully. It checks several complex target points, three polynomial cutoffs, and positive weights including values below and above one. It verifies that the high-degree weighted zero formula agrees numerically with the unweighted block moment ratio at fixed cutoff, and that the latter approaches the intended target as cutoff increases.

These checks are finite sanity checks, not an exhaustive enumeration and not a proof of density. The proof does not give a practical degree bound or address the zero-parameter Hardy endpoint. No external independent audit has been performed.
