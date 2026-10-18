---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

The identity A=J+I-B^T B gives the true 1-eigenspace ker B of dimension n(n-3)/2; the orthogonal projector has diagonal (n-3)/(n-1). For h in ker B, h_e<=1 transforms bijectively to By=1,y>=0 via h=1-(n-1)y. Positive-support independence at an extreme fractional one-factor forces isolated weight-one edges and disjoint half-weight odd cycles. With q odd-cycle vertices, ||h||^2=n(n-1)(n-2)/2-(n-1)^2 q/4, so qmin=0 even or 3 odd gives exactly the proposed radius and all contact-facet counts. Irreducibility of the edge-permutation representation restricted to ker B plus uniqueness forces centered John/Löwner balls. Independently checked projector/radius algebra for n=5..13; finite checks do not establish the representation result, which follows from the scalar commutant argument. Normalization by orthonormal eigenvectors is essential.

## originality

PASS

Winter formally defines orthonormal eigenpolytopes and proves symmetry/reconstruction statements, but not the exact Kneser KG(n,2) fractional-matching polar, radii, or inball tangent-facet parity law. The published complete-graph *full matching* polytope and *fractional matching* John-ellipsoid records have different ambient bodies and ellipsoid objectives; their formulas do not imply this eigenpolytope John radius. A plausible older eigenpolytope source was not fully available, leaving explicit priority risk; present best-of-knowledge PASS concerns the structural identification and exact all-n invariant, not classical fractional matching half-integrality.

## value

PASS

The 1-eigenspace realization of an infinite, canonical distance-regular Kneser family is natural; its exact metric distortion and the surprising even/odd tangent-orbit classification answer a motivated geometric question. The polar-to-fractional-matching affine duality is a reusable structural bridge. It is more than a routine spectral normalization or tabulated single small graph.

The dated certificate retains the supplied scientific assessment, sources and limitations.
