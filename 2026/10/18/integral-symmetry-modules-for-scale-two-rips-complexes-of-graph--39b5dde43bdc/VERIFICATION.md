---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The distances in the bipartite subdivided graph give exactly old-old edges of G, endpoint incidences, and pairs of incident graph edges. Pairwise intersecting distinct edges either share one endpoint or form a triangle; the all-edge triangle cannot be extended. Removing these maximal triangles leaves the core A. At any stage of deleting edge vertices, the link of e_uv in the remaining core consists of two disjoint simplices supported at u and v joined by the edge uv: cross-star edge-vertex link edges would require one of the removed triangles. This link stays contractible even when either star has no other edges, so B→A is a homotopy equivalence. For each triangle, its six vertices have exactly the three stated nonedges. The join of its three augmented 0-cycles is an integral 2-cycle with coefficient −1 on the relative generator ordered by the three opposite old vertices, and zero on all other relative generators. Its alternating sign under permuting factors is precisely the relative orientation action. A common sign convention makes the cycles an integral equivariant right inverse, killing the connecting homomorphism and proving every asserted inclusion isomorphism. In degree one, replacing each subdivided edge by its old edge changes the chain by the boundary of a filled mixed triangle, which proves the persistent quotient, integrally and naturally. The character and exterior-power statements follow by reading the signed oriented-subset basis; a stabilizing transposition forces each invariant coefficient to vanish. This argument proves the general statement, including B with torsion. The inspected verification files give finite regression evidence, not a general proof.

## originality

PASS

Credit the prior total-graph homotopy type, exceptional cells, core reduction and attaching argument in full. The supported distinction is the canonical integral section by specified absolute cycles, with the signed automorphism module and the inclusion-induced description of persistence. The prior nonequivariant splitting and its relative-cell model do not themselves supply an isomorphism-natural integral choice of lift in absolute homology. This is a close refinement of that proof, not a new sphere-count theorem.

## value

PASS

The uniform splitting supplies a specific canonical homology lattice over Z, not a Betti number or an arbitrarily chosen lift. That information is usable for symmetry and integral calculations even when the base contributes torsion; for K_n it distinguishes the oriented lattice from the tempting unsigned sphere-permutation interpretation, which would have invariants. The result is valuable as this precise refinement, not on the strength of the already known wedge count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
