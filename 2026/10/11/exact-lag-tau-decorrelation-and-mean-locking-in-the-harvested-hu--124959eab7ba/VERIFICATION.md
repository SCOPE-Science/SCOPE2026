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

It checks the pointwise algebra
\[
r\left(1-\frac{q}{K}\right)-\delta
=
\frac rK(K_\delta-q)
\]
and verifies the stationary covariance consequence
\[
\mathbb E[X_0X_{-\tau}]
-
\mathbb E[X_0]\mathbb E[X_{-\tau}]
=
0
\]
from the exact moment identities.

It also verifies the activity conversion
\[
\operatorname{Var}(X_0)
=
\frac{K^2}{r^2}
\mathbb E
\left[
\left(
\frac{\dot x(0)}{X_0}
\right)^2
\right]
\]
and the harvested equilibrium specialization
\[
K_\delta
=
\frac94
\]
for
\[
r=2,
\qquad
K=3,
\qquad
\delta=\frac12.
\]

The conditional-expectation quantifier, history-space equality classification, and periodic crossing theorem are analytic arguments in `RESULT.md`; no finite trajectory simulation is used.

The stored output in `verification_output.txt` is `VERIFY_OK`.
