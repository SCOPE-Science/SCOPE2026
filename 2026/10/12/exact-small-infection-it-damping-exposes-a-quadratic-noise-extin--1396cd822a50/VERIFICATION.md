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

The theorem is analytic. Define
\[
Q(E,I)=\frac{\rho_1^2E^2(\sigma_{21}+\sigma_{22}E)^2+
\rho_2^2I^2(\sigma_{31}+\sigma_{32}I)^2}
{2(\rho_1E+\rho_2I)^2}.
\]
With
\[
a=\frac{\rho_1E}{\rho_1E+\rho_2I},
\qquad
b=1-a,
\]
one has
\[
Q(E,I)\ge\frac12\left(\sigma_{21}^2a^2+\sigma_{31}^2b^2\right).
\]
The latter quadratic has the exact minimum
\[
\delta_*=
\frac{\sigma_{21}^2\sigma_{31}^2}
{2(\sigma_{21}^2+\sigma_{31}^2)}.
\]
Choosing
\[
E_\varepsilon=\frac{a_*\varepsilon}{\rho_1},
\qquad
I_\varepsilon=\frac{b_*\varepsilon}{\rho_2}
\]
at the minimizing composition makes \(P=\varepsilon\) and sends the quadratic-noise additions to zero. This proves that \(\delta_*\) is the global infimum of the full nonlinear expression.

For Example 5.2,
\[
\sigma_{21}=\sigma_{31}=0.2,\qquad
\sigma_{22}=\sigma_{32}=1,
\]
so
\[
\delta_*=0.01.
\]
The published term is \(0.25\). The bundled standard-library checker evaluates \(Q\) along the minimizing ray and verifies convergence to \(0.01\); it also checks
\[
-0.0651+0.25-0.01=0.1749.
\]

The finding is deliberately limited to the invalid uniform damping step and the resulting loss of the published sufficient certificate. It does not infer actual persistence from certificate failure.
