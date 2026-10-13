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
The proof is analytic. The checker replays exact rational instances of the displayed family.

For
\[
A_M=
\begin{pmatrix}
-1&M\\
0&-1
\end{pmatrix},
\qquad
B=e_2,
\qquad
\sigma=1,
\]
the Cayley factor is
\[
C_M=
(A_M+I)(A_M-I)^{-1}
=
\begin{pmatrix}
0&-M/2\\
0&0
\end{pmatrix},
\qquad
C_M^2=0.
\]

The exact solution is
\[
P=
\begin{pmatrix}
M^2/4&M/4\\
M/4&1/2
\end{pmatrix},
\]
and after one ADI column,
\[
P_1=
\begin{pmatrix}
M^2/8&M/4\\
M/4&1/2
\end{pmatrix}.
\]
The checker reconstructs
\[
R_0=e_2e_2^{\mathsf T},
\qquad
R_1=\frac{M^2}{4}e_1e_1^{\mathsf T},
\qquad
R_2=0,
\]
and verifies
\[
P-P_1=\frac{M^2}{8}e_1e_1^{\mathsf T}.
\]

For \(M=6\), it checks the exact residual amplification factor \(9\).

The arbitrary-\(M\) conclusion and one-dimensional minimality are proved symbolically in `RESULT.md`; finite replay is supporting evidence only.

Unproved limits include finite-precision behavior and sharp residual bounds under additional dissipativity, numerical-range, or eigenvector-conditioning assumptions.
