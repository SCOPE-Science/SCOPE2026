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
The bundled checker uses exact symbolic arithmetic.

For
\[
b=\frac15,\qquad
d=\frac1{20},\qquad
r=\frac12,\qquad
s=\frac{1091}{1000},
\]
it verifies the invariant-ray relation and obtains
\[
\kappa=\frac9{1100},
\qquad
\lambda_\perp=\frac{18}{275}.
\]

It reconstructs
\[
E_1=\left(\frac9{1100},\frac9{110}\right)
\]
and the exact Jacobian
\[
J(E_1)=
\begin{pmatrix}
\frac{248}{3025}&-\frac{1091}{121000}\\
\frac{20}{121}&-\frac{299}{12100}
\end{pmatrix},
\]
whose eigenvalues are
\[
-\frac9{1100},\qquad \frac{18}{275}.
\]

It also verifies the source's two-positive-equilibria inequalities and reconstructs
\[
E_2=\left(\frac{7371}{28100},\frac{1539}{2810}\right).
\]

The general invariant-ray and stable-manifold claims are analytic and do not rely on finite simulation.
