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

For q=1 vector field has first integral H=xz−y²/2+x|x|y, preserved in both x signs. H=-h<0 meets x=0 only at y=±sqrt(2h), hence switching is transverse, no sliding and unique crossing flow; gradient H≠0, coordinate w=z+|x|y shows each leaf is cylinder R×S¹. Divergence of vector field equals −|x| sectorwise; at x=0 saltation S=I±4y e_z e_x^T, determinant one and dH invariant. This gives exact coarea-area decay without surface delta. Surface divergence theorem on disk/annulus bounded by cycles yields 0=−∫|x|ω<0, proving at most one cycle; existence from Llibre–Novaes–Valls 2023 Theorem 1 yields exactly one. Periodic derivative μ=exp(−∫|x|dt) strictly in (0,1); two unit Floquet multipliers from time and first integral. Weighted scaling (a x(at),a² y(at),a³ z(at)) maps h→a^4 h and invariant integral μ; bounded omega-limit on cylinder with no equilibria tends to unique cycle by crossing-flow Poincaré–Bendixson. Independent SymPy recomputed sector conserved H, divergence, saltation det and vector mapping; global existence not proved computationally.

## originality

PASS

Best-of-knowledge PASS for discontinuous q=1 uniqueness, full leafwise bounded-orbit basin and saltation-corrected Floquet multiplier, distinct from published existence and separate smooth q>=2 uniqueness result. Strong risk remains because complete 2024 same-system sequel not obtained; Oxford institutional retrieval was blocked by safety controls and was not bypassed.

## value

PASS

The discontinuity q=1 is the natural parameter boundary omitted by existing smooth uniqueness results; a crossing-corrected coarea proof determines multiplicity, attracting dynamics and energy-invariant transverse Floquet multiplier for every negative level. This is an analytically substantive structural result beyond known existence or a routine substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
