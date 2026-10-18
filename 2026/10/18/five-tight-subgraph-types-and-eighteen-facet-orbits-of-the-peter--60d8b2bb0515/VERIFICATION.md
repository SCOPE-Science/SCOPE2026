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

The standalone `verify.py` is the executable finite certificate. It uses only Python's standard library and evaluates two logically distinct complete descriptions of Petersen maximal bipartite facet subgraphs: connected crossing-edge cuts (511 tests) and every one of the 32768 edge subsets with connectedness, bipartiteness and maximality tests. The two sets are compared for exact equality.

All facet potentials are exhausted by testing all 59049 ternary labelings; the analytic integer-tight-tree and graph-diameter-two lemmas in `RESULT.md` show why this finite universe is complete. The verifier separately checks the 120 graph automorphisms induced by permutations of five points, the five size-four independent stars that force every graph automorphism to arise this way, orbit disjointness and exhaustion, exact hard-coded representative tables, subgraph fiber counts and histograms. Two Burnside fixed-point sums independently confirm the five and eighteen orbit counts.

Actual replay: `python verify.py` completed without error and printed `ALL EXACT CHECKS PASSED`. This is an exhaustive certificate for the ten-vertex graph, not a claim about an infinite family. No external or independent audit has been performed.
