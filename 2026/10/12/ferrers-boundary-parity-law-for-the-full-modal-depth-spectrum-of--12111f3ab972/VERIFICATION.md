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

The independent-of-formula, standard-library `verify.py` recomputes depth-bounded modal types by their sets of row and column successor types on every Ferrers profile with at most seven rows and seven columns. It checks all depths through stabilization and beyond against the stated closed formulas, including zero-length rows, zero-height columns, duplicates and constant labels. An implementation using direct Boolean set closure and modal images of every definable subset independently checks all Ferrers profiles with at most three rows and columns.

Actual run:

`VERIFY_OK 12854 Ferrers shapes; 182954 depth comparisons; 12854 structural wavefront tests; 62 direct Boolean-closure cases; 5 further witnesses`

The verifier performs exhaustive enumeration only in its specified finite parameter range; no claim of exhaustive verification over all sizes or independent mathematical certification is made. The general induction in RESULT.md handles unbounded parameter sizes.

Reproduce with `python3 verify.py` from the bundle directory, with Python 3 standard library only.
