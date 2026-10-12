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
F(t)
=
\left(
1+\frac{\alpha}{2(1+\alpha)t}
\right)e^{-\alpha/t},
\]
the defining numerator is
\[
\int_0^t F(y)\,dy.
\]
The substitution
\[
u=\alpha/y
\]
gives
\[
\int_0^t \frac{e^{-\alpha/y}}{y}\,dy
=
E_1(\alpha/t)
=
-\operatorname{Ei}(-\alpha/t).
\]
Therefore the exponential-integral term in the source's Eq. (15) has the wrong sign.

The included checker independently evaluates the defining integral, the corrected special-function expression, and the source-sign expression for several parameter values. It also checks the asymptotic ratios
\[
\alpha m(t)/t^2\to1
\]
and
\[
\alpha m_{\mathrm{pub}}(t)/t^2\to-1.
\]

At
\[
(\alpha,t)=(1,0.1),
\]
the corrected and directly integrated mean inactivity time is
\[
0.0089507141557596967\ldots,
\]
while the source-sign expression is
\[
-0.0041297621213528864\ldots.
\]
