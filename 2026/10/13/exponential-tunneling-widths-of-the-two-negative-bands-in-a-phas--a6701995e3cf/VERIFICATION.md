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

The proof starts from the exact negative-energy coefficients in the cited source. After multiplying the secular equation by \(4e^{-2\kappa\ell}/\sin(2\mu)\), direct algebra yields
\[
F(\kappa)+\frac{4Q\kappa(1+\kappa^2)}{\sin(2\mu)}(e^{-\kappa\ell}-e^{-3\kappa\ell})-2(1+\kappa^2)^2e^{-2\kappa\ell}+B(\kappa)e^{-4\kappa\ell}=0.
\]
This identity is the critical check: it exposes the order-\(e^{-\kappa\ell}\) fiber term. Factoring \(F\) gives the two positive simple roots, and differentiating there gives the coefficients \(+tQ\) and \(-uQ\) in the momentum shifts. The packaged numerical checker evaluates this exact normalized equation rather than the asymptotic truncation.

The error estimates use fixed \(0<\mu<\pi/2\). They are not uniform when either positive root approaches an endpoint regime. The numerical replay is not used to establish existence, uniqueness, or an infinite-domain statement.
