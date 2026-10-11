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

The complete proof reduces to the known exposed-arc dangling insertion and the two analytic functions
\[
f_L(t)=2\rho\sin(t/2),
\qquad
f_\theta(t)=2\arcsin(\rho\sin(t/2)),
\]
where
\[
0<s\le1,
\qquad\rho=\sqrt{1-s^2/4}<1,
\qquad0<t<\varphi<\pi.
\]
Direct differentiation gives
\[
f_L''(t)=-\frac\rho2\sin(t/2)
\]
and
\[
f_\theta''(t)
=-\frac{\rho(1-\rho^2)\sin(t/2)}
{2(1-\rho^2\sin^2(t/2))^{3/2}}.
\]
These formulas establish strict concavity without numerical approximation, so equiangular partitions uniquely maximize the sum of the subarc contributions.

The exact expansions are
\[
f_L(t)=\rho t-\frac{\rho t^3}{24}+O_s(t^5),
\]
\[
f_\theta(t)=\rho t-\frac{\rho(1-\rho^2)t^3}{24}+O_s(t^5).
\]
Substitution of \(t=\varphi/r\) followed by multiplication by \(r\) yields both sharp \(r^{-2}\) convergence coefficients with \(O_{s,\varphi}(r^{-4})\) remainder.

The standalone symbolic checker verifies both second-derivative identities and both Taylor coefficients, and evaluates a regular-tetrahedron exposed edge as a normalization case. This finite example is not a proof of universal strictness. Universal strictness follows from the analytic negative second derivatives, and global finite nonattainment follows from the primary dangling-incidence theorem applied to an arbitrary exposed pair. No proof of the global supremum's value is claimed.
