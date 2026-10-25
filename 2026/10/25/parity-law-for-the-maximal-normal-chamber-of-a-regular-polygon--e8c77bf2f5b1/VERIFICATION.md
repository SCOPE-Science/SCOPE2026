---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The analytical verification proceeds in four steps: (1) express each edge-active region as a strip using orthogonal projection onto its supporting line; (2) use parity to determine whether the intersection has \(2n\) or \(n\) sides; (3) prove its circumradius is no greater than the inradius of the original polygon for all admissible \(n\); (4) compute both areas exactly and divide. The strict interior of the strip intersection gives one distinct normal from every edge and every vertex. Conversely, \(2n\) distinct face-based normals force every edge projection to lie in its segment.

The exact formulas were evaluated in algebraically equivalent forms for \(n=5,6,7,8,9,10,11,21\). Agreement is a numerical sanity check, not a proof. The infinite statement is supported by the analytic derivation above. Boundary points where a strip inequality is an equality form a finite union of line segments and have area zero. No external checker, independent validator, or independent audit is claimed.
