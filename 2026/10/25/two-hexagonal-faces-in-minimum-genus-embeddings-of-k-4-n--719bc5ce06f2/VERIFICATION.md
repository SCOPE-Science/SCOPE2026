---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

Face-traced every oriented dart in the explicit K4,5 rotation to seven 4-faces and two 6-faces; V=9, E=20, F=9 yields genus 2. The prescribed two-vertex operation inserts x,y before/after a distinguished b0 at alternating a-vertices and gives two consistent x,y rotations, causing four new quad faces while preserving the two 6-faces. Independently implemented face permutation on every extension for odd n=5 through 31, each exactly 2n-3 quadrilaterals and two hexagons. The local boundary switching is verified as a fixed rotation pattern, and Euler gives genus increase 1; Ringel lower bound ceil((4-2)(n-2)/4) gives (n-1)/2 for odd n. Finite tracing corroborates but cannot by itself prove arbitrary n; the local induction supplies that step.

## originality

PASS

Best-of-knowledge originality after statement/implication comparison against relevant primary literature and published Resultary records; preexisting general ingredients and exact special cases explicitly credited; residual priority risks retained.

## value

PASS

A concrete face-size realization across all odd n settles a natural graph-embedding existence pattern that Euler excess allows but cannot guarantee. The local stable two-hexagon extension is a reusable constructive genus-embedding mechanism, distinct from isolated small witnesses. No claim of uniqueness or all distributions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
