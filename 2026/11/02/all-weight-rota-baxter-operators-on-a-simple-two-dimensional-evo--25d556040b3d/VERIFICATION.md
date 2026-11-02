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

Reproduce with `python3 verify.py` in this directory (only the Python standard library is used). The checker tests the original six scalar equations for each operator matrix, not just the necessary rank or characteristic-polynomial constraints. The complete sets are compared against the displayed projection and characteristic-\(31\) formulas for \(q=2,3,4,5,7,8,11,13,31\) and weights zero and one. Implementations of \(\mathbb F_4\) and \(\mathbb F_8\) use irreducible binary polynomials. It emits `VERIFY_OK` when all equalities hold. This supplies finite-field checks only; the field-uniform proof is the mathematical argument in `RESULT.md`.
