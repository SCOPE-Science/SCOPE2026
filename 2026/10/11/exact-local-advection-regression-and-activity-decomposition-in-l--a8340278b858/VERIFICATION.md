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

It verifies the Lorenz–96 cyclic energy cancellation
\[
\sum_i x_i
(x_{i+1}-x_{i-2})x_{i-1}
=
0
\]
for exact rational states.

It checks the stationary site-time energy algebra
\[
\mathbb E[X^2]
=
F\mathbb E[X]
\]
and the resulting classical state variance
\[
\operatorname{Var}(X)=m(F-m).
\]

It then checks the abstract conditional-residual consequences
\[
A=X-F+V,
\qquad
\mathbb E[V]=0,
\qquad
\operatorname{Cov}(X,V)=0,
\]
which imply
\[
\operatorname{Cov}(X,A)=\operatorname{Var}(X)
\]
and
\[
\operatorname{Var}(A)=\operatorname{Var}(X)+\mathbb E[V^2].
\]

At
\[
F=8
\]
it verifies the exact activity and correlation formulas for a rational stationary test moment set.

The stored output in `verification_output.txt` is `VERIFY_OK`.

The conditional-expectation quantifier and equilibrium-support equality classification are analytic arguments in `RESULT.md`; no finite trajectory computation is used.
