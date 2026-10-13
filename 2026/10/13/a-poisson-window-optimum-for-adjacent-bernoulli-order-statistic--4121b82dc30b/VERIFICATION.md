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

Run `python3 artifacts/verify_adjacent.py` with the Python standard library. The recorded exact finite enumeration consists of 28 comparisons for sample lengths 2–8, each with four rational zero-probabilities. The script brackets the positive solution of the exponential equation and compares finite probabilities against the sharp asymptotic constant at sample sizes 20, 100, 1000, and 10000. Direct enumeration of finitely many samples is not a proof for arbitrary sample sizes. The proof uses the exact nested-event covariance, two uniform escaping-regime bounds, and a uniqueness argument for the limiting exponential critical point. The numerical values are approximate. No independent audit has been performed.
