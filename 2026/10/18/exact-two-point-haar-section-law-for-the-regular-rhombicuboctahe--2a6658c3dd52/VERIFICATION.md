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

Run `python3 verify_rhombicuboctahedron.py` from the extracted package. The standard-library checker verifies signed-permutation vertex coordinates, the 48 edges and their common squared lengths, and the six algebraic sign patterns in exact \(\mathbb Z[\sqrt2]\). It prints `EXACT_SIGN_CHAMBERS_OK` on success. It also compares the probabilities from edge-crossing expectation with a spherical-cone evaluation to floating-point tolerance.

The all-directions result rests on the proof that the four critical linear forms obey a diamond partial order, admitting only the six checked sign patterns. Testing a finite set of normals alone would not prove that reduction. The exact probabilities depend on the common edge angle and rotational invariance, not on Monte Carlo or decimal approximations. Historical novelty remains subject to older unindexed stereological literature. Independent audit has not been performed.
