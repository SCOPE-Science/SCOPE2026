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

The section type under translation-invariant unoriented affine-plane measure is obtained from ordered vertex projections: quadrilateral offsets are the middle gap. Integrating edge-crossing counts gives (3+p4) E(width)=sum(edge lengths)/2. The polyhedral exterior-dihedral mean width identity E(width)=sum(length*exterior_angle)/(4*pi) verifies the full tetrahedron normalization. In T_t the edge and facet normal dot products give L=sqrt(1+t²), alpha=2acos(t/sqrt(1+2t²)), beta=2acos(1/sqrt(1+2t²)). Differentiating F=(2L alpha+sqrt(2) beta)/(2L+sqrt(2)) cancels the angular derivative and gives F'=2 sqrt(2) t (alpha-beta)/(L(2L+sqrt(2))²). Its sign is sign(1-t); since p4=2pi/F-3 this proves unique global minimum t=1, strict monotonicity on both sides, and limit values sqrt(2)-1 and 1. The expansion coefficient pi sqrt(2)/(9 acos(-1/3)^2) follows by F''(1)=-sqrt(2)/9. Independently computed p4 using 30,000 deterministic spherical directions at seven t values: agreement to <=0.0031; numerical agreement does not establish infinite-t monotonicity.

## originality

PASS

The genuinely claimed contribution is the global one-parameter extremal theorem for invariant hitting-plane quadrilateral probability, not the classical Crofton/Steiner formula or regular tetrahedron width. Finch's full regular-polyhedron width preprint concerns moment profiles of a single regular shape, while the closest published Resultary tetrahedron silhouette study measures projected shadows, not affine-plane hitting-section types. Hajja--Walker treats equifacial geometry and may conceal a relevant ratio inequality; only partial accessible material was inspected, so no whole-document noncoverage claim is made. No strong prior implication or database/table coverage was found in the actual bounded search.

## value

PASS

Quadrilateral-vs-triangle section frequency is a natural stereological invariant under the correctly width-biased invariant-plane law. The exact rigid optimizer, monotonic shape profile, both distinct degenerations, and quantitative second-order stability provide a motivated structural classification of a canonical continuous family; they are not merely reprinting the classical mean-width identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
