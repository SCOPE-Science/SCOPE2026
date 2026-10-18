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

The `verify.py` program uses only Python's standard library and exact integer/rational arithmetic. Run with `python3 verify.py` alongside the files in this package.

For each \(n=4,5,6,7,8\), the program enumerates all \(n^{n-2}\) Prüfer sequences, constructs the corresponding labeled tree, and directly counts crossing pairs by the alternating-endpoint criterion. It checks the conditional leaf-stratum means, exact counts of trees in every stratum, unconditional crossing mean, mixed covariance, leaf variance, degree-wedge first and second moments, and strict monotonicity. The highest enumerated dimension contains 262,144 labeled trees. It also computes independent exact Stirling-ratio inequalities for code lengths two through 100. The observed output is:

`VERIFY_OK 280562 exact assertions; Prüfer enumeration through 8 vertices`

The all-size results are justified by combinatorial arguments in `RESULT.md`; finite enumeration is only a consistency check. The total-crossing leading variance is cited from Arizmendi–Cano–Huemer (2019), not inferred from enumerated data. No independent audit or third-party validation has been performed.
