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

The `verify.py` program is standalone Python 3 and uses no packages beyond the standard library. Run `python verify.py` beside these documents. It reconstructs the automorphism matrix from the structure products, computes its kernel rank by finite-field row elimination, exhaustively counts every automorphism over thirteen field/dimension pairs, and checks the complete frequency polynomial and its Burnside specialization. It also solves the finite coefficient conjugacy equation and checks all unipotent normal forms for four pairs. The final output was `VERIFY_OK`.

**Scope:** finite instances are checks, not proofs. The general proof is the recursive normalization and kernel decomposition in `RESULT.md`. No external independent audit or mathematical certification has been performed.
