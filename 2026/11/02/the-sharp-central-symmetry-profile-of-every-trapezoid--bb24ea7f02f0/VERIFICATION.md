---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

Affine shear and scaling reduce every nondegenerate positive-base trapezoid to horizontal sections [-r(z),r(z)], r(z)=1-(1-t)z. For center (x,y), each slice has overlap <= twice the lesser radius, with equality at x=0, uniquely globally because at z=y any x !=0 strictly reduces positive-measure overlap. At x=0 direct slice integration yields A(y)=4m(1-(1-t)y)-2(1-t)m^2, m=min(y,1-y). Its lower branch 4y-6(1-t)y^2 and strictly decreasing upper branch give unique y=1/[3(1-t)] for 0<t<=1/3 and y=1/2 for 1/3<=t<=1. Dividing by area (1+t) gives kappa=2/[3(1-t^2)] or (1+3t)/[2(1+t)]. Derivatives match C1 at t=1/3 with right-minus-left second derivative -27/8; near t=0 kappa-2/3=(2/3)t^2+O(t^4), yielding sharp inverse 1/2-Hoelder. Case t=1 parallelogram checked separately. Independent convex-polygon intersection using Shapely checked five rational shape/center profiles; the continuous maximization is analytic, not proved by sampling.

## originality

PASS

The full two-branch base-ratio profile, unique center and inverse-conditioning claim were compared, not just the numerical 2/3 lower bound. The universal Kovner–Besicovitch estimate and axial-symmetry papers are different statements; generic overlap algorithms compute instances but do not visibly report this structural symbolic classification. Best-of-knowledge originality is qualified because older specialized convex-symmetry texts were not fully available.

## value

PASS

A normalized exact point-symmetry invariant for every trapezoid, including unique maximizing center, exact migration threshold, invertibility and conditioning at the triangular limit, is a natural complete affine classification for a standard symmetry measure; it is neither a one-off coordinate exercise nor merely recomputing the universal 2/3 bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
