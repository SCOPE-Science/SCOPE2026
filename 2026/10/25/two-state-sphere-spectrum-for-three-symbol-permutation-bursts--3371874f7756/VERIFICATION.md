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

# Verification details

The standalone `verify.py` has no external dependencies. Invoke `python3 verify.py` in a directory containing the script. The exhaustive check constructs the set of actual outputs by enumerating all six permutations in each length-three window for each center; it does not use the claimed local formula to generate that set. It then independently computes the local support statistic and the two-state weighted recurrence and compares the full frequency tables.

The test ranges are \(q=2, n=3\ldots12\); \(q=3, n=3\ldots10\); \(q=4, n=3\ldots8\); \(q=5, n=3\ldots7\); and \(q=6, n=3\ldots6\). Together they contain 337,673 center words in 33 parameter cases. Exact rational arithmetic checks means and variances against the displayed formulas and verifies the exact minimum and maximum population counts. The recorded output ends with `VERIFY_OK`.

These are exhaustive checks only within the stated finite ranges. The all-length statements follow from the proof in `RESULT.md`; the Gaussian limit uses the cited finite-dependence theorem. No independent audit has been performed.
