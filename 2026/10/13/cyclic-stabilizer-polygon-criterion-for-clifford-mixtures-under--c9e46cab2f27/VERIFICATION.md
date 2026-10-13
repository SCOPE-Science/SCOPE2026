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

# Reproducible verification and scope

Install the packages in `requirements.txt`, then run `python3 artifacts/verify_polygon.py`. The complete expected output is `VERIFY_OK 88 LP-vs-polygon cases; 24 Clifford rotations`.

The standalone script enumerates all proper signed-permutation qubit Clifford Bloch matrices. It computes the criterion from the axis image, finite stabilizer, and oriented transverse rotation. Separately, it poses convex-hull membership as a linear program with all 24 Clifford matrices as vertices and compares the two membership decisions across 88 test cases. All 88 agreed in the packaged replay. The script exercises four stabilizer orders, both endpoints, non-Clifford phase rotations, and generic tilted axes.

The universal proof is analytic: strict norm convexity fixes each summand's axis; subgroup cosets yield the regular polygons. Numerical linear programming does not certify a theorem for untested angles or probabilities, and floating-point tolerances are used only for corroboration. No external independent audit has been performed.
