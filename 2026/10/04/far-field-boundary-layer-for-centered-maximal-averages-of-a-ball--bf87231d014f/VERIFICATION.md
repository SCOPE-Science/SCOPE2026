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

The verification is analytic.

For the averaging radius \(\rho=R+1-\delta\), axial coordinates based at the farthest point of the unit ball give the exact cross-section conditions
\[
|z|^2\le2u-u^2
\]
for the unit ball and
\[
|z|^2>2(R+1)(u-\delta)-u^2+\delta^2
\]
for the part missed by the averaging ball. Their boundaries meet at
\[
u_*=\frac{2(R+1)\delta-\delta^2}{2R}.
\]
This shows that the transition strip has width \(O(\delta/R)\).

The fully missed cap has the asymptotic
\[
\omega_{n-1}\int_0^\delta(2u-u^2)^{(n-1)/2}\,du
=
\frac{2^{(n+1)/2}\omega_{n-1}}{n+1}
\delta^{(n+1)/2}(1+O(\delta)).
\]
Combining this with the expansion of \((R+1-\delta)^{-n}\) gives the limiting scaled objective
\[
G_n(t)=nt-a_nt^{(n+1)/2},
\]
whose unique positive maximizer yields the constants in the finding.

A direct numerical quadrature/maximization check was performed in dimensions \(2,3,4,5\) for several large radii. It was used only to detect algebraic mistakes; it is not evidence for the asymptotic theorem.

The principal remaining verification risk is literature access, not the mathematical derivation: the full motivating preprint could not be retrieved during this review, and that limitation is disclosed in the originality assessment.
