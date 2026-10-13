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

Run `python verify.py` with Python 3 standard library in this directory. The checker enumerates all 64 sign vectors with exact fractions, builds both endpoint distributions from their stated conditional laws, verifies 6 univariate and 15 bivariate constraints for each, and confirms rejection probabilities 0 and 1/6 and independent benchmark 3/64. It also verifies five mixtures and the pointwise inequality used in the upper bound. Its successful output was: `PASS: exact six-sign calibration, both sharp extremizers, mixtures, and moments`.

Independently, a 64-variable pairwise-moment linear program evaluated with SciPy HiGHS returned minimum 0 and maximum 0.16666666666667. This numerical experiment is corroborative, not an infinite or symbolic proof. The proof of sharpness and the continuous, pairwise-independent observation construction is supplied in RESULT.md and does not rely on these computations.

The verified object is only the six-rank cutoff, not the asymptotic behavior of general signed-rank tests, and not the entire null class of pairwise-independent observations without conditioning on magnitudes. Historical originality has not been independently certified.
