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

Deleting a leaf block except for its attachment gives a smaller connected cactus (retain any one vertex if the whole graph is one block), proving exhaustive leaf-block generation. Alternatively, deleting just one non-articulation vertex from a leaf block preserves the connected cactus property, proving exhaustive vertex augmentation. The independent check used the latter generation with a fresh exact filter: enumerate each simple cycle once by fixing its least vertex and orientation, and reject two cycles sharing an edge. Isomorphism-invariant fingerprints are only buckets before exact adjacency-preserving bijections; every vertex is tested as root, and testing one representative against all vertices of its stable cell suffices by orbit equivalence. The dependency-free census reproduced 1,1,2,4,9,23,63,188,596 unrooted types, all 2,153 rootings passing through eight and exactly one of 5,364 failing at nine, with exact rooted isomorphism to the stated witness. Directly, the root, its two neighbors, and the other six vertices form an equitable partition after one round: each vertex of the six-cell sees one in that cell and one in the two-cell. The pentagon is invariant, so its two further vertices cannot map into either triangle. Reflection and the two triangle swaps provide exactly the claimed four rooted orbits. Having a single failing representative/root choice also establishes uniqueness up to rooted isomorphism.

## originality

PASS

The closest literature result identifies connected rooted outerplanar graphs across inputs and explicitly allows an orbit-recovery failure with a different stable-cell profile. The closest indexed results change the graph class, the initial coloring, or the property. The inspected claims do not cover the sharp rooted cactus cutoff and unique witness.

## value

PASS

One root often makes refinement effective on block-structured graphs, so the first point where it still merges structurally different vertices is a natural boundary. The unique minimal example exposes the mechanism: vertices on a long cycle and in attached triangles can see identical class multiplicities even though the blocks cannot be exchanged. The lower bound and uniqueness make this more informative than an isolated obstruction or an unrooted graph count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
