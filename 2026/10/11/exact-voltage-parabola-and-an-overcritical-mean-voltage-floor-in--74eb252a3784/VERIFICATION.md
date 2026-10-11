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

It checks the conversion
\[
\gamma\mathbb E[v^2]=Im
\]
to
\[
\operatorname{Var}(v)=m(I/\gamma-m).
\]

It verifies the abstract orthogonal-regression formulas
\[
\operatorname{Var}(\sin\phi)
=
\gamma^2\operatorname{Var}(v)
+
\mathbb E[\dot v^2]
\]
and
\[
\operatorname{Cov}(v,\sin\phi)
=
-\gamma\operatorname{Var}(v).
\]

At
\[
I=\frac32,
\qquad
\gamma=\frac23,
\qquad
m=2,
\]
it verifies
\[
\frac54<m<\frac94,
\]
\[
\mathbb E[v^2]=\frac92,
\]
and
\[
\operatorname{Var}(v)=\frac12.
\]

The stored output in `verification_output.txt` is `VERIFY_OK`.

The conditional-expectation theorem, equilibrium rigidity, support strip, and strict overcritical floor are analytic arguments in `RESULT.md`; no finite trajectory computation is used.
