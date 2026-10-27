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

Run the five Python files in the order shown in `RESULT.md` from the `verification` directory. `sympy` 1.14.0 was used for the Gröbner implementation; independent polynomial reduction uses only the standard Python library. The enumerations are finite and exact over the two-element field.

The rational-point ideal has dimension 15 in bidegree \((3,5)\). Its exact total of 32,768 forms is counted twice: once through Gaussian elimination of the nine evaluation constraints, once through the explicit ideal generators. Their rationally smooth subfamilies both have size 5,832. Four affine chart ideals are tested exactly for geometric singularities, first on all 206 orbit representatives by `sympy.groebner`, then with a separate standard-library Buchberger implementation on all 5,832 rationally smooth forms. Both methods give exactly 2,304 geometrically smooth forms, and the representative method produces 76 orbits.

`orbit_representatives.csv` is the complete table of projective orbit representatives, encoded by bitmask \(\sum c_{ij}2^{6i+j}\); the source computes their orbit sizes from generator closure rather than inferring size from distinct bitmasks. `classification.json` includes the singularity-test outcome of every screened orbit representative, permitting targeted reruns of disputed cases. The programs were executed from the embedded-file directory and the reference count files agree.

**Unproved limits.** No abstract isomorphism classification of all genus-eight curves is asserted. No evidence of uniqueness against unindexed prior computational publications is claimed. Independent audit: not performed.
