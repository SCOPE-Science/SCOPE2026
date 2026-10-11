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

It verifies, as exact polynomial identities,
\[
L(y^2+z^2)
=
2\rho y-2y^2-2z^2,
\]
\[
xy-z=\dot z,
\]
\[
xz-(\rho-y)=-\dot y,
\]
and
\[
\zeta z+\alpha yz-\sigma x=\dot x.
\]

It verifies the algebraic equivalence between
\[
\mathbb E[y^2+z^2]=\rho m
\]
and
\[
\mathbb E[(y-\rho/2)^2+z^2]=\rho^2/4.
\]

It also verifies the abstract orthogonal-regression formulas used to derive
\[
\operatorname{Var}(xy)
=
\operatorname{Var}(z)+\mathbb E[\dot z^2]
\]
and
\[
\operatorname{Cov}(z,xy)
=
\operatorname{Var}(z).
\]

The stored output in `verification_output.txt` is `VERIFY_OK`.

The conditional-expectation identification and the zero-speed recurrence classification are analytic proofs in `RESULT.md`; they are not inferred from finite trajectory sampling.
