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
For a connected graph, the two metrics are exact functions of the unordered pair-distance histogram:
\[
L(G)=\frac{\sum_r r h_r}{\binom{n}{2}},
\qquad
E(G)=\frac{\sum_r h_r/r}{\binom{n}{2}}.
\]

The embedded `verify_efficiency_path_boundary.py` uses only the Python standard library.

It enumerates every labeled simple graph for
\[
2\le n\le6,
\]
filters exactly for connectivity, computes all-pairs shortest-path distances by breadth-first search, and compares exact rational metric pairs within every fixed \((n,m)\) group.

It reproduces the connected labeled graph counts
\[
1,\ 4,\ 38,\ 728,\ 26704
\]
and finds zero strict ranking reversals through six vertices.

For the displayed seven-vertex witnesses it verifies distance histograms
\[
1^7,2^6,3^6,4^2
\]
and
\[
1^7,2^7,3^4,4^2,5,
\]
the common degree multiset
\[
(1,1,2,2,2,3,3),
\]
and exact values
\[
L(A)=\frac{15}{7},\quad E(A)=\frac{25}{42},
\]
\[
L(B)=\frac{46}{21},\quad E(B)=\frac{188}{315}.
\]

Run:

`python3 verify_efficiency_path_boundary.py`

The first output line must be:

`VERIFY_OK`

The finite lower bound is exhaustive; the seven-vertex existence statement is verified directly from the complete shortest-path data of the two explicit graphs.
