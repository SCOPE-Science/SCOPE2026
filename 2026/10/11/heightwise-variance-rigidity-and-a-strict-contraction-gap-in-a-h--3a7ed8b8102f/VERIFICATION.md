---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Direct symbolic differentiation of P=z+(p/2)x²−qxy+(q/2)y² gives dot P=c−kx−q(x−y)²; compact invariant probability makes E[dot P|P]=0 via antiderivative tests. Likewise dot y=x−y gives E[x|y]=y and E(x−y)²=Var x−Var y. If defect is zero, invariant support lies in x=y, hence y constant, x constant, z=0, and x=c/k. Mean trace −1−px+qy gives the exact contraction-gap formula and strictness when p>q>0. For ergodic compact measures Liouville and Oseledets yield the stated exponent sum; no numerical chaotic measure existence is assumed.

## originality

PASS

Full 2013 same-object source reports SE17 dynamics but not the polynomial P or invariant-height calibration; the 2018 Liénard source is a distinct planar equation. Related published hidden-attractor coboundaries act on distinct vector fields. The 2021 Jacobi paper full text was inaccessible and remains a named priority risk, not an unsupported novelty certification.

## value

PASS

A cancelling polynomial for the actual 3D SE17 flow yields exact fiberwise constraints and a strict phase-volume gap relative to its only equilibrium, stronger than an isolated coordinate normalization. These are natural invariant-measure and Lyapunov constraints for a hidden-attractor model and have independent mathematical use.

The dated certificate retains the supplied scientific assessment, sources and limitations.
