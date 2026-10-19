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

# Reproduction and proof boundaries

Run `python3 check.py` using the Python 3 standard library. This checks the closed radial-eigenvalue integrals at several radii by an independent composite Simpson quadrature, verifies adjacent eigenvalue differences, checks equal top levels and the decreasing tail at the unit-area disk in a finite band, and verifies the optimized annular test value and its positive gap.

The mathematical certificate of the claim is the analytic derivation in `RESULT.md`: Hermite completeness, angular orthogonality, explicit infinite-index difference factorization, phase-space translation covariance, elementary differentiation of annular energy, and the strict integral inequality for the logarithm. The checker is not an exhaustive verification of infinitely many modes or all possible domains. Numerical output is approximate; the strict claim is proved symbolically.

The displayed disk concentration is an exact supremum over all signals. The displayed annular concentration is an explicitly attained **lower bound**, not a claimed exact operator norm; within the restricted class of the fixed input and concentric area-one annuli, the maximum is exact and unique. External independent assessment has not been performed.
