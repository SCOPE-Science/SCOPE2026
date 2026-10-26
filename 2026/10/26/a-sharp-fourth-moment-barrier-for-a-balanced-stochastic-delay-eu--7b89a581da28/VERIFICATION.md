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

# Verification

The bundled `verify.py` reconstructs the exact symmetric-tensor moment matrices, verifies the 5-by-5 determinant and fourth-moment rational formula symbolically, checks the interval root count through the Descartes transform, and independently checks the second-moment determinant. The script needs Python 3, SymPy and NumPy. Execute `python verify.py`.

The printed positive root is a numerical approximation; uniqueness is certified algebraically. The infinite fourth-moment assertion rests on the positive Perron operator and conditional Jensen, not on finite simulation. Source-priority review is incomplete, and no independent audit has occurred.
