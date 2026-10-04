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

The verification replays the source parameters
\[
q=\frac13-\frac16i,
\qquad
r=\frac{399}{400},
\qquad
\alpha=\frac89+\frac49i,
\qquad
w=1-q^3.
\]

At
\[
z_0=\frac1r,
\]
the source gives
\[
F'(z_0)=1-\alpha r^2,
\qquad
G'(z_0)=q^2,
\]
\[
z_0F''(z_0)=2\alpha r^2,
\qquad
z_0G''(z_0)=\frac{2w}{q}.
\]

For
\[
H_\lambda=\lambda F+(1-\lambda)G,
\]
exact expansion of
\[
\operatorname{Re}
\left[
\left(
H_\lambda'(z_0)+z_0H_\lambda''(z_0)
\right)
\overline{H_\lambda'(z_0)}
\right]
\]
gives
\[
\frac{
15391097599\lambda^2
-
17772056000\lambda
+
2956000000
}{
25920000000
}.
\]
The squared derivative modulus is
\[
\frac{
2868678401\lambda^2
+
2046392000\lambda
+
500000000
}{
25920000000
}.
\]

The numerator discriminant is
\[
133861636456560000000
=
36000^2\cdot103288299735.
\]
This yields the exact roots \(\lambda_-\) and \(\lambda_+\) stated in the finding.

The included checker independently reconstructs these coefficients from rational complex arithmetic and verifies the specialization
\[
\lambda=\frac35
\]
against the source's exact rational curvature value.

No finite sampling is used to certify the sign interval.
