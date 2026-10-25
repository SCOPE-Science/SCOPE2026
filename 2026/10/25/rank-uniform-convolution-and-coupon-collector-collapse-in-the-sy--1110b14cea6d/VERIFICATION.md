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

Run `python verify.py` using Python 3.11 or later; only the standard library is needed. The script directly enumerates partial bijections and their products, checks all individual-map probabilities from the inclusion-exclusion expression for 21 rank profiles, verifies 3,024 hypergeometric transition eigenfunction identities, and separately checks singleton-deletion Stirling counts and the harmonic hitting-time formula through size seven. Expected stdout begins `VERIFY_OK_ROOK_MONOID_BATCH_COUPON_CONVOLUTION 21 product-profiles 21 spectral-checks 3024`.

The proof of the exact law does not depend on the finite checks. The asymptotic result follows from factorial moments and requires fixed positive batch size. No independent audit or infinite computer proof was performed.
