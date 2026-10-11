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

It verifies the pointwise thermostat relation
\[
x^2-1=\frac{\dot z}{\alpha}.
\]

It verifies that if
\[
\mathbb E[x^2]=1,
\]
then
\[
\operatorname{Var}(x^2)=\mathbb E[(x^2-1)^2].
\]

It also verifies the exact scaling
\[
\operatorname{Var}(x^2)
=
\alpha^{-2}\mathbb E[\dot z^2].
\]

The stored output in `verification_output.txt` is `VERIFY_OK`.

The conditional-expectation identities, strictness of the thermostat-speed defect, and the compact-invariant-set crossing theorem are analytic arguments in `RESULT.md`; they are not inferred from finite numerical simulation.
