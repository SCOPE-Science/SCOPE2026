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
The proof is analytic. The bundled checker replays the exact algebra and the source-parameter witness.

With
\[
q=\frac{d^*}{b},
\qquad
x=qP,
\qquad
y=M,
\]
the linear medusa transfer cancels because
\[
qb=d^*.
\]
The weighted drift becomes
\[
\left(a-d+\frac{bc}{d^*}\right)x
-
\frac{bb_1}{d^*}x^2
-
b_2y^2.
\]

For the source values and the test noises
\[
\sigma_1=0.1,
\qquad
\sigma_2=1,
\]
the checker verifies
\[
a-d-\frac{\sigma_1^2}{2}
=
\frac{181}{1250}
=
0.1448,
\]
\[
\frac{a-d-\sigma_1^2/2}{b_1}
=
14480,
\]
whereas
\[
c-d^*-\frac{\sigma_2^2}{2}
=
-\frac{813}{2000}
=
-0.4065.
\]
It also verifies the weighted lower mean
\[
\frac{d^*}{b}\,14480
=
\frac{14842}{425}
\approx34.9223529412.
\]

No simulation or finite sample is used to establish the theorem. The stochastic limits follow from the explicit scalar logistic solution, Brownian strong law, and a bounded-quadratic-variation martingale law.
