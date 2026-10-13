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
The packaged checker `artifacts/verify.py` uses the dual-number multiplication
\[
(x_0+x_1\varepsilon)(y_0+y_1\varepsilon)
=
x_0y_0+(x_0y_1+x_1y_0)\varepsilon.
\]

It reconstructs the anti-Rota–Baxter defect of a general matrix
\[
T=
\begin{pmatrix}
a&b\\
c&d
\end{pmatrix}
\]
on all four ordered basis pairs and verifies the six scalar equations in `RESULT.md`.

It separately checks the strong identity on every ordered basis triple and the conjugation action of every algebra automorphism.

Direct exhaustive enumeration over
\[
\mathbf F_2,\quad\mathbf F_3,\quad\mathbf F_5,\quad\mathbf F_7
\]
gives anti-Rota–Baxter counts
\[
2,\quad17,\quad5,\quad7.
\]
Over \(\mathbf F_3\) it gives rank profile
\[
(1,10,6),
\]
strong count \(9\), invertible count \(6\), and \(11\) automorphism-conjugacy classes.

The checker returns `VERIFY_OK`.

The arbitrary-field result rests on the exact symbolic equations and case analysis in `RESULT.md`; finite enumeration is a replay check.
