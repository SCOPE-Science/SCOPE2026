---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

C: z=|axial cosine| is uniform [0,1]; support-function subtraction gives W/r=a+max(a,kz), a=√(1−z²), k=h/r. Split at z0=1/√(1+k²), and for k>1 at zm=k/√(1+k²). Inverse-Jacobian branches C,B,A give exact nonnegative piecewise density integrating to 1. Global minima/maxima switch simultaneously at k=√3; L,U formulas agree by direct extremization. At lower edge, if k<√3 density tends to zero, whereas for k≥√3 its right limit is (k/2+k/(k²−1))/r>0. Thus edge law identifies regime and reconstructs (r,h). In strict support-ratio regime both broad and slender solutions exist, unique within their branch. Independent direct directional grid and numerical quadrature confirmed normalization for k=.4,1,1.3,√3,2.2,5; proof is analytic for all ratios.

## originality

PASS

O: Inspected full Kim–Yaskin–Zvavitch concerns orientation-unlabeled hyperplane projection volumes and nonuniqueness for general bodies, not right circular cone line-width injection. Primary studies of cone planar projected area/perimeter are different measurements. Strongest similar exact width results returned for cubes and octahedra, not cones.

## value

PASS

V: Solves a natural geometric tomography identifiability problem for a canonical two-parameter convex family, with sharp failure when retaining only extrema and a precise local density statistic needed to restore uniqueness. An exact self-contained all-aspect-ratio inverse invariant is useful independent of general-body reconstruction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
