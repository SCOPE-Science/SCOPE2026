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

# Reproducibility and limits

The exact conditional Laplace transform is given in RESULT.md. Run `python verification.py` with Python 3 and the public `mpmath` package installed. The executable performs nine high-precision checks of the first and second transform derivatives at zero, six numerical integrations of those conditional moments against the exponential target density, five checks of the large-distance limiting normalized moments, and analytic-value substitutions at the two optimized rates. This executable has been run successfully from the delivered contents.

The exact moment-finiteness conditions, nonexistence of moments at critical values, and uniqueness of the two optimal rates are derived analytically in RESULT.md; no finite computations are used as proof of these infinite-domain statements. The numerical large-distance convergence checks are empirical corroboration rather than a uniform-convergence certificate. The first-passage model fixes one randomly sampled target for all resets and excludes target resampling.

Independent scientific audit has not been performed.
