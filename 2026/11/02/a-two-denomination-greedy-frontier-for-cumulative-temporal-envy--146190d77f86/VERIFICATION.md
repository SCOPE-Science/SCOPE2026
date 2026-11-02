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

Run `python verification/check.py` with Python 3 and no external packages. The program computes cumulative maximum envy using integer arithmetic and enumerates all possible irrevocable assignments for the bounded examples. It verifies all two-agent sequences over \(\{1,2\}\) through length ten, all three-agent sequences over \(\{1,2\}\) through length three, and the three four-good sharpness witnesses. The observed terminal line is `VERIFY_OK cases=2063 assignments=1398471`.

The general theorem is proved symbolically in `RESULT.md`. Finite enumeration cannot establish the theorem for unbounded horizons. The outputs are not an independently audited certification, and the review is limited to the disclosed model, proof, and exact reproducibility checks.
