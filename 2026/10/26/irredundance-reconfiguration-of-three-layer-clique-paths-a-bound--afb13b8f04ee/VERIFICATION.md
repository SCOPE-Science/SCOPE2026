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

If the middle is empty, a multi-vertex outer occupancy forces every one of its vertices to use its matched middle vertex as witness; this requires disjoint indices across the outer layers. Singletons in both outer layers can share an index. If the middle is occupied, a second vertex in either outer layer is impossible because the whole middle clique is dominated by a selected middle vertex. With both outer singletons a middle vertex can only witness in the middle clique, so at most one middle vertex can be selected; any triple works by taking outer witness indices different from the middle index and a middle witness outside the two outer indices. A unique outer singleton can witness exactly when a proper subset of middle indices is selected, and middle vertices use the vacant outer layer. The middle-only selections always work. Counting the four disjoint cases yields I_n. Irredundance is hereditary, so the maximal configurations are exactly full complementary outer allocations (2^n), the full middle layer, the two families of singletons plus n−1 middle vertices (2n^2), and the three-layer triples (n^3). For n≥4, only size n is optimal. A slide within a singleton-plus-middle family changes one coordinate, yielding each rook graph. The hub slides to each family only at matched diagonal indices. A within-layer slide of a full outer allocation creates a repeated index, and a middle slide leaves n−1≥3 outer vertices, forbidden with a nonempty middle. No outer-to-outer slide can join the two families. Thus the maximum-set slide graph is exactly the stated union; an off-diagonal vertex is at distance two from the hub, so opposite off-diagonal vertices realize diameter four. Edge count and component counts follow.

## originality

PASS

The closest exact-host claim concerns a different set predicate; the same slide framework and related private-witness classifications do not classify this host family. This is a bounded best-of-knowledge decision.

## value

PASS

On a natural Cartesian-product family, the result resolves both the quantitative gap between minimal size of a maximal set and the optimum, and the reachability of every optimum under an established slide model. The coexistence of exponentially many frozen optima with a diameter-four nontrivial component is information neither a count of optima nor the known domination result determines. The nontrivial component has quadratic size, not size uniformly bounded in n.

The dated certificate retains the supplied scientific assessment, sources and limitations.
