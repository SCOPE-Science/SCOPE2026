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

The result is a finite classification of one completely specified labelled simplicial complex, and was independently reconstructed. At the pinned 100-facet source, E=117 and T=200. Exact signed integral boundaries, a 200x100 primitive kernel basis and 100x200 integer left inverse satisfy d2B=0, LB=I; independently computed exact 100x100 determinant det(Ld3)=-2 with zero Bareiss divisibility failures. Independent unimodular reduction of the 200x101 contracted graph presentation isolates 99 unit factors then a 4 times primitive rank-one residual, giving H1=Z+Z/4. Direct mod-two rank computations give rk d2=99, rk d3=99, dim ker d2=101 and dim H2(F2)=2. Explicit halved boundaries paired with verified free and mod-four cocycles yield beta classes (0,2),(0,0),(0,2). A distinct Python source built from the public Manifold Page facets examines every 65,535 nonempty support of size ≤8, finds minimum supports 8,7,8 and carrier counts 15,7,20 with rank-one images, and verifies all seven 7-vertex minimizers have 21 edges,14 triangles, zero tetrahedra, edge degree two, coherent orientation and connectedness, hence are tori. All 42 original claimed carrier supports were separately checked against their exact one-dimensional class images. No proof rests only on a verifier log.

## originality

PASS

Best-of-knowledge original precise induced-vertex-support filtration for the published labelled B4 triangulation. The 2003 and 2009 primary tables give the exact complex and ambient homology; exactness of the coefficient Bockstein gives only the dimensions/kernel and cannot dictate the labelled subset minima or carrier multiplicities. The closest published B3 seven-torus census treats a different 102-tetrahedron complex and only integral support. The identical indexed B4 listing is the same finding mirrored, not an independent earlier result. Unindexed equivalent enumerations remain a real priority risk.

## value

PASS

The fixed triangulation B4 is a classical small nonorientable flat 3-manifold with H1 order-four torsion and H2 order-two torsion. The induced vertex-support filtration of H2(F2) is a natural combinatorial invariant, and the coefficient connecting Bockstein supplies an intrinsic distinction between liftable and nonliftable classes. The sharp one-vertex obstruction, seven minimal induced torus representatives and complete (7,15,20) classwise counts form a motivated exact structural boundary not implied by ambient homology tables. Future work on support filtrations or comparisons among minimal flat-manifold triangulations can use the precise fact without requiring a general theorem. It is not merely recomputing Smith groups.

The dated certificate retains the supplied scientific assessment, sources and limitations.
