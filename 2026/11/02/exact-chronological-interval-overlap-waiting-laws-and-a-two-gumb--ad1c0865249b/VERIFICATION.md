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

The exact pathwise argument and inclusion–exclusion / geometric decomposition are proved in `RESULT.md`. The independently programmed finite cross-check is `CHECK.py`; execute `python CHECK.py` in the same directory. It enumerates empirical first/last label intervals directly and compares their overlap with the derived criterion on all finite words in the listed small ranges. It separately computes rational nonuniform CDFs from independently enumerated weighted words and compares them to the finite formula. It checks geometric first and second moments and minimum completion probabilities with exact integer/rational arithmetic.

Actual script run from the extracted final package: `PASS: 117928 independent exact finite assertions`.

No Monte Carlo results, numerical tolerances or external unlisted dependencies are needed. The infinite-dimensional statements are supported by the explicit analytic proofs and not inferred from finite enumerations. The historical-priority comparison is qualified by indexed-only access to the dissertation and published journal passage; no independent audit has been performed.
