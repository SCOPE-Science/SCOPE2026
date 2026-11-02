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

# Reproducible checks and limits

Run `python3 verify_cartier.py` alongside this file. The self-contained implementation computes multiplication in characteristic-two extension fields, applies the semilinear Cartier matrix and verifies ranks of its first four iterates for all coefficient pairs over fields of sizes \(2,4,8,16,32\). It also checks four zeta numerator calculations by direct point enumeration of low-degree extensions.

Expected final line: `ODD_TRIGONAL_CHAR2_CARTIER_STABLE_RANK_AND_ZETA_OK`.

Finite enumeration does not prove the theorem for arbitrary algebraically closed characteristic-two fields. The unlimited assertion follows from the differential and semilinear Cartier identities in `RESULT.md`. No independent mathematical audit or validation has been performed.
