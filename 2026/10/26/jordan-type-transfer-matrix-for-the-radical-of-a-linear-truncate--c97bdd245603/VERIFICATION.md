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

The standalone `verify.py` constructs actual left-regular multiplication matrices from the path basis over prime fields, performs independent modular Gaussian elimination on each matrix and its square, and compares their joint rank counts against both a support enumeration and a two-state recurrence. It runs the bounded exhaustive cases for \(n\le7\), \(q\in\{2,3,5\}\) under a 25,000-element cap. Expected final stdout marker: `VERIFY_OK_REGULAR_NAKAYAMA_JORDAN`.

The proof handles every prime power using path-coordinate independence and finite coefficient counting. The finite verifier checks prime fields only and is not an exhaustive mathematical certification. The representation is the full regular action, not just an action on a vertex-space truncation.
