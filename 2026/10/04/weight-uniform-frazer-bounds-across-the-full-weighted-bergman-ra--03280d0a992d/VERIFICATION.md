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

The critical new estimate is
\[
\kappa_\alpha(\rho)
=
\int_\rho^1(1-u^2)^\alpha\,du
\ge
\frac{(1-\rho^2)^{\alpha+1}}{2(\alpha+1)}
\]
for
\[
-1<\alpha<\infty,
\qquad
0\le\rho<1.
\]

Define
\[
H_\alpha(\rho)
=
\kappa_\alpha(\rho)
-
\frac{(1-\rho^2)^{\alpha+1}}{2(\alpha+1)}.
\]
Then
\[
H_\alpha'(\rho)
=
-(1-\rho)(1-\rho^2)^\alpha<0
\]
and
\[
\lim_{\rho\uparrow1}H_\alpha(\rho)=0.
\]
Therefore
\[
H_\alpha(\rho)>0.
\]

The coefficient is sharp because
\[
\lim_{\rho\uparrow1}
\frac{\kappa_\alpha(\rho)}
{(1-\rho^2)^{\alpha+1}}
=
\frac1{2(\alpha+1)}.
\]

The source Fubini identity uses exactly this \(\kappa_\alpha\). Replacing its weaker lower estimate by the sharp one gives
\[
I
\ge
\frac1{2(\alpha+1)}
\sum_{j=0}^1
\int_{D_j}
|f(z)|^p(1-|z|^2)^{\alpha+1}\,|dz|.
\]

The source's unchanged upper estimate is
\[
I
\le
\frac{\pi}
{(\alpha+1)(\sin(\theta/2)+\cos(\theta/2))}
\int_{\mathbb D}(|h|+|g|)^p\,dA_\alpha.
\]
Combining them cancels \(\alpha+1\). The elementary inequality
\[
(|h|+|g|)^p
\le
2^{p/2}(|h|^2+|g|^2)^{p/2}
\]
and the verified weighted harmonic Riesz bound then yield
\[
\widetilde A_p(\theta)
=
\frac{2^{1+p/2}\pi}
{(\sin(\theta/2)+\cos(\theta/2))
(1-|\cos(\pi/p)|)^{p/2}}.
\]

The proof is analytic. No finite experiment, numerical extrapolation, or unproved endpoint interpolation is used.
