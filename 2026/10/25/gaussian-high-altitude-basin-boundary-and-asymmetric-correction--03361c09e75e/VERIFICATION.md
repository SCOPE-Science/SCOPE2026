---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

Starting from the exact planar system rdot=-mu*r*(21r^4-125r^2+400z^2+100)/21 and zdot=-z-r^2/10, set eta=sqrt(mu),U=eta z. Then Rdot=-(400/21)RU^2-(eta^2/21)R*C(R), Udot=-U-eta R^2/10. At eta=0 the normally attracting U=0 line has transverse eigenvalue -1; integrating its strong-stable leaf ending at (1,0) gives log R=(200/21)U^2. For fixed |U|<=M, compact bounded-time continuation of the smooth strong-stable foliation supplies the regular eta expansion. The invariance equation yields dL1/dU=-(40/21)exp((400/21)U^2), and the saddle normalization R(-eta/10)=1 fixes L1(0)=0. This yields the claimed uniform O_M(eta^2) expansion and odd correction. The fixed scaled-height restriction is essential and is not inferred from finite integration.

## originality

PASS

The exact vector field, basin-separatrix interpretation, and fixed-height O(mu) formula are in Castañeda–Rebollo-Perdomo 2026 Section 4, and receive full priority credit. Substitution of z=U/sqrt(mu) into their bounded-height nonuniform remainder would be invalid. Their full inspected source does not derive the compact-scaled-height Gaussian limit or parity-breaking eta correction. Fenichel stable foliation is a standard tool, not the explicit conclusion.

## value

PASS

The stable separatrix is the natural two-basin boundary of a published saddle-cycle flow. The height z∼mu^{-1/2} is the sharp scale where a visually vertical boundary deviates by order one: the Gaussian limiting radius and an explicit odd asymmetry provide concrete basin thresholds beyond the published bounded-height expansion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
