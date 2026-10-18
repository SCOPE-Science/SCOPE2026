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

The stated optimizer and quantitative gap follow from the explicit support geometry, a Green-integral area identity, the Dirichlet Poincaré inequality and a monotonicity comparison for the potential divided by \(\cos x\). These are analytical, infinite-dimensional arguments.

The standalone standard-library verifier `verify.py` ran successfully and returned `VERIFY_OK`. It uses exact rational intervals, not unqualified floating-point approximations, to bound the explicit angle and optimal area for \(m=15/16\). An independent trigonometric quadrature splitting the two bang-bang intervals agreed with the closed area expression to the digits reported in the finding.

The scope is midpoint-symmetric measurable curvature splittings \(0\le r\le1/2\) at each fixed angle \(\pi/4<m<\pi/2\). The proof does not optimize over the angle or arbitrary reduced bodies. Literature comparison is documented in `REVIEW.md` and `AUDIT.json`; historical novelty has not received external certification.
