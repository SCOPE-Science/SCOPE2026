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
The universal bound is analytic. The standalone checker replays an exact rational equality case.

For
\[
A=
\begin{pmatrix}
9&0\\
0&1
\end{pmatrix},
\qquad
B=
\begin{pmatrix}
1/9&-1/6\\
-1/6&1
\end{pmatrix},
\]
the symmetrically preconditioned matrix is
\[
C=
\begin{pmatrix}
1&-1/2\\
-1/2&1
\end{pmatrix}.
\]
Its trace and determinant are
\[
2
\quad\text{and}\quad
\frac34,
\]
so its eigenvalues are exactly
\[
\frac12
\quad\text{and}\quad
\frac32.
\]
Thus
\[
\delta=\frac12,
\qquad
\kappa_2(A)=9.
\]

The residual propagator is
\[
I-AB=
\begin{pmatrix}
0&3/2\\
1/6&0
\end{pmatrix}.
\]
Applying it to \(e_2\) gives
\[
\frac32e_1,
\]
so the Euclidean amplification is exactly
\[
\frac32
=
\delta\sqrt{\kappa_2(A)}.
\]

Finite replay is corroborative only. The all-dimensional upper bound and the all-parameter equality family are proved in `RESULT.md`.
