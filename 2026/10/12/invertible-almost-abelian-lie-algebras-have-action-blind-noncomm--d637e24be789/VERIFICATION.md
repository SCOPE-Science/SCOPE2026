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
The proof is symbolic.

The packaged checker `artifacts/verify.py` constructs the algebras directly over
\[
\mathbf F_2,\quad\mathbf F_3,\quad\mathbf F_5
\]
for scalar, Jordan, and nonscalar diagonal invertible actions.

It tests
\[
(q,n)=(2,1),(2,2),(2,3),(3,2),(5,2).
\]
For every pair of nonzero elements it computes the bracket and checks that adjacency is exactly inequality of the predicted multipartite labels. It verifies both degree formulas.

For
\[
(q,n)=(2,2)
\quad\text{and}\quad
(3,2),
\]
it exhaustively checks that \(I_2\) is not proportionally similar to \(I_2+E_{12}\).

The checker returns `VERIFY_OK`.

Finite computation is not used to prove the all-field theorem.
