---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

The pinned source defines a unit flow on a finite acyclic directed graph with every arc on a source-sink route and at least two distinct routes. Nonnegative flow decomposes into route-incidence vectors because of acyclicity. Arc precedence e<f when head(e) reaches tail(f) is a strict poset, and a chain of arcs extends to a route. Dilworth makes its width w equal the minimum number of routes covering all arcs, allowing overlaps. For an admissible reflection with factor lambda every c_e>=1/(lambda+1); summing over a size-w antichain yields lambda>=w-1 since a route meets an antichain at most once. Averaging a width-w route cover gives a unit flow c_e>=1/w; for any c with those inequalities, wc-chi_R is a nonnegative flow of strength w-1 for every route R, yielding exact containment for all F(G), and conversely this condition is forced at optimum. Positive integer flows decompose into integer routes, so the minimal k with all arc entries positive is exactly cover width w; this is the codegree in the declared lattice. A matching in the transitive-closure poset provides w=|E|-nu. No inference from the bounded checker is necessary for the all-DAG proof.

## originality

PASS

This is the all-DAG equality s(F)=width(arc poset)-1 and equality of minimizing-center set with the coordinate lower-bound slice, together with lattice codegree. Earlier flow-polytope papers establish route vertices/triangulations and codegree for stronger balance/Gorenstein assumptions; their theorems do not state the current all-network reflection containment or all centers. An abstract Dilworth identity alone has no Minkowski centers. Originality is qualified by general combinatorial-polytope symmetry literature.

## value

PASS

Acyclic unit-flow polytopes are central combinatorial optimization objects, and Minkowski asymmetry is a natural but difficult affine invariant. Identifying it exactly for arbitrary acyclic networks by a readily computable arc-poset width, simultaneously classifying every center and relating the same number to lattice codegree, is a genuine complete infinite-family structural classification. The polytime Dilworth matching formula is useful even when the graph is not planar, balanced, or Gorenstein.

The dated certificate retains the supplied scientific assessment, sources and limitations.
