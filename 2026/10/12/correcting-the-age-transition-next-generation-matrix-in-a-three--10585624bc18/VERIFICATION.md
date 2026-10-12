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
The general correction is analytic.

For a valid new-infection decomposition, the youth-adult next-generation block is
\[
B=
\begin{pmatrix}
\frac{\beta_{11}}{\eta_1}+\frac{\beta_{21}\alpha_y}{\eta_1\eta_3}
&
\frac{\beta_{21}}{\eta_3}
\\[4pt]
\frac{\beta_{12}}{\eta_1}+\frac{\beta_{22}\alpha_y}{\eta_1\eta_3}
&
\frac{\beta_{22}}{\eta_3}
\end{pmatrix}.
\]
Direct algebra gives
\[
\det(I-B)
=
\frac{
(\eta_1-\beta_{11})(\eta_3-\beta_{22})
-\beta_{21}(\beta_{12}+\alpha_y)
}{
\eta_1\eta_3
}.
\]
The numerator is the determinant of the actual youth-adult infected Jacobian at the disease-free equilibrium.

The bundled checker uses exact rational arithmetic for the explicit positive-parameter witness. It verifies
\[
\det(I-B)
=
\frac{396801}{1000000}>0,
\]
and
\[
\det(I-B_{\mathrm{printed}})
=
-\frac{203199}{1000000}<0.
\]
It also verifies that the direct youth-adult Jacobian has negative trace and positive determinant, while the elder infection eigenvalue is negative.

No trajectory simulation is used to establish the threshold reversal.
