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

It checks the three pointwise residual identities
\[
yz-\mu x=\dot x,
\qquad
x(z-a)-\mu y=\dot y,
\qquad
xy-1=-\dot z.
\]

It checks the abstract variance and covariance decomposition for a residual with zero conditional mean.

For rational test parameters it checks the positive equilibrium root relation
\[
z_+(z_+-a)=\mu^2
\]
through its defining quadratic coefficients and verifies the equilibrium products
\[
x_\pm y_\pm=1.
\]

The stored output in `verification_output.txt` is `VERIFY_OK`.

The conditional-expectation identities, recurrence-based equality classification, and periodic threshold-crossing theorem are analytic arguments in `RESULT.md`; they are not inferred from finite numerical trajectories.
