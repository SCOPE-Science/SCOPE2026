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
# Reproducibility and limits

Run `python3 verify.py` from the extracted file directory. It uses only the Python standard library and terminates with `VERIFY_OK` if all checked finite instances agree. It builds the multiplication coefficients of the length-four truncated oriented cycle from concatenation, exhaustively evaluates the single-element square relation for the full algebra over the two-element field at cycle length four, and independently enumerates the two nontrivial coefficient layers for cycle lengths four through eight over the two-element field and for selected larger prime fields. It checks the gap-rank formula for all independent supports through cycle length fifteen over two prime fields, and compares maximal-support counts with the Perrin recurrence.

The verified general result is proved mathematically in RESULT.md. Finite enumeration and row reduction do not prove the unbounded-size theorem. Reduced varieties are considered; the original square-equation scheme might possess additional nilpotent structure. No independent mathematical audit has been performed.
