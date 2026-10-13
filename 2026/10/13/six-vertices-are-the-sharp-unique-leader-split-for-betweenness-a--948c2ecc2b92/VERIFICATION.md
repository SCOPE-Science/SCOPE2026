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
The embedded `verify_betweenness_eigenvector_boundary.py` performs an exact finite replay using only the Python standard library and the embedded `graph_atlas_connected_2to6.json` table.

The graph-domain counts are
\[
1,2,6,21,112
\]
connected unlabeled graphs for orders \(2,3,4,5,6\).

For every graph, betweenness is computed independently by:
1. the exact Brandes dependency recurrence;
2. exact all-pairs shortest-path counts using the factorization \(\sigma_{sv}\sigma_{vt}/\sigma_{st}\) when \(v\) lies on an \(s\)-\(t\) geodesic.

The two rational vectors must agree identically.

Eigenvector-centrality maxima are certified without floating-point eigensolvers. The verifier computes the adjacency characteristic polynomial and every principal characteristic cofactor over the integers, isolates the Perron root with rational Sturm sequences, and uses the diagonal adjugate identity to compare squared Perron coordinates exactly.

The replay verifies conflict-class counts
\[
0,0,0,0,7
\]
through order six, automorphism-group orders
\[
1,1,1,1,4,2,2,
\]
orbit sizes
\[
720,720,720,720,180,360,360,
\]
total connected labeled order-six count \(26704\), and total labeled first-conflict count \(3780\).

Run:

`python3 verify_betweenness_eigenvector_boundary.py`

The first output line must be:

`VERIFY_OK`
