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

The file `verify.py` was executed from this package's source code on 2026-10-17 UTC with Python and NumPy available; it printed `PASS 4675 checks` after three seeded Gaussian comparisons. Exact rational enumeration establishes finite-sample conditional-unbiasedness and conditional-variance checks for many small dimensions and sample selections. Independent integer searches check minimizer formulas and gamma-function reductions. The Gaussian simulation verifies only finite examples (observed/theory squared-risk ratios 0.99684, 1.00783, 0.99709), not any universal theorem.

The exact mixture distribution, infinite-moment threshold, full range of integer parameters and optimal real allocation follow from the written proof, not numerical enumeration. No independent human audit or other validation is claimed. No external data or internet access is necessary to run the checks.
