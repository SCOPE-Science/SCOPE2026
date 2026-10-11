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

It verifies the cancellation identity
\[
\frac12\frac{d}{dt}(x^2+s w^2)
=
\sigma xy-\sigma x^2-\sigma s w^2.
\]

It verifies the elimination of the mixed third moment between
\[
\frac12\frac{d}{dt}y^2
=
rxy-xyz-y^2
\]
and
\[
\frac12\frac{d}{dt}z^2
=
xyz-bz^2,
\]
together with the factorization
\[
brm-bm^2=bm(r-m).
\]

It verifies the abstract orthogonal-regression identities
\[
\operatorname{Var}(bz+R)
=
b^2\operatorname{Var}(z)+\mathbb E[R^2]
\]
and
\[
\operatorname{Cov}(z,bz+R)
=
b\operatorname{Var}(z)
\]
when \(R\) has zero mean and is orthogonal to functions of \(z\).

At
\[
\sigma=1,\qquad
b=\frac7{10},\qquad
r=26,\qquad
s=\frac32,
\]
the checker verifies the exact displayed coefficients.

The stored output in `verification_output.txt` is `VERIFY_OK`.

The conditional-expectation identification and endpoint arguments are analytic proofs in `RESULT.md`; they are not inferred from finite trajectory sampling.
