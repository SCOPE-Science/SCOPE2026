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

The analytic verification starts from the exact one-particle identity
\[
M\bar C=\left(\sum_i|\psi_i|\right)^2-1.
\]
For the normalized continuum exponential \(\psi(x)=\xi^{-1/2}e^{-|x|/\xi}\), direct integration gives a full-profile mass \(4\xi-1\), while truncating at one localization length on each side gives \(4(1-e^{-1})^2\xi-1\).

For the finite geometric envelope \(\psi_n=Z_L^{-1/2}r^{|n|}\), the verifier reconstructs the sum of every pairwise concurrence and compares it with \(S_L^2/Z_L-1\) over multiple chain sizes and decay ratios. It then checks convergence to
\[
\frac{2r(r^2+r+2)}{(1-r)(1+r^2)}
\]
and checks the displayed large-\(\xi\) expansion numerically at stable scales.

The recorded execution returns `VERIFY_OK`. These finite checks do not establish the infinite statement by enumeration; the infinite formula and asymptotic are proved analytically in `RESULT.md`.

Unproved beyond the stated scope: no claim is made that arbitrary Anderson eigenstates are exact exponentials, that finite-boundary corrections are negligible for every parameter regime, or that every operational localization-length estimator obeys the same exact relation.
