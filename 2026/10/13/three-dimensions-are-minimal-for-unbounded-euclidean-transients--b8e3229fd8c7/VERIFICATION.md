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
The universal arguments are analytic. The embedded checker replays exact consequences from the finalized formulas.

For
\[
H=\operatorname{diag}(1,2,4),
\qquad
\alpha=2,
\]
and
\[
S_t=t
\begin{pmatrix}
0&1&0\\
-1&0&-1\\
0&1&0
\end{pmatrix},
\]
the checker reconstructs
\[
M_t=(2I+S_t)^{-1}(2I-H)(2I+H)^{-1}(2I-S_t)
\]
using exact rational arithmetic.

At \(t=6\), it verifies
\[
M_6e_2=(-1,0,1)^{\mathsf T},
\]
so
\[
\frac{\|M_6e_2\|_2^2}{\|e_2\|_2^2}=2.
\]
At \(t=12\), the corresponding squared ratio is \(8\).

The checker also verifies the characteristic-polynomial identity
\[
\det(\lambda I-M_t)
=
\lambda
\left(
\lambda^2+\frac{t^2-2}{9(t^2+2)}
\right)
\]
at several exact rational values.

For a two-dimensional sample it reconstructs the HSS matrix and verifies, through exact trace and determinant invariants of \(M^{\mathsf T}M\), that its squared singular values agree with those of
\[
D=(\alpha I-H)(\alpha I+H)^{-1}.
\]

Finite replay is corroborative only. The all-real-\(2\times2\) contraction statement follows from the orthogonal factorization proved in `RESULT.md`, and unboundedness follows from the exact formula for \(M_te_2\).

Unproved limits include the general complex \(2\times2\) case, inexact HSS, full-matrix condition-number constraints, and finite-precision transients.
