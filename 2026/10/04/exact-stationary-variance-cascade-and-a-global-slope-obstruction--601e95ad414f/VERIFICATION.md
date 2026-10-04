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
The packaged `verify.py` uses only the Python standard library and exact arithmetic.

It verifies the abstract residual-variance identity
\[
\mathbb E[(A-B)^2]
=
\operatorname{Var}(A)-\operatorname{Var}(B)
\]
under
\[
\mathbb E[AB]=\mathbb E[B^2],
\qquad
\mathbb E[A]=\mathbb E[B].
\]

For Hill exponent
\[
h=2,
\]
it verifies the exact critical point
\[
s^2=\frac13
\]
for
\[
|R'(s)|=\frac{2\alpha s}{(1+s^2)^2}
\]
and the exact maximum
\[
L=\frac{9\alpha}{8\sqrt3}.
\]
It also verifies the equivalent threshold
\[
L\le1
\iff
\alpha\le\frac{8\sqrt3}{9}.
\]

The stored output in `verification_output.txt` is `VERIFY_OK`.

The conditional-expectation identities, equality rigidity, general-\(h\) slope maximization, and cyclic variance-product argument are analytic proofs given in `RESULT.md`; they are not inferred from numerical experiments.
