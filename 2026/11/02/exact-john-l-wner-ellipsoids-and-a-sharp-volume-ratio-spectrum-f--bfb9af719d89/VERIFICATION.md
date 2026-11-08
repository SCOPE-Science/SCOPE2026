---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For d>=3, 0<=t<1, direct support tests for the permutation-invariant inscribed ellipsoid yield q+s²<=y², y-s>=t, y+s<=1. Maximizing s(1-2s)^((d-1)/2) gives s=min{1/(d+1),(1-t)/2}. The Löwner candidate is certified globally by positive weights on the two vertex orbits, mean y1/d, covariance Q_L/d and unit gauges on both layers; at t=0 the inner orbit is one origin. The quadratic t²r²+d(1-t²)r=1 has its admissible unique root and yields the stated semiaxes. Exact differentiation or nested-ellipsoid uniqueness gives strict ratio decrease from d^d to d^(d/2)(d-1)^((d-1)/2); the one-sided second derivative jump follows solely from the John phase switch. Independently recomputed positive-root and ratio bounds in dimensions 3..7 and several t, corroborative only.

## originality

PASS

Best-of-knowledge original contribution after comparing actual claims and implications with primary literature: The established general contact theorem plus a new symmetry optimization reconstructs this result, but the reviewed prior statements do not already imply the evaluated formulas and sharp ratio.

## value

PASS

The same geometric body bridges a simplex and a degenerating homothetic facet; the complete extremal ellipsoid pair, contact transition and sharp volume-ratio spectrum are intrinsic affine-invariant quantities. Explicit phase regularity supplies a meaningful natural boundary rather than a renamed general theorem. The planar trapezoid special case is explicitly excluded from novelty.

The dated certificate retains the supplied scientific assessment, sources and limitations.
