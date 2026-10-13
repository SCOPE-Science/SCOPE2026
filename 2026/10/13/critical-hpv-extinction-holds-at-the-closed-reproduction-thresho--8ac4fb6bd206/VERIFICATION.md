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
The bundled checker reconstructs the disease-free infectious-core matrix
\[
A_0=
\begin{pmatrix}
\beta_1-q_E & \beta_2+\alpha_4 & \beta_3\\
\alpha & -q_1 & \alpha_3\\
0 & \alpha_1 & -q_2
\end{pmatrix}.
\]

At the critical threshold it uses
\[
w=
\left(
\alpha q_2,\;
q_2(q_E-\beta_1),\;
\alpha\beta_3+\alpha_3(q_E-\beta_1)
\right).
\]
Symbolic expansion verifies
\[
w^{\mathsf T}A_0
=
\left(0,\det A_0,0\right).
\]
Therefore
\[
\det A_0=0
\]
implies the exact left-null identity.

The checker also verifies that the determinant equation is equivalent to
\[
(q_E-\beta_1)(q_1q_2-\alpha_1\alpha_3)
=
\alpha\left[q_2(\beta_2+\alpha_4)+\alpha_1\beta_3\right].
\]
Because every rate is positive and
\[
q_1q_2>\alpha_1\alpha_3,
\]
the critical vector \(w\) is strictly positive.

No numerical trajectory or finite parameter scan is used.
