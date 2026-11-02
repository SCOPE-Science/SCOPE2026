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

# Finite verification

Execute `python3 verify_icosahedral_perfect_matching.py` with a Python 3 standard-library environment. Its terminal marker is `ICOSAHEDRAL_PERFECT_MATCHING_43S2_19S3_EXACT_OK`.

It independently enumerates the 12 graph vertices, 30 graph edges, 20 graph triangles, 125 perfect matchings and the 4,056 augmented simplices, with face vector `(30,315,1260,1575,750,125)` in dimensions 0–5. It produces 1,975 matched pairs on the augmented complex and 65 critical two-cells plus 41 critical three-cells. A global topological sort over all 15,240 directed Hasse incidences establishes acyclicity.

Its signed gradient-path recursion constructs the exact integral Morse matrix of shape `65 x 41`. Full integer unit-pivot elimination yields 22 pivots with all residual entries zero. A separate fraction-free algorithm computes the determinant of a selected 22-by-22 submatrix as `-1`, certifying primitive image and 22 unit Smith factors. Direct mod-two simplicial boundary ranks are `(29,286,931,625,125)`, agreeing with the rank-level homology calculation.

Zero-based indices for this determinant are supplied in `RESULT.md` and reproduced by the checker itself. The homotopy conclusion further invokes the standard acyclic-matching CW equivalence and the degree classification of maps from two-spheres to wedges of two-spheres. These are mathematical arguments, not properties inferred from a log or finite test alone. No independent audit has been performed. No inclusion map, representation on homology, or broader graph classification is verified here.
