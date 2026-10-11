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

It verifies the stationary-shell algebra
\[
\operatorname{Var}(x)=2c^2-m^2
\]
and its sharp bound, the equilibrium threshold
\[
x^2=2c^2,
\]
and the pointwise forcing residual
\[
(x^2+2y)-2c^2=-2\dot z.
\]

It also verifies the abstract zero-predictor variance identity used for
\[
\operatorname{Var}(x^2+2y)=4\mathbb E[\dot z^2].
\]

The stored output in `verification_output.txt` is `VERIFY_OK`.

The conditional-expectation, support-rigidity, and periodic-crossing arguments are analytic proofs in `RESULT.md`; they are not inferred from finite numerical sampling.
