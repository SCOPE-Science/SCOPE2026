---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-02.md",
      "INDEPENDENT_AUDIT_2026-10-02.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

Run python artifacts/verify.py --check. It checks the relator exponent matrix, degree-two Magnus/Fox coefficients for cocycle cups only, every integer unitriangular relator defect, and exact equality with artifacts/results.json. Its final line is VERIFY_OK: corrected U4 integral triple table and cocycle cups.

The eight middle coordinates in table order are 0,0,0,1,0,-2,1,0. The underlying Dwyer correspondence and naturality to the presentation complex are explained in RESULT.md. This replaces the invalid noncocycle Fox shortcut; the old verifier is historical evidence only.


The verifier additionally proves the central relator identities in the exact polynomial ring with all six cohomology coefficients, all four freely chosen second-superdiagonal entries, and all three central lift entries. SYMBOLIC_OK is an identity check, not a finite parameter sample. The integer bar-cochain proof and cell obstruction argument are given in RESULT.md.
