---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproduction and verification

Run `python3 verify.py` in this directory. The standard-library script checks the coefficients of both polynomial identities for five rim vertices, and verifies the exact rational Green column and row-sum witness for six rim vertices. The analytic proof in `RESULT.md` establishes the strict bounds for every weight and the extension from the two decisive sizes to all sizes.
