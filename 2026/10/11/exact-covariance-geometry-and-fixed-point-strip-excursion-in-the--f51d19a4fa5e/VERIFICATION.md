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

It checks the stationary algebra implied by
\[
X=x+Y,
\]
including the deductions
\[
\mathbb E[xY]=-\frac12\mathbb E[y^2]
\]
and
\[
\mathbb E[xy]=\frac12\mathbb E[y^2].
\]

It checks the conversion of
\[
k\,\mathbb E[x(x-1)]
+
\frac{\mu}{2}\mathbb E[y^2]
=
0
\]
to the centered fixed-point-strip identity
\[
\mathbb E[(x-1/2)^2]
=
\frac14-\frac{\mu}{2k}\operatorname{Var}(y).
\]

It also verifies the covariance-determinant inequality algebra and the equality reflection
\[
(X-m,Y)=(-(x-m),-y)
\]
from
\[
x-m=\frac12y,
\qquad
X-m=\frac12Y,
\qquad
X=x+Y.
\]

The stored output in `verification_output.txt` is `VERIFY_OK`.

The invariant-measure quantifiers, zero-variance fixed-point classification, and ergodic period-two conclusion are analytic arguments in `RESULT.md`; they are not inferred from finite orbit sampling.
