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

The analytic proof is the source of the unbounded claim. The key identity is that for occupancies \(d_i\) and set size \(s\), an outside vertex in part \(V_i\) has exactly \(s-d_i\) selected neighbors. Therefore a proper \(3\)-dominating set is characterized by \(s-d_i\ge3\) on every incomplete part and equality for at least one incomplete part.

`verify.py` checks the theorem in two independent finite ways. Its occupancy enumerator examines every nondecreasing complete-multipartite profile of total order at most \(20\) and every feasible occupancy vector. Its labeled-graph enumerator independently builds adjacency and checks every vertex subset for every profile of total order at most \(9\). It also checks the published complete-bipartite special cases on a wider range.

These tests can expose algebraic or boundary mistakes in the classification, but they do not prove the theorem for unbounded part sizes. The proof in RESULT.md supplies that step. Literature searches also cannot certify absolute novelty; they establish only that the inspected sources and searched formulations do not cover the claim.
