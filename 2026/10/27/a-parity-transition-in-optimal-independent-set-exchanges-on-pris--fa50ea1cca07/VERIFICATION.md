---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

RESULT.md lines 5–17 and 19–37. A rung holds at most one token and consecutive occupied columns alternate. Full occupancy closes for even n only, yielding two disjoint checkerboards. With one vacancy, the remaining occupied path has n−1 vertices. In the odd case its endpoints have opposite layers, so the only allowed exchanges fill the vacancy from one neighboring column; the moved token keeps its layer. In-place flips are impossible because each occupied column has an occupied neighbor, including n=3. A full clockwise vacancy circuit shifts the alternating word on the even-length occupied path by one cyclic position and exchanges its two phases; the exchange graph is one C_(2n). In the even case the two exposed layers agree and force a unique extension to a checkerboard. Deletions from each checkerboard form K_n and there are no edges across the two families. At two vacancies the adjacent pairs contribute 2n, and nonadjacent pairs contribute 4 times (binomial(n,2)−n), giving 2n(n−2). A vacancy can move toward the other until adjacent by filling opposite to the remaining occupied neighbor. For odd n the adjacent-vacancy states extend to maxima whose deletion cliques overlap around the maximum exchange cycle. For even n they lie in two connected Johnson graphs, and shifting an occupied block one column from its vacant end in decreasing order preserves legal layers (the already shifted neighbor has opposite layer) and changes the checkerboard class. This also works for the shortest even prism n=4. Both bundled checkers and captures were inspected, not executed; a fresh explicit vertex/edge and deletion/insertion enumeration for n=3 through 8 passed all three levels, replay via python3 /workspace/branches/independent_discrete_checks.py. The symbolic arguments establish all n≥3.

## originality

PASS

The supported distinct result is the joint fixed-cardinality token-jump classification for ordinary independent sets, including the sharp even-prism connectivity threshold at two vacancies. Several indexed results overlap on exact cases or analogues; neither those nor the inspected primary results establish the full exchange geometry. No credit is assigned for the independence-number parity by itself.

## value

PASS

This is a natural cubic graph family and a concrete sharp obstruction to reconfiguration at large independent-set cardinalities. Odd optima already form an exact single cycle; even optima and one-token deletions stay separated, with all two-vacancy states connected by explicit moves. The threshold plus exchange structure is useful beyond the standard independence number or a transfer-matrix count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
