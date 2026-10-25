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

# Verification and scope

Run `python3 verify_two_rank.py` from the directory containing this file. The script independently builds all nonempty cliques of the two-rank Hamming distance-two adjacency graph, computes signed simplicial Lefschetz traces on each conjugacy class, and compares with the predicted Specht characters using exact Jacobi–Trudi determinants and cycle-coloring counts.

Checked pairs: \((5,2),(6,2),(6,3),(7,3),(8,3),(8,4)\). Each uses *all* conjugacy classes of its ground-label symmetric group (respectively \(7,11,11,15,22,22\) classes). At \((8,3)\), the face vector by cardinality is \((126,1260,2940,1890,630,84)\) and the total is \(6930\), with degree-two rank \(461\). The success marker is `TWO_RANK_BOOLEAN_EQUIVARIANT_OK`.

The finite enumeration checks neither every parameter pair nor integral homology. The proof relies on the published homotopy concentration and explicit infinite-parameter chain and character calculations. No independent audit or external certification is claimed.
