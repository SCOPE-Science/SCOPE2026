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

Uniform convexity is equivalent to
\[
p_f(\mathbb D)
\subset
\mathcal P,
\qquad
p_f(z)
=
1+\frac{zf''(z)}{f'(z)},
\]
where
\[
\mathcal P
=
\left\{
u+iv:
u>\frac{1+v^2}{2}
\right\}.
\]

For the exponentially convex class, the whole-class problem is therefore the exact image inclusion
\[
e^{\lambda\mathbb D}
\subset
\mathcal P.
\]

The principal logarithm reduces this to
\[
\lambda
\le
\operatorname{dist}
\left(
0,\partial(\Log\mathcal P)
\right).
\]
Parameterizing the parabolic boundary by
\[
w_y
=
\frac{1+y^2}{2}+iy
\]
gives
\[
\Log w_y
=
a(y)+ib(y),
\]
with
\[
a(y)
=
\frac12
\log\!\left(
\frac{y^4+6y^2+1}{4}
\right)
\]
and
\[
b(y)
=
\arctan\!\left(
\frac{2y}{1+y^2}
\right).
\]

The derivative of the squared distance is
\[
\frac{d}{dy}
\left(
a(y)^2+b(y)^2
\right)
=
\frac{4N(y)}{y^4+6y^2+1}.
\]
The proof in RESULT.md establishes analytically that \(N\) has exactly one positive zero \(y_*\), so the numerical solver is only evaluating an already unique exact minimizer.

Replaying the packaged bisection checker gives
\[
y_*
=
0.2241944779359010240194013275\ldots
\]
and
\[
\lambda_{\mathrm{uc}}
=
0.6905440336407464277786112389\ldots.
\]

For every
\[
\lambda>\lambda_{\mathrm{uc}},
\]
the source extremal has an interior point
\[
z_*=
\frac{\Log w_*}{\lambda}
\]
with
\[
|z_*|<1
\]
and curvature value
\[
e^{\lambda z_*}=w_*\in\partial\mathcal P.
\]
Thus failure above the threshold is exact, not numerical.
