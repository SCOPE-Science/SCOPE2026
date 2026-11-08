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

# Verification record

The mathematical argument proves the support-function identity for all integer parameters, the Gaussian radial normalization, the one-dimensional order-statistic formula, the normalized limit for every sequence with positive finite label density, and the differentiability transition at half density.

For independent computational corroboration of these algebraic and probabilistic steps, run `python check_width.py` with the package dependencies installed from `requirements.txt`. The checker enumerates all allowed vertex-label assignments for small dimensions, compares their maxima with the sorted-coordinate optimizer, compares exact one-dimensional Gaussian integrals with seeded numerical Gaussian averages, and checks the predicted asymptotic profile at four density ratios. The observed terminal marker was `PARTIAL_PERMUTOHEDRON_GAUSSIAN_WIDTH_CHECKS_PASSED`.

Numerical sampling does not certify infinite-dimensional limits, uniqueness of prior discovery, or source coverage. The limiting result rests on the analytical empirical-quantile and uniform-integrability proof. Independent mathematical audit has not been performed.
