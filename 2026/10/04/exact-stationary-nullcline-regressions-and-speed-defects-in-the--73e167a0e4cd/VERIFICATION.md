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

It checks the abstract conditional-regression moment algebra. Under
\[
\mathbb E[A]=\mathbb E[B],
\qquad
\mathbb E[AB]=\mathbb E[B^2],
\]
the checker verifies exactly that
\[
\mathbb E[(A-B)^2]
=
\operatorname{Var}(A)-\operatorname{Var}(B).
\]

It also checks the rate-tilt identity. If
\[
\dot W=q\Delta,
\]
then
\[
q\Delta^2=\frac{\dot W^2}{q}.
\]
After normalization by
\[
Z=\mathbb E[q],
\]
this is precisely the residual term in the tilted variance decomposition.

For
\[
q=\frac{\phi}{\tau},
\]
the checker verifies the factor conversion
\[
\frac{\dot W^2/q}{\mathbb E[q]}
=
\frac{\tau\dot W^2}{\phi^2\mathbb E[\tau^{-1}]}
\]
at the level of exact scalar factors.

The stored output in `verification_output.txt` is `VERIFY_OK`.

The conditional-expectation identities, equality classification, and nullcline crossing are analytic arguments in `RESULT.md`; they are not inferred from finite numerical experiments.
