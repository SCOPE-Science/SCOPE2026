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
The packaged `verify.py` uses only the Python standard library and exact rational sparse-polynomial arithmetic.

For
\[
\dot x=yz+a,\qquad
\dot y=x^2-y,\qquad
\dot z=1-4x,
\]
it verifies the polynomial vector field and the equilibrium
\[
\left(\frac14,\frac1{16},-16a\right).
\]

It verifies the Jacobian characteristic polynomial
\[
\lambda^3+\lambda^2+\left(8a+\frac14\right)\lambda+\frac14,
\]
and confirms that the Routh–Hurwitz determinant reduces to
\[
8a.
\]

It also verifies the exact algebra
\[
D
=
\mathbb E[(1-4x)^2]
=
16\operatorname{Var}(x)
\]
under
\[
\mathbb E[x]=\frac14,
\]
and
\[
\frac{-a}{(1+D)/16}
=
-\frac{16a}{1+D}.
\]

The stored output in `verification_output.txt` is `VERIFY_OK`.

The checker validates the algebraic certificates. The conditional expectation uses arbitrary one-variable antiderivative tests; positivity of \(y\), defect rigidity, and the strict mass conclusions use bounded-complete trajectories and invariant-support arguments.
