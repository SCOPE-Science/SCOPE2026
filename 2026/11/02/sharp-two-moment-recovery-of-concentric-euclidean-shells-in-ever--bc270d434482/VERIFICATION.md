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

The derivation was checked directly from the radial density and isotropic covariance identity. Exact rational formulas were evaluated in dimensions 2 through 12 at seven rational radius ratios; a separate rational grid of 200 shapes per dimension showed the stated strict ordering. Independent Gaussian-direction and radial inverse-CDF sampling used 65,000 point pairs for each of six dimension/shape combinations. Exact rational arithmetic was used for high-order endpoint-coefficient checks to avoid cancellation.

Run the included `verify_shell_moments.py` with Python 3; no external dependencies are needed. The checks ended in `ALL_CHECKS_PASSED`. Finite grids and simulations support normalization and detect errors; the displayed calculus proof supplies strict monotonicity, all-dimensional quantifiers and the sharp inverse exponents. The checker does not establish historical priority, sample-based recovery guarantees or independent mathematical validation.
