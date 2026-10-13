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
The universal theorem is analytic. The standalone checker replays exact rational instances.

For
\[
A=
\frac1{169}
\begin{pmatrix}
244&180\\
180&601
\end{pmatrix},
\]
the eigenvalues are \(1\) and \(4\). The exact one-step factor in the displayed order is
\[
\frac{\det A}{a^2+b^2}
=
\frac{169}{136}>1.
\]
After swapping coordinates, the factor is
\[
\frac{676}{2329}<1.
\]

For
\[
A=
\frac12
\begin{pmatrix}
5&3\\
3&5
\end{pmatrix},
\]
both column norms are equal and both orders attain
\[
\frac8{17}
=
\frac{2\cdot4}{4^2+1}.
\]

The checker also verifies directly that the formula
\[
b^+
=
b\,\frac{\det A}{a^2+b^2}
\]
matches an exact QR construction for several rational matrices after clearing the square-root normalization.

Finite replay is corroborative only. The all-orientation extremal statements follow from the analytic proof.

Unproved limits include shifted QR, dimensions three and higher, nonsymmetric matrices, and global iteration complexity.
