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

The supplementary `verify.py` is standalone Python 3 code requiring only the standard library. Execute `python3 verify.py` from its directory. Successful output ends with `VERIFY_OK`.

It checks 25 basis products, exhaustively obtains the single-commutator image from 390625 ordered effective pairs over the prime field, reconstructs all 585 simple values using Pluecker minors, and compares the remaining 40 failures to the discriminant. For the quadratic extension, it checks the stated 7200 nonsimple elements by direct field discriminant arithmetic, plus 1419 constructive cases and more nonzero-linear cases. The general any-field statement follows from the written Pluecker proof; the extension-field check is not an exhaustive commutator-pair enumeration over the larger field. No independent external mathematical certification is asserted.
