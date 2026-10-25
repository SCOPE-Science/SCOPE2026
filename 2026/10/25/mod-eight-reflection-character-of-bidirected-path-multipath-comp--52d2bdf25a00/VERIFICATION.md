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

# Verification and boundaries

Execute `python3 check.py` from a directory containing the supplied standalone file. The script enumerates every admissible ternary face word for graph lengths 1 through 12 and verifies the character of the geometric reversal, the precise count of invariant faces, and the Euler–Lefschetz sign identity. For lengths 1 through 9 it also reconstructs all simplicial faces and reduces boundary matrices over the binary field, checking the predicted unique reduced Betti number and degree. A successful run ends with `REFLECTION_CHARACTERS_OK`.

These computational checks are exhaustive only for the stated finite ranges and use characteristic two for the independent homology check. The theorem for arbitrary length follows separately from the proven signed-word fixed-face correspondence, the Hopf trace theorem and the previously published integral sphere homotopy classification. This file does not claim a full integral quotient-homology calculation or an independent external audit.
