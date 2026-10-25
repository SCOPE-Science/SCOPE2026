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

The frozen RESULT.md defines K=[-2,2]^3∩{||x||_1≤3} and Haar-normal central sections (U and −U identify the same plane; degeneracies measure zero). Reconstructed the 24 signed-permutation vertices, 36 edges and all facet incidence inequalities. For ordered positive normal coordinates x>y>z>0, the generic polygon count is N=4+2·1[y<2z]+2·1[x>2z]+2·1[x>2y]; its range is exactly {6,8,10}. N=10 is the cone with rays X=(1,0,0),R=(4,2,1),Q=(2,1,1); the spherical triangle formula yields q=24 arctan(1/(11+3√14+4√6+2√21))/π. Independently, 36 edges all have endpoint dot product 4 and endpoint norms √5, so Crofton crossing probability θ/π with θ=arccos(4/5) gives EN=36θ/π. Normalization and these two moments uniquely give p6=4+q−18θ/π, p8=18θ/π−3−2q, p10=q; numeric sum=1, all positive. Independently regenerated 24 vertices, 36 edges and compared the direct edge-crossing count with the facet indicator on 25,000 Haar Gaussian normals; all cases agreed, empirical frequencies within sampling error. Computation supports but does not prove measure identities; proof is the finite facet-cone analysis plus exact solid angle and expectation.

## originality

PASS

Best-of-knowledge PASS for the complete exact three-atom Haar central-section type law of the specific regular truncated octahedron, not for Crofton crossing counts or the classical solid-angle identity. Resultary's cube, octahedron and icosahedron section laws concern distinct bodies; Lonke gives general cube section expectations. Paul's 1981 paper explicitly includes truncated octahedra in random stereological section-area simulations, a same-object priority risk, but the accessible abstract does not establish the center-passing polygon-vertex distribution or displayed closed law. Its full text was inaccessible, so no whole-document noncoverage claim is made.

## value

PASS

A regular truncated octahedron is a canonical Archimedean, space-filling solid and an archetypal non-vertex-transitive section problem. Its full Haar central-section polygon-type law is a motivated natural exact invariant, not merely an arbitrary numerical evaluation: the calculation distinguishes 6/8/10 faces and a nonobvious decagonal solid-angle chamber. The exact closed probabilities and first-moment consistency provide a reusable benchmark in integral geometry; value does not rest on overstated downstream theorems.

The dated certificate retains the supplied scientific assessment, sources and limitations.
