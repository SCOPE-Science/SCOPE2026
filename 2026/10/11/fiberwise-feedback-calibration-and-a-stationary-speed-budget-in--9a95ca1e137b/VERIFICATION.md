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

It checks the variance-defect algebra under a zero-conditional-mean residual:
\[
\operatorname{Var}(bX+R)
=
b^2\operatorname{Var}(X)
+
\mathbb E[R^2]
\]
when
\[
\mathbb E[R]=0,
\qquad
\operatorname{Cov}(X,R)=0.
\]

It checks the directed covariance identity
\[
\operatorname{Cov}(X,bX+R)
=
b\operatorname{Var}(X).
\]

It checks that the three cyclic inequalities
\[
B\ge b^2A+U,
\quad
C\ge b^2B+V,
\quad
A\ge b^2C+W
\]
sum to
\[
U+V+W\le(1-b^2)(A+B+C)
\]
and compose to the directional coefficient pattern
\[
b^4U+b^2V+W\le(1-b^6)A.
\]

It also checks the exponential-kernel normalization used in the bounded-memory representation at exact rational damping values.

The stored output in `verification_output.txt` is `VERIFY_OK`.

The conditional-expectation identification, one-Lipschitz variance contraction, and bounded-complete-trajectory limit are analytic arguments in `RESULT.md`; they are not inferred from finite numerical sampling.
