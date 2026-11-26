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

The cited product CDF is equation (8) in the proof of Theorem 1 with perimeter one; rescaling the polygon gives n d_H/P. In a Poisson wedge let x,y be the first distances on its rays. All convex combinations of ray points have coordinates a,b≥0 with a/x+b/y≥1 in the ray basis, so radial scaling to equality cannot increase distance; the first-point segment is itself in the hull. Its distance is at least min(x,y)cos(α/2) by projection on the bisector. At fixed x>0 the distance divided by y tends to 1 in the acute case (the y-endpoint is nearest for small y) and to sin α in the obtuse case (the perpendicular foot is inside); the perpendicular formula at π/2 also tends to 1. The event D≤t lies in the two small-coordinate strips; their overlap is O(t²), and dominated convergence after rescaling one coordinate by t gives the coefficient 2ℓ(α). For the tail the point with equal ray coefficients xy/(x+y) gives the upper distance bound (x+y)cos(α/2)/2. The exponential-minimum lower bound and gamma-sum upper bound agree on logarithmic rate. The polygon product takes the smallest of those rates. The flat part of log ℓ ends at π/2, after which it is strictly convex; nonconstant angles averaging at least π/2 cannot all be in the flat part, so strict Jensen applies, including at m=4. The least angle is strictly smaller than the regular angle, giving the opposite sign in the tail. These strict inequalities transfer to the converging finite-n CDFs at each fixed threshold, not uniformly in threshold or sample size.

## originality

PASS

Credit the fixed-polygon sharp endpoint laws and their strict all-non-equiangular comparison with the regular polygon, not the full limiting distribution or Poisson construction, which are already established. The inspected catalogue and primary comparisons supply either a prior premise or a different limit/statistic, not the joint endpoint-and-crossing conclusion.

## value

PASS

The exact asymptotics explain why non-equiangular polygons are favored at small errors but disfavored in the extreme tail, ruling out either first-order stochastic dominance for every such polygon at fixed m. The tail identifies a geometric parameter, the smallest angle, whereas the lower-tail coefficient combines all angles. This is useful information not supplied by mean comparisons alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
