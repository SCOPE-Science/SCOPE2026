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

A fixed geometric point has simplex support invariant under the group and barycentric coordinates constant on each arrow orbit. The actual admissible orbits are singleton-to-singleton arrows and independently transitive stars from one fixed label into one block; other orbits produce competing incoming edges or a directed cycle. Hence invariant simplices form the PL orbit-barycenter join F_f*D_f^{*t}. For f=0 it has no vertices; f=1 is a (t-1)-simplex; for f>=2 the standard complete directed-forest homotopy theorem and join formula yield (f-1)^(f-1+t) spheres of dimension f+t-2. The verification source explicitly tests orbit admissibility; independently checked the f=2,t=1 two-element block orbit classification (four admissible vertex orbits). General conclusion rests on proof and cited directed-tree theorem, not that finite check.

## originality

PASS

Best-of-knowledge originality after comparing actual theorem statements, relevant Resultary records and available primary material. Key inapplicable/covering distinctions and residual full-text risks are recorded; lack of accessible full text is not treated as proof of novelty.

## value

PASS

A natural symmetry-fixed-space classification for a canonical rooted-forest subcomplex; the all-block-size-independent PL join model and exact sphere count refine a nonequivariant result and can serve equivariant topology computations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
