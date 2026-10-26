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
# Reproducibility

Run `python verify.py` from this package directory. The verifier directly enumerates the ordered-prefix/sorted-tail law of random-to-top shuffling for finite decks; it compares conditional and direct-history joint moments, projection-remainder variances, and published univariate Gaussian variance formulas when SymPy is available. In the checked environment all 202 cases passed. None of the tests is a proof of the infinite-dimensional or large-sample central limit theorem: that proof is in `RESULT.md` and relies on the standard occupancy CLT and 1-dependent blocking argument.

The calculation covers no shuffle densities outside the stated assumptions and supplies no independent audit.
