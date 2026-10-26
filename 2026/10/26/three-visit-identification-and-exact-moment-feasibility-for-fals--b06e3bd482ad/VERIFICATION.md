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

`artifacts/check.py` is standalone Python 3 code using only the standard library. Run it with `python artifacts/check.py` and compare its sorted, indented JSON output to `artifacts/certificate.json` byte for byte.

The script enumerates 3456 exact-rational parameter configurations, computes the independent-Poisson intensities of every nonempty detection subset, derives mixed distinct-index cumulants by summing those intensities, and reconstructs the original rates from the claimed inverse. It also checks that two different admissible two-visit parameter vectors have exactly the same Poisson shock intensities, hence the same complete joint law, and that a nontrivial scaling family preserves means and covariances but not the third cross-cumulant.

No external computation or numerical tolerance is needed. The infinite-domain proof is the symbolic generating-function and algebraic argument in `RESULT.md`. Finite enumeration does not independently establish its universal quantifiers. No independent external scientific audit has been performed.
