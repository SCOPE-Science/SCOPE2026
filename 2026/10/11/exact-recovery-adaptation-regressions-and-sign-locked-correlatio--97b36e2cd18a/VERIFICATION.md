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
(y-z)-(a x^3-bx^2-I)=\dot x,
\]
\[
(c-dx^2)-y=\dot y,
\]
and
\[
s(x-x_R)-z=\frac{\dot z}{r}.
\]

It checks the abstract conditional-regression identity
\[
\operatorname{Var}(A)-\operatorname{Var}(B)
=
\mathbb E[(A-B)^2]
\]
from
\[
\mathbb E[A]=\mathbb E[B],
\qquad
\mathbb E[AB]=\mathbb E[B^2].
\]

It also verifies the recovery covariance reduction
\[
\operatorname{Cov}(x^2,y)
=
-\frac{\operatorname{Var}(y)}d
\]
from the first two moments implied by
\[
\mathbb E[x^2\mid y]=\frac{c-y}{d},
\]
and the adaptation covariance reduction
\[
\operatorname{Cov}(x,z)
=
\frac{\operatorname{Var}(z)}s
\]
from
\[
\mathbb E[x\mid z]=x_R+\frac zs.
\]

The stored output in `verification_output.txt` is `VERIFY_OK`.

The conditional-expectation, support, and equilibrium-rigidity arguments are analytic proofs in `RESULT.md`; they are not inferred from finite numerical simulations.
