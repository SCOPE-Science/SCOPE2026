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

# Reproducibility and checks

Run `python3 verify_star_zero_pairs.py` with Python 3.9 or later; no dependencies outside the Python standard library are required. The program enumerates every ordered pair of sparse matrices and multiplies them as ordinary dense matrices. It separately evaluates the proposed component equations and asserts that their union coincides with zero multiplication. For each component it also constructs a field-rational witness belonging to no other proposed component. It checks the closed polynomial count against exhaustive direct products for nine field/size combinations, including \(\mathbb F_4\) implemented with its irreducible polynomial \(t^2+t+1\).

Expected final output: `STAR_INCIDENCE_ZERO_PRODUCT_GEOMETRY_OK 9`.

These tests cover finitely many fields and ranks only. The proofs of irreducibility, closure, component dimensions, and all-field arithmetic formulas are algebraic arguments in `RESULT.md`; finite enumeration is not an infinite-family proof. The assertion concerns reduced varieties. Full priority certification and independent mathematical audit have not been performed.
