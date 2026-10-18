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

# Verification and reproducibility

The six scientific files and a standalone checker accompany the result. Run `python verify_diagonal_pyramid.py` in an environment with Python 3, SymPy and SciPy.

The checker independently derives the Gaussian moments, confirms the exact rational second-order coefficients and the dimension-three optimizer, and evaluates the Fourier integral numerically for selected larger dimensions. Its assertions check only those reproducible finite identities and examples. The universal log-concavity argument, analytic bounds on Fourier tails, and asymptotic error estimates are part of the written proof and are not independently machine-certified.

For the precise claim, the asymptotic offset is in coordinate-sum units. No unrestricted high-dimensional optimality is asserted for non-diagonal hyperplanes. Historical priority beyond the reported source inspections is unverified.
