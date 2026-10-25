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

# Reproducibility and limitations

Run `python3 verify.py` with Python 3 and the standard library. This standalone file is embedded in the finding, and was executed successfully in its packaged form. It checks the formula across positive integer budgets, independently computes the integer-partition upper bound by dynamic programming, evaluates the explicit complex phase witnesses, verifies the arithmetic equality criterion against the published two-row endpoint bound, and tests finite phase grids in the original complex supremum. The observed test count was 75,263; no third-party package or network access is required.

The proof for all integers and continuous phase variables is in `RESULT.md`, using projective circular ordering, a geometric progression and strict concavity. Finite phase grids do not certify global maxima independently; the analytic proof does. No independent scientific audit or formal machine proof is represented.
