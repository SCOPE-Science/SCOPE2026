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

# Verification record

**Analytic checks.** Direct interval transport verifies Lebesgue stationarity for both kernels and identifies them as stationary reversals. Every two-step component path contains fresh within-cell uniformization. The exact three-by-three rank-one recurrence extends the component coefficient identity to all integer lags at least two. The deterministic alternating word occurs with strictly positive weight at *every* lag, making the normalized joint-event ratio arbitrarily large by shrinking source intervals. Three-step minorization is derived from a positive all-forward word, and standard Doeblin splitting yields the uniform total-variation bound. The proof is included in RESULT.md.

**Standalone exact-arithmetic replay.** `verify.py` uses only Python standard-library rational fractions and no external data or dependencies. It checks group-level stationarity, transposition, exact matrix powers, a rank-one recurrence, two component coefficient profiles through lag 64, the mixture's minorization constant and 64 alternating-word weights. Successfully replayed test output: 445 exact finite checks and \(3/32\) minorization.

**Limits.** The finite checker does not prove claims quantified over every lag or arbitrarily small intervals; those claims depend on the written induction and probability inequalities. The publication evidence supports self-review, not an independent audit or a universal priority certificate. No external validation is claimed.
