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

It verifies the pointwise identities
\[
\dot z=x^2-\alpha z
\]
and
\[
\frac{d}{dt}(xy)=y^2+x^2-\lambda xy-x^2z.
\]

It then replays the exact stationary substitutions
\[
\mathbb E[xy]=0,
\qquad
\mathbb E[x^2]=\alpha\mathbb E[z],
\qquad
\mathbb E[x^2z]=\alpha\mathbb E[z^2]
\]
to obtain
\[
\mathbb E[y^2]=\alpha\mathbb E[z(z-1)].
\]

It also checks the abstract projection algebra behind
\[
\operatorname{Var}(x^2)-\alpha^2\operatorname{Var}(z)=\mathbb E[\dot z^2]
\]
and
\[
\operatorname{Cov}(x^2,z)=\alpha\operatorname{Var}(z).
\]

The stored output in `verification_output.txt` is `VERIFY_OK`.

The conditional-expectation theorem, support statement, equality classification, outer-height barrier, and bounded-complete memory formula are proved analytically in `RESULT.md`; they are not inferred from finite experiments.
