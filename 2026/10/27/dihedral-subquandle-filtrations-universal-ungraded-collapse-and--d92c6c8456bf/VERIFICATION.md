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

# Verification notes

The accompanying `verify.py` is a self-contained Python 3 program requiring only the standard library. Run `python3 verify.py` in the directory containing this file and the checker. It emits `ALGEBRA_OK`, `GRADED_OK`, `VERIFY_OK` on success, together with example terms for modulus nine.

The checker independently enumerates every function \(R_n	o R_n\) for \(2\le n\le5\), verifies that only the affine maps preserve the operation, and independently enumerates all nonempty closed subsets for \(2\le n\le10\), comparing them with all subgroup cosets. It checks the respectful-map count on one- and two-color subsets, directly simulates closed positive two-strand braids for a collection of small moduli and odd crossing numbers, and enumerates all \(n^2\) endomorphism images of each coloring. It compares every resulting graded monomial and multiplicity to the closed divisor formulas.

These tests provide finite error detection, not an infinite or independent proof. The symbolic argument establishing the identities for all \(n\ge2\), odd \(k\ge1\), all oriented links, and all indicated filtrations is contained in `RESULT.md`. Full independent mathematical auditing has not been performed.
