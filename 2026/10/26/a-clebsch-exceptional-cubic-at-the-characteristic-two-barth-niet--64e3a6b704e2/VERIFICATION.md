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

Run `python3 verify.py` using Python 3 with only the standard library. The polynomial arithmetic is exact over the field with two elements. The checker verifies the defining-equation expansion near the marked singularity, characteristic-two Euler identity, leading partial derivatives, and a degree-by-degree Gaussian elimination calculation of the Jacobian complete-intersection Hilbert function \((1,4,6,4,1,0,0)\). It also exactly enumerates the rational points over the two-element field and verifies the twenty-line/fifteen-point incidence configuration. A smoothness check over the four-element field is included only as a finite sanity test.

The proof of geometric completeness over the algebraic closure is the torus-and-coordinate-strata argument in RESULT.md, not a finite enumeration. The proof of the length-sixteen Tjurina algebra additionally uses regular-sequence initial forms and Euler's identity, not just program output. The full Jacobian scheme along the boundary lines and any global arithmetic stable model are outside scope.
