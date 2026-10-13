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
For
\[
x=2\pi\alpha\beta,
\]
the derivative sign is the sign of
\[
B(\theta)
=
1-\alpha
\left(
1+\beta\theta+
\frac{2\pi\beta e^{-x}}{1-e^{-x}}
\right),
\]
and
\[
B'(\theta)=-\alpha\beta<0.
\]

The stationary point is
\[
\theta_0
=
\frac{1-\alpha}{\alpha\beta}
-
\frac{2\pi}{e^x-1}.
\]
For \(\alpha\ge1\), this is negative.

For \(0<\alpha<1\), \(\theta_0>0\) is equivalent to
\[
(1-\alpha)(e^x-1)>x.
\]
The unique positive equality root is
\[
x_\alpha
=
-W_{-1}
\left(
-(1-\alpha)e^{-(1-\alpha)}
\right)
-(1-\alpha),
\]
so
\[
\beta_c(\alpha)=x_\alpha/(2\pi\alpha).
\]

The bundled checker verifies the threshold equation, the normalization of the published density, numerical agreement of the analytic derivative with differentiation, and the sign regimes below and above \(\beta_c\).
