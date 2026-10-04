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
# Verification

The embedded `verify.py` is dependency-free and reconstructs the three six-point height-two models from their bipartite Hasse graphs. For each model it chooses a spanning tree and the three associated fundamental cycles, verifies that those cycles have zero boundary, and uses their non-tree edges as exact integral homology coordinates.

The program then enumerates all \(6^6=46656\) set maps. A map survives exactly when it is order-preserving. For each surviving map the program computes the induced edge-chain map, checks that each cycle image reconstructs exactly from its three homology coordinates, forms the integral \(3\times3\) matrix, and records its rank and determinant. A separate inverse-monotonicity test detects finite-poset homeomorphisms.

Run `python3 verify.py`. The expected output is:

`VERIFY_OK`
`K2,4_self_maps=1782`
`K2,4_distinct_H1_actions=421`
`K2,4_distinct_rank_profile=1,84,288,48`
`K2,4_H1_isomorphism_maps=48=homeomorphisms`
`K4,2_opposite_same_counts=yes`
`K3,3_minus_edge_self_maps=646`
`K3,3_minus_edge_distinct_H1_actions=113`
`K3,3_minus_edge_distinct_rank_profile=1,60,48,4`
`K3,3_minus_edge_H1_isomorphism_maps=4=homeomorphisms`
`direct_H1_action_count_depends_on_minimal_model=yes`

The finite census is exhaustive for the stated spaces. Literature comparison and originality assessment are not machine-certified.
