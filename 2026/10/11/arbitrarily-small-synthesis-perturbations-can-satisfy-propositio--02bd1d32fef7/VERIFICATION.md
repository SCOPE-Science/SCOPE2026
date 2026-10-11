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
T_\Phi=
\begin{pmatrix}
1&1\\
a&-a
\end{pmatrix},
\qquad
T_\Psi=
\begin{pmatrix}
1&1\\
-a&a
\end{pmatrix},
\]
we have
\[
T_\Phi T_\Phi^*
=
T_\Psi T_\Psi^*
=
\begin{pmatrix}
2&0\\
0&2a^2
\end{pmatrix}.
\]
Thus
\[
\|T_\Phi\|=\|T_\Psi\|=\sqrt2
\]
for \(0<a\le1/8\).

The difference is
\[
T_\Phi-T_\Psi=
\begin{pmatrix}
0&0\\
2a&-2a
\end{pmatrix},
\]
so
\[
\|T_\Phi-T_\Psi\|=2\sqrt2\,a.
\]
Taking
\[
\lambda=2\sqrt2\,a
\]
gives
\[
\lambda(\|T_\Phi\|+\|T_\Psi\|)
=
8a
\le1
=
\frac{A_\Phi}{2}\|K^\dagger\|^{-2}.
\]

For
\[
f_a=-a e_1+e_2,
\qquad
g_a=e_1+a e_2,
\]
we have
\[
\langle f_a,g_a\rangle=0
\]
and
\[
\|K^*f_a\|^2=a^2.
\]
Hence the weave containing two copies of \(g_a\) has coefficient energy \(0\) on a vector whose \(K^*\)-seminorm is positive.

The publisher PDF was inspected at the proposition statement and the complete proof, including the page image containing the conversion from an ambient \(\|f\|^2\) term to a \(K^*\)-term. The earlier woven-\(K\)-frame perturbation theorem was also inspected at its critical restricted-space estimate.

No numerical approximation is used; the matrix norms and frame inequalities are exact.
