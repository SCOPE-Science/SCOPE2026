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

The planar intersection-body radial function is the centered chord length in the perpendicular line. Its affine covariance ensures both |I(T-z)| and |T| scale by |det A|, so normalize triangle vertices to (1,0),(0,1),(-p,-q), p,q>0. For each slope m, intersections with the actual three edges yield the proof’s three rational branch formulas for the chord horizontal span d(m); polar area is exactly ∫_{−∞}^{∞} d(m)^2 dm. The given substitutions on negative, middle and positive intervals have elementary rational/log primitives and yield area S+2/S times the displayed symmetric log sum (S=1+p+q), equivalent to barycentric formula after dividing by S/2. Independently constructed raw line–segment intersections and quadrature, without using the provided d(m) branch code, at (p,q)=(1,1),(0.4,2.2),(4,0.12), matching areas 5.7725887222,5.6855004163,6.0450975291. For g(t)=t(1-t)log((1-t)/t), g′ is symmetric around 1/2 and strictly decreasing on (0,1/2); for any two distinct coordinates a>b with a+b<1, compare a to either b or 1-a to prove strict balancing increases ∑g. Evaluate g(1/3) and boundary pair g(t)+g(1-t)=0, proving the strict sharp bounds and all equality/limit cases. Quadrature is corroboration, not the universal proof.

## originality

PASS

Brandenburg–Meroni’s primary full paper on translated intersection bodies rigorously describes section-polynomial regions and convexity conditions but not this center-dependent *area ratio* for every triangle. The precursor Brandenburg–Berlow–Meroni–Shankar develops semialgebraic machinery and structure of intersection bodies, not the explicit barycentric integral and strict centroid extremum. The relevant general Busemann intersection inequality has different scope and an abstract alone cannot exclude a specific sharp triangle bound. Published Resultary and exact barycentric searches found related geometric statistics but no direct stronger area-profile implication; this is qualified best-of-knowledge originality.

## value

PASS

A translated-center intersection-body area functional is an intrinsic, affine-invariant quantitative statistic of a simplex. The exact profile resolves the complete natural range, strict barycentric majorization, and unique centroid optimizer for all planar triangles; these are reusable extremal and geometric-functional facts not a manufactured finite slice. The boundary limit and affine normalization are structurally meaningful, even if higher-dimensional analogues are unknown.

The dated certificate retains the supplied scientific assessment, sources and limitations.
