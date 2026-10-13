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

## Reproduction

Run `python3 artifacts/verify.py`. It uses only Python 3 and runs a direct finite-field matrix census, including a quadratic extension field. The expected final line is `EXHAUSTIVE_CASES 12 DIRECT_PULLBACK_CASES 8 PULLBACK_CHECKS 125 VERIFY_OK`.

The verifier independently enumerates all values of the free cross-block entries for twelve cases and computes matrix ranks by finite-field elimination. It compares entire rank histograms to the closed product-sum formula, not only their totals. Separately it checks total pullback-map counts for 125 field-size, symplectic-dimension, and source-dimension combinations.

The infinite-family proof is in RESULT.md, Lemmas 1 and 2. Exhaustive finite enumerations do not imply the universal theorem without that proof. Source comparisons cannot rule out all equivalent unpublished or historical formulations. Independent audit is not performed.
