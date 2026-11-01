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
# Reproducibility and scope

Run `python3 verify.py` from the directory containing this file, using Python 3.10 or later. No third-party modules, network requests, precomputed data, or external files are required. The expected final line is `ALL_VERIFY_OK`; all assertions must succeed. The checker builds its own vertex and edge ordering for \(\operatorname{KG}(5,2)\), enumerates all fifteen-edge masks, and cross-checks the face polynomial using an independent vertex-deletion recurrence.

It builds the indicated 160-pair Morse matching, checks all 975 Hasse incidences and the full directed graph for acyclicity, calculates every coefficient in the integral Morse boundary by signed gradient paths, and finds the zero 5-by-5 matrix. These are sufficient for the ordinary integral wedge-of-spheres homotopy conclusion. They do not claim an equivariant homotopy equivalence.

For symmetry it evaluates signed chain actions for all 120 permutations. Modular Gaussian elimination computes the image of the degree-three simplicial boundary, which has rank 79 both rationally (by the proven homotopy ranks) and modulo 1000003. The modular trace is uniquely lifted to an integer because a finite-order linear operator on a 79-dimensional rational space has trace between -79 and 79. Every permutation is checked against the closed expressions for the two rational characters. The code verifies the degree-three character has norm one and is the difference of the two-subset and point permutation characters.

Limitations: the checker is exhaustive only for the Petersen graph, not for other cubic graphs. Exact signed Morse coefficients do not independently certify the entire mathematical literature comparison. Independent human validation has not been performed.
