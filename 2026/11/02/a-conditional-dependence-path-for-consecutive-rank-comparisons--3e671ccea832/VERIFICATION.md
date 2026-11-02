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

Run `python verify_conditional_comparisons.py` (standard library only). The program constructs exact distribution counts by independent enumeration of all permutations from length 3 through 10, checks the sign of every conditional 2-by-2 table for every pair of remaining comparison sites and every observed subset/pattern, and verifies the separate polynomial Rayleigh diagnostic at length five. It prints 105,796 conditional sign checks (55,152 strictly negative; 50,644 exactly zero) and six certificate assertions. The finite enumeration is a corroborative check; the proof establishes the result for every size and for independent nonidentical continuous inputs.
