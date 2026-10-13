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

The verifier rebuilds the full binary length-\(6\) domain, generates each at-most-one-transposition/at-most-one-deletion output ball directly, builds all \(928\) compatibility edges, and exhaustively enumerates all maximal cliques. It then independently checks each maximum code's pairwise disjointness, intersects all maxima to obtain the two constant words, and exhausts reversal/complement images.

Fresh replay output:

`VERIFY_OK vertices=64 edges=928 maximal_cliques=2921 histogram=3:218,4:1861,5:816,6:26 maximum=6 labeled_maxima=26 core=000000,111111 group_size=4 orbits=10 orbit_sizes=1x2,2x4,4x4 coverage=28x1,32x4,33x4,36x5,37x8,38x4 nodes=3735 witness=000000,000011,001111,110000,111100,111111`

The proof is finite and exhaustive. No statement about longer lengths, the full graph automorphism group, or asymptotic behavior is inferred from this computation.
