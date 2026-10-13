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
# Verification

The proof in `RESULT.md` is the evidence for the infinite real-coefficient statement. In particular, the critical step is the analytic inequality \(\tau\ge\min\{b_3,b_1+b_2\}\), followed by an exact ordering of the fourth and fifth candidate subset weights.

The companion `verify.py` script was executed from the packaged artifact path. It enumerates all nondecreasing integer five-tuples with entries from \(0\) through \(8\), excludes the all-zero tuple, checks all \(32\) sign patterns using integer comparisons against the Euclidean norm, and checks the equality criterion without floating-point arithmetic.

Observed regression output:

`VERIFY_OK tuples=1286 minimizer_tuples=261 min_positive_count=4`

This finite grid is not an exhaustive proof for real coefficients and is not used to infer the theorem. It is a reproducibility check against sign-count, boundary, zero-padding, and tie-handling errors. The theorem does not address more than five nonzero coefficients or the strict-tail variant.
