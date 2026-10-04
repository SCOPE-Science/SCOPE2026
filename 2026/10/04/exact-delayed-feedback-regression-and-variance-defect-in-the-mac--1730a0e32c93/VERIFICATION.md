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
The packaged `verify.py` uses only the Python standard library.

It verifies the abstract residual-variance algebra. Under
\[
\mathbb E[A]=\mathbb E[B],
\qquad
\mathbb E[AB]=\mathbb E[B^2],
\]
it checks exactly that
\[
\mathbb E[(A-B)^2]
=
\operatorname{Var}(A)-\operatorname{Var}(B).
\]

For the normalized classical parameters
\[
\beta=2,\qquad
\gamma=1,\qquad
\theta=1,\qquad
n=9.65,
\]
the checker evaluates
\[
f'(u)
=
\frac{1+(1-n)u^n}{(1+u^n)^2}
\]
and locates by deterministic bisection the three positive roots of
\[
|f'(u)|=\frac12.
\]

The computed roots are
\[
0.7356331449,
\qquad
0.8457944677,
\qquad
1.3248837609.
\]
Their residuals are below
\[
10^{-10}.
\]

The stored output in `verification_output.txt` is `VERIFY_OK`.

The invariant-measure regression, delayed/current marginal identity, equilibrium equality classification, and local Lipschitz obstruction are analytic proofs in `RESULT.md`; they are not inferred from finite trajectory simulation.
