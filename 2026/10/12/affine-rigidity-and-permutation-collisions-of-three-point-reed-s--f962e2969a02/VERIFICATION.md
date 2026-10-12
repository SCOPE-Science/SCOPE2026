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

The mathematical proof in `RESULT.md` establishes all finite-field cases uniformly. The executable `verify.py` independently enumerates affine stabilizers in ten representative fields and, for fields up to order nine, directly constructs the unordered outputs of every affine message polynomial. It checks the exact histogram of collision-fiber sizes and the absence of an admissible evaluation triple below field size eight. Run `python3 verify.py` with Python 3 (standard library only). The expected marker is `VERIFY_OK`.

Finite enumeration is not an infinite proof. There has been no independent external audit or independent certification of the symbolic argument.
