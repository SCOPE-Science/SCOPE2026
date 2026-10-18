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

The enclosed Python scripts are standalone apart from standard-library imports and the local import from `quasitrivial_exhaustive.py` to `quasitrivial_checker.py`. Run from a folder containing all three scripts with `python3 quasitrivial_checker.py`, `python3 quasitrivial_exhaustive.py`, and `python3 quasitrivial_bivariate.py`, respectively; all were executed from the enclosed source files and produced their respective success markers. The two first tests are distinct constructions (weak-order enumeration and brute-force enumeration of all quasitrivial operations). The latter tests associativity explicitly, not only a normal-form criterion. The third checks the exact bivariate counts via a labeled integer recurrence. Exhaustiveness holds only within the declared finite parameter ranges; proof for every degree is given in the accompanying mathematical argument. Root values were numerically checked but their existence, uniqueness, and asymptotic use are proved analytically.
