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

The counterexample uses
\[
H=H_1=\mathbb C,\qquad
C=C'=K=I,\qquad
\Lambda_1=\frac12I,\qquad
\Theta_1=0.
\]

The original controlled energy is
\[
\|\Lambda_1f\|^2
=
\frac14\|f\|^2,
\]
so
\[
A=B=\frac14.
\]

The operator under the source perturbation square root is positive and equals
\[
\Lambda_1^*\Lambda_1-\Theta_1^*\Theta_1
=
\frac14I.
\]
Therefore
\[
\left\|
\left(
\Lambda_1^*\Lambda_1-\Theta_1^*\Theta_1
\right)^{1/2}f
\right\|
=
\frac12\|f\|.
\]
For
\[
c_1=\frac12,\qquad
\lambda_1=\lambda_2=0,
\]
the hypothesis is an equality and
\[
\eta=\sum_i c_i^2=\frac14.
\]

The printed lower bound becomes
\[
\left(
\sqrt{\frac14}-\frac14
\right)^2
=
\frac1{16},
\]
while the actual perturbed energy is
\[
\|\Theta_1f\|^2=0.
\]
Thus the source conclusion is false.

For the replacement theorem, define
\[
X(f)^2=\sum_i\|A_i^{1/2}f\|^2,
\qquad
Y(f)^2=\sum_i\|B_i^{1/2}f\|^2.
\]
Minkowski's inequality gives the error estimate
\[
\left(
\sum_i
\|A_i^{1/2}f-B_i^{1/2}f\|^2
\right)^{1/2}
\le
\lambda_1X(f)+\lambda_2Y(f)+\sqrt{\eta}\,\|K^*f\|.
\]
The upper and lower triangle inequalities then yield
\[
(1-\lambda_2)Y(f)
\le
(1+\lambda_1)X(f)+\sqrt{\eta}\,\|K^*f\|
\]
and
\[
(1+\lambda_2)Y(f)
\ge
(1-\lambda_1)X(f)-\sqrt{\eta}\,\|K^*f\|.
\]
Substitution of the original frame bounds proves the stated replacement constants.

The publisher PDF was inspected at the theorem and proof by both extracted text and page image. The scalar verification is exact and uses no numerical approximation.
