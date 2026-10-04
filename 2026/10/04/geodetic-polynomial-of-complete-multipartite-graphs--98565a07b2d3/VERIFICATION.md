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

`verify.py` independently builds each tested complete multipartite graph, computes graph distances by breadth-first search, and declares a subset geodetic only when every vertex lies on a shortest path between some selected pair according to the distance identity. It then compares that literal test with the theorem's heavy-part criterion.

For every tested part profile it also counts geodetic subsets by cardinality, reconstructs the closed polynomial coefficient vector from its algebraic formula, and checks equality coefficient-by-coefficient. Finally it compares the literal minimum geodetic-set size with the stated scalar corollary.

The finite census is not a proof for arbitrary order. The infinite statement is proved in `RESULT.md` from the exact shortest-path structure of complete multipartite graphs.
