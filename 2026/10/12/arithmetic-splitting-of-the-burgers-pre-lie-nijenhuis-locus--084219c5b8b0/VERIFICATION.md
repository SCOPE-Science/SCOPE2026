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
The bundled checker reconstructs the Burgers pre-Lie product and every Nijenhuis torsion coefficient.

For
\[
N=\begin{pmatrix}A&B\\C&D\end{pmatrix},
\]
it verifies the complete criterion
\[
C(B+C)=0,\qquad C(A-D)=0,\qquad (A-D)^2+B(B+C)=0.
\]

It independently reconstructs the two-element automorphism group and exhaustively tests every \(2\times2\) matrix over
\[
\mathbf F_3,\quad\mathbf F_5,\quad\mathbf F_7,\quad\mathbf F_{11},\quad\mathbf F_{13}.
\]
Point totals, rank profiles, and conjugacy-orbit counts agree with the split/nonsplit formulas.

The checker also verifies the odd/even extension-degree point laws used in the nonsplit zeta calculation and returns `VERIFY_OK`.

Finite enumeration is replay evidence. The arbitrary-field theorem is proved directly in `RESULT.md`.
