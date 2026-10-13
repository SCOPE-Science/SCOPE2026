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
The theorem is analytic. The standalone checker replays the explicit sharp family.

For
\[
\tau=\frac34
\]
and
\[
\kappa=2,
\]
it reconstructs
\[
B_\tau=
\begin{pmatrix}
0&1&\tau\\
1&0&-\tau\\
\tau&-\tau&0
\end{pmatrix}
\]
and the \(45^\circ\) Jacobi rotation
\[
Q=
\begin{pmatrix}
1/\sqrt2&1/\sqrt2&0\\
-1/\sqrt2&1/\sqrt2&0\\
0&0&1
\end{pmatrix}.
\]
The transformed off-diagonal maximum is verified to be
\[
\sqrt2\,\tau
=
\frac{3\sqrt2}{4}>1.
\]

The checker also reconstructs the eigenvalue formula, applies the prescribed scalar shift, and verifies that the resulting SPD matrix has condition number \(2\).

Finite replay is corroborative only. The universal inequality follows from orthogonal preservation of the norm of every affected two-entry vector.

Unproved limits include full-sweep max-entry dynamics, block Jacobi variants, finite-precision pivot selection, and rounding-error effects.
