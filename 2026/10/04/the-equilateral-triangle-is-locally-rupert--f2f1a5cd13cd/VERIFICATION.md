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

The normalized triangle is represented by three exact half-space inequalities. For the explicit rotation path, the projected linear map satisfies
\[
A_0=I
\]
and
\[
A'_0
=
\begin{pmatrix}
-\frac12-\frac{\sqrt3}{4}&-\frac12\\
0&-\frac12+\frac{\sqrt3}{4}
\end{pmatrix}.
\]

With
\[
q=(2\sqrt3-4,0),
\]
the exact identity
\[
A'_0q=(1/2,0)
\]
holds.

The embedded checker implements arithmetic in \(\mathbb Q(\sqrt3)\) directly. It enumerates the six tight vertex-side incidences and obtains five copies of
\[
-\frac14+\frac{\sqrt3}{8}<0
\]
and one copy of
\[
-\frac14-\frac{5\sqrt3}{8}<0.
\]
This is the critical certificate used by the proof.

The checker also reconstructs the full three-dimensional matrices
\[
Q_t
=
R_z(t/4-5\pi/12)
R_x(\arccos(1-t))
R_z(5\pi/12)
\]
at several positive parameter values. It verifies orthogonality, determinant \(1\), and strict satisfaction of every projected triangle side inequality after applying the fixed translation.

The replay output is:

`VERIFY_OK equilateral triangle local Rupert passage`

Finite parameter checks are supplementary. The theorem for all sufficiently small positive parameters follows from the exact first-order certificate together with continuity.
