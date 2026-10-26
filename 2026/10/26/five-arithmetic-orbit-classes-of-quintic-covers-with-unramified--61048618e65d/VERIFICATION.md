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

# Verification procedures

`checker.py` is a standalone pure-Python exhaustive enumeration and characteristic-two Hasse-derivative verification. Execute `python3 checker.py > observed.json` and compare JSON data with `expected.json`. The program asserts all principal counts and orbit representatives.

`independent_check.py` is a separately implemented SymPy algebraic cross-check. Execute `python3 independent_check.py > observed_symbolic.json` and compare with `symbolic_expected.json`. It independently constructs homogeneous forms, tests squarefreeness and resultants, and verifies the 22-pencil, five-orbit and branch-polynomial classification.

`catalogue.json` supplies the exact 22 pencils. Its masks follow the encoding described in `RESULT.md`. Source automorphisms are the six invertible matrices over the binary field, and target changes of basis permute the three nonzero pencil members. The polynomial Wronskian is a square in characteristic two; the first nonzero Hasse coefficient, rather than its ordinary vanishing order, determines the local ramification index.

Both programs were executed successfully against the packaged sources. No third-party verification, independent audit, or infinite-field theorem is claimed. Source material overlaps remain subject to the scientific limitations recorded in `RESULT.md` and `REVIEW.md`.
