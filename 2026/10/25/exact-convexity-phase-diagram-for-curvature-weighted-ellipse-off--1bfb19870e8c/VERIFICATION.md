---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

The explicit curvature-radius normal displacement is C_k=((alpha+kq/alpha)cos t,(beta+kq/beta)sin t), q=alpha^2 sin^2 t+beta^2 cos^2 t. Direct symbolic differentiation independently reproduced the signed curvature numerator beta^2/sqrt(x) times Q_x(k,u) in u=sin^2 t. The polar-angle determinant is strictly positive, providing a regular simple once-around radial graph; nonnegative signed curvature is therefore equivalent to convexity. Both Q endpoints, interior-vertex condition (0<k<(x-3)/(2x)), its discriminant 3k(2k-1)(x-1)^2R_x(k), and the discriminant 9(x-1)^2(x^2-34x+1) were checked against the stated proof. All edge cases x=1, x=3/2, x=x*, k=k±, k=k0, and k>k0 are handled with nonnegative zero-curvature endpoints. The independent numeric checker tested analytic quadratic minima over a deterministic grid of 10 axis ratios and 401 k values each, in addition to checking the symbolic determinant at 405 configurations; these samples corroborate but do not replace the exact quadratic proof.

## originality

PASS

Veerman 2023 Section 6 introduces this exact ellipse with normal displacement proportional to reciprocal curvature and explicitly remarks that the offset loses convexity for large k, but gives no exact phase partition or high-eccentricity convexity recovery interval. Its full relevant Section 6 and figure were inspected. Hinterleitner 2011 studies geodesic mappings of surfaces of revolution rather than this normal-offset planar convexity question. Searches across equivalent normal-offset and curvature-radius formulation found no exact x*=17+12sqrt2 and k± phase transition. This is best-of-knowledge, not an assertion of exhaustive novelty.

## value

PASS

The exact parameter range determines when the geodesic-preserving-projection construction stays geometrically convex, and the reentrant convexity interval at axis ratio above 3+2sqrt2 is a qualitative phase transition missed by a mere large-k loss statement. It is a natural sharp boundary for the original geometric family, not an arbitrary parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
