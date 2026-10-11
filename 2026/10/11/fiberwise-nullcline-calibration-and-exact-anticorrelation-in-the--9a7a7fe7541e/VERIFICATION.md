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

It verifies directly that
\[
\dot S=\dot x+\dot y=a-x
\]
for the Brusselator vector field.

It verifies the cleared-denominator nullcline residual
\[
x^2
\left(
y-\frac{(b+1)x-a}{x^2}
\right)
=
a-(b+1)x+x^2y.
\]

It also checks the covariance algebra. Under
\[
\operatorname{Cov}(x,S)=0
\]
and
\[
y=S-x,
\]
the checker verifies
\[
\operatorname{Cov}(x,y)=-\operatorname{Var}(x)
\]
and
\[
\operatorname{Var}(y)
=
\operatorname{Var}(S)+\operatorname{Var}(x).
\]

For
\[
a=1,\qquad b=3,
\]
it verifies exactly that
\[
\frac{a}{b+1}=\frac14.
\]

The stored output in `verification_output.txt` is `VERIFY_OK`.

The conditional-expectation and equality-rigidity steps are analytic consequences of invariant-measure testing and are not inferred from finite simulation.
