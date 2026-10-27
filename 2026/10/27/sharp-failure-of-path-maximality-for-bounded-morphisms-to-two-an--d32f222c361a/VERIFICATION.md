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

The standalone `checker.py` enumerates every rooted unlabelled tree through size eight by recursively taking multisets of previously enumerated rooted shapes. It evaluates the exact coupled recurrences for all of those shapes and, **independently**, checks the direct quantified forth/back definition against every map to both reflexive chains through size seven. The exhaustive tree-shape totals are 1, 1, 2, 4, 9, 20, 48, 115 for sizes one through eight. The maximum p-morphism counts are computed independently for each tree size, and all explicit infinite-family formulas are checked at several parameter values. See `verification_output.txt` for actual output.

The general root recurrences and all-order strict inequalities are established in `RESULT.md`; finite enumeration proves the small-order sharpness only. The program does not establish originality, does not assess larger-chain targets, and does not certify an infinite proof. No independent external audit was performed.
