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

# Reproduction

Run the embedded `verify.py` with Python 3 and the standard library only. It must print `TERNARY_SUPPORT_REFINEMENT_PASS` or raise an assertion. It constructs the proposed full support-refined coefficients by an independent integer-sum expansion; enumerates all ternary words for lengths 1–11; and separately enumerates all balanced integer matrices by signed flow and checks graph connectivity for lengths 1–14. All support categories are compared exactly.

Expected total profile counts at lengths 1–15: 3, 6, 11, 24, 48, 95, 174, 306, 510, 819, 1266, 1901, 2775, 3960, 5531. Example full coefficient distribution at length 7: 0:3, 2:36, 3:36, 4:90, 5:6, 6:3.

Finite enumeration is a check, not a proof for unbounded lengths. The all-length result relies on the Euler-circuit characterization and exhaustive three-symbol flow decomposition in RESULT.md. No outside audit or certification has been performed.
