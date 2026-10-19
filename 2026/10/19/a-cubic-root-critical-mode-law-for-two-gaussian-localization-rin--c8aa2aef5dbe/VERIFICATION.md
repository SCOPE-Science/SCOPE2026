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
# Verification of two-ring asymptotic mode selection

The standalone `verify.py` evaluates the two incomplete-gamma integrals by 16-node Gauss–Legendre quadrature using logarithmically stabilized Poisson masses. It checks critical-mode convergence for area-coordinate centers \(a=2500,10000,40000\), the subcritical bounded shift at two center sizes, and supercritical global selection for two separation values at two center sizes. It also checks the critical algebraic coefficient, for 10 passing checks in total.

Scientific proof checks: the Gaussian radial operator has eigenvalues \(\lambda_n=\sum_{\pm}\int_{a\pm d\sqrt a-w/2}^{a\pm d\sqrt a+w/2}e^{-t}t^n/n!\,dt\); the uniform Stirling polynomial is \(Q(x,u)=u^3/3-xu^2/2+x^3/6-x/2\); the correction at the nonzero Gaussian-mixture stationary point has the sign of \(x(x^2-d^2-3)\), which is negative for the positive branch; at criticality the quartic coefficient and linear correction yield the scaled optimizer \(-2^{1/3}\).

Finite tests cannot prove the asymptotic mode theorem. The rigorous argument is the uniform asymptotic expansion, the Gaussian-tail localization of maximizers, and the unique global maximum of the limiting scaled quartic. Independent mathematical audit: not performed.
