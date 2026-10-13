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

The analytic argument has four independently checkable steps.

First, within a fixed cut \(E(V_i,V_j)\), two edges conflict exactly when they are disjoint, so the induced conflict graph is \(\overline{L(K_{n_i,n_j})}\).

Second, any two edges from different cuts conflict. If they share a vertex, the other endpoints are in distinct parts and form a triangle with the shared vertex. If they are disjoint, an endpoint of one edge is adjacent to at least one endpoint of the other, giving a three-edge path. Hence the cut factors form a complete graph join.

Third, an independent set of \(\overline{L(K_{a,b})}\) is a star. Any coloring therefore gives star centers forming a vertex cover of \(K_{a,b}\), so at least \(\tau(K_{a,b})=\min\{a,b\}\) colors are necessary. Taking the stars centered on a smaller shore attains the bound.

Fourth, every optimum corresponds to a minimum vertex cover of each complete-bipartite cut. Unequal shores force the smaller shore; equal shores of size at least two allow exactly two choices. This gives the exact optimizer count.

The standalone script `artifacts/verify.py` reconstructs the conflict relation directly from the edge-coloring definition, computes exact conflict-graph chromatic numbers for all complete multipartite types through order seven, counts optimal unlabeled colorings through order six, and checks the explicit construction through order twenty-five. Its output is:

`ALL CHECKS PASSED; exact_types=37; exact_edges=388; structural_pairs=2375; count_types=23; counted_optimal_partitions=34; constructive_types=9270; constructive_edges=1685858; max_constructive_order=25`

The finite checks do not establish the arbitrary-order theorem; they stress-test the proof and the boundary cases. In particular, the direct analytic check on \(K_{2,2,2}\) gives \(2+2+2=6\), independently refuting the value \(2\) predicted by the 2023 proposition.
