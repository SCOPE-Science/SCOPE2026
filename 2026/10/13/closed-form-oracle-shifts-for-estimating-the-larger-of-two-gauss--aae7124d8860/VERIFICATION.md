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
# Verification

Let
\[
h(\Delta)
=
\sqrt2\,\phi\!\left(\frac{\Delta}{\sqrt2}\right)
-
\Delta\,\Phi\!\left(-\frac{\Delta}{\sqrt2}\right).
\]
The analytic proof uses the positive-part normal identity
\[
\mathbb E[Y_+]
=
s\phi(\mu/s)+\mu\Phi(\mu/s),
\qquad
Y\sim N(\mu,s^2),
\]
with
\[
\mu=-\Delta,
\qquad
s=\sqrt2.
\]
This gives
\[
E[X_{(2)}-\theta_{(2)}]=\sigma h(\Delta).
\]

The exact quadratic risk identity is
\[
R_\Delta(b)
=
R_\Delta(0)-2b\sigma h(\Delta)+b^2,
\]
hence
\[
R_\Delta(b)-R_\Delta(\sigma h(\Delta))
=
(b-\sigma h(\Delta))^2.
\]

Differentiation gives
\[
h'(\Delta)
=
-\Phi\!\left(-\frac{\Delta}{\sqrt2}\right)<0,
\]
so the boundary-shift versus usual-estimator risk difference has exactly one zero.

The standalone `verify.py` numerically integrates the positive-part normal expectation at deterministic separations, checks the derivative identity by finite differences, solves the crossover equation by bisection, and checks the risk-difference sign on both sides.

Expected successful terminal line:
`VERIFY_OK delta_star=0.699454801905 h0=0.564189583548`.

The numerical root is not used to prove uniqueness; monotonicity proves uniqueness analytically.
