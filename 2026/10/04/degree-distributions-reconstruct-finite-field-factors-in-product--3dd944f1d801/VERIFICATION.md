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
The proof is symbolic and does not depend on finite enumeration.

The critical local fact is that for nonzero
\[
A\in M_n(\mathbf F_q),
\]
the functional
\[
B\longmapsto\operatorname{tr}(AB)
\]
is nonzero. If \(a_{uv}\ne0\), then
\[
\operatorname{tr}(AE_{vu})=a_{uv}.
\]
Therefore its kernel has \(q^{n^2-1}\) elements.

For a product vertex with support size \(s\), the component equations are independent because they live in different factors. Hence the full orthogonal set has \(q^{T-s}\) elements. The two degree values differ only by whether the vertex itself belongs to that orthogonal set.

The packaged checker `artifacts/verify.py`:

- exhaustively verifies all trace-functional kernels for \(2\times2\) matrices over \(\mathbf F_2,\mathbf F_3,\mathbf F_4,\mathbf F_5\);
- constructs the entire graph of \(M_2(\mathbf F_2)\times M_2(\mathbf F_2)\) and checks all vertex degrees directly from adjacency;
- independently enumerates component self-orthogonality types and reconstructs the degree distributions for
\[
(2;2,3),\quad
(3;2,2,3),\quad
(4;2,3,3),\quad
(5;2,2,3,3);
\]
- recovers \(q\), the number of factors, and the unordered matrix-size multiset from only graph order and degree multiplicities.

The \(\mathbf F_4\) implementation uses
\[
\mathbf F_2[t]/(t^2+t+1).
\]

The checker returns `VERIFY_OK`.

Finite computation is not used to prove the theorem.
