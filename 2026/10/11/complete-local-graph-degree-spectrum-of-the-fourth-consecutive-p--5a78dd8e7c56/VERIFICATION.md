---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

The final finding specifies all 24 separately labeled arcs of Ov(4) and six length-three state vertices, so the normalized nonnegative circulation polytope is precisely the unrestricted frequency polytope. Each cycle support yields one extreme point by nonnegative flow decomposition and support minimality. The full directed graph has incidence rank 5, hence affine dimension 18. For two cycles the positive midpoint is in the relative interior of the union-support nonnegative-flow face; its dimension equals |E(U)|-|V(U)|+components(U)-1, and rank two gives exactly one-dimensional adjacency. Fresh independent code constructs every graph arc and all 160 simple directed cycle supports, evaluates all 12720 unordered pairs with both union-graph cycle rank and all-contained-simple-cycle counting, and confirms the ten-class degree and complete length-by-degree tables with zero criterion disagreements. The degree handshake sum 5334 yields 2667 edges; precisely all 72 Hamiltonian length-six cycles have the minimal degree 18. Two monotone loops have degree 159 and all other vertices distance 2 via them. The proof is a complete exact finite census of this fixed graph, not an extrapolation to all pattern lengths.

## originality

PASS

The exact identity of the frequency polytope with a directed cycle polytope, its dimension, and its general skeleton adjacency test are already established and excluded from the originality claim. Primary text comparisons distinguish those general facts from an evaluated order-four table. The complete ten-class graph-degree census, 2667 edges, joint 1..6 cycle-length/degree table, and 72 Hamiltonian/simple classification were not present in the inspected primary publications or another indexed finding. This is a best-of-knowledge new evaluated natural finite invariant, not a new general theorem on cycle polytopes or proof of exhaustive publication priority. The known general criterion does determine the instance algorithmically, but obtaining the full explicit distribution requires a nontrivial exhaustive computation.

## value

PASS

Order four is the first natural unrestricted consecutive-pattern frequency polytope beyond the small illustrated order-three example; its 18-dimensional geometry is accessible only indirectly through the overlap graph. The complete exact one-skeleton degree spectrum and joint cycle-length classification are natural local face invariants of the whole canonical polytope, not an arbitrary small slice or a textbook substitution. They distinguish all 72 simple Hamiltonian vertices from 88 nonsimple ones and quantify ten degree classes, providing reusable structure for polytope optimization and comparisons. No all-order theorem or downstream application is required for the independently useful natural complete finite invariant. The generic diameter-two fact is cheap and supplies background, not the value basis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
