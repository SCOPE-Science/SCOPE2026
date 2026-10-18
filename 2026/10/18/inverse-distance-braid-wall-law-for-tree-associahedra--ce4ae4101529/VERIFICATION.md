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

The formula is established for every labelled tree of order at least two by a combinatorial proof using the positivity of the Minkowski coefficients and uniform permutations of contracted adjacent blocks. The executable `checker.py` independently enumerates connected subsets, direct exposed vertices, and adjacent objective-order swaps, and compares exact pair-labelled counts against independently computed graph distances. Its test suite covers all labelled trees with two through five vertices and six selected six- and seven-vertex trees (151 trees total); all comparisons passed.

Run `python3 checker.py` using Python 3. No external data or dependencies are required. These tests do not enumerate all trees of larger sizes or establish the result without the analytical proof. The count concerns surviving braid-wall edges, not distinct edges of the quotient polytope. Earlier literature may contain an equivalent formulation not identified by the searches. Independent mathematical audit has not been performed.
