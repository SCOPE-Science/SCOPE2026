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

The proof is symbolic and uniform. Its critical checks are: (1) in a distance-regular graph, every 2-WL multiplicity for a pair at distance \(k\) is determined by intersection numbers and therefore depends only on \(k\); (2) from a threshold \(m\), geodesic witnesses make the minimum occurring singleton-distance sum equal to each \(k\le2m\); and (3) for \(k>2m\), the two radius-\(m\) balls are disjoint, so all signature counts depend only on fixed sphere sizes.

The accompanying `artifacts/verify.py` performs direct ordered-pair 2-WL, all-pairs shortest paths, and an exact check of the distance-regular intersection-number condition. It verifies the theorem on 26 graphs from five standard families and checks that terminal 2-WL colors coincide exactly with graph-distance classes. Its expected terminal line is:

`VERIFY_OK graphs=26 max_vertices=32 families=cycles,balanced_complete_bipartite,hypercubes,Petersen,Johnson`

This finite computation is a regression check rather than a proof of the infinite theorem.
