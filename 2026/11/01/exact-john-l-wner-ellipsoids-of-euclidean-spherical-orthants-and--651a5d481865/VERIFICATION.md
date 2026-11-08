---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

John candidate Q has diagonal d/(d+1)^2 equal squared center coordinate, giving nonnegative coordinates; axial inequality implies ||x||²<=1. d+1 contact points form normalized regular simplex with zero barycenter and covariance I/d, sufficient for unique John maximality. Löwner candidate unit-sphere gauge q(z) is strictly convex in z=e·omega∈[1/sqrt d,1], with both endpoints gauge one; interior is strictly inside. Origin has gauge <=1 and equals one for d=3,4,5, strictly <1 for d>=6. Explicit positive weights for contact sets give center and covariance Q/d; contact certificate gives unique covering ellipsoid. Independently recomputed Q/covariance identities for d=3,4,5,6,7,10,20 (max numerical error 2.8e-17), and origin gauges 1 through d=5, 0.9439 at d=6. All-dimensional claim rests on exact algebra, not finite checks.

## originality

PASS

Best-of-knowledge: identified and materially compared directly relevant primary theorems, distinguished prerequisite frameworks from implication of the final exact claim, recorded access and priority risks.

## value

PASS

This gives complete dual extremal ellipsoids of a canonical symmetric nonpolyhedral body in every dimension, exposes an unexpected dimension-six contact loss, and proves nontrivial invariance under enclosing polytopes; directly useful as exact convex-geometry benchmarks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
