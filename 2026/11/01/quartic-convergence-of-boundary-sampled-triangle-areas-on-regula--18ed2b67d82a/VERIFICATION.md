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

Equal edges give independent uniform labels and uniform coordinates along each edge. By convex cyclic order the oriented area for distinct edges has nonnegative sign and is separately affine, so averaging is equivalent to using their midpoints. Summing over gap triples a+b+d=m with the cyclic starting index counts each midpoint triangle three times; summing its three sine terms gives the stated weighted sine sum. If exactly two points share side i, their mean separation is 2 sin(π/m)/3; the mean height on side j is its midpoint's distance to the supporting line, and summing these heights gives m²cos(π/m). Exactly three on a side contribute zero. For the second moment, rotation gives centered covariance (1+2cos²(π/m))I/6; the square of the determinant of the two differences has three terms with expectation 2 det Σ each, and mixed terms vanish by independence and centering. Normalizing by the area gives both formulas. In the derivative test for Q all denominators are positive, and H′(z)=3 sin(z)(z−sin(z)cos(z))>0; thus m=3 is the unique upper endpoint and the disk value is an unattained lower limit. The Taylor coefficients agree through order m^−6. In particular the variance coefficient at m^−4 is π²/15−3/10>0, not another cancellation.

## originality

PASS

The supported distinct content is the evaluated all-m moment pair, strict mean ordering and quartic approach in both moments for the arclength model. The general gap integral in the related parallelogram record covers the mean as an exact integral, the triangle and square records cover specific endpoints, and the covariance identity used for the second moment is standard. These overlaps are credited rather than counted as novelty. The inspected statements do not cover the full regular-polygon side-count result, and catalog dates alone do not decide priority.

## value

PASS

The first two exact moments quantify the finite-sidedness error in a natural boundary sampling experiment. The shared cancellation of the quadratic term, despite the quadratic geometric discrepancy between a regular polygon and its circumcircle, and the strict ordering at all side counts provide information beyond the isolated endpoint laws or a general unevaluated integral. A researcher using regular polygons to approximate the disk boundary can use the distinct mean and variance corrections without assuming the geometric approximation rate carries over to these statistics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
