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
The bundled checker `artifacts/verify.py` reconstructs the multiplication and verifies the anti-flexible identity on every basis triple.

For
\[
N=\begin{pmatrix}a&b\\c&d\end{pmatrix},
\]
it reconstructs the Nijenhuis torsion and verifies the complete criterion
\[
b=0,\qquad c(a-d)=0.
\]

It exhaustively checks every \(2\times2\) matrix over
\[
\mathbf F_2,\quad\mathbf F_3,\quad\mathbf F_5,\quad\mathbf F_7.
\]
The totals are
\[
6,\quad15,\quad45,\quad91,
\]
with rank profiles
\[
(1,3,2),\quad(1,6,8),\quad(1,12,32),\quad(1,18,72).
\]

It separately verifies that the automorphism group is trivial and that the weight-zero Rota--Baxter operators are exactly \(cE_{21}\).

The checker returns `VERIFY_OK`.

Finite enumeration is replay evidence. The arbitrary-field classification is proved in `RESULT.md`.
