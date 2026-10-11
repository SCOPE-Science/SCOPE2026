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

It checks the exact cancellation
\[
\dot u+\dot v=a+b-u
\]
and therefore
\[
u-(a+b)=-\dot S.
\]

It checks the covariance consequences of
\[
\operatorname{Cov}(S,u)=0:
\]
\[
\operatorname{Cov}(u,v)=-\operatorname{Var}(u)
\]
and
\[
\operatorname{Var}(v)=\operatorname{Var}(S)+\operatorname{Var}(u).
\]

It also checks the unique positive equilibrium
\[
\left(
a+b,\frac{b}{(a+b)^2}
\right)
\]
by exact substitution at rational parameters.

The stored output in `verification_output.txt` is `VERIFY_OK`.

The conditional-expectation laws and the periodic crossing theorem are analytic consequences of invariance and continuity; they are not inferred from finite trajectory sampling.
