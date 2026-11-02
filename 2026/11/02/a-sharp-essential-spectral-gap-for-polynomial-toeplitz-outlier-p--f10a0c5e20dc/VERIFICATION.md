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

# Verification scope

The proof in `RESULT.md` is an infinite-dimensional analytic proof. The supplied `checker.py` uses no external packages and checks its finite algebraic consequences as well as finite truncations of the harmonic-Bergman Toeplitz operator. A finite truncation is not used as an infinite-dimensional proof. Reproduce using `python3 checker.py`.

The checker directly evaluates normalized monomial projection coefficients, builds the constructed eigenfunction's analytic Taylor coefficients after removing its removable singularity, and compares the operator action against its claimed eigenvalue. It checks numerical root and maximum-gap identities across many degrees, including large-degree asymptotic illustrations. Exact structural premises appear separately in the proof and cited spectral theorems.

# Limits

Numerical tolerances apply only to the supplemental finite tests. No independent audit, external proof certificate, or global classification of all exceptional eigenvalues has been performed. The older low-degree article was not available in complete form during source comparison.
