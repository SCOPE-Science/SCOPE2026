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

It checks the pointwise residual identities
\[
Q-1=-\dot x,
\qquad
Q-y=\frac{\dot y}{\alpha},
\]
for
\[
Q=xy^\gamma.
\]

It verifies the abstract covariance consequences
\[
\operatorname{Cov}(x,Q)=0,
\qquad
\operatorname{Cov}(y,Q)=\operatorname{Var}(y),
\]
and the exact activity decomposition
\[
\mathbb E[\dot x^2]
=
\operatorname{Var}(y)
+
\frac1{\alpha^2}\mathbb E[\dot y^2].
\]

It also checks the equilibrium equations and the strict-convexity exponents for integer
\[
\gamma>1.
\]

The stored output in `verification_output.txt` is `VERIFY_OK`.

The conditional-expectation quantifiers, strict Jensen cases, complete-trajectory equality classification, and periodic crossing theorem are analytic arguments in `RESULT.md`; no finite orbit simulation is used.
