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

Run `python verify.py` with Python 3.10+ standard library. The corresponding `verification_output.txt` records the checks executed. The script independently evaluates admissible color classes for each order from 3 to 9 using adjacency masks, exhaustively enumerates unlabeled class partitions, and checks the falling-factorial formula. It also directly enumerates all named-color assignments for a fixed set of small orders and palettes (1,201,518 assignments). These are finite corroborations, not independent auditing or a proof over all integers. The proof in RESULT.md treats all orders symbolically.
