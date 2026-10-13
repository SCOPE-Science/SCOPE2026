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
`artifacts/verify.py` uses only the Python standard library.

For every full-vertex simplicial complex on at most four vertices, it computes generalized Hamming weights directly from all message subspaces over both
\[
\mathbb F_2
\]
and
\[
\mathbb F_3.
\]
It independently computes
\[
|\Delta|-\max_{|T|=k-r}|\Delta|_T|
\]
and checks equality for every \(r\).

The verifier also reconstructs source Example 4.2 from maximal faces
\[
\{0,1\},\quad\{0,2,3\},\quad\{4,5,6,7\}.
\]
It confirms length \(24\), dimension \(8\), and the direct binary generalized-weight hierarchy
\[
(2,6,8,9,17,21,23,24),
\]
matching the induced-subcomplex formula.

Finally, for several values of \(N\), it constructs the cone over the \((N-1)\)-skeleton of an \(N\)-simplex and checks
\[
d_r=2^{N+2}-2-2^{N+2-r}
\]
for every \(1\le r\le N+2\).

Successful replay prints `VERIFY_OK`.
