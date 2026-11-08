---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For K_r=[-1,1]^2 intersection B(0,r) with 1<=r<=sqrt(2), diameter 2r follows from antipodal feasible circle points; subtract four disjoint disk caps for A(r), and surviving circular-arc angles have measure Theta(r). The local antipodal polar deficit is u+v+(r/4)phi^2, giving the fixed-shape epsilon^(5/2) law with coefficient 16 r^(3/2)Theta/(15 A^2). At the square endpoint, four ordered opposite-corner configurations give epsilon^4/24. For r=sqrt(2)-t epsilon, four-dimensional corner-variable integration yields J(t)=1/24+t/3+t^2/2. On the distinct r=sqrt(2)-lambda, epsilon=z lambda^2 scale, tangential variables w,w' and radial slacks give H(z)=1/16 integral_0^(2sqrt2) (2sqrt2-v)(sqrt2 z-v^2/8)_+^2 dv, yielding the exact piecewise formula and matching boundary at z=1/sqrt2. I independently symbolically integrated both branches of H and J, checking their identity/interface. Remainder control is pointwise for fixed z or t, not uniform in unbounded scaling parameters; endpoint arc localization is supported by compactness and negligible angular boundary strips. Independent verification: /mnt/data/scope_worker03_20261105T0838Z/independent_checks.py; run output ALL_FIVE_INDEPENDENT_CHECKS_OK. Finite checks support but do not prove universal statements.

## originality

PASS

Current primary literature supplies fixed-disk and fixed-square distance distributions, but no identified exact joint boundary-layer crossover for the disk–square intersection. The piecewise curvature-scale and corner-scale formulas are new relative to the material actually inspected; Sheng (1985) remains incompletely accessible.

## value

PASS

The joint asymptotic law for random distances near diameter in a disk-clipped square has genuine geometric motivation: a rounding-to-polygon degeneration changes the tail exponent and admits two distinct boundary layers. The exact universal functions H and J are not mechanical restatements of disk/square marginals and can be used to analyze rare long-distance pairs and shape-induced tail phase changes. The fixed disk and square coefficients alone are established phenomena and are not the proposed novelty.

The dated certificate retains the supplied scientific assessment, sources and limitations.
