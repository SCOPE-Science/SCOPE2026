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

The arbitrary-order proof is analytic. For a vertex in a partite class, every partition block has distance exactly \(0\), \(1\), or \(2\), and the number of \(2\)-entries is determined by the number of blocks lying wholly in that partite class and by whether the vertex's own block is pure. This yields at most two representation types per graph part and forces the cross-part collision described in `RESULT.md`.

The standalone script `verify.py` independently enumerates every complete multipartite part-size profile of total order \(2\) through \(7\), every set partition of the vertex set, and every multiset partition representation directly from graph distances. It also checks the closed representation formula for every vertex. The expected replay summary is:

`ALL CHECKS PASSED; graph_profiles=37; set_partitions=14692; vertex_formula_checks=99960; order_range=2..7`

This finite computation is not the proof for arbitrary order. No independent audit has been performed.
