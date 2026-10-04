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

`verify.py` is dependency-free and reconstructs the finite problem from the definition of Chebyshev distance. It checks all 120 permutations of five symbols, creates the compatibility graph for threshold 3, exhaustively enumerates every maximal clique with an exact bitset Bron--Kerbosch search, and confirms that the largest cliques have size 10 and number exactly 192.

It then applies all 120 coordinate permutations and both value-path isometries (identity and reversal), verifies closure on the 192 maxima, computes the three orbit sizes and stabilizers, and recomputes the full pair-distance spectrum of each orbit representative.

Expected output:

`VERIFY_OK maximum=10 labeled_maxima=192 orbits=3 orbit_sizes=24,48,120 stabilizers=10,5,2 maximal_cliques=4694132 edges=5340`

The computation is finite and exhaustive. It does not infer infinite behavior and does not assert that the stated 240-element subgroup is the full automorphism group.
