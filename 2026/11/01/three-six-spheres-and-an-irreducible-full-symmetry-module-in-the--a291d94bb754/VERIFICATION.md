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

# Verification of finite claims
The supplied `verify_mk.py` uses only the Python 3 standard library and must print `ALL_CHECKS_PASS`. `verify_mk.out` records one execution on the exact included source. The script independently tests all \(2^{16}\) induced vertex subsets by component size and vertex degree, counts all faces, builds and globally topologically sorts the directed Hasse diagram, computes integer Morse matrices by signed gradient paths, and checks all determinant gcds. Separate original-boundary mod-two ranks are computed without using the Morse matrices. A separate backtracking enumeration of graph automorphisms produces all \(96\) maps, and two combinatorially distinct Lefschetz computations agree for every map.

The determinant gcds certify the elementary cell-cancellation degrees. The homotopy argument uses Forman's theorem and the standard low-dimensional homotopy groups of wedge spheres; the character argument uses the simplicial Lefschetz theorem and finite-group character orthogonality. This is a complete finite computation, not an infinite-family theorem. Independent validation has not been performed. No numerical linear algebra or random tests are used.
