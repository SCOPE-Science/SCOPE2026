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

The bundled `checker.py` performs brute-force full substring and minimal-absent-word enumeration on substitution ranks 1 through 6, independently of the three-adic candidate generator, and asserts equality of complete sets as well as the closed cardinality. Expected output counts: 3, 6, 13, 32, 87, 250. These finite checks are not a proof of the unrestricted theorem. The unrestricted argument is in `RESULT.md` and relies on a complete ruler-boundary context split. No independent mathematical audit has been performed.
