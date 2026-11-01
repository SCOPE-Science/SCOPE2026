---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

The gradient of the quartic is e(yzw,xzw,xyw,xyz), so its critical support is exactly six projective coordinate lines. Every vertex has value a≠0, so edge cuts are disjoint. Restricting to each edge gives a monic binary quartic a(u^4+v^4)+βu²v², finite locally free degree 4. A root has order 2 if β≠0, order 4 if β=0. The transverse polar uv coefficient is a unit; formal splitting gives UV+s² or UV+s⁴ (Artin A1 and A3), including zero-wall intersections. Finite singular support implies normal irreducible quartic and K3 resolution. On torus the Gauss map is an involutive cubic Cremona; F after substitution is degree12 primitive irreducible on torus, no coordinate divisor. Independently GF4 count across r=0,1,2,3 gives supports 12,10,8,6 and rank 24; finite computation corroborates but does not establish relative flatness.

## originality

PASS

Best-of-knowledge originality with disclosed antecedents and material access limits. The classical Heisenberg, Dwork, q²+xyzw and Cremona descriptions were compared by equations. The same ambient char-2 q²+xyzw family covers generic and maximally degenerate examples, but neither a degree-12 dual nor all intermediate scheme structures follows merely from those example counts. The prior published examples imply some endpoints, but do not from accessible text entail all intermediate parameter-wall contact orders and a globally uniform degree-12 Cremona dual. Without full III text, an exact stronger implication remains a residual risk.

## value

PASS

A natural primitive integral quartic family has characteristic-two ADE wall-crossing with constant scheme-theoretic length and polar-degree invariant. Flatness despite collision of reduced singular points and explicitly birational dual map are mathematically distinct from already known generic and special fibers. Not a new discovery of the generic 12 nodes or 6 A3 endpoint.

The dated certificate retains the supplied scientific assessment, sources and limitations.
