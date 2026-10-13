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
The graph domain is finite for the lower-bound step. Every connected simple graph is generated and quotiented by all vertex permutations for
\[
2\le n\le5.
\]
The connected unlabeled counts recovered are
\[
1,\ 2,\ 6,\ 21.
\]

Adjacency Perron roots are isolated from
\[
\det(\lambda I-A).
\]
For multicyclic graphs, nonbacktracking Perron roots are isolated from the Ihara--Bass auxiliary polynomial
\[
\det(\lambda^2I-\lambda A+D-I).
\]
Trees and connected unicyclic graphs use their exact nonbacktracking radii \(0\) and \(1\).

All polynomial arithmetic, greatest-common-divisor checks, and Sturm root counts use exact rational arithmetic.

The explicit six-vertex edge sets are rebuilt directly and their dominant roots are isolated again. The verifier proves
\[
\rho_A(G)>\rho_A(H)
\]
and
\[
\rho_B(G)<\rho_B(H).
\]

Run:

`python3 verify_adjacency_nonbacktracking_boundary.py`

The final output line must be `VERIFY_OK`.
