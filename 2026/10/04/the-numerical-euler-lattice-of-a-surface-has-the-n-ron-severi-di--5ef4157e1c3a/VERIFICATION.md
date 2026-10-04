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

The verifier constructs matrices of the form
\[
M=
\begin{pmatrix}
-c&0&1\\
k&-Q&0\\
1&0&0
\end{pmatrix}
\]
for several nonsingular integral intersection matrices \(Q\), canonical-intersection vectors \(k\), and integers \(c\).

For each example it performs exactly the proof operations: reorder to \((e,p,f_1,\ldots,f_\rho)\), subtract \(k_i\) times the point row from each divisor row, and add \(c\) times the point column to the rank column. It checks that the result is
\[
H\oplus(-Q).
\]

It independently checks
\[
\det M=(-1)^{\rho+1}\det Q
\]
and verifies with exact Smith-normal-form arithmetic that the invariant factors of \(M\) are two unit factors plus those of \(Q\).

These finite examples are not the proof of the theorem for arbitrary Picard rank. The uniform integral operations in `RESULT.md` establish the general matrix equivalence; Riemann–Roch supplies the matrix and Hodge index supplies the determinant sign.

The saved replay output ends in `VERIFY_OK`.
