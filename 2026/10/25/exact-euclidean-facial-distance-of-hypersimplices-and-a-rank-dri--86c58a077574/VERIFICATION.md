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

Run `python verify.py` with Python 3, NumPy and SciPy. The code checks integer-orbit maximizations and rational face-distance witnesses over its finite declared ranges. For smaller dimensions, it explicitly averages actual vertices outside each face to build attaining points. The SciPy section separately solves eight quadratic problems directly over the convex hulls of explicitly enumerated binary vertices and compares their results with the exact formula. In a verified execution, the output was:

`EXACT_OK rank_cases=465 face_orbits=50840 explicit_complement_mixtures=140 independent_vertex_QP=8`

The exact arithmetic does not constitute exhaustive verification of arbitrarily large dimensions. The universal theorem relies on the complete analytic face classification, a block-symmetrization argument, an attaining construction, and an exact integer quadratic maximization. Numerical checks use the SciPy SLSQP implementation with a declared tolerance; small numerical errors do not enter the proof.
