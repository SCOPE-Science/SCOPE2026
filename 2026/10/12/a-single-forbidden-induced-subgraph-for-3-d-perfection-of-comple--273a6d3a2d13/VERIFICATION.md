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

The proof is analytic. A direct finite checker is supplied only as a stress test.

`verify.py` constructs each complete multipartite graph from its part profile, derives shortest-path triples from the graph adjacency relation, computes the exact chromatic and clique numbers of the resulting three-uniform hypergraph, and checks every induced part profile. It does not assume the forbidden-subgraph criterion during those invariant computations.

The replay covers every connected complete multipartite profile of orders \(2\) through \(8\), all induced profiles, and \(d\in\{2,3,4\}\). It also checks directly that \(K_{3,2,1}\) fails perfection and that each of its three vertex-deletion profile types is perfect.

Finite enumeration is not an all-orders proof. The infinite statement rests on the structural argument in `RESULT.md`.
