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

It verifies the radial identity
\[
\dot R=2(z-\beta)R
\]
from the first two Langford equations.

It checks the abstract orthogonal-regression consequences of
\[
\mathbb E[z-\beta\mid R]=0
\]
and
\[
\mathbb E[\dot z\mid z]=0.
\]

It verifies
\[
\operatorname{Var}(z)
=
\frac14
\mathbb E
\left[
\left(
\frac{\dot R}{R}
\right)^2
\right]
\]
and
\[
\operatorname{Var}((1+\rho z)R)
=
\operatorname{Var}(G(z))
+
\mathbb E[\dot z^2].
\]

At the standard axisymmetric parameters
\[
(\alpha,\beta,\lambda,\omega,\rho)
=
\left(
1,\frac7{10},\frac35,\frac72,\frac14
\right),
\]
it verifies exactly
\[
R_*=\frac{3557}{3525}.
\]

The stored output in `verification_output.txt` is `VERIFY_OK`.

The conditional-expectation quantifiers, uniform angular marginal, equality classification, and two-sided height conclusion are analytic proofs in `RESULT.md`; no finite trajectory sampling is used.
