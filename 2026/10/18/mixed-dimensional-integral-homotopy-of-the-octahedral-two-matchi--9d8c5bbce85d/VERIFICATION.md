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

The accompanying executable `verify_octa_two_matching.py` enumerates all 4096 edge subsets and all 772 legal simplicial faces, confirms the nonempty face vector, identifies maximal simplices, and constructs 377 element-toggle Morse pairs. An exhaustive topological sort of the oriented Hasse diagram with 771 faces and 2928 covering incidences verifies acyclicity. Integer chain reductions reconstruct the signed 6-by-10 Morse boundary; its rational rank is three and a 3-by-3 determinant is one, proving three unit Smith invariants. Separate full simplicial boundary matrices over two prime fields yield reduced Betti ranks three and seven in degrees three and four respectively, and zero elsewhere.

The full integral homotopy conclusion uses the fact that the Morse CW complex has a single vertex and cells only in dimensions three and four, where all four-cell attaching classes are measured completely by degrees. The independent-audit channel has not been performed. The calculation is exhaustive only for the specified 12-edge graph; it does not claim an all-parameter classification or establish global uniqueness in the literature.

Reproduction: run `python3 verify_octa_two_matching.py` with Python 3.10 or later, using only the standard library. Expected signature: `OCTAHEDRON_TWO_MATCHING_INTEGRAL_HOMOTOPY_CHECKS_OK`.
