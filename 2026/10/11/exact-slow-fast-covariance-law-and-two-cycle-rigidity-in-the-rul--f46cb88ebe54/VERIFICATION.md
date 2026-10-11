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

It checks the exact stationary second-moment algebra for
\[
y'=y-\mu(x-m),
\qquad
m=\sigma-1,
\]
and verifies
\[
\operatorname{Cov}(x,y)
=
\frac{\mu}{2}\operatorname{Var}(x).
\]

It verifies the covariance-determinant rearrangement
\[
4\det\Sigma
=
4\operatorname{Var}(x)\operatorname{Var}(y)
-
\mu^2\operatorname{Var}(x)^2.
\]

It also checks
\[
\operatorname{Var}(\Delta y)=\mu^2\operatorname{Var}(x),
\qquad
\operatorname{Cov}(y,\Delta y)
=
-\frac12\operatorname{Var}(\Delta y),
\]
and verifies algebraically that the equality-line relation at consecutive iterates implies
\[
x'-m=-(x-m).
\]

For the exact rational representation of the source example
\[
\mu=\frac1{1000},
\qquad
\sigma=\frac{161}{500},
\]
the checker verifies
\[
m=-\frac{339}{500}=-0.678
\]
and
\[
\frac{\mu}{2}=\frac1{2000}=0.0005.
\]

The stored output in `verification_output.txt` is `VERIFY_OK`.

The invariant-measure argument and the period-two equality classification are analytic; they do not rely on finite orbit sampling.
