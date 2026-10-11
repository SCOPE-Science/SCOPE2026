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
The packaged `verify.py` uses only the Python standard library and exact rational arithmetic.

It verifies the pointwise identities
\[
xy-z=\dot z,
\]
\[
y(h-z)-\nu_1x=\dot x,
\]
and
\[
x(h+z)-\nu_2y=\dot y.
\]

It verifies
\[
\frac{d}{dt}\frac{x^2+y^2}{2}
=
2hxy-\nu_1x^2-\nu_2y^2
\]
and
\[
\frac{d}{dt}\frac{x^2-y^2}{2}
=
-\nu_1x^2+\nu_2y^2-2xyz.
\]

The checker solves the stationary quadratic balances exactly to obtain
\[
\nu_1\mathbb E[x^2]=hm-q,
\qquad
\nu_2\mathbb E[y^2]=hm+q,
\]
then verifies
\[
\operatorname{Var}(z)+\nu_1\mathbb E[x^2]=m(h-m).
\]

It also checks the abstract orthogonal-regression variance identity used for each coordinate-speed defect.

At
\[
(\nu_1,\nu_2,h)
=
\left(1,4,\frac{123}{25}\right),
\]
it verifies the specialized pump-height parabola exactly.

The stored output in `verification_output.txt` is `VERIFY_OK`.

The invariant-measure quantifiers, zero-defect origin classification, strict mean-height interval, and positive slab-mass theorem are analytic arguments in `RESULT.md`; no finite trajectory computation is used as proof.
