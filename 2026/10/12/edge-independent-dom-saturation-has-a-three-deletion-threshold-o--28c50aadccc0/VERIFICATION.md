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

The universal argument is analytic. The critical checks are:

1. A matching is maximal exactly when the unmatched vertices span no edge.
2. In a matching-deleted biclique, each vertex has at most one cross-shore nonneighbor.
3. If the shores are unequal, every maximal matching saturates the smaller shore.
4. If the shores are equal, every maximal matching has size at least \(n-1\).
5. For one or two deletions, the present edge \(a_1b_2\) cannot occur in a size-\(n-1\) maximal matching.
6. With at least three deletions, choose a deleted pair disjoint from the prescribed edge; after fixing that edge and reserving the deleted pair as the two unmatched vertices, the residual graph is complete bipartite minus a matching and has a perfect matching by Hall's theorem.

`verify.py` independently enumerates every maximal matching for all \(2\le m\le n\le6\) and \(0\le t\le m\), computes the prescribed-edge local minima, and checks the theorem and the stronger structural assertions. The enumeration is finite evidence only; it is not extrapolated beyond its tested range.

Replay output: `ALL CHECKS PASSED; parameter_cases=65; edge_checks=1098; maximal_matchings=10722; range=2<=m<=n<=6; 0<=t<=m`
