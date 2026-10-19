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
Run `python3 check.py` in the directory containing the extracted science files. The self-contained script uses Python's standard library, independently expands the polynomial coefficients of \((z_1+z_2)f\), checks Gram identities, and tests the analytic upper bound for a deterministic range of real parameters and complex coefficients. A successful run reports eleven exact rational identities, 12,008 sampled/equality configurations, 100 phase-extremizers, and 2,400 independently expanded coefficient checks.

The correctness argument is the generalized Rayleigh optimization and maximum-modulus proof printed in RESULT.md. Finite checks do not establish a continuum theorem, and numerical tolerances in the sampled comparisons are not rigorous interval certificates. Publication priority is not externally certified. Independent audit has not been performed.
