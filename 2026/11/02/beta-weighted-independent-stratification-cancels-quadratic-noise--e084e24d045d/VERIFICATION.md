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

# Reproducibility and verification

The standalone `verify.py` uses only the Python standard library. Run `python3 verify.py` in the extracted package directory. It checks exact rational Beta moments and covariance, pathwise polynomial exactness, cubic unbiasedness, finite-sample cubic variance, the uniform benchmark moment, and the quartic variance asymptotic using an exact finite-sample expression. Seeded beta variates are converted to rational numbers for deterministic identity checks.

The proof of uniform Taylor remainders, the universal density uniqueness, the Lindeberg limit and the Hoeffding inequality is analytic and is explained in `RESULT.md`. Finite checks do not certify an infinite quantifier. Floating-point cancellation near the beta endpoints, general multidimensional integration, and optimality outside the specified independent fixed-density family are not verified.
