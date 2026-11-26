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

In characteristic p dividing q, F_Y=X^(q−1), so possible singular points have X=0 and hence Y=0, but F_X(P0) is nonzero. In the Hessian the Y row and column have only the X entry −X^(q−2); the Z diagonal is −2XZ^(q−3), yielding the determinant 2X^(2q−3)Z^(q−3). Since p is odd this is nonzero. The divisor of X on the curve is qP0, and Z cuts q simple roots of t^q−t−1, with derivative −1. Their sum with the Hessian exponents gives the stated divisor of degree 3q(q−2), including the absent Z contribution at q=3. Directly, on X=1 the affine equation is 1−z^(q−1)+y−y^q. At a point with z=z0 its tangent has slope dy/dz=−z0^(q−2); the quadratic term on this line is −binom(q−1,2)z0^(q−3), nonzero at z0≠0 since the binomial coefficient is 1 in the field. For z0=0 the tangent is y=t, with exact contact q−1. Homogeneously that line cuts −XZ^(q−1), proving its remaining simple point is P0; the tangent X=0 at P0 has contact q. This also independently excludes any other flex, including in characteristic three. Finally t maps to t+1 under q-power Frobenius, so all q roots have orbit length exactly p and there are q/p orbits.

## originality

PASS

The degree-q model, smoothness and extremal point count are known; neither is credited here. The distinct claim is the entire weighted geometric Hessian section, exact contacts and arithmetic of its exceptional points for odd q. The inspected same-curve article, adjacent indexed results and accessible comparisons do not supply this package. The inaccessible uniqueness paper limits historical confidence but is not a scientific failure by itself.

## value

PASS

The ordinary Hessian and contact orders are natural projective invariants of a fixed extremal family, and the rational point count conceals its nonrational geometry. Concentration of the entire divisor of degree 3q(q−2) at explicit points, the disappearance of the nonrational flexes at q=3, and their length-p splitting otherwise give exact data usable in extension-field and tangent geometry. The straightforward differentiation is a means to that complete result, not the value claim by itself.

The dated certificate retains the supplied scientific assessment, sources and limitations.
