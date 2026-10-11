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

For exact rational parameters it checks the coexistence coordinates
\[
x_*=\frac{\gamma}{\delta},
\qquad
y_*=\frac{\alpha}{\beta},
\]
and the pointwise identities
\[
\frac{\dot x}{x}=-\beta(y-y_*),
\qquad
\frac{\dot y}{y}=\delta(x-x_*).
\]

It checks that the conditional-mean consequences
\[
\mathbb E[x]=x_*,
\qquad
\mathbb E[y]=y_*,
\qquad
\mathbb E[xy]=x_*y_*
\]
give exactly
\[
\operatorname{Cov}(x,y)=0.
\]

It also checks the two variance–per-capita-speed conversions and exact vanishing of both vector-field components at the coexistence equilibrium.

The stored output in `verification_output.txt` is `VERIFY_OK`.

The conditional-expectation theorem, invariant-support rigidity, and periodic crossing conclusion are analytic arguments in `RESULT.md`; they are not inferred from finite orbit sampling.
