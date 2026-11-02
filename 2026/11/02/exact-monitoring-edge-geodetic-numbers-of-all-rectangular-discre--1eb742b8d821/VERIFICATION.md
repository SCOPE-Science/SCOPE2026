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

The theorem is a mathematical proof using the Cartesian-fiber criterion and an explicit cyclic-gap estimate. The integer ceiling bound is verified symbolically for all orders at least 13, while all 36 smaller pairs are reduced to a finite arithmetic comparison. Two exceptional arrays are displayed and checked directly.

Run `python3 verify.py` (Python 3 standard library only) to reproduce:

`VERIFY_OK: 36 arithmetic small pairs; 7491 cycle-slice parameter pairs; 14 independent adjacency/BFS graph cases; 1318 edge-deletion checks; 16 forced-small-factor graph cases`

The 14 independent tests construct each graph's adjacency from scratch and verify, separately for each edge, that deleting the edge increases the distance of some selected vertex pair. No finite test proves the assertion for unbounded orders: that assertion follows from the written ceiling argument and exceptional arrays. The novelty comparison is a literature search, not a proof of publication priority. No independent audit has been performed.
