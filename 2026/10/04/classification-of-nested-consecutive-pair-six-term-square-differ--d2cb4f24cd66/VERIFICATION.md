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

`verify_identity_family.py` checks the exact coefficient identities, derives every integer collision among the six affine offsets, verifies the \(q\leftrightarrow1-q\) shape equivalence and span formulas over a wide deterministic range, checks the 1999 and 2026 specializations, and directly evaluates the nested reductions for many integer inputs. A successful run prints `VERIFY_OK`.

The computational replay is corroborative only. The infinite classification and minimality statements are proved algebraically in `RESULT.md`.
