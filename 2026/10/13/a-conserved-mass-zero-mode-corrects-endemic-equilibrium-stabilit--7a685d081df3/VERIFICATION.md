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

For
\[
q=1-\frac1{\mathcal R_0},
\qquad
\beta=\gamma\mathcal R_0,
\]
the zero-mode matrix is
\[
M_0=
\begin{pmatrix}
-\beta q^2 & \gamma q\\
\beta q^2 & -\gamma q
\end{pmatrix}.
\]
Its determinant is exactly zero and its trace is
\[
-\beta q^2-\gamma q
=
-\gamma(\mathcal R_0-1).
\]

The two exact homogeneous eigenvectors are
\[
\begin{pmatrix}1\\ \mathcal R_0-1\end{pmatrix}
\quad\text{with eigenvalue }0,
\]
and
\[
\begin{pmatrix}1\\-1\end{pmatrix}
\quad\text{with eigenvalue }-\gamma(\mathcal R_0-1).
\]
The first changes total mass; the second has zero total perturbation.

For positive spatial modes,
\[
B_l=f_*g_*l^4+
\bigl(f_*\gamma q+g_*\beta q^2\bigr)l^2>0,
\]
while
\[
B_0=0.
\]
Thus the source's claim that \(B_l\) is positive for all Neumann modes cannot include \(l=0\).

The bundled checker verifies these identities using exact rational arithmetic for multiple admissible rational values of \(\mathcal R_0\), \(\gamma\), \(f_*\), \(g_*\), and \(l\). The general proof is algebraic and appears in `RESULT.md`.
