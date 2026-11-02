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

# Verification and limits

The accompanying `verify.py` uses only the Python standard library. Its exhaustive scan covers all admissible binary words through length \(16\), and the direct definition-level subsequence check through length \(12\). It independently compares the exact coefficient formula, a three-state transfer recurrence, and brute-force histograms. The script checks totals and numerical algebraic constants and prints `VERIFY_OK` on success.

The source-level mathematical verification consists of the greedy-arch equivalence, exhaustive three-state transition partition, formal power-series solution and analytically dominant root with positive second cumulant. These all-length statements rely on the provided proof, not on the finite run. No independent audit or external certification has been performed.
