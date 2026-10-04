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
The packaged `verify.py` uses exact rational arithmetic and sparse one-variable polynomial bookkeeping.

It verifies the nonlinear cancellation in
\[
L\left(\frac12(x^2+y^2)\right)
=(a+c)xy-a x^2-y^2.
\]

Writing \(a=s^2\) and \(c=2s-s^2\), it verifies the critical tangency identity
\[
\left.\frac{d}{dt}(y-sx)\right|_{y=sx}
=(1+s^2)x\bigl(s(1-s)-z\bigr).
\]

It also checks that the nonzero-equilibrium height equation
\[
z^2-(c-a)z-a(c-1)=0
\]
has discriminant
\[
(a+c)^2-4a,
\]
and replays the rational threshold instance
\[
a=\frac14,\qquad b=2,\qquad c=\frac34,
\]
with equilibria
\[
(\pm1,\pm\tfrac12,\tfrac14).
\]

The stored checker output in `verification_output.txt` is `VERIFY_OK`.

The checker verifies the critical algebra. The invariant-measure conditional law uses arbitrary continuous test functions through antiderivatives on the compact \(z\)-range; global convergence and measure-support rigidity are analytic deductions stated in `RESULT.md`.
