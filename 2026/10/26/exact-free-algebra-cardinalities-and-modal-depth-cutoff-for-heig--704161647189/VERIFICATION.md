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

# Reproducibility checks

Execute `python3 verify_height_two.py` with a standard Python 3 interpreter. The checker builds each canonical reflexive partial order for \(k=1,2,3\), repeatedly refines classes according to the colours of accessible previous-stage classes, and independently obtains the exact type counts and depth-stage counts. At \(k=1\) it also generates the actual full Boolean modal subalgebra and verifies its size is \(64\).

Expected output includes `TWO_LEVEL_MODAL_TYPES_EXACT_OK`. The test confirms finite instances and is not an infinite proof. The infinite proof uses only explicit bisimulation matching and characteristic formulas contained in RESULT.md. No independent audit is asserted.
