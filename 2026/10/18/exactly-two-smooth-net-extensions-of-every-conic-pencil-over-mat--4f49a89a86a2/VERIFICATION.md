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

# Reproducible verification

Run `python3 verify_full_census.py` and `python3 verify_orbit_reduction.py` with a standard Python 3 interpreter. Both files use only its standard library and reproduce the exact finite-field arithmetic independently. The expected non-timing lines of the two actual program runs are included for comparison.

The first program exhausts all 364 projective quadratic forms, all 11011 two-spaces, and all 33880 three-spaces, tests the determinant condition for all nonzero projective members, and checks the incidence multiplicity for every one of 1872 smooth pencils. It then constructs projective orbits of the 288 nets and 1872 pencils.

The second program fixes an explicit smooth pencil, enumerates all 40 three-space extensions in its four-dimensional quotient, and checks precisely two are smooth. Four invertible coordinate changes generate exactly the 11232-element full linear group and hence the 5616-element projective group. Their action gives exactly one 1872-element smooth-pencil orbit and two disjoint 144-element smooth-net orbits.

The determinant criterion is exact for singularities over the algebraic closure in characteristic three; no untested extension-field smoothness assertion is made. The group and coefficient-space computations are completely finite, with explicit algorithms rather than a nonexhaustive sample. No independent human audit has been performed.
