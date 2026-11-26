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

Over the fixed finite valuation universe, each nonempty convex union-closed family is upward closed inside its maximum team. Conjunction preserves this description in a nonempty intersection. For strict splitting, a successful partition can be extended to any larger team in the union of the operands' maximum teams by allocating each additional row to one permitted side. This proves soundness without assuming that a pair of arbitrary overlapping witnesses can be disjointed. Conversely, a flat test constrains the team to its maximum, and hitting the complements of all maximal nonmembers describes the family there. Each hit is expressible by a nonempty flat witness and its leftover, so the formula works under either split convention; bottom conjoined with NE covers the empty family. For strict model checking, certificates give one subset per split occurrence, and the explicit team and syntax tree make verification polynomial. Encoding distinct hypergraph vertices by binary valuations makes each edge test a polynomial-size flat minterm disjunction. Under strict splitting, both sides must hit all edges, exactly property B of a 3-uniform hypergraph; the lax witnesses can both be the whole team. The published lax P result applies. Scope is fixed declared domain for expressivity, variable domain and explicit team for combined complexity; no claim of locality. The supplied checker was inspected, not run. Its three-row closure calculation concerns an abstract subuniverse of valuations rather than all valuations of an exact alphabet of size log2(3); the general proof applies to actual declared domains.

## originality

PASS

Credit the known lax P baseline and the prior expressive-completeness construction (which already yields common-semantics witnesses). The supported distinct claim is the complexity separation, in particular strict NP-completeness on a single self-split of a conjunction of positive edge tests, despite fixed-domain expressive equivalence. No inspected source covers this restricted strict model-checking result.

## value

PASS

The separation shows why equal expressive power on a fixed valuation domain is not a reliable guide to combined model-checking complexity. Hardness already emerges from a single outer redundant-looking disjunction of identical positive formulas: disjointness alone creates the two-colour obstruction. This identifies a sharply restricted source of complexity without attributing novelty to property B or to the previous lax results.

The dated certificate retains the supplied scientific assessment, sources and limitations.
