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

## Reproducible checks
Run `python3 verify.py` using the Python 3 standard library. It independently evaluates the radial means of two polygons directly by angular quadrature at four increasing smoothing parameters, without substituting the claimed limit. The square and nonsymmetric triangle exhibit successively smaller errors against the limiting facet formula. It also checks the exact equal-facet and equal-coordinate boundary equations for the cubical John and Löwner radii in dimensions two, three and five.

## Proof-level verification
The general theorem is proved analytically. Critical checks are: the almost-everywhere radial derivative of a translate; the uniform multiplicative inclusion used for domination; the cone-volume Jacobian; cancellation of the linear outer-normal integral; equicontinuity on bounded test-vector sets; exclusion of far-away sublevel components via the ordinary covariogram; and the strict concavity determining all cubical contact vectors. Every quantity and normalization is defined in the proof.

## Limits
Numerical quadrature cannot certify all dimensions or all convex bodies; the proof, not numerical sampling, establishes those quantifiers. No uniform rate in the convex body, dimension, or threshold is asserted. Independent mathematical validation has not been performed.
