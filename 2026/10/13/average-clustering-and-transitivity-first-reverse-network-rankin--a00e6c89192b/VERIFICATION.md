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
The embedded `verify_clustering_transitivity_minimal_reversal.py` performs a complete exact finite replay.

For each order from \(2\) through \(5\), it enumerates every labeled simple graph, retains exactly the connected graphs, and canonically quotients them under all vertex permutations. It recovers
\[
1,\ 2,\ 6,\ 21
\]
connected unlabeled graph types.

All statistics are computed with exact `Fraction` arithmetic from:
- triangle counts;
- centered connected-triple counts;
- local neighbor-edge counts.

Under averaging over degree-at-least-\(2\) vertices, the strict reversal counts are
\[
0,\ 0,\ 0,\ 13.
\]

Under the alternative convention assigning local clustering \(0\) below degree \(2\), the counts are
\[
0,\ 0,\ 0,\ 12.
\]

The displayed witness is also checked from independent hand-count identities:
\[
\tau(A)=8,\qquad
\tau(B)=7,
\]
with one triangle in each graph, and local-clustering lists
\[
\left(\frac16,1,1\right)
\]
and
\[
\left(\frac13,\frac13,1\right).
\]

Run:

`python3 verify_clustering_transitivity_minimal_reversal.py`

The first output line must be:

`VERIFY_OK`

The finite enumeration is exhaustive because every labeled simple graph on the relevant vertex set is generated and isomorphism is tested against every vertex permutation.
