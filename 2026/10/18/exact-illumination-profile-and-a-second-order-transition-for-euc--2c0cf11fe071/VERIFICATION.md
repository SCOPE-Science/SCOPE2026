---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-19.md",
      "INDEPENDENT_AUDIT_2026-10-19.json"
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

Reconstructed feasible center lens B_{R-r}(0) intersect B_R(se1), corner supporting arcs, Green area formula F=R^2 beta-R(R-r)sin(beta)-r^2 theta and endpoint 0 to pi(R^2-r^2). Strict nesting gives monotone disk illumination, R-ball-convex iff s<=R. Independently checked F(R) trigonometric threshold and numerically extracted second inverse-area correction at k=0.2,0.8,2-2sqrt(3)/3; source symbolic checker read confirms exact b^3/b^5 coefficients and C=(3k^2-12k+8)/(5(1-k)). Boundaries r<s<=2R-r, positive radii; not uniform as r/R approaches 0 or 1.

## originality

PASS

Best-of-knowledge PASS: accessible source descriptions establish definition and qualitative asymptotics, while inspected published related result treats curvature Hessians, not this exact unweighted disk illumination profile. The highly relevant 2026 Oliva–Werner–Yalikun full text remained inaccessible; it may contain a disk case and is recorded as a material priority risk, not falsely declared NOT_COVERING.

## value

PASS

Natural exact model for newly introduced R-ball illumination: complete disk profile determines precisely where illumination stops being ball-convex, and sign of the first curvature-sensitive correction gives a sharp meaningful parameter transition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
