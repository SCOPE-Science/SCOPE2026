---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-01.md",
      "INDEPENDENT_AUDIT_2026-11-01.json"
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

For d>=2, n=d+1 and s=1+lambda, the nonconvex union is exactly the barycentric cap union max_i x_i>=1 in sP; it fills sP iff lambda>=d. Regular simplex zero-sum barycentric differences have norm squared ell^2/2 times sum of squared coefficients. For a point outside the caps with m=max x_i<1, the radial feasible point on x_i=1 yields dist^2 <=(ell^2/2)*s(1-m)^2/(s-m). Its derivative in m is s(1-m)(m+1-2s)/(s-m)^2<0, so only the centroid can attain the global bound. Orthogonal projection of the centroid to a cap has other coordinates lambda/d and attains exactly ell^2(d-lambda)^2/[2d(d+1)], giving the claimed positive-part Hausdorff law and unique deepest point. The lambda=0 and lambda=d boundaries are covered. Examined the exact-rational active-set verification source; its 16,848 reported instances are ancillary, not a universal proof.

## originality

PASS

Meyer's general convexification criteria and the related vertex-generated-polytope literature concern thresholds/coverings, not the exact Euclidean Hausdorff gap for every real dilation with unique deepest-point rigidity. Published simplex skeleton Minkowski averages and discrete vertex averages change the set operation, so their exact distances do not imply this continuous one-sided union profile. This is a qualified best-of-knowledge PASS; some plausible older geometric papers were not fully read and historical priority is not certified.

## value

PASS

An exact full one-parameter Hausdorff defect profile for canonical regular simplices, with unique extremizer and quantitative off-center stability, is independently useful in quantitative convexification. It is not merely the known convexification threshold or a finite test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
