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

Let
\[
C=\begin{pmatrix}2&1\\1&1\end{pmatrix},
\qquad
C'=\begin{pmatrix}1&-1\\-1&2\end{pmatrix}.
\]
Direct multiplication gives \(CC'=C'C=I\). Both matrices have positive trace and determinant \(1\), hence are positive definite.

For
\[
P_1=\begin{pmatrix}1&0\\0&0\end{pmatrix},
\qquad
P_2=\begin{pmatrix}0&0\\0&1\end{pmatrix},
\]
one has
\[
C^*P_1C'
=\begin{pmatrix}2&-2\\1&-1\end{pmatrix},
\qquad
C^*P_2C'
=\begin{pmatrix}-1&2\\-1&2\end{pmatrix},
\]
and their sum is \(I\). Hence
\[
\sum_{i=1}^2
\langle P_iC'f,P_iCf\rangle
=
\|f\|^2
\]
for every \(f\).

The first local operator is not self-adjoint, and
\[
\left\langle
\begin{pmatrix}2&-2\\1&-1\end{pmatrix}e_2,e_2
\right\rangle=-1.
\]
Therefore it is not positive. A positive square root \(R\) satisfying \(R^2=C^*P_1C'\) cannot exist; equivalently, the source's coefficient identity would force the impossible equality
\[
\|Re_2\|^2=-1.
\]

The target full text was checked at Definition 3.1 and the immediately following controlled-analysis-operator construction. The 2012 precursor was checked at its corresponding definition and square-root construction. The proof uses no numerical approximation, finite sampling, or extrapolation.
