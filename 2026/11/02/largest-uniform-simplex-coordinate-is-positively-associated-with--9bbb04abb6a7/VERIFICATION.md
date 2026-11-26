---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The invertible linear map y_j=j(x_j-x_{j+1}) sends the constant-density ordered chamber to the uniform simplex. In the first m-1 coordinates the divergence of the coefficient field y_i(delta_{iℓ}-y_ℓ) is 1-m y_i; its flux vanishes on coordinate faces and on y_m=0 (the sum of its components is y_i y_m). Integration by parts and pairing i,j therefore give the claimed covariance identity with factor 1/m. The two-coordinate transfer criterion orders the gradient of F on the strict chamber. The prefix means b_i-b_j for i<j are (1/(ij)) times the sum of all g_k-g_ℓ for k≤i<ℓ≤j, so they are nonnegative. Equality forces every tangential derivative of f to vanish throughout the interior, hence constancy by connectedness, continuity and symmetry. For p>1, the positive-part p-power supplies a C¹ extension. For entropy the smoothed differences are sums of positive log ratios that increase as epsilon decreases; uniform convergence on the simplex and monotone convergence in the identity give strictly positive covariance for negative entropy. At m=2, E[M H]=7/24+log(2)/12, E[M]=3/4 and E[H]=1/2, giving exactly the claimed covariance.

## originality

PASS

Credit the strict all-statistics covariance law and its positive-pair identity, not the already-known largest-spacing/Greenwood covariance or the ranked-gap substitution itself. The closest exact records share the quadratic special case and in one case the same coordinates, but do not cover general symmetric Schur-convex statistics. No inspected primary theorem implies the credited claim.

## value

PASS

A single inequality with a sharp equality condition treats simultaneous dependence of the maximum with all admitted dispersion scores, including nonseparable ones; entropy and power sums illustrate why a one-statistic formula does not settle this question. The positive-pair representation explains the sign and strictness, rather than just computing selected moments.

The dated certificate retains the supplied scientific assessment, sources and limitations.
