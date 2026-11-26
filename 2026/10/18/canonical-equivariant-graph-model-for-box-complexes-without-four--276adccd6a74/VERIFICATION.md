---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Both coordinates of a Hom cell cannot have cardinality at least two, since four distinct alternating vertices would then form a four-cycle, even if chorded. The left and right simplex families meet only at the specified oriented-edge vertices. Minimum degree two ensures their centers are distinct from those vertices. The equivariant radial retraction can be seen explicitly: in a simplex with r vertices and barycentric weights x_i, let m be the second-largest weight, including ties, and λ=max_i x_i−m. Map to weights (1−λ)/r+max(x_i−m,0). This is continuous and permutation-equivariant, lies in the center-to-vertex tree, and fixes the tree pointwise, also for r=2 and ties. Straight-line homotopy gives the required local strong retraction and fixes all shared vertices, so both coordinate swap and every automorphism commute with the glued retraction. Each oriented-edge vertex subdivides exactly one edge of the double cover; its geometric quotient by swap is G after suppressing subdivisions. The cover has 2n vertices and 2m edges; path parity gives one component for nonbipartite G and two for bipartite G, proving integral homology by graph chains. In the rational trace identity H1=H0−C0+C1 in the representation ring, no-swap fixed cover vertices and forward-oriented edges have counts 2f and 2e. Swap fixes no cover vertices; each exchanged original edge fixes both lifts with reversed orientation, giving −2s. The action on the two bipartite components is the XOR of the graph bipartition swap and the cover layer swap, giving the stated H0 terms.

## originality

PASS

Credit a narrow increment: the specified embedded spine in the polyhedral Hom model with a simultaneous Aut(G)×C2 strong retraction, and the explicit full action including the mixed trace. The abstract homotopy type, ordinary homology, coordinate-swap-only graph model, and its swap quotient are materially covered by the older square-free literature (especially Kamibeppu), and do not constitute novelty. The later indexed Lovász/neighborhood result also covers the no-swap trace. The inspected prior claims do not give the joint action on this embedded Hom spine, nor a statement of the full mixed character; that character is a direct chain consequence once the full model is established, not a new representation-theoretic method.

## value

PASS

The useful refinement is a simultaneous equivariant model in the original Hom space: it gives a concrete integral cycle module and controls subgroup fixed spaces and the mixed swap/automorphism action, data an unadorned graph homotopy equivalence and Betti numbers do not encode. Keeping the swap sign on endpoint-exchanged edges gives an exact character for a natural symmetry action across the full stated class, not just a computation for selected examples. Neither the already-known graph type nor the routine graph-chain trace principle alone is credited as new value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
