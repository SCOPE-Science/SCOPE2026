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

It verifies the three pointwise residual identities
\[
y+x=-\frac{\dot x}{a},
\]
\[
xz+\frac{y}{k}=-\frac{\dot y}{k},
\]
and
\[
xy+\frac{d}{g}=\frac{\dot z}{g}.
\]

It verifies the abstract orthogonal-regression formulas
\[
\operatorname{Var}(B+R)
=
\operatorname{Var}(B)+\mathbb E[R^2]
\]
and
\[
\operatorname{Cov}(B,B+R)=\operatorname{Var}(B)
\]
when \(R\) has zero mean and is orthogonal to \(B\), with the signs and coefficient scalings used in the result.

At
\[
a=k=g=10,
\qquad
d=4.272,
\]
the checker verifies exactly that
\[
d/g=0.4272
\]
using rational arithmetic and verifies both equilibrium points by direct substitution.

The stored output in `verification_output.txt` is `VERIFY_OK`.

The conditional-expectation and equality-rigidity arguments are analytic proofs in `RESULT.md`; they are not inferred from finite trajectory sampling.
