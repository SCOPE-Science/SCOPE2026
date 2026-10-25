---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

The claimed universal convex order is valid for all nonparallel edge generators u,v in R² with a=|u|,b=|v|>0,L=a+b and |c|<1. Direct edge-arclength mixture yields the mean L²/3. For any convex test, sign averaging the ±2abcT perturbation grows in |c|, reducing the lower bound to a rectangle and upper bound to c=1. In the collinear limit the signed boundary coordinate is uniform on [-L,L]. For rectangles the exact CDF sqrt((s-a²)+)/L+sqrt((s-b²)+)/L has one change relative to the square CDF at (L²-b²)/3; equal means give every integrated-CDF stop-loss inequality. Strictness holds for nondegenerate skewness or non-square side ratio. Power p∈(-1,0)∪(2,∞) gives convex tests of squared radius, p∈(0,2) concave reversed, p=0,2 equal; singular negative powers require p>-1 and dominated convergence. Independently expanded the exact fourth radial moment L⁴/5-area²/12 (symbolic residual zero) and checked 99 positive-part hinges via 256-point Gauss-Legendre quadrature in four independent shape/angle choices. Quadrature alone is not a theorem.

## originality

PASS

The new content is a two-sided whole-convex-test comparison for *single-point squared radial laws across different fixed-perimeter parallelograms*. Existing Sachs p=2 invariant and prior fourth boundary radial moment are explicitly credited; selected weighted-perimeter needle extremizers under stronger symmetries and interior-vs-boundary convex order for a *fixed* body neither imply square lower bound nor all test functions. Read the 38-page Csató et al paper incl theorem and majorization passages, and the complete four-page Tokmachev paper, confirming the latter compares different sampling measures for the same K. A covered single moment does not subsume an infinite family of stop-loss inequalities. Historical indexed-priority gap remains.

## value

PASS

Convex order gives a single optimal inequality stronger than separate moment optimizations, specifies the uniquely extremal square and sharp degenerating needle, and settles all radial power weights in one natural fixed-perimeter quadrilateral class. This is a meaningful structured geometric-probability comparison, not merely the known quadratic/fourth-moment recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
