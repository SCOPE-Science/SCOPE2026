---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Direct substitution into the first rank-one update gives x2=[((rho+gamma)I-A)b]/(gamma rho), with rho the Rayleigh quotient of b. If gamma is at least L-mu then rho+gamma is at least L, so the shifted Stieltjes matrix is entrywise nonnegative. Conversely for A=diag(mu,L), b=(1,epsilon), the high-curvature coordinate is negative exactly when epsilon squared is below (L-mu-gamma)/gamma. Fresh arithmetic reproduces the package witness rho=8/5 and x2=(13/16,-1/16).

## originality

PASS

Classical Broyden theory covers the rank-one update, residual projection structure and finite termination on linear systems. The fresh Resultary query and the inspected O'Leary full text do not give an entrywise second-iterate positivity theorem for Stieltjes matrices, the universal spectral-width threshold, or the two-dimensional sharpness family.

## value

PASS

Scalar Jacobian initialization is a natural low-information quasi-Newton choice, while Stieltjes systems encode a meaningful positivity order. The exact robust threshold and minimal obstruction provide a concrete safety rule and a sharp boundary not supplied by ordinary convergence theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
