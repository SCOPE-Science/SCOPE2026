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
For a bipartition \(A\mid B\) in a graph with \(m\) edges, let
\[
a=\operatorname{vol}(A),\qquad
b=\operatorname{vol}(B),\qquad
c=|E(A,B)|.
\]

Then
\[
Q=\frac{ab}{2m^2}-\frac{c}{m}
\]
and
\[
\operatorname{Ncut}=\frac{2mc}{ab},
\]
so
\[
Q=\frac{ab}{2m^2}\left(1-\operatorname{Ncut}\right).
\]

The embedded `verify_modularity_ncut_boundary.py` enumerates every connected labeled simple graph through six vertices and every bipartition with at least two vertices per side and positive modularity.

It verifies connected labeled graph counts
\[
1,\ 4,\ 38,\ 728,\ 26704
\]
for orders \(2\) through \(6\).

It finds no strict modularity–normalized-cut reversal through five vertices, exactly \(420\) labeled reversing partition pairs at six vertices, and exactly two graph-plus-partition-pair isomorphism classes after canonicalization by all vertex permutations and partition symmetries.

Run:

`python3 verify_modularity_ncut_boundary.py`

The first output line must be:

`VERIFY_OK`

All objective values and comparisons use exact rational arithmetic.
