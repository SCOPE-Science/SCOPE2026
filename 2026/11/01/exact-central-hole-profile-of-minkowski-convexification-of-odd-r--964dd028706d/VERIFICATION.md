---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

For every odd m>=5, h_P(-v_j)=cos(pi/m). Thus each vertex translate excludes the strict interior of the concentric polygon with vertex-normal support h=1-t cos(pi/m). In the nearest-vertex sector, the intersection of (1+t)P with X>=h is a five-vertex polygon: A=(1+t,0), E_±=(1+t)(cos²theta,±cos theta sin theta), H_±=(h,±h tan theta). A and E_± belong to v_0+tP by explicit convex combinations; H_± lie on its opposite edge because 1<=2t cos theta for t>=1. Convexity establishes coverage outside the hole, including its boundary. At t=sec theta the center becomes covered; addition of (t-sec theta)P proves all larger dilations convexify. For 0<=t<1 an outer polygon edge has a central uncovered segment, so no earlier convexification. The inradius-area calculation gives m(1-t cos theta)^2 tan theta, and normalization and theta-series give the exact relative law and both fourth-order asymptotics. No finite geometry experiment is used as proof.

## originality

PASS

Best-of-knowledge PASS for the precise changing central-hole identity and area law, not for the inherited Schneider index definition, general Carathéodory bound or existence of finite convexification. Direct primary-paper comparisons and subject searches found no dominating result; historical closed-form odd-regular specializations remain a residual risk.

## value

PASS

PASS: exact birth and closure of the unique central hole for every odd regular order, including a sharp Schneider transition and quantitative all-scale area obstruction, is a natural geometric missing-data problem. This is not a renamed generic convexification inequality; it measures a meaningful shape and defect.

The dated certificate retains the supplied scientific assessment, sources and limitations.
