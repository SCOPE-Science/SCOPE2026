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

Reproducibility: run `python3 checker.py` with Python 3 standard library. The checker evaluates the exact finite Burnside–Möbius expression, separately enumerates total-preorder tuples and their label/axis relabeling orbits in selected small cases, checks the known two-coordinate baseline, and prints `ALL_CHECKS_OK` only when all assertions hold.

Finite checks provide exact small-domain corroboration, not a proof of the all-size formula. The independent audit is not performed. The uniform proof is in RESULT.md.
