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

For any fixed nondegenerate convex polygon, circumradius≤t forces pairwise distances≤2t. Compactness and absence of noncollinear same-edge triples localize sufficiently small triangles at one vertex on its two incident rays; finite positive threshold depends on the polygon. For two ordered ray coordinates a,b and one c the exact circumradius factor is sqrt(a²+c²−2ac cosθ)sqrt(b²+c²−2bc cosθ)/(2c sinθ); substituting a=cu,b=cv with Jacobian c² gives an integral of 8t³ sin³θ/3 times the square of an explicit 1D integral (1+cosθ)/sin²θ. Exactly six ordered assignments across two rays yield factor 16t³(1+cosθ)²/sinθ per vertex, including the collinear positive-mass atom at +∞ outside the event. Exterior turns δ_i sum to 2π and the angle score f(δ)=2tan³(δ/2)/(1+tan²(δ/2)) has f″=tan(δ/2)(1+tan²(δ/2))+2tan(δ/2)/(1+tan²(δ/2))>0. Exact symbolic differentiation independently checked this identity, proving Jensen and equality exactly at equiangular polygons. Regular m-gon formula agrees algebraically. Checker.py uses finite quadrature and MC only as diagnostics.

## originality

PASS

Primary random-triangle studies Kórus 2020 and Labelle 2023 select circle points or random side lengths, not three independent fixed-polygon perimeter points; their law cannot directly imply this exact corner-angle distribution. Nearby published short-distance coefficient concerns TWO sampled polygon-boundary points, not triangle circumradius (three-point noncollinearity). Smooth-body interior-uniform random triangles have different measure and tail exponent. Search yielded no exact cubic corner-coefficient or sharp equiangular minimization for the specified observable; unindexed stochastic-geometry literature remains a risk.

## value

PASS

This exact (not asymptotic only) local CDF gives a universal cubic corner exponent and an explicit angle/perimeter fingerprint across all convex polygons, plus sharp equiangular shape ordering, a natural geometrical probability question with motivated boundary nonsmoothness. The shape-dependent t_K is an honest limitation rather than an incomplete finite census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
