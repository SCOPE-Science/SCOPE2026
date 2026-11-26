---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

Run `python3 VERIFY.py` to replay 217 finite assertions and print representative effective-rate pairs. Of these assertions, 126 compare three closed-form state probabilities with a seven-state uniformization calculation. The remaining assertions include positivity, finite sign tests and internal consistency checks. This is not a test of the uniform large-time remainder or of the theorem over arbitrary rate laws; the exact factorization and covariance argument in `RESULT.md` establish those results.
