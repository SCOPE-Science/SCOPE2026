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
The packaged `verify.py` uses only the Python standard library and exact sparse-polynomial arithmetic.

For
\[
\dot x=A-(B+1)x+x^2y,\qquad
\dot y=Bx-x^2y,
\]
it verifies
\[
\dot x+\dot y=A-x
\]
and
\[
\dot y=x(B-xy).
\]

It also verifies, after clearing the denominator \(A\), that the positive equilibrium
\[
\left(A,\frac BA\right)
\]
annihilates both vector-field components.

Finally it checks the abstract variance identity
\[
\operatorname{Var}(s-x)
=
\operatorname{Var}(s)+\operatorname{Var}(x)
\]
when
\[
\operatorname{Cov}(x,s)=0.
\]

The stored output in `verification_output.txt` is `VERIFY_OK`.

The conditional-expectation, support-barrier, and equality-rigidity steps are analytic consequences detailed in `RESULT.md`; they are not inferred from finite numerical experiments.
